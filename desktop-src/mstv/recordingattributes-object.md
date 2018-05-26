---
title: RecordingAttributes Object
description: RecordingAttributes Object
ms.assetid: dfb3e588-cf58-4f0f-a686-3aa7c7869247
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RecordingAttributes Object

This topic applies only to Windows XP Service Pack 1 or later.

The **Recording Attributes** object retrieves and updates metadata in the header of a Stream Buffer Engine recording file.



|            |                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------|
| CLSID      | CLSID\_StreamBufferRecordingAttributes                                                                                       |
| Interfaces | [**IFileSourceFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389981), [**IStreamBufferRecordingAttribute**](/windows/previous-versions/Sbe/nn-sbe-istreambufferrecordingattribute?branch=master) |



 

## Remarks

To use this object, call [**IFileSourceFilter::Load**](https://msdn.microsoft.com/library/windows/desktop/dd389983) and pass in the name of the recording file. Then query the object for the **IStreamBufferRecordingAttribute** interface and use this interface to retrieve or update the metadata.

Although this object exposes the **IFileSourceFilter** interface, it is not a DirectShow filter. It is a stand-alone COM object.

## Related topics

<dl> <dt>

[Stream Buffer Engine Objects](stream-buffer-engine-objects.md)
</dt> </dl>

 

 




