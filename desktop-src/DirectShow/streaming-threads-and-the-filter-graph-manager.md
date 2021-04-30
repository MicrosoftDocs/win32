---
description: Streaming Threads and the Filter Graph Manager
ms.assetid: b490b72a-ab34-46e6-8dc6-a7bb07cfc7b1
title: Streaming Threads and the Filter Graph Manager
ms.topic: article
ms.date: 05/31/2018
---

# Streaming Threads and the Filter Graph Manager

When the Filter Graph Manager stops the graph, it waits for all streaming threads to shut down. This has the following implications for filters:

-   A filter must never call methods on the Filter Graph Manager from a streaming thread.

    The Filter Graph Manager uses a critical section to synchronize its own operations. If a streaming thread tries to hold this critical section, it can cause a deadlock. For example: Suppose that another thread stops the graph. That thread takes the filter graph lock and waits for your filter to stop delivering data. If your filter is waiting for the lock, it will never stop, causing a deadlock.

-   A filter must never **AddRef** or **QueryInterface** the Filter Graph Manager from a streaming thread.

    If the filter holds a reference count on the Filter Graph Manager (through **AddRef** or **QueryInterface**), it might become the last object to hold a reference count. When the filter calls **Release**, the Filter Graph Manager destroys itself. Inside its cleanup routine, the Filter Graph Manager attempts to stop the graph, causing it to wait for the streaming thread to exit. However, it is waiting inside the streaming thread, so the streaming thread cannot exit. The result is a deadlock.

 

 



