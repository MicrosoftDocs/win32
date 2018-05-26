---
Description: The CheckMediaType method determines if the pin accepts a specific media type.
ms.assetid: 2d5f784a-8970-487d-94ef-d96d04f8eb2e
title: CTransInPlaceInputPin.CheckMediaType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransInPlaceInputPin.CheckMediaType method

The `CheckMediaType` method determines if the pin accepts a specific media type.

## Syntax


```C++
HRESULT CheckMediaType(
   const CMediaType *pmt
);
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

This method overrides the [**CTransformInputPin::CheckMediaType**](ctransforminputpin-checkmediatype.md) method. It calls the filter's [**CTransformFilter::CheckInputType**](ctransformfilter-checkinputtype.md) method to check the input type. If the output pin is connected, this method also calls the [**IPin::QueryAccept**](/windows/win32/Strmif/nf-strmif-ipin-queryaccept?branch=master) method on the downstream input pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




