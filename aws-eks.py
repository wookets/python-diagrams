from diagrams import Cluster, Diagram
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.network import VPC

with Diagram("AWS EKS", show=False, filename="aws-eks"):
    vpc = VPC("My VPC")

    with Cluster("EKS Cluster"):
        eks_control_plane = EKS("EKS Control Plane")

        with Cluster("Worker Nodes"):
            worker_nodes = [EC2("Worker Node 1"),
                            EC2("Worker Node 2")]

    vpc >> eks_control_plane >> worker_nodes 
