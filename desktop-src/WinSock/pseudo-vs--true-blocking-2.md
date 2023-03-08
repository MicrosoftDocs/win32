---
title: Pseudo-blocking and true blocking
description: Pseudo-blocking operations in Windows Sockets (Winsock).
ms.assetid: fa8f29f1-bb4f-4814-ab8a-52d3c83232bb
ms.topic: article
ms.date: 02/08/2023
---

# Pseudo-blocking and true blocking

In 16-bit Windows environments, true blocking isn't supported by the operating system (OS); therefore, a blocking operation that can't be completed immediately is handled as follows:

* The service provider initiates the operation, and then enters a loop during which it dispatches any Windows messages (yielding the processor to another thread if necessary).
* It then checks for the completion of the Windows Sockets function.
* If the function has completed, or if [**WSPCancelBlockingCall**](/previous-versions/windows/desktop/legacy/ms742269(v=vs.85)) has been invoked, then the loop is terminated and the blocking function completes with an appropriate result.

This is what is meant by the term pseudo-blocking, and the loop referred to above is known as the default blocking hook.
