---
title: Connecting to WMI
description: To use the Network Load Balancing Provider, your application establishes a connection to WMI and requests access to a namespace, often in the form of an object path such as \ 0034;\\\\ computer name \\root\\MicrosoftNLB \ 0034;.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7e3c3719-ec5c-4bca-ac37-24bdb8f1fe28'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["connections Failover Cluster", "connections Failover Cluster , NLB to WMI", "WMI Failover Cluster", "WMI Failover Cluster ,connecting NLB to"]
---

# Connecting to WMI

To use the Network Load Balancing [*Provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly), your application establishes a connection to [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) and requests access to a [*namespace*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-1-gly), often in the form of an object path such as "\\\\&lt;computer name&gt;\\root\\MicrosoftNLB". WMI creates a client-server connection between the computer system on which your application is running (the [*provider client*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-10-gly)) and the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) that will load the provider and carry out provider operations (the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly)). The namespace you use determines how the provider node is selected. For more information, refer to the following sections:

-   [Direct Connections](direct-connections.md)
-   [Routed Connections](routed-connections.md)
-   [Remote Administration](remote-administration.md)

 

 




