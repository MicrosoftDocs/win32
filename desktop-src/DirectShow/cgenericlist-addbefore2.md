---
Description: The AddBefore method inserts a list before the specified position.
ms.assetid: 0fdb2a59-d9de-4dbb-8536-8e10726201d0
title: CGenericList.AddBefore method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CGenericList.AddBefore method

The `AddBefore` method inserts a list before the specified position.

## Syntax


```C++
BOOL AddBefore(
   POSITION             pos,
   CGenericList<OBJECT> *pList
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position to insert the list. The list is inserted before this position.

</dd> <dt>

*pList* 
</dt> <dd>

Pointer to the list to insert.

</dd> </dl>

## Return value

Returns **TRUE** if successful. Otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




