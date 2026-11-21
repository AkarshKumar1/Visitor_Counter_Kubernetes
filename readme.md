
# Visitor Counter Web Application
### Docker, Kubernetes, Autoscaling, Hybrid Failover & Resource Optimization

> **Cloud Computing Internal Assessment Project**  
> A containerized visitor counter web application deployed using Docker and Kubernetes, with self-healing, Horizontal Pod Autoscaling (HPA), hybrid failover simulation, and resource optimization.

---

## 📌 Project Overview

This project demonstrates the deployment and management of a web application using containerization and Kubernetes orchestration.

The application is built using **Python Flask** and uses **Redis** to store visitor counts. Docker is used to containerize the application, while Kubernetes manages application deployment, scaling, service discovery, and self-healing.

The project also demonstrates a simulated hybrid environment using two local Kubernetes clusters, along with practical resource optimization techniques.

This project was developed as part of a **Cloud Computing Internal Assessment** to gain hands-on experience with containerization, orchestration, scalability, availability, and resource efficiency.

---

## 🎯 Project Objectives

- Containerize the Flask web application using Docker.
- Run the application and Redis using Docker Compose.
- Deploy the application on Kubernetes.
- Implement Kubernetes self-healing.
- Configure Horizontal Pod Autoscaling (HPA).
- Simulate a primary and secondary Kubernetes environment.
- Demonstrate application availability during primary cluster failure.
- Optimize Docker image size.
- Reduce Kubernetes CPU and memory resource requests and limits.
- Compare resource utilization configurations before and after optimization.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Lightweight web framework |
| Redis | Visitor counter data storage |
| Docker | Containerization |
| Docker Compose | Local multi-container deployment |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes cluster |
| kubectl | Kubernetes cluster management |
| Metrics Server | CPU metrics for autoscaling |
| HPA | Automatic scaling of application replicas |

---

## 🏗️ Architecture

The project consists of a primary Kubernetes cluster and a secondary Kubernetes cluster used to simulate a failover environment.

### Primary Cluster

- Flask application deployment
- Redis deployment
- NodePort service
- Two initial Flask replicas
- Horizontal Pod Autoscaler
- Automatic pod recovery

### Secondary Cluster

- Flask application deployment
- Redis deployment
- Application service
- Two Flask replicas
- Optimized Docker image
- Reduced CPU and memory configuration

### Architecture Diagram

![Visitor Counter Kubernetes Architecture](architecture_diagram.png)

---

## 📂 Project Structure

```text
visitor-counter-kubernetes/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── kubernetes/
│   ├── app-deployment.yaml
│   └── redis-deployment.yaml
│
├── screenshots/
│   ├── 01_minikube_cluster_setup.png
│   ├── 02_kubernetes_system_pods.png
│   ├── 03_docker_image_loaded.png
│   ├── 04_redis_deployment_created.png
│   ├── 05_redis_pod_verification.png
│   ├── 06_kubernetes_deployments_running.png
│   ├── 07_visitor_counter_application.png
│   ├── 08_self_healing_initial_status.png
│   ├── 09_self_healing_pod_deletion.png
│   ├── 10_self_healing_pod_recreation.png
│   ├── 11_hpa_configuration.png
│   ├── 12_CPU_Load_Generation.png
│   ├── 13_HPA_Scalling.png
│   ├── 14_Scaled_Pods.png
│   ├── 15_hpa_scaling_success.png
│   ├── 16_hpa_scale_down.png
│   └── ... additional hybrid failover
│        and optimization screenshots
│
├── architecture_diagram.png
├── Dockerfile
├── docker-compose.yml
├── k8s.yaml
├── hpa.yaml
├── .dockerignore
├── .gitignore
└── readme.md
```

---

## ⚙️ Application Features

### 1. Visitor Counter

A web application built using Flask that displays and updates the visitor count.

Redis is used as the backend data store for maintaining the visitor counter.

### 2. Docker Containerization

The application is packaged into a Docker image to ensure portability and consistent execution across environments.

### 3. Kubernetes Deployment

The application and Redis are deployed as Kubernetes workloads. Kubernetes manages the pods and services required to run the application.

### 4. Self-Healing

Kubernetes automatically recreates application pods when a running pod is deleted or becomes unavailable, maintaining the desired replica count.

