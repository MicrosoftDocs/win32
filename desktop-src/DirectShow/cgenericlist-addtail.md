---
Description: The AddTail method appends an item to the end of the list.
ms.assetid: e365a23e-7447-42ec-b836-21dd68962db1
title: CGenericList.AddTail method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CGenericList.AddTail method

The `AddTail` method appends an item to the end of the list.

## Syntax


```C++
POSITION AddTail(
   OBJECT *pObj
);
```



## Parameters

<dl> <dt>

*pObj* 
</dt> <dd>

Pointer to an object of type **OBJECT** (the template type).

</dd> </dl>

## Return value

Returns a POSITION value for the new tail position. If the method fails, it returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




