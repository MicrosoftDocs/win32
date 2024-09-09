---
description: The AddBefore method inserts a list before the specified position.
ms.assetid: a4c0dbec-64a0-445b-95e5-000603cc0264
title: CBaseList.AddBefore method (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.AddBefore
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseList.AddBefore method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AddBefore` method inserts a list before the specified position.

## Syntax


```C++
BOOL AddBefore(
   POSITION  pos,
   CBaseList *pList
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position before which to insert the list.

</dd> <dt>

*pList* 
</dt> <dd>

Pointer to the list to insert.

</dd> </dl>

## Return value

Returns **TRUE** if successful. Otherwise, returns **FALSE**.

## Remarks

Existing position indicators, including the one specified in the *pos* parameter, remain valid. If the method fails, some of the items might have been added.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




