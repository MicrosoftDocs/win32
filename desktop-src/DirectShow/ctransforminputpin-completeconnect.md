---
Description: The CompleteConnect method completes a connection to another pin.
ms.assetid: 568cee55-b9ea-4fc2-ac9d-0080b7de9790
title: CTransformInputPin.CompleteConnect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformInputPin.CompleteConnect method

The `CompleteConnect` method completes a connection to another pin.

## Syntax


```C++
HRESULT CompleteConnect(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the other pin's [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method overrides the [**CBasePin::CompleteConnect**](cbasepin-completeconnect.md) method. It calls the filter's [**CTransformFilter::CompleteConnect**](ctransformfilter-completeconnect.md) method, which returns S\_OK in the base class. The derived class can override the **CTransformFilter::CompleteConnect** method to perform additional checks.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




