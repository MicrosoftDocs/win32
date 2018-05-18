---
Description: 'The CheckConnect method determines whether a pin connection is suitable.'
ms.assetid: '3dae5c6d-720e-4445-b601-3bdfe32f4c21'
title: 'CTransformOutputPin.CheckConnect method'
---

# CTransformOutputPin.CheckConnect method

The `CheckConnect` method determines whether a pin connection is suitable.

## Syntax


```C++
HRESULT CheckConnect(
   IPin *pPin
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the output pin's [**IPin**](ipin.md) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                 |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | The filter's input pin is not connected.<br/> |



 

## Remarks

This method overrides the [**CBaseOutputPin::CheckConnect**](cbaseoutputpin-checkconnect.md) method. It calls the filter's [**CTransformFilter::CheckConnect**](ctransformfilter-checkconnect.md) method, which returns S\_OK in the base class. The derived class can override the **CTransformFilter::CheckConnect** method to perform additional checks.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




