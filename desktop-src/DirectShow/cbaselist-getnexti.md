---
description: The GetNextI method retrieves the item at the specified position, and advances the position.
ms.assetid: 3ec217ec-b0f9-4ff4-bdb7-ac204df99010
title: CBaseList.GetNextI method (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.GetNextI
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseList.GetNextI method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetNextI` method retrieves the item at the specified position, and advances the position.

## Syntax


```C++
void* GetNextI(
  [ref] POSITION &rp
);
```



## Parameters

<dl> <dt>

*rp* \[ref\]
</dt> <dd>

Reference to a POSITION value.

</dd> </dl>

## Return value

Returns a pointer to the item. If *rp* is **NULL**, the method returns **NULL**.

## Remarks

This method advances the position indicator to the next position. If the position indicator moves past the end of the list, the method sets it to **NULL**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




