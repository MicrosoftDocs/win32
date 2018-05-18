---
title: Standard Usage Model
description: The most reliable and secure way to use the Network Load Balancing provider is to never make use of remote operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '759eb246-32c7-4262-91b3-162b9c62d156'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["usage model in NLB Failover Cluster"]
---

# Standard Usage Model

The most reliable and secure way to use the Network Load Balancing [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) is to never make use of remote operations. This can be done by observing the following procedure:

**To Configure a Cluster**

1.  Independently obtain and maintain a list of cluster members which includes their dedicated IP addresses.

2.  Using the membership list, establish a [direct connection](direct-connections.md) with a cluster node.

    1.  Obtain a [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class representing the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly). If necessary, use class methods to initiate draining, suspend cluster activity, or otherwise halt the flow of traffic to the node.
    2.  Obtain a [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class representing the node's configuration settings.
    3.  Obtain [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) classes representing the [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) associated with the node.
    4.  Configure the node. See [Configuring User Interface Settings](configuring-user-interface-settings.md). The SetToDefault method can be useful here.
    5.  When all settings are correct, use the [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) method to commit the changes to the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

3.  Repeat step 2 until all cluster nodes have been configured.

 

 




