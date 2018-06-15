---
Description: Represents a request for a sample from a MediaStreamSource.
ms.assetid: 43617cda-84b1-405f-8a20-be793413c186
title: IMFMediaStreamSourceSampleRequest interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMFMediaStreamSourceSampleRequest interface

Represents a request for a sample from a MediaStreamSource.

## Members

The **IMFMediaStreamSourceSampleRequest** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IMFMediaStreamSourceSampleRequest** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMFMediaStreamSourceSampleRequest** interface has these methods.



| Method                                                           | Description                                             |
|:-----------------------------------------------------------------|:--------------------------------------------------------|
| [**SetSample**](imfmediastreamsourcesamplerequest-setsample.md) | Sets the sample for the media stream source.<br/> |



 

## Remarks

**MFMediaStreamSourceSampleRequest** is implemented by the [**Windows.Media.Core.MediaStreamSourceSampleRequest**](https://msdn.microsoft.com/en-us/library/Dn282723(v=WIN.10).aspx) runtime class.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                       |
| IDL<br/>                      | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Interfaces](media-foundation-interfaces.md)
</dt> </dl>

 

 




