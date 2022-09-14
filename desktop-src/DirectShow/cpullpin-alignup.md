---
description: The AlignUp method rounds a value up to a specified alignment boundary.Note  Removed in Windows 7. .
ms.assetid: fa2a6567-3eb1-4aa9-b966-2e88b15c67b1
title: CPullPin.AlignUp method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.AlignUp
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPullPin.AlignUp method

The **AlignUp** method rounds a value up to a specified alignment boundary.

> [!Note]  
> Removed in Windows 7.

 

## Syntax


```C++
LONGLONG AlignUp(
   LONGLONG ll,
   LONG     lAlign
);
```



## Parameters

<dl> <dt>

*ll* 
</dt> <dd>

Specifies the number to align.

</dd> <dt>

*lAlign* 
</dt> <dd>

Specifies the alignment boundary.

</dd> </dl>

## Return value

Returns the aligned result.

## Remarks

> [!Caution]  
> This method can cause numeric overflow if *ll* + (*lAlign* - 1) overflows.

 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




