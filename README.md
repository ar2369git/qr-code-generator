# QR Code Generator

A straightforward Python application that generates a QR code image for any given URL. This project is fully Dockerized for effortless deployment and includes a GitHub Actions workflow to automate building and publishing the Docker image to Docker Hub.

---

## Features

* **Generates QR Codes:** Creates QR code images in PNG format.
* **Flexible Input:** Reads URLs via the `--url` command-line interface (CLI) flag.
* **Organized Output:** Saves all generated QR codes into a dedicated `qr_codes/` directory.
* **Secure Containerization:** Runs as a non-root user within the Docker container for enhanced security.
* **Automated CI/CD:** Leverages GitHub Actions for continuous integration and continuous deployment, ensuring your Docker image is always up-to-date on Docker Hub.

---

## Prerequisites

Before you begin, ensure you have the following:

* **Python 3.7+**: For local development and running the script without Docker.
* **Docker 24+**: Essential for building and running the containerized application.
* **A GitHub account**: To host your repository and utilize GitHub Actions.
* **A Docker Hub account**: To store and manage your Docker images.
* **(Optional) GitHub Secrets Configured**: For automated Docker Hub login via GitHub Actions, you'll need two repository secrets:
    * `DOCKERHUB_USERNAME`: Your Docker Hub username.
    * `DOCKERHUB_TOKEN`: A Personal Access Token (PAT) generated from your Docker Hub account with "Read & Write" access to repositories.

---

## Getting Started

Follow these steps to get your QR Code Generator up and running.

### 1. Clone the Repository

First, clone the project to your local machine:

```bash
git clone https://github.com/<your-github-username>/qr-code-generator.git
cd qr-code-generator

## Repository Structure

qr-code-generator/
├── .github/
│   └── workflows/
│       └── docker-publish.yml # GitHub Actions workflow for building and pushing the Docker image
├── .gitignore               # Specifies intentionally untracked files to ignore
├── Dockerfile               # Defines the Docker image
├── main.py                  # The core QR code generation script
├── requirements.txt         # Lists Python dependencies
└── README.md                # This project documentation

## Getting Started

Follow these steps to get your QR Code Generator up and running.

### 1. Clone the Repository

First, clone the project to your local machine:

```bash
git clone [https://github.com/](https://github.com/)<your-github-username>/qr-code-generator.git
cd qr-code-generator

Remember to replace `<your-github-username>` with your actual GitHub username.

### 2. Install Python Dependencies (Local Development)
If you plan to run the application locally without Docker, install the Python dependencies:

```bash
python3 -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.\.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

### 3. Run Locally
Execute the Python script to generate a QR code for a given URL:


python main.py --url [https://example.com](https://example.com)
This command will create a qr.png file inside the qr_codes/ directory in your project root.

## Docker Usage

### Build the Image
Build the Docker image for the application:

```bash
docker build -t qr-code-generator-app .

### Run the Container
Run the Docker container to generate a QR code. The `-v` flag maps a local directory to the container's output directory, ensuring your generated QR codes persist on your host machine.

```bash
docker run --rm \
  -v "$(pwd)/qr_codes:/app/qr_codes" \
  qr-code-generator-app \
  --url "[https://www.njit.edu](https://www.njit.edu)"

You can override the default URL by specifying `--url` after the image name, as shown in the example above.

### Cleanup
To remove the Docker image from your local system:

```bash
docker rmi qr-code-generator-app

You can override the default URL by specifying `--url` after the image name, as shown in the example above.

### Cleanup
To remove the Docker image from your local system:

```bash
docker rmi qr-code-generator-app

## Pushing to Docker Hub
To publish your Docker image to Docker Hub, follow these steps:

### Log In
First, log in to Docker Hub from your terminal. When prompted for a password, enter your Docker Hub Personal Access Token (PAT).

```bash
docker login

### Tag the Image
Tag your local image with your Docker Hub username and the desired repository name. This makes it ready for pushing.

```bash
docker tag qr-code-generator-app \
  <your-dockerhub-username>/qr-code-generator-app:latest

Remember to replace `<your-dockerhub-username>` with your actual Docker Hub username.

### Push the Image
Finally, push the tagged image to Docker Hub:

```bash
docker push <your-dockerhub-username>/qr-code-generator-app:latest

### Verify
You can verify that your image has been pushed successfully by visiting your Docker Hub repository:
`https://hub.docker.com/r/<your-dockerhub-username>/qr-code-generator-app`

---

## CI/CD with GitHub Actions
The repository includes a GitHub Actions workflow defined in `.github/workflows/docker-publish.yml`. This workflow automates the process of building and pushing your Docker image to Docker Hub whenever you push changes to the `main` branch.

The workflow automatically:

* Checks out your code.
* Sets up Docker Buildx and QEMU for multi-platform builds.
* Logs in to Docker Hub using the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets you've configured.
* Builds and pushes the `latest` tag of your Docker image on every push to `main`.

To enable automated publishing, ensure you've added your Docker Hub credentials as repository secrets under your GitHub repository's **Settings** → **Secrets and variables** → **Actions**.

---

## Environment Variables & Placeholders
Keep the following in mind when setting up your project:

* **Git Remote URL:** When setting up your Git remote, remember to replace `<your-github-username>`:
    ```bash
    git remote add origin [https://github.com/](https://github.com/)<your-github-username>/qr-code-generator.git
    ```
* **Dockerfile Default URL:** You can update the default URL used by the Docker image by modifying the `CMD ["--url", "..."]` instruction in your `Dockerfile`.
* **Docker Hub Username:** Always replace `<your-dockerhub-username>` with your actual Docker Hub username when tagging and pushing images.

---

## Contributing
We welcome contributions! If you'd like to improve this project:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/your-feature-name`).
3.  Commit your changes (`git commit -m 'feat: Add new feature'`).
4.  Push to your branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

Please adhere to **PEP 8 style guidelines** and include **tests** for any new functionality.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.