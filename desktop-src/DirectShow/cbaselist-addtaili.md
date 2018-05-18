---
Description: 'The AddTailI method adds an item to the end of the list.'
ms.assetid: '699408d1-fee2-43d7-b2c3-51637d063b2c'
title: 'CBaseList.AddTailI method'
---

# CBaseList.AddTailI method

The `AddTailI` method adds an item to the end of the list.

## Syntax


```C++
POSITION AddTailI(
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

Returns a POSITION value for the new tail position.

## Remarks

If the method fails, it returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




