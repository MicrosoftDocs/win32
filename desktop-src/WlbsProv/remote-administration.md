---
title: Remote Administration
description: One of the benefits of WMI is its ability to facilitate remote administration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8ffd3a45-aecd-4581-b65d-e5f7df025f25'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["remote administration Failover Cluster", "remote administration Failover Cluster ,vs. remote operations in NLB", "remote operations Failover Cluster ,vs. remote administration in NLB"]
---

# Remote Administration

One of the benefits of [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) is its ability to facilitate remote administration. With the Network Load Balancing [*Provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly), it is important to distinguish between the meaning of "remote" in "remote administration" versus the meaning of "remote" in "[*remote operations*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-14-gly)."

-   The word "remote" in remote administration refers to the WMI connection model. WMI implements a connection as a remote client/server connection regardless of whether the [*provider client*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-10-gly) and the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly) are different computer systems or the same computer system.
-   The word "remote" in remote operations refers to the relationship between the provider node and the effects of operations initiated by the provider. For more information see [Local and Remote Operations](local-and-remote-operations.md)).

Note that the physical relationship between the provider client and the provider node is irrelevant. You can run your application on a cluster [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) and establish a [direct connection](direct-connections.md) to that node, but this has no impact on whether operations are considered local or remote, and you are still performing remote administration.

 

 




