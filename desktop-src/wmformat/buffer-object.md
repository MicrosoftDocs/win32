---
title: Buffer Object
description: Buffer Object
ms.assetid: 0812261c-698c-4071-929c-4363a16dd5a8
keywords:
- Windows Media Format SDK,buffer objects
- Advanced Systems Format (ASF),buffer objects
- ASF (Advanced Systems Format),buffer objects
- objects,buffer objects
- buffer objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Buffer Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A buffer object is used to hold samples and deliver them between the objects of the Windows Media Format SDK and your application. When you write a file, you pass your input samples to the writer using buffer objects. When you read a file, the reader object or synchronous reader object provides samples to your application in buffer objects.

For writing samples to a file, you can create a buffer object using the [**IWMWriter::AllocateSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample) method. For reading samples, the reader object and synchronous reader object both create buffer objects internally. If you choose to, you can allocate your own buffer objects for file reading by using [**IWMReaderAllocatorEx::AllocateForOutputEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforoutputex) or [**IWMReaderAllocatorEx::AllocateForStreamEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforstreamex).

The following interfaces are supported by every buffer object.



| Interface                          | Description                                                          |
|------------------------------------|----------------------------------------------------------------------|
| [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer)   | Controls and provides access to the buffer.                          |
| [**INSSBuffer2**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer2) | Not implemented.                                                     |
| [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) | Supports buffer properties, which are used for data unit extensions. |
| [**INSSBuffer4**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer4) | Enumerates buffer properties.                                        |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




