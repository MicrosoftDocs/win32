---
description: The ISampleGrabber interface is exposed by the Sample Grabber filter. It enables an application to retrieve individual media samples as they move through the filter graph.
ms.assetid: 97cf1127-d5d7-4e6a-a371-19f24e497a7f
title: ISampleGrabber interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabber interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **ISampleGrabber** interface is exposed by the [**Sample Grabber**](sample-grabber-filter.md) filter. It enables an application to retrieve individual media samples as they move through the filter graph.

## Members

The **ISampleGrabber** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ISampleGrabber** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISampleGrabber** interface has these methods.



| Method                                                                | Description                                                                                                                       |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**GetConnectedMediaType**](isamplegrabber-getconnectedmediatype.md) | Retrieves the media type for the connection on the input pin of Sample Grabber.<br/>                                        |
| [**GetCurrentBuffer**](isamplegrabber-getcurrentbuffer.md)           | Retrieves a copy of the sample that the filter received most recently.<br/>                                                 |
| [**GetCurrentSample**](isamplegrabber-getcurrentsample.md)           | Not implemented.<br/>                                                                                                       |
| [**SetBufferSamples**](isamplegrabber-setbuffersamples.md)           | Specifies whether to copy sample data into a buffer as it goes through the filter.<br/>                                     |
| [**SetCallback**](isamplegrabber-setcallback.md)                     | Specifies a callback method to call on incoming samples.<br/>                                                               |
| [**SetMediaType**](isamplegrabber-setmediatype.md)                   | Specifies the media type for the connection on the input pin of the Sample Grabber.<br/>                                    |
| [**SetOneShot**](isamplegrabber-setoneshot.md)                       | Specifies whether the [**Sample Grabber**](sample-grabber-filter.md) filter halts after the filter receives a sample.<br/> |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> </dl>

 

 
