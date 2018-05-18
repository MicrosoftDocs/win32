---
title: Buffer Object
description: Buffer Object
ms.assetid: '0812261c-698c-4071-929c-4363a16dd5a8'
keywords: ["Windows Media Format SDK,buffer objects", "Advanced Systems Format (ASF),buffer objects", "ASF (Advanced Systems Format),buffer objects", "objects,buffer objects", "buffer objects"]
---

# Buffer Object

A buffer object is used to hold samples and deliver them between the objects of the Windows Media Format SDK and your application. When you write a file, you pass your input samples to the writer using buffer objects. When you read a file, the reader object or synchronous reader object provides samples to your application in buffer objects.

For writing samples to a file, you can create a buffer object using the [**IWMWriter::AllocateSample**](iwmwriter-allocatesample.md) method. For reading samples, the reader object and synchronous reader object both create buffer objects internally. If you choose to, you can allocate your own buffer objects for file reading by using [**IWMReaderAllocatorEx::AllocateForOutputEx**](iwmreaderallocatorex-allocateforoutputex.md) or [**IWMReaderAllocatorEx::AllocateForStreamEx**](iwmreaderallocatorex-allocateforstreamex.md).

The following interfaces are supported by every buffer object.



| Interface                          | Description                                                          |
|------------------------------------|----------------------------------------------------------------------|
| [**INSSBuffer**](inssbuffer.md)   | Controls and provides access to the buffer.                          |
| [**INSSBuffer2**](inssbuffer2.md) | Not implemented.                                                     |
| [**INSSBuffer3**](inssbuffer3.md) | Supports buffer properties, which are used for data unit extensions. |
| [**INSSBuffer4**](inssbuffer4.md) | Enumerates buffer properties.                                        |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




