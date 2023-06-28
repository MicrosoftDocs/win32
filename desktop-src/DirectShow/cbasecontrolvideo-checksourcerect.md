---
description: Determines if a source rectangle is valid.
ms.assetid: 3fef107b-6f4c-4fab-91d3-6ab72dcc32be
title: CBaseControlVideo.CheckSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.CheckSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.CheckSourceRect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Determines if a source rectangle is valid.

## Syntax


```C++
virtual HRESULT CheckSourceRect(
   RECT *pSourceRect
);
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the source rectangle to check.

</dd> </dl>

## Return value

Returns E\_INVALIDARG if not valid; otherwise, returns NOERROR (S\_OK).

## Remarks

This member function checks that the source rectangle requested does not exceed the available source video. The left and top coordinates cannot be negative, and the width and height cannot exceed the right and bottom of the video.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




