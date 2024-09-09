---
description: Saves the filter's data to the given stream.
ms.assetid: f45c8c6e-f0bb-4358-805a-da2669706d34
title: CPersistStream.Save method (Pstream.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.Save
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPersistStream.Save method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Saves the filter's data to the given stream.

## Syntax


```C++
HRESULT Save(
   LPSTREAM pStm,
   BOOL     fClearDirty
);
```



## Parameters

<dl> <dt>

*pStm* 
</dt> <dd>

Pointer to the stream to which data is to be saved.

</dd> <dt>

*fClearDirty* 
</dt> <dd>

Flag that indicates whether to reset the current stream's dirty flag; **TRUE** means to reset it. (When the method is called as part of a Save operation, the value is typically **TRUE**; when called as part of a Save As operation, the value is typically **FALSE**.)

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the **IPersistStream::Save** method. It calls **WriteInt** with the software version, calls [**CPersistStream::WriteToStream**](cpersiststream-writetostream.md) with the stream in *pStm*, and resets **mPS\_fDirty**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




