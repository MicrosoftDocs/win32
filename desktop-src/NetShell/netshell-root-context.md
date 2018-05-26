---
title: NetShell Root Context
description: The NetShell root context is the starting point for NetShell.
ms.assetid: d58ab87c-3375-422d-bb9b-348482887114
keywords:
- NetShell NetSh , described, root context
- root context NetSh
- context NetSh
- context NetSh , root
- components NetSh , root context
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NetShell Root Context

The NetShell root context is the starting point for NetShell. All top-level contexts in NetShell originate as immediate children of the root context. The following example shows how to view the NetShell root context from a command prompt:

``` syntax
c:\> netsh
netsh>
```

The command prompt in the NetShell shell reflects the location in the context tree, as the following example shows:

``` syntax
netsh> ras
netsh ras>
```

In this example, the prompt is in the **ras** context. Many contexts have subcontexts, which present sub-areas of a given context to further group administrative tasks associated with an area of networking functionality. For example, the **ras** context has **ip** and **ipx** subcontexts. These subcontexts are reached from the command prompt in a similar fashion to primary contexts, as the following shows:

``` syntax
netsh> ras
netsh ras> ip
netsh ras ip>
```

NetShell presents contexts similarly to how DNS segregates areas of the Internet based on domains: Microsoft.com is a domain, and Msdn.Microsoft.com is its subdomain.

 

 




