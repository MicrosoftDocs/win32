---
Description: The GetNext method retrieves the item at the specified position, and advances the position.
ms.assetid: d24d3388-1af9-4a62-bdb6-d3d3f5b0b97a
title: CGenericList.GetNext method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CGenericList.GetNext method

The `GetNext` method retrieves the item at the specified position, and advances the position.

## Syntax


```C++
OBJECT* GetNext(
  [ref] POSITION &amp;rp
);
```



## Parameters

<dl> <dt>

*rp* \[ref\]
</dt> <dd>

Reference to a POSITION value.

</dd> </dl>

## Return value

Returns a pointer to an object of type **OBJECT** (the template type).

## Remarks

This method advances the position indicator to the next position. If the position indicator moves past the end of the list, the method sets it to **NULL**.

If *rp* is **NULL**, the method returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




