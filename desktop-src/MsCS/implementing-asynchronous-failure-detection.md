---
title: Implementing Asynchronous Failure Detection
description: When Online is called for a resource instance, you have the option of returning a handle to a synchronization object (an \ 0034;event handle \ 0034;).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1448d64d-12d0-4fe8-9049-b520a4b32932
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resources Failover Cluster ,failure,asynchronous detection
- resource failure Failover Cluster ,asynchronous detection
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Asynchronous Failure Detection

When [**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine) is called for a [resource](resources.md) instance, you have the option of returning a handle to a synchronization object (an "event handle"). This has the following effects:

-   The [Resource Monitor](resource-monitor.md) will not call the [**LooksAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine) entry point function for that instance, regardless of the [**LooksAlivePollInterval**](resources-looksalivepollinterval.md) setting.
-   You can signal the handle at any time to indicate a possible failure in a resource instance. Signaling the handle causes the Resource Monitor to call [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine) immediately. The event handle allows you to report failure asynchronously from anywhere in your [resource DLL](resource-dlls.md).

**To implement asynchronous failure detection**

-   Recommended: If you support multiple resource instances, devise a system so that one synchronization object serves several (if not all) resource instances. The routine that signals the handle should identify the instance that has failed for your [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine) routine.

 

 




