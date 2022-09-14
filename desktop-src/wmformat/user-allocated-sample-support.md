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
ms.date: 05/31/2018
---

# User Allocated Sample Support

Under normal circumstances, both the reader object and the synchronous reader object create a new buffer object for each sample delivered to your application. This is because the reading object has no way of knowing what your application does with the samples after it gets them. Even though many applications read samples only to render them immediately, some applications may need to maintain samples for a long time. The reading object cannot, therefore, reuse any of the buffers it allocates; it delivers them to your application, which then has control over them.

The problem with this approach is that a file can contain an immense number of samples. If each one of them requires a new buffer object to be created, a lot of processor time is wasted allocating and releasing memory. In time-sensitive applications such as media players, this overhead can be very detrimental to performance.

To alleviate the performance issues of reader-allocated samples, both the reader and the synchronous reader support user-allocated samples. To use samples allocated by your application, the reading object makes calls to a sample allocation callback method that you implement. The logic used by the callback to deliver buffers to the reading object is entirely up to you. You can use a pool of buffers for the entire file or use multiple pools of buffers, one for each output or stream, or any other scheme that works for your application.

## Related topics

<dl> <dt>

[**Allocating Buffers for File Reading**](allocating-buffers-for-file-reading.md)
</dt> <dt>

[**File Reading Features**](file-reading-features.md)
</dt> </dl>

 

 




