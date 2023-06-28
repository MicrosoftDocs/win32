---
description: The get\_DestinationHeight method retrieves the current destination rectangle height.
ms.assetid: 0001d98a-3a5c-47f1-8f5e-ce464d64131a
title: CBaseControlVideo.get_DestinationHeight method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.get_DestinationHeight
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.get\_DestinationHeight method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `get_DestinationHeight` method retrieves the current destination rectangle height.

## Syntax


```C++
HRESULT get_DestinationHeight(
   long *pDestinationHeight
);
```



## Parameters

<dl> <dt>

*pDestinationHeight* 
</dt> <dd>

Pointer to the destination height.

</dd> </dl>

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                           | Description                                                                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>                | Failure.<br/>                                                              |
| <dl> <dt>**E\_POINTER**</dt> </dl>             | **NULL** pointer argument.<br/>                                            |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The operation cannot be performed because the pins are not connected.<br/> |
| <dl> <dt>**NOERROR**</dt> </dl>                | Success.<br/>                                                              |



 

## Remarks

This member function implements the [**IBasicVideo::get\_DestinationHeight**](/windows/desktop/api/Control/nf-control-ibasicvideo-get_destinationheight) method.

An application can change the source and destination rectangles for the video through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface. The source rectangle affects which section of the native video source will appear on the display; the destination rectangle affects where it will be played. The destination rectangle is relative to the client area of the window that it is playing in. The upper-left corner of the window is coordinate (0,0).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




