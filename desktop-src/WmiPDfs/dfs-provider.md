---
title: DFS Provider
description: The preinstalled Distributed File System (DFS) provider supplies scriptable DFS functions through WMI.
audience: developer
author: REDMOND\\martinek
manager: REDMOND\\martinek
ms.assetid: 01d17f24-7a14-4d25-b653-52ba12f83326
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DFS Provider
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DFS Provider

The preinstalled Distributed File System (DFS) provider supplies scriptable DFS functions through WMI. DFS provides the ability to group shares logically on multiple servers, and link shares transparently to a tree-like structure in a single namespace. This provider can create a DFS node, and uses an association class to represent the connection between a node, and the shares and servers being linked to the node.

A DFS root can be defined at the domain level for domain-based operation, or at the server level for stand-alone operation. Domain-based DFS can have multiple roots in the domain but only one root on each server.

As an instance and method provider, the DFS provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Wmipdfs.mof file defines the DFS provider, and association and registration classes. You can access the DFS provider classes only in the Root\\CIMv2 namespace.

The DFS provider supports the following classes:

-   [**Win32\_DFSNode**](win32-dfsnode.md)
-   [**Win32\_DFSTarget**](win32-dfstarget.md)
-   [**Win32\_DFSNodeTarget**](win32-dfsnodetarget.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




