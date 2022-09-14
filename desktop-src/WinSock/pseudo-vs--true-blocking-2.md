---
description: Pseudoblocking pseudo blocking operations in Windows Sockets (Winsock).
ms.assetid: fa8f29f1-bb4f-4814-ab8a-52d3c83232bb
title: Pseudo Blocking and True Blocking
ms.topic: article
ms.date: 05/31/2018
---

# Pseudo Blocking and True Blocking

In 16 Windows environments, true blocking is not supported by the operating system; therefore, a blocking operation that cannot be completed immediately is handled as follows:

-   The service provider initiates the operation, and then enters a loop during which it dispatches any Windows messages (yielding the processor to another thread if necessary)
-   It then checks for the completion of the Windows Sockets function.
-   If the function has completed, or if [**WSPCancelBlockingCall**](/previous-versions/windows/desktop/legacy/ms742269(v=vs.85)) has been invoked, the loop is terminated and the blocking function completes with an appropriate result.

This is what is meant by the term pseudo blocking, and the loop referred to above is known as the default blocking hook.

 

 
