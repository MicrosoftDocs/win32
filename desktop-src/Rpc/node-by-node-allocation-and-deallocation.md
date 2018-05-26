---
title: Node-by-Node Allocation and Deallocation
description: Node-by-node allocation and deallocation of data structures by the stubs is the default method of memory management for all parameters on both the client and the server.
ms.assetid: 04752fd9-438c-4b52-830b-ce136f83b3b8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Node-by-Node Allocation and Deallocation

Node-by-node allocation and deallocation of data structures by the stubs is the default method of memory management for all parameters on both the client and the server. On the client side, the stub allocates each node with a separate call to [midl\_user\_allocate](https://msdn.microsoft.com/library/windows/desktop/aa367095). On the server side, rather than calling **midl\_user\_allocate**, private memory is used whenever possible. If **midl\_user\_allocate** is called, the server stubs will call **midl\_user\_free** to free the data. In most cases, using node-by-node allocation and deallocation instead of using **\[allocate (all\_nodes)\]** will result in increased performance of the server side stubs.

 

 




