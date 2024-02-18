from diagrams import Cluster, Diagram
from diagrams.azure.compute import AKS, VM
from diagrams.azure.network import VPC

with Diagram("Hybrid Data Platform", show=False, filename="hybrid-data-platform"):
  vpc = VPC("My VPC")

  with Cluster("EKS Cluster"):
    eks_control_plane = EKS("EKS Control Plane")

    with Cluster("Worker Nodes"):
      worker_nodes = [EC2("Worker Node 1"),
                      EC2("Worker Node 2")]

  vpc >> eks_control_plane >> worker_nodes 
