---
Description: The AddTail method appends a list to the end of the list.
ms.assetid: 006cccc5-4fb2-4e3f-9481-5d10c090d24e
title: CGenericList.AddTail method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CGenericList.AddTail method

The `AddTail` method appends a list to the end of the list.

## Syntax


```C++
BOOL AddTail(
   CGenericList<OBJECT> pList
);
```



## Parameters

<dl> <dt>

*pList* 
</dt> <dd>

Pointer to the list to append.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




