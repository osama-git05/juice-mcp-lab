# Setup and operational walkthrough

## 1 Prepare Kali

Stage dependencies before isolating the target. The model runs on Windows and the Python clients run in Kali.

```bash
sudo apt update
sudo apt install -y docker.io python3-venv curl jq openssh-server git
sudo systemctl enable --now docker
git clone https://github.com/osama-git05/juice-mcp-lab.git
cd juice-mcp-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 2 Start the pinned target

```bash
IMAGE=$(cat image-reference.txt)
sudo docker pull "$IMAGE"
sudo docker run --name juice-mcp-target -d \
  -p 127.0.0.1:3000:3000 "$IMAGE"
sudo docker ps --filter name=juice-mcp-target
curl --max-time 5 -sS -o /dev/null -w 'HTTP %{http_code}\n' http://127.0.0.1:3000/
```

Open http://127.0.0.1:3000 in Kali. For an existing container, inspect it and use docker start. Preserve evidence before replacing a target.

The recorded runner used 10.0.2.15:3000. This setup uses loopback for the same local-container role. Record the actual address used in every future run.

## 3 Configure Unsloth

Load Qwen2.5-Coder-7B-Instruct GGUF. The existing model-selection capture shows Q5_K_M. Record the publisher, revision, file hash, context and offload configuration in future trials.

Start the local API on loopback port 8888. Create a dedicated key in Settings → API, after revoking the earlier exposed key. Disable remote providers and built-in execution tools for the lab.

## 4 Establish the SSH tunnel

Choose the network method already configured for your VM. On a host-only network, assign Windows 192.168.57.1/24 and Kali 192.168.57.10/24.

In Kali:

```bash
sudo systemctl enable --now ssh
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

In Windows PowerShell:

```powershell
$KaliUser = Read-Host "Kali username"
ssh -N -T -o ExitOnForwardFailure=yes -R 127.0.0.1:8888:127.0.0.1:8888 "$KaliUser@192.168.57.10"
```

If VirtualBox instead forwards Windows loopback TCP 2222 to Kali TCP 22, use:

```powershell
$KaliUser = Read-Host "Kali username"
ssh -N -T -p 2222 -o ExitOnForwardFailure=yes -R 127.0.0.1:8888:127.0.0.1:8888 "$KaliUser@127.0.0.1"
```

Compare the first SSH fingerprint with Kali. Leave the tunnel terminal open. Port 2222 is an SSH entry point in the NAT variant. Port 8888 carries inference. No safe committed tunnel transcript proves which variant was used in the original run.

## 5 Create private configuration

The template has an empty key. This interactive procedure keeps a literal key out of shell history.

```bash
python - <<'PY'
from getpass import getpass
from pathlib import Path
import os
os.umask(0o077)
key = getpass("New Unsloth API key: ")
if not key or any(c in key for c in "\r\n'"):
    raise SystemExit("Invalid key format")
Path(".env").write_text(
    "OPENAI_API_BASE=http://127.0.0.1:8888/v1\n"
    f"OPENAI_API_KEY='{key}'\n"
    "TARGET_URL=http://127.0.0.1:3000\n"
    "MODEL_NAME=Qwen2.5-Coder-7B-Instruct\n"
)
PY
git check-ignore .env
```

Check the model identifier without printing the token:

```bash
python - <<'PY'
import os
import requests
from dotenv import load_dotenv
load_dotenv(".env")
r = requests.get(
    os.environ["OPENAI_API_BASE"].rstrip("/") + "/models",
    headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]},
    timeout=10,
)
r.raise_for_status()
for item in r.json()["data"]:
    print(item["id"])
PY
```

Update MODEL_NAME in private configuration if needed. Do not commit .env.

## 6 Run the current workflow

```bash
python runner.py
python tests.py
python generate_report.py
```

runner.py requests a checklist after checking the target. tests.py sends ten GET requests and does not invoke its LLM helper. The report generator exports a reviewed baseline rather than reading a new execution.

| Symptom | First check |
|---|---|
| Target refused | Container and loopback mapping |
| Inference refused | Model listener and reverse tunnel |
| Inference 401 | Revoked or invalid key |
| Wrong model | Identifier from /v1/models |
| 200 on hash route | Browser fragments are not transmitted |
| 500 on login/reset | Correct method and baseline required before assessing a vulnerability |
