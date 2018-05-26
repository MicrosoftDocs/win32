---
Description: The DeliverBeginFlush method requests the connected input pin to begin a flush operation.
ms.assetid: 0d7c7bd7-2a7a-42a4-a0de-60205b62e49c
title: CBaseOutputPin.DeliverBeginFlush method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseOutputPin.DeliverBeginFlush method

The `DeliverBeginFlush` method requests the connected input pin to begin a flush operation.

## Syntax


```C++
virtual HRESULT DeliverBeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                           | Description                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>              |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | Pin is not connected.<br/> |



 

## Remarks

This method calls the [**IPin::BeginFlush**](/windows/win32/Strmif/nf-strmif-ipin-beginflush?branch=master) method on the input pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




