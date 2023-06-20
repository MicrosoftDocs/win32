---
description: The MoveToHead method splits the list and inserts the tail portion at the head of another list.
ms.assetid: 46e4f8fe-6707-44c6-9d49-0168b35d2364
title: CBaseList.MoveToHead method (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.MoveToHead
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseList.MoveToHead method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `MoveToHead` method splits the list and inserts the tail portion at the head of another list.

## Syntax


```C++
BOOL MoveToHead(
   POSITION  pos,
   CBaseList *pList
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position indicator that marks the split in the list.

</dd> <dt>

*pList* 
</dt> <dd>

Pointer to another list.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

This method splits the list before the position specified by the *pos* parameter. The head portion remains in the list. The tail portion is inserted at the head of the other list.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




