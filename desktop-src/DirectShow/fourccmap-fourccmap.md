---
description: A constructor method that provides the mapping between old-style multimedia format DWORD types and GUID subtypes. This method uses no parameters.
ms.assetid: 2152803c-f45f-43b0-9207-4eaeddf5eeb6
title: FOURCCMap::FOURCCMap constructor (Fourcc.h) - No parameters
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FOURCCMap.FOURCCMap
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# FOURCCMap::FOURCCMap constructor (Fourcc.h) - No parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method. The constuctor provides the mapping between old-style multimedia format **DWORD** types and **GUID** subtypes.

## Syntax


```C++
FOURCCMap();
```



## Parameters

This constructor has no parameters.

## Remarks

If this object is constructed with the **FOURCC** code, a **GUID** is created to match it. If this object is created with an existing **GUID**, the **FOURCC** value of the object is set to zero. Thereafter, the **FOURCC** value can be set or retrieved using the [**SetFOURCC**](fourccmap-setfourcc.md) and [**GetFOURCC**](fourccmap-getfourcc.md) member functions, respectively.

## Requirements


| Requirement | Value |
|-|-|
| Header  | Fourcc.h (include Streams.h) |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |



## See also

<dl> <dt>

[**FOURCCMap Class**](fourccmap.md)
</dt> </dl>

 

 




