# Spin outbound HTTP regression: URL without trailing slash

Outbound `GET https://example.com` (no trailing slash) works on Spin v4.0.2 but fails on v4.1.0. `https://example.com/` works on both.

Bisected to [spinframework/spin#3605](https://github.com/spinframework/spin/pull/3605) (Bump Wasmtime to v47.0.0).

## Setup

```bash
spin plugins install verman
python3 -m venv venv && source venv/bin/activate
pip3 install -r requirements.txt
```

## Reproduce

```bash
spin verman set v4.0.2   # or v4.1.0
spin up --build
curl localhost:3000/
```

| Spin   | Result                               |
|--------|--------------------------------------|
| v4.0.2 | `200 example.com returned 200`       |
| v4.1.0 | `500 outbound failed: None`          |
