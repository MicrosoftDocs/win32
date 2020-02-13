---
title: Allocating Buffers for File Reading
description: Allocating Buffers for File Reading
ms.assetid: da66ef5b-ec92-445c-90ba-5ee89e0def36
keywords:
- Windows Media Format SDK,reading ASF files
- Advanced Systems Format (ASF),reading files
- ASF (Advanced Systems Format),reading files
- Windows Media Format SDK,allocating buffers
- Advanced Systems Format (ASF),allocating buffers
- ASF (Advanced Systems Format),allocating buffers
- Advanced Systems Format (ASF),buffer allocation
- ASF (Advanced Systems Format),buffer allocation
- buffer allocation
ms.topic: article
ms.date: 05/31/2018
---

# Allocating Buffers for File Reading

In the most basic file-reading scenario, the buffers used to deliver samples are allocated by the reading object (the reader object or the synchronous reader object). You can, however, allocate buffers yourself. For more information about the benefits of allocating your own buffers, see [User Allocated Sample Support](user-allocated-sample-support.md).

To use your own buffers for file reading, perform the following steps.

1.  Implement a callback or callbacks for the reader to call when it needs a buffer. If you are reading output samples, use [**IWMReaderAllocatorEx::AllocateForOutputEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforoutputex). If you are reading stream samples, use [**IWMReaderAllocatorEx::AllocateForStreamEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforstreamex). Include whatever logic for managing buffers that suits your application.
2.  Allocate a pool of buffers that you will use for file reading.
    -   Find the size required for your buffers by calling [**IWMReaderAdvanced::GetMaxOutputSampleSize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getmaxoutputsamplesize) or [**IWMReaderAdvanced::GetMaxStreamSampleSize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getmaxstreamsamplesize) for each output and/or stream for which the buffer is used. If using the synchronous reader, use [**IWMSyncReader::GetMaxOutputSampleSize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getmaxoutputsamplesize) or [**IWMSyncReader::GetMaxStreamSampleSize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getmaxstreamsamplesize) instead.
    -   Create each buffer for the pool.
3.  Set up the reader or synchronous reader for reading. For more information see [Reading Files with the Asynchronous Reader](reading-files-with-the-asynchronous-reader.md) or [Reading Files with the Synchronous Reader](reading-files-with-the-synchronous-reader.md).
4.  Before beginning writing, call [**IWMReaderAdvanced::SetAllocateForOutput**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setallocateforoutput) or [**IWMReaderAdvanced::SetAllocateForStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setallocateforstream) for each output and stream for which you are allocating buffers using the reader object. For the synchronous reader, call [**IWMSyncReader2::SetAllocateForOutput**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader2-setallocateforoutput) or [**IWMSyncReader2::SetAllocateForStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader2-setallocateforstream) instead.
5.  Begin reading the file.

The reading object will make calls to the appropriate allocator callback and get samples from your application. Your buffer management logic must include a way to signal that a buffer is free to be used again. Typically, a buffer is put back into the pool when its contents are rendered. Depending upon your application, you may need just a few buffers in the pool or many.

## Related topics

<dl> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> </dl>

 

 




