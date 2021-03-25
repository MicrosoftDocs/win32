---
description: Constructor method. The constructor obtains access to the specified pin.
ms.assetid: 518d41aa-8361-4769-aa9b-14676b676d6f
title: CAutoUsingOutputPin.CAutoUsingOutputPin constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAutoUsingOutputPin.CAutoUsingOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAutoUsingOutputPin.CAutoUsingOutputPin constructor

Constructor method. The constructor obtains access to the specified pin.

## Syntax


```C++
CAutoUsingOutputPin(
   CDynamicOutputPin *pOutputPin,
   HRESULT           *phr
);
```



## Parameters

<dl> <dt>

*pOutputPin* 
</dt> <dd>

Pointer to a [**CDynamicOutputPin**](cdynamicoutputpin.md) object.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that contains an **HRESULT** value. The value must be S\_OK.

</dd> </dl>

## Remarks

When the method returns, the value of *\*phr* indicates the success or failure of the method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAutoUsingOutputPin Class**](cautousingoutputpin-cautousingoutputpin.md)
</dt> </dl>

 

 




