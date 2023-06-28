---
title: User Allocated Sample Support
description: User Allocated Sample Support
ms.assetid: c747139e-e157-4ea0-9132-256dc70e2b15
keywords:
- Windows Media Format SDK,user allocated sample support
- Advanced Systems Format (ASF),user allocated sample support
- ASF (Advanced Systems Format),user allocated sample support
- user allocated sample support
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# User Allocated Sample Support

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Under normal circumstances, both the reader object and the synchronous reader object create a new buffer object for each sample delivered to your application. This is because the reading object has no way of knowing what your application does with the samples after it gets them. Even though many applications read samples only to render them immediately, some applications may need to maintain samples for a long time. The reading object cannot, therefore, reuse any of the buffers it allocates; it delivers them to your application, which then has control over them.

The problem with this approach is that a file can contain an immense number of samples. If each one of them requires a new buffer object to be created, a lot of processor time is wasted allocating and releasing memory. In time-sensitive applications such as media players, this overhead can be very detrimental to performance.

To alleviate the performance issues of reader-allocated samples, both the reader and the synchronous reader support user-allocated samples. To use samples allocated by your application, the reading object makes calls to a sample allocation callback method that you implement. The logic used by the callback to deliver buffers to the reading object is entirely up to you. You can use a pool of buffers for the entire file or use multiple pools of buffers, one for each output or stream, or any other scheme that works for your application.

## Related topics

<dl> <dt>

[**Allocating Buffers for File Reading**](allocating-buffers-for-file-reading.md)
</dt> <dt>

[**File Reading Features**](file-reading-features.md)
</dt> </dl>

 

 




