---
Description: The AddHead method inserts another list at the front of this list.
ms.assetid: 10999d93-2eb0-481f-8909-6f1184137786
title: CBaseList.AddHead method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.AddHead method

The `AddHead` method inserts another list at the front of this list.

## Syntax


```C++
BOOL AddHead(
   CBaseList *pList
);
```



## Parameters

<dl> <dt>

*pList* 
</dt> <dd>

Pointer to the list of items to add.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

If the method fails, some items might have been added to the list.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




