---
description: Streaming Threads and the Filter Graph Manager
ms.assetid: b490b72a-ab34-46e6-8dc6-a7bb07cfc7b1
title: Streaming Threads and the Filter Graph Manager
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Streaming Threads and the Filter Graph Manager

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the Filter Graph Manager stops the graph, it waits for all streaming threads to shut down. This has the following implications for filters:

-   A filter must never call methods on the Filter Graph Manager from a streaming thread.

    The Filter Graph Manager uses a critical section to synchronize its own operations. If a streaming thread tries to hold this critical section, it can cause a deadlock. For example: Suppose that another thread stops the graph. That thread takes the filter graph lock and waits for your filter to stop delivering data. If your filter is waiting for the lock, it will never stop, causing a deadlock.

-   A filter must never **AddRef** or **QueryInterface** the Filter Graph Manager from a streaming thread.

    If the filter holds a reference count on the Filter Graph Manager (through **AddRef** or **QueryInterface**), it might become the last object to hold a reference count. When the filter calls **Release**, the Filter Graph Manager destroys itself. Inside its cleanup routine, the Filter Graph Manager attempts to stop the graph, causing it to wait for the streaming thread to exit. However, it is waiting inside the streaming thread, so the streaming thread cannot exit. The result is a deadlock.

 

 



