---
title: Enumerating Nodes
description: Behavior of WMI enumeration procedures when used with the Network Load Balancing provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 275eb49b-452b-4fe0-a366-d7a2e541b2bf
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- enumerating nodes in NLB Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Nodes

When you use the standard [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) enumeration procedures to enumerate [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) with the Network Load Balancing (NLB) [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly), the results vary as follows:

-   You always get a [**MicrosoftNLB\_Node**](microsoftnlb-node.md) instance representing the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly). This node is always listed first in the enumeration.
-   You will get additional [**MicrosoftNLB\_Node**](microsoftnlb-node.md) instances for each node that is currently running NLB and that has the [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) [**RemoteControlEnabled**](https://msdn.microsoft.com/library/aa371006) property set to **TRUE**.

The following table illustrates enumeration results in a NLB [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) consisting of nodes A, B, C, and D. The results shown for a node are obtained by connecting directly to the node (see [Making Direct Connections](making-direct-connections.md)) and enumerating all available nodes:



| Provider node | NLB is running | Cluster operations are enabled | [**RemoteControlEnabled**](https://msdn.microsoft.com/library/aa371006) | Enumeration results (in order of appearance) |
|---------------|----------------|--------------------------------|--------------------------------------------------------------|----------------------------------------------|
| A<br/>  | yes<br/> | yes<br/>                 | **TRUE**<br/>                                          | A, C<br/>                              |
| B<br/>  | yes<br/> | yes<br/>                 | **FALSE**<br/>                                         | B, A, C<br/>                           |
| C<br/>  | yes<br/> | no<br/>                  | **TRUE**<br/>                                          | C, A<br/>                              |
| D<br/>  | no<br/>  | no<br/>                  | **TRUE**<br/>                                          | error<br/>                             |



 

-   Node D does not show up in any enumeration because NLB is not running on that node.
-   Node C shows up in all enumerations even though cluster operations have been stopped on that node.
-   Node B appears only in enumerations performed from node B.
-   WMI allows a connection to Node D, but any provider operation will return an error because NLB is not running on node D.

Because of the behavior described above, WMI enumeration is not a reliable indicator of [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) membership. This is by design. Do not use enumeration as the basis of a NLB cluster membership algorithm. The most accurate method to use to enumerate the nodes in a NLB cluster is to locate the cluster using the [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly). For an example, see [Monitoring Application Level Health](https://msdn.microsoft.com/library/cc307934).

 

 





