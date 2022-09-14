---
description: The GetSourceRect method retrieves the current source rectangle.
ms.assetid: e9ca091f-3fd7-4e42-90e9-b7831dd488a9
title: CDrawImage.GetSourceRect method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.GetSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.GetSourceRect method

The `GetSourceRect` method retrieves the current source rectangle.

## Syntax


```C++
void GetSourceRect(
   RECT *pSourceRect
);
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to a **RECT** structure that receives the source rectangle.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




