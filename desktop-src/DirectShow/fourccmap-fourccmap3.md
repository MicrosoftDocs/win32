---
description: "A constructor method that provides the mapping between old-style multimedia format DWORD types and GUID subtypes. This method uses the 'pguid' parameter."
ms.assetid: 4de6cb49-938e-42f8-8687-dc60a0f23e87
title: FOURCCMap::FOURCCMap constructor (Fourcc.h) - pguid parameter
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

# FOURCCMap::FOURCCMap constructor (Fourcc.h) - pguid parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method. The constuctor provides the mapping between old-style multimedia format **DWORD** types and **GUID** subtypes.

## Syntax


```C++
FOURCCMap(
   const GUID *pguid
);
```



## Parameters

<dl> <dt>

*pguid* 
</dt> <dd>

Pointer to the globally unique identifier (**GUID**).

</dd> </dl>

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

 

 




