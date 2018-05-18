---
title: How the Provider Works
description: A provider is an architectural element of Windows Management Instrumentation (WMI).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b8efea2f-29a9-4266-aaa5-119a14496d37'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["provider Failover Cluster", "provider Failover Cluster ,how the NLB provider works"]
---

# How the Provider Works

A provider is an architectural element of [*Windows Management Instrumentation (WMI)*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-20-gly). As a working definition, WMI defines a unified architecture for describing, accessing, and instrumenting objects. Part of this architecture is a large database of WMI classes used to carry out remote management tasks on specific objects.

A provider extends the WMI schema of classes to allow WMI to work with new types of objects. The Network Load Balancing Provider defines classes for querying and configuring Network Load Balancing [*clusters*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly), [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly), and [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly).

The Network Load Balancing Provider has a set of unique behaviors not found in other providers. The following sections describe these behaviors as well as the intended usage model for the provider:

-   [Connecting to WMI](connecting-to-wmi.md)
-   [Local and Remote Operations](local-and-remote-operations.md)
-   [Enumerating Nodes](enumerating-nodes.md)

For a complete description and definition of WMI, please see the [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582) documentation.

 

 




