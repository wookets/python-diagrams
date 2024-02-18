from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.podconfig import Secret

with Diagram("Meilisearch Running on Kubernetes", show=False, filename="k8s-meilisearch"):
  with Cluster("Kubernetes"):
    svc = Service("Service")
    sts = StatefulSet("Stateful Set")

    meilisearch1 = Pod("Replica 1")
    meilisearch2 = Pod("Replica 2")
    pvc = PVC("pvc")

    secret = Secret("MasterKey")

    svc >> meilisearch1 >> pvc
    svc >> meilisearch2 >> pvc
    
    sts >> meilisearch1
    sts >> meilisearch2

    sts >> secret

    #apps = []
    # for _ in range(2):
    #   pod = Pod("pod")
    #   pod - sts - pvc
    #   apps.append(svc >> pod >> pvc)

#apps << PV("pv") << StorageClass("sc")