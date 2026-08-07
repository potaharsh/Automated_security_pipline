# Automated DevSecOps Pipeline & Security Guardrail

An automated CI/CD security gatekeeper built using GitHub Actions, Gitleaks, Semgrep, and Trivy. The pipeline enforces Shift-Left security practices by automatically scanning code, dependencies, and container configurations for vulnerabilities on every push and Pull Request.

## 🏗 Architecture & Scanning Stages

```mermaid
graph TD
    A[Developer Push / Pull Request] --> B[GitHub Actions Pipeline]
    B --> C[1. Gitleaks: Secret Scanning]
    B --> D[2. Semgrep: SAST Code Analysis]
    B --> E[3. Trivy: SCA & Container Scan]
    C --> F[GitHub Security Tab / SARIF]
    D --> F
    E --> F
    F --> G{Security Gate Passed?}
    G -- Yes --> H[Code Merged]
    G -- No --> I[Pull Request Blocked]
