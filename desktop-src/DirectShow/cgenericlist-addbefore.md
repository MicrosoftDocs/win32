---
description: "The AddBefore method inserts an item before the specified position. This method uses the 'p' and 'pObj' parameters."
ms.assetid: ec10fd08-6bb9-4357-830c-78b3d3a32e03
title: CGenericList.AddBefore method (Wxlist.h) - p, pObj parameters
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.AddBefore
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CGenericList.AddBefore method (Wxlist.h) - p, pObj parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AddBefore` method inserts an item before the specified position.

## Syntax


```C++
POSITION AddBefore(
   POSITION p,
   OBJECT   *pObj
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Position before which to insert the list. If *p* is **NULL**, this method adds the item to the tail of the list.

</dd> <dt>

*pObj* 
</dt> <dd>

Pointer to an object of type **OBJECT** (the template type).

</dd> </dl>

## Return value

Returns the position indicator for the inserted item.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




