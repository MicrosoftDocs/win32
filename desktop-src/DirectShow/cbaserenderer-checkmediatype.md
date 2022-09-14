---
description: The CheckMediaType method determines if the filter accepts a specific media type.
ms.assetid: 90d26cf6-443c-4a06-98c6-ffa14e27ee41
title: CBaseRenderer.CheckMediaType method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.CheckMediaType method

The `CheckMediaType` method determines if the filter accepts a specific media type.

## Syntax


```C++
virtual HRESULT CheckMediaType(
   const CMediaType *pmt
) = 0;
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the proposed media type.

</dd> </dl>

## Return value

Returns S\_OK if the proposed media type is acceptable. Otherwise, returns S\_FALSE or an error code.

## Remarks

The input pin calls this method from its own [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method. The derived class must implement this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




