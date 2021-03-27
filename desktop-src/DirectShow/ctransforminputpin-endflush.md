---
description: The EndFlush method ends a flush operation. This method implements the IPin::EndFlush method.
ms.assetid: ebc70df3-e99d-4292-990b-99b79ff06461
title: CTransformInputPin.EndFlush method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformInputPin.EndFlush method

The `EndFlush` method ends a flush operation. This method implements the [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) method.

## Syntax


```C++
HRESULT EndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                             |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                     |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | Output pin is not connected.<br/> |



 

## Remarks

This method calls the filter's [**CTransformFilter::EndFlush**](ctransformfilter-endflush.md) method to deliver the call downstream. Then it calls the pin's [**CBaseInputPin::EndFlush**](cbaseinputpin-endflush.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