### 5. Horizontal Pod Autoscaling

The application automatically scales based on CPU utilization.

- Minimum replicas: 2
- Maximum replicas: 6
- Target CPU utilization: 50%

### 6. Hybrid Failover Simulation

Two local Minikube Kubernetes clusters are used:

- Primary cluster
- Secondary cluster

The secondary cluster was tested by stopping the primary cluster and verifying that the application remained accessible through the secondary environment.

### 7. Resource Optimization

The project includes:

- Docker image size reduction
- CPU request optimization
- Memory request optimization
- CPU limit optimization
- Memory limit optimization
- Dynamic replica scaling using HPA

---

# 🚀 Installation and Setup

## Prerequisites

Install the following tools:

- Python
- Docker Desktop
- Docker Compose
- kubectl
- Minikube
- Git

Verify installations:

```bash
docker --version
docker compose version
kubectl version --client
minikube version
git --version
```

---

# 🐍 Run Locally

Navigate to the application directory:

```bash
cd app
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

---

# 🐳 Docker Deployment

Build the Docker image:

```bash
docker build -t visitor-counter-kubernetes-web:latest .
```

Check available images:

```bash
docker images
```

Run the application with Docker Compose:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

---

# ☸️ Kubernetes Deployment

Start Minikube:

```bash
minikube start --driver=docker
```

Check cluster status:

```bash
minikube status
```

Check Kubernetes nodes:

```bash
kubectl get nodes
```

Check system pods:

```bash
kubectl get pods -n kube-system
```

---

## Deploy Redis

Apply the Redis configuration:

```bash
kubectl apply -f kubernetes/redis-deployment.yaml
```

Verify Redis:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

---

## Deploy Flask Application

Apply the application deployment:

```bash
kubectl apply -f kubernetes/app-deployment.yaml
```

Verify application pods:

```bash
kubectl get pods
```

Verify deployments:

```bash
kubectl get deployments
```

Verify services:

```bash
kubectl get services
```

---

## Access the Application

Access the application through the Kubernetes service:

```bash
minikube service visitor-web
```

Or retrieve the service URL:

```bash
minikube service visitor-web --url
```

Open the generated URL in your browser to access the visitor counter.

---

# ♻️ Self-Healing Demonstration

Kubernetes self-healing was tested by manually deleting one of the running application pods.

### Check running pods

```bash
kubectl get pods
```

### Delete one application pod

```bash
kubectl delete pod <pod-name>
```

### Observe automatic recovery

```bash
kubectl get pods -w
```

Kubernetes automatically creates a replacement pod to maintain the desired replica count defined in the deployment.

---

# 📈 Horizontal Pod Autoscaling (HPA)

The application was configured to scale automatically based on CPU utilization.

### Enable Metrics Server

```bash
minikube addons enable metrics-server
```

Verify resource metrics:

```bash
kubectl top nodes
kubectl top pods
```

### Configure HPA

```bash
kubectl autoscale deployment visitor-web \
  --cpu-percent=50 \
  --min=2 \
  --max=6
