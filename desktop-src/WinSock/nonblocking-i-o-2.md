---
Description: 'If a socket is in nonblocking mode, any I/O operation must either complete immediately or return the error code WSAEWOULDBLOCK indicating that the operation cannot be finished right away.'
ms.assetid: 'badd279b-ec71-4761-9066-d501aa2485c2'
title: 'Nonblocking Input/Output'
---

# Nonblocking Input/Output

If a socket is in nonblocking mode, any I/O operation must either complete immediately or return the error code WSAEWOULDBLOCK indicating that the operation cannot be finished right away. In the latter case, a mechanism is needed to discover when it is appropriate to try the operation again with the expectation that the operation will succeed. A set of network events has been defined for this purpose. These events can be polled or waited on by using [**WSPSelect**](wspselect-2.md), or they can be registered for asynchronous delivery by calling [**WSPAsyncSelect**](wspasyncselect-2.md) or [**WSPEventSelect**](wspeventselect-2.md). See [Notification of Network Events](notification-of-network-events-2.md) for more information.

 

 



