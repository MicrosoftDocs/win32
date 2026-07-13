---
description: The GetConnectedMediaType method retrieves the media type for the connection on the input pin of the Sample Grabber.
ms.assetid: 65f5603a-1151-4ffd-a662-84e265663b04
title: ISampleGrabber::GetConnectedMediaType method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber.GetConnectedMediaType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# ISampleGrabber::GetConnectedMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetConnectedMediaType` method retrieves the media type for the connection on the input pin of the Sample Grabber.

## Syntax


```C++
HRESULT GetConnectedMediaType(
   AM_MEDIA_TYPE *pType
);
```



## Parameters

<dl> <dt>

*pType* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure allocated by the caller.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                           | Description                             |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl>             | **NULL** pointer argument.<br/>   |
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                     |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The filter is not connected.<br/> |



 

## Remarks

This method copies the media type into the **AM\_MEDIA\_TYPE** structure specified by *pType*. The caller must free the format block of the media type. You can use the **CoTaskMemFree** function, or the [**FreeMediaType**](freemediatype.md) function in the base-class library.

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
</dt> <dt>

[**ISampleGrabber Interface**](isamplegrabber.md)
</dt> </dl>

 

 




