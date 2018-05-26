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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Buffer Object

A buffer object is used to hold samples and deliver them between the objects of the Windows Media Format SDK and your application. When you write a file, you pass your input samples to the writer using buffer objects. When you read a file, the reader object or synchronous reader object provides samples to your application in buffer objects.

For writing samples to a file, you can create a buffer object using the [**IWMWriter::AllocateSample**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample?branch=master) method. For reading samples, the reader object and synchronous reader object both create buffer objects internally. If you choose to, you can allocate your own buffer objects for file reading by using [**IWMReaderAllocatorEx::AllocateForOutputEx**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforoutputex?branch=master) or [**IWMReaderAllocatorEx::AllocateForStreamEx**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforstreamex?branch=master).

The following interfaces are supported by every buffer object.



| Interface                          | Description                                                          |
|------------------------------------|----------------------------------------------------------------------|
| [**INSSBuffer**](/windows/win32/wmsbuffer/nn-wmsbuffer-inssbuffer?branch=master)   | Controls and provides access to the buffer.                          |
| [**INSSBuffer2**](/windows/win32/wmsbuffer/nn-wmsbuffer-inssbuffer2?branch=master) | Not implemented.                                                     |
| [**INSSBuffer3**](/windows/win32/wmsbuffer/nn-wmsbuffer-inssbuffer3?branch=master) | Supports buffer properties, which are used for data unit extensions. |
| [**INSSBuffer4**](/windows/win32/wmsbuffer/nn-wmsbuffer-inssbuffer4?branch=master) | Enumerates buffer properties.                                        |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




