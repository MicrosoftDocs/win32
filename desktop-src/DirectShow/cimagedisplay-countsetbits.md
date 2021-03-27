---
description: The CountSetBits method returns the number of bits set to 1 in a specified bit field.
ms.assetid: fc5701b8-88ff-4c23-9d26-854bb65cc55c
title: CImageDisplay.CountSetBits method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.CountSetBits
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.CountSetBits method

The `CountSetBits` method returns the number of bits set to 1 in a specified bit field.

## Syntax


```C++
DWORD CountSetBits(
   const DWORD Field
);
```



## Parameters

<dl> <dt>

*Field* 
</dt> <dd>

Specifies a bit field as a **DWORD** value.

</dd> </dl>

## Return value

Returns the number of bits that are set to 1.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




