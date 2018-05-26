---
Description: The CheckConnect method determines whether a pin connection is suitable.
ms.assetid: b8ace40d-31f5-49b0-a4cd-6ece0f883d96
title: CTransformInputPin.CheckConnect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformInputPin.CheckConnect method

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

Pointer to the output pin's [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                               | Description                    |
|-----------------------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success<br/>             |
| <dl> <dt>**VFW\_E\_INVALID\_DIRECTION**</dt> </dl> | Wrong pin direction<br/> |



 

## Remarks

This method overrides the [**CBasePin::CheckConnect**](cbasepin-checkconnect.md) method. It calls the filter's [**CTransformFilter::CheckConnect**](ctransformfilter-checkconnect.md) method, which returns S\_OK in the base class. The derived class can override the **CTransformFilter::CheckConnect** method to perform additional checks.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




