---
description: "Learn about the constructor method for CGenericList.CGenericList (Wxlist.h). This method uses 'pName' and 'iItems' parameters."
ms.assetid: 2258ecd6-7594-4ff8-961b-9e5e1ae9ff82
title: CGenericList.CGenericList constructor (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.CGenericList
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CGenericList.CGenericList constructor (Wxlist.h) - pName, iItems parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CGenericList(
   TCHAR *pName,
   INT   iItems,
   BOOL  bLock,
   BOOL  bAlert
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the list.

</dd> <dt>

*iItems* 
</dt> <dd>

Size of the node cache.

</dd> <dt>

*bLock* 
</dt> <dd>

Not used.

</dd> <dt>

*bAlert* 
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

For efficiency, the `CGenericList` class maintains a cache of list nodes. If you know approximately how many items the list will hold, use this version of the constructor.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




