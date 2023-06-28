---
description: The AddAfterI method inserts an item after the specified position.
ms.assetid: 6da6c1ed-5f22-4364-b636-64b5a0ce1560
title: CBaseList.AddAfterI method (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.AddAfterI
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseList.AddAfterI method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AddAfterI` method inserts an item after the specified position.

## Syntax


```C++
POSITION AddAfterI(
   POSITION pos,
   void     *pObj
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position after which to add the item.

</dd> <dt>

*pObj* 
</dt> <dd>

Pointer to the item to add.

</dd> </dl>

## Return value

Returns the position indicator of the inserted item.

## Remarks

If *pos* is **NULL**, this method adds the item to the head of the list (equivalent to calling the [**CBaseList::AddHeadI**](cbaselist-addheadi.md) method).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




