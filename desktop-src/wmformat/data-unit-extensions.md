---
title: Data Unit Extensions
description: Data Unit Extensions
ms.assetid: 5dc0a596-68ae-409a-9abc-15ca507d6ec7
keywords:
- Windows Media Format SDK,data unit extensions
- Advanced Systems Format (ASF),data unit extensions
- ASF (Advanced Systems Format),data unit extensions
- Windows Media Format SDK,payload extension systems
- Advanced Systems Format (ASF),payload extension systems
- ASF (Advanced Systems Format),payload extension systems
- data unit extensions,about
- payload unit extensions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Unit Extensions

The Windows Media Format SDK enables you to supplement data in samples with *data unit extensions*, also called payload extension systems. This documentation uses the term "data unit extensions" in order to remain consistent with method names such as [**AddDataUnitExtension**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension?branch=master). A data unit extension is a name/value pair that is attached to the sample in the data section of the file. You can access the extended data using methods of the buffer object when the sample is retrieved by the reader.

You can create data unit extensions to your own specifications, but several types are predefined and supported by the objects of this SDK. These standard extensions are used to provide additional data for file names (in script and Web streams), SMPTE time code data, non-square pixel aspect ratio, duration, and type of interlacing.

To use data unit extensions, you must configure the stream to accept them, and then add extensions to each sample for that stream.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Configuring Data Unit Extensions**](configuring-data-unit-extensions.md)
</dt> <dt>

[**Setting Data Unit Extensions**](setting-data-unit-extensions.md)
</dt> </dl>

 

 