```

Verify HPA:

```bash
kubectl get hpa
```

### Generate CPU Load

CPU load was generated inside the Kubernetes environment to test automatic scaling.

During the test:

- The application initially ran with 2 replicas.
- CPU utilization increased under generated load.
- HPA scaled the application up to 6 replicas.
- After the load was stopped, the replicas scaled back down to 2.

Monitor scaling:

```bash
kubectl get hpa -w
```

Monitor pods:

```bash
kubectl get pods -w
```

---

# 🌐 Hybrid Cluster & Failover Simulation

The project uses two local Kubernetes clusters to simulate a primary and secondary environment.

| Environment | Role |
|---|---|
| Primary Cluster | Main application environment |
| Secondary Cluster | Backup/failover environment |

### Failover Test Performed

1. Deploy the application in the primary environment.
2. Verify application accessibility.
3. Stop the primary cluster.
4. Verify that the secondary environment remains operational.
5. Access the application through the secondary cluster.
6. Restore the primary environment.

The failover scenario was demonstrated successfully using two local Minikube environments.

> **Note:** This is a local hybrid/failover simulation. The clusters are not deployed across separate cloud providers or geographically distributed infrastructure.

---

# 💰 Cost & Resource Optimization

Three optimization techniques were demonstrated.

## 1. Docker Image Optimization

The original Docker image was optimized using a lightweight Alpine-based Python image and reduced image build overhead.

| Before | After |
|---|---|
| 53.65 MB | 21.74 MB |

**Image size reduction: approximately 59.5%.**

---

## 2. CPU & Memory Optimization

Resource requests and limits were reduced in the optimized secondary deployment.

| Resource | Before | After | Reduction |
|---|---:|---:|---:|
| CPU Request | 100m | 50m | 50% |
| Memory Request | 128Mi | 64Mi | 50% |
| CPU Limit | 500m | 250m | 50% |
| Memory Limit | 256Mi | 128Mi | 50% |

These changes reduce the configured resource allocation for the application containers.

---

## 3. Dynamic Scaling with HPA

Instead of maintaining a fixed number of application replicas, HPA dynamically adjusts the replica count according to CPU demand.

| Configuration | Value |
|---|---|
| Minimum replicas | 2 |
| Maximum replicas | 6 |
| CPU target | 50% |
| Scale-up observed | 2 → 6 |
| Scale-down observed | 6 → 2 |

Dynamic scaling allows the application to use more replicas when demand increases and reduce replicas when demand decreases.

### Optimization Summary

| Technique | Demonstrated Result |
|---|---|
| Lightweight Docker base image | Image reduced by ≈59.5% |
| Reduced CPU allocation | CPU requests and limits reduced by 50% |
| Reduced memory allocation | Memory requests and limits reduced by 50% |
| HPA | Dynamic scaling from 2 to 6 replicas |

> The project was tested locally using Minikube. These results represent measured image-size and resource-configuration improvements, not actual cloud billing reductions.

---

# 📸 Screenshots & Evidence

The `screenshots/` directory contains evidence of the project's implementation and testing.

Evidence includes:

- Minikube cluster setup
- Kubernetes system pods
- Docker image creation
- Redis deployment
- Application deployment
- Visitor counter running in the browser
- Self-healing pod replacement
- HPA configuration
- CPU load generation
- Autoscaling from 2 to 6 replicas
- Scale-down after load stops
- Primary and secondary cluster setup
- Failover demonstration
- Secondary application accessibility
- Optimized image build
- Resource optimization configuration

---

# 📊 Results

The project successfully demonstrated:

- Flask visitor counter application deployment.
- Redis integration.
- Docker containerization.
- Docker Compose execution.
- Kubernetes deployment and service exposure.
- Kubernetes self-healing.
- Horizontal Pod Autoscaling.
- CPU-based scale-up and scale-down.
- Primary and secondary cluster simulation.
- Failover application accessibility.
- Docker image size optimization.
- Kubernetes CPU and memory resource optimization.

---

# ⚠️ Limitations

- Kubernetes clusters were deployed locally using Minikube.
- Hybrid failover was simulated locally rather than across actual cloud providers.
- No actual cloud billing data was collected.
- Cost optimization is evaluated through resource configuration and image-size measurements.
- Production-grade networking, persistent storage, security, monitoring, and cross-region disaster recovery are outside the scope of this prototype.

---

# 🔮 Future Scope

The project can be extended with:

- Deployment to AWS, Azure, or Google Cloud.
- Real multi-cloud or cross-region failover.
- Persistent Redis storage.
- CI/CD pipelines using GitHub Actions.
- Prometheus and Grafana monitoring.
- Ingress and domain-based access.
- Kubernetes secrets and security hardening.
- Infrastructure as Code using Terraform.
- Automated disaster recovery workflows.
- Cloud cost monitoring and real billing comparisons.

---

# 👨‍💻 Author

**Akarsh Kumar**  
B.Tech – Computer Science & Engineering  
Batch: 3CSE2  
Roll No.: 2410030259

Cloud Computing Internal Assessment Project

---

## 📄 Project Submission

This repository contains the source code, Docker configuration, Kubernetes manifests, architecture diagram, screenshots, and project documentation required to demonstrate the implementation.

---

⭐ If you find this project useful for learning Docker and Kubernetes, feel free to explore the repository.


---

**Project:** Visitor Counter Application using Docker and Kubernetes

**Primary Technologies:** Flask, Redis, Docker, Docker Compose, Kubernetes, Minikube, Python
