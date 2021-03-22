---
description: The EqualPins function checks if two pins are on the same object.
ms.assetid: b6a92cb6-f4a9-4a14-831c-3b123e4692c0
title: EqualPins function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EqualPins
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# EqualPins function

The EqualPins function checks if two pins are on the same object.

## Syntax


```C++
BOOL EqualPins(
   IUnknown *pPin1,
   IUnknown *pPin2
);
```



## Parameters

<dl> <dt>

*pPin1* 
</dt> <dd>

Pointer to one pin.

</dd> <dt>

*pPin2* 
</dt> <dd>

Pointer to the other pin.

</dd> </dl>

## Return value

Returns **TRUE** if both pins are on the same object, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> </dl>

 

 




