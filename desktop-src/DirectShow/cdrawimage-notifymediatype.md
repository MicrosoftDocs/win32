---
description: The NotifyMediaType method notifies the CDrawImage object of the current media type.
ms.assetid: 419d516f-4b96-47aa-80cc-ac785e65af8b
title: CDrawImage.NotifyMediaType method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.NotifyMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDrawImage.NotifyMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `NotifyMediaType` method notifies the **CDrawImage** object of the current media type.

## Syntax


```C++
void NotifyMediaType(
   CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object, or **NULL** to clear the media type.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method whenever the media type changes. Typically this occurs when the pin first connects, and after a dynamic format change.

The **CDrawImage** object stores the *pMediaType* pointer in the **m\_pMediaType** member variable. Therefore, if the caller needs to release the **CMediaType** object, it should update the **CDrawImage** object by calling this method again, either with a new pointer or with a **NULL** value. Otherwise, an error can occur when the **CDrawImage** object attempts to reference the old pointer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




