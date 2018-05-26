---
Description: The BeginFlush method begins a flush operation. This method implements the IPinBeginFlush method.
ms.assetid: 7c76ca06-dc3c-4f9a-9761-32aea7db4c7e
title: CTransformInputPin.BeginFlush method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformInputPin.BeginFlush method

The `BeginFlush` method begins a flush operation. This method implements the [**IPin::BeginFlush**](/windows/win32/Strmif/nf-strmif-ipin-beginflush?branch=master) method.

## Syntax


```C++
HRESULT BeginFlush();
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

This method calls the pin's [**CBaseInputPin::BeginFlush**](cbaseinputpin-beginflush.md) method. Then it calls the filter's [**CTransformFilter::BeginFlush**](ctransformfilter-beginflush.md) method to deliver the call downstream.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




