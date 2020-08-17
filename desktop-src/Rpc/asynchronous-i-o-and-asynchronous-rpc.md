---
title: Asynchronous I/O and Asynchronous RPC
description: Asynchronous I/O is an efficient means for a single thread to manage multiple I/O requests simultaneously.
ms.assetid: a9105518-4130-4119-b8d1-e73064b077e9
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous I/O and Asynchronous RPC

Asynchronous I/O is an efficient means for a single thread to manage multiple I/O requests simultaneously. Asynchronous RPC on the server accomplishes a similar purpose for RPC requests. In versions of Windows prior to Windows Vista, posting asynchronous I/O requests from server procedures using asynchronous RPC is discouraged. However, in Windows Vista and later versions of Windows, asynchronous I/O requests that are associated with an I/O completion port are supported by asynchronous RPC.

Prior to Windows Vista, an asynchronous remote procedure call may complete before the asynchronous I/O request completes. When the asynchronous call completes, its thread may terminate if the RPC runtime decides it has enough threads available to service the expected workload. The system binds all I/O requests to the thread that initiates them. If the thread terminates, any I/O requests pending on that thread are aborted. Pending I/O requests cannot be moved to another thread.

Therefore, application designers targeting versions of Windows prior to Windows Vista can either use synchronous I/O in server procedures, or they can forward all requests that involve asynchronous I/O to procedures executing on a thread pool that the application manages. The Windows API provides functions for thread-pool management. See [Process and Thread Functions](/windows/desktop/ProcThread/process-and-thread-functions).

 

 