---
Description: The RemoveHead method removes the first item in the list.
ms.assetid: 95902028-d2c2-4c16-9ca6-ef57174a9292
title: CGenericList.RemoveHead method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CGenericList.RemoveHead method

The `RemoveHead` method removes the first item in the list.

## Syntax


```C++
OBJECT* RemoveHead();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to an object of type **OBJECT** (the template type), or **NULL** if the list is empty.

## Remarks

This method deletes the list node, but not the item that the node contains.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




