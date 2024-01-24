---
title: Data Unit Extensions
description: Data Unit Extensions
ms.assetid: 'f95de189-0449-4b88-aba3-7b19f385c8fe'
keywords:
- Windows Media Format SDK,data unit extensions
- Advanced Systems Format (ASF),data unit extensions
- ASF (Advanced Systems Format),data unit extensions
- Windows Media Format SDK,payload extension systems
- Advanced Systems Format (ASF),payload extension systems
- ASF (Advanced Systems Format),payload extension systems
- data unit extensions,about
- payload unit extensions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Data Unit Extensions

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK enables you to supplement data in samples with *data unit extensions*, also called payload extension systems. This documentation uses the term "data unit extensions" in order to remain consistent with method names such as [**AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension). A data unit extension is a name/value pair that is attached to the sample in the data section of the file. You can access the extended data using methods of the buffer object when the sample is retrieved by the reader.

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

 

 




