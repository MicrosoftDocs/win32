---
title: Resource Identifiers
description: Each instance of a resource must be assigned a unique resource identifier, or RESID, which is passed back to the Cluster service from the Open entry point function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a6683346-228c-4eaf-b84a-f55bed44b17a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,resource identifiers
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Identifiers

Each instance of a [resource](resources.md) must be assigned a unique resource identifier, or RESID, which is passed back to the [Cluster service](cluster-service.md) from the [**Open**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_routine) entry point function. The RESID (defined as a PVOID by ResUtils.h) allows the Cluster service to refer to specific instances in subsequent calls to the resource DLL. Thus the RESID must behave like an index, allowing your resource DLL to locate the correct instance and its associated data.

For more information, see [Implementing Instance Management](implementing-instance-management.md).

 

 




