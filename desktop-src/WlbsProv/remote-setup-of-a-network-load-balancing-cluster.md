---
title: Remote Setup of a Network Load Balancing Cluster
description: Currently, there is no way to remotely bind the Network Load Balancing driver to the network interface card (NIC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3dcb09ea-9456-4889-9233-afd7c6c80be4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["clusters Failover Cluster ,remote setup in NLB", "remote setup of a network load balancing cluster Failover Cluster"]
---

# Remote Setup of a Network Load Balancing Cluster

Currently, there is no way to remotely bind the Network Load Balancing driver to the [*network interface card*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-2-gly) (NIC). The binding must be done manually through the **Network and Dial-Up Connections** dialog box and thus requires a working installation of the operating system. Once the Network Load Balancing driver is bound to a NIC, you can perform all other configuration steps remotely, but you will need to use two additional [*providers*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly):

-   Use the Domain Name System (DNS) provider to register the cluster name and [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) with DNS.
-   Use the WMI provider to register the cluster name and IP address with TCP/IP.

 

 




