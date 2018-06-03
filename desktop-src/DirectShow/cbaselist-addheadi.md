---
Description: The AddHeadI method adds an item to the front of the list.
ms.assetid: d83b3c5e-2c6d-4369-a74d-18bf19cfd34d
title: CBaseList.AddHeadI method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.AddHeadI method

The `AddHeadI` method adds an item to the front of the list.

## Syntax


```C++
POSITION AddHeadI(
   void *pObj
);
```



## Parameters

<dl> <dt>

*pObj* 
</dt> <dd>

Pointer to the item.

</dd> </dl>

## Return value

Returns a POSITION value indicating the new head position.

## Remarks

If the method fails, the return value is **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




