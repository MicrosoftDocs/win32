---
description: Passes an EC\_VIDEO\_SIZE\_CHANGED message to the filter graph manager.
ms.assetid: 39cb4f30-c12d-49bd-8d8a-70bf686b680d
title: CBaseControlVideo.OnVideoSizeChange method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.OnVideoSizeChange
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.OnVideoSizeChange method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Passes an EC\_VIDEO\_SIZE\_CHANGED message to the filter graph manager.

## Syntax


```C++
virtual HRESULT OnVideoSizeChange();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                   | Description               |
|-----------------------------------------------------------------------------------------------|---------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Failure.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/> |



 

## Remarks

A video renderer should call this member function each time the video size is changed; this will typically be called once after initial connection. If the renderer can support dynamic format changes (from 320 x 240 to 160 x 120), it should also call it after each change.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




