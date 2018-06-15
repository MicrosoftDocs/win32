---
Description: If a socket is in nonblocking mode, any I/O operation must either complete immediately or return the error code WSAEWOULDBLOCK indicating that the operation cannot be finished right away.
ms.assetid: badd279b-ec71-4761-9066-d501aa2485c2
title: Nonblocking Input/Output
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Nonblocking Input/Output

If a socket is in nonblocking mode, any I/O operation must either complete immediately or return the error code WSAEWOULDBLOCK indicating that the operation cannot be finished right away. In the latter case, a mechanism is needed to discover when it is appropriate to try the operation again with the expectation that the operation will succeed. A set of network events has been defined for this purpose. These events can be polled or waited on by using [**WSPSelect**](https://msdn.microsoft.com/en-us/library/ms742289(v=VS.85).aspx), or they can be registered for asynchronous delivery by calling [**WSPAsyncSelect**](https://msdn.microsoft.com/en-us/library/ms742267(v=VS.85).aspx) or [**WSPEventSelect**](https://msdn.microsoft.com/en-us/library/ms742276(v=VS.85).aspx). See [Notification of Network Events](notification-of-network-events-2.md) for more information.

 

 



