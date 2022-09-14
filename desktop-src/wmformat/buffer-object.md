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
ms.date: 05/31/2018
---

# Buffer Object

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

 

 




