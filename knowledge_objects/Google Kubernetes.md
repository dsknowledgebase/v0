# Google Kubernetes

## What is Google Kubernetes


Google Kubernetes is a cluster management platform developed by Google. Since 2014 Kubernetes has been open source and managed by The Cloud Native Computing Foundation [1]. Kubernetes is popular because of its flexibility and powerful capabilities to meet the demands of modern cloud-based architecture. Kubernetes is the result of efforts at Google to manage containers with hallmarks of both Infrastructure as a Service and Platform as Service. Building Kubernetes, google engineers had some specific goals;

&quot;… _make it easy to deploy and manage complex distributed systems, while still benefiting from the improved utilization that containers enable&quot; [2]._

So what is Kubernetes? In simple terms Kubernetes intended be the central platform and managing entity for applications, tools and workloads in any environment. Kubernetes is geared towards container environments where workloads go up and down. Kubernetes can organize and balance the connectivity, disk space and distributed computing in a containerized infrastructure [1].

Kubernetes is not limited to the cloud, but it seeks to be at the forefront of cloud architecture. Flexibility and extensibility are key Kubernetes hallmarks [3]. The goal with Kubernetes is to allow as many other solutions to be used in the infrastructure as possible. Kubernetes is intended to be extremely flexible. With this goal it doesn&#39;t dictate a CI or automation policy. It allows the user to build a container in a way that best serves the organizations needs then provides the management tools to scale, manage, and maintain that complex cloud based applications or infrastructure [3].

Kubernetes can be broken into two architectural buckets; the master node and workers notes. Within the master node as you might expect one of the key components is the API server [4]. The API server controls the cluster and executes REST commands. Scheduled jobs and activities are initiated from the API server via the scheduler. Outside of the master node are the worker nodes Pods are run in the worker nodes [4].Pods are run on the same host and can contain a group of containers that work together. Pods share volumes and network connectivity and other resources. Kubelets receive from the API server configuration info for the pod.

## Who should use Google Kubernetes

Anyone looking to employ a containerized scalable clustered environment should consider Kubernetes. Kubernetes is an industry leading solution with significant support and widespread utilization which has led to significant documentation and use cases available



## When should I use Google Kubernetes



Use Kubernetes when you have the need for a containerized environment that is extensible and flexible. By nature Kubernetes is a devops focused solution that might be relevant to many data scientists. The need for a containerized solution will however be relevant in many big data enterprise environments. The investment required to understand Kubernetes will not be wasted in a world that is increasingly utilizing microservice, saas, and big data solutions.

## Strengths Google Kubernetes

Kubernetes appears to be future proof with new updates and features continuing to be rolled in to keep up with industry practices and trends. With Google as the backer, the technology has seen enormous success. Kubernetes provides for high availability needs, for example it&#39;s perfect for rolling updates.



## Weaknesses Google Kubernetes

Kubernetes might be overkill, overly complex and expensive for more simple environments.

## References

[1] kubernetes.io, &quot;What is kubernetes?&quot; Web page, Sep-2018 [Online]. Available: [https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

[2] B. Burns, B. Grant, D. Oppenheimer, E. Brewer, and J. Wilkes, &quot;Borg, omega, and kubernetes,&quot; _Queue_, vol. 14, no. 1, pp. 10:70–10:93, Jan. 2016 [Online]. Available: [http://doi.acm.org/10.1145/2898442.2898444](http://doi.acm.org/10.1145/2898442.2898444)

[3] redhat.io, &quot;What is kubernetes.&quot; Web page, Oct-2018 [Online]. Available: [https://www.redhat.com/en/topics/containers/what-is-kubernetes](https://www.redhat.com/en/topics/containers/what-is-kubernetes)

[4] grodrigues3, &quot;Kubernetes design and architecture.&quot; Web page, Aug-2017 [Online]. [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/architecture/architecture.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/architecture/architecture.md)
