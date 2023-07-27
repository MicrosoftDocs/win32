---
description: The GetCurrentImage method retrieves a copy of the current image at the renderer.
ms.assetid: fa322bd2-18e4-481d-bde1-92deb0f7de61
title: CBaseControlVideo.GetCurrentImage method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetCurrentImage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.GetCurrentImage method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetCurrentImage` method retrieves a copy of the current image at the renderer.

## Syntax


```C++
HRESULT GetCurrentImage(
   long *pBufferSize,
   long *pVideoImage
);
```



## Parameters

<dl> <dt>

*pBufferSize* 
</dt> <dd>

Pointer to the size of the output buffer.

</dd> <dt>

*pVideoImage* 
</dt> <dd>

Pointer to the output buffer for the image.

</dd> </dl>

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                        | Description                                                                       |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Failure.<br/>                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Invalid argument.<br/>                                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Out of memory. Returned when the *pVideoInfo* parameter is **NULL**.<br/>   |
| <dl> <dt>**NOERROR**</dt> </dl>             | Success.<br/>                                                               |
| <dl> <dt>**VFW\_E\_NOT\_PAUSED**</dt> </dl> | The operation could not be performed because the filter is not paused.<br/> |



 

## Remarks

This member function retrieves the image from the sample and copies it into the output buffer. The section of video copied into the output buffer reflects the source rectangle set through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface. It does not reflect the destination rectangle.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




