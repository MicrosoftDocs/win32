---
description: The CompleteConnect method completes a connection to another pin.
ms.assetid: 10cbf29c-2e1a-419c-b0c0-c99f9a285810
title: CBasePin.CompleteConnect method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CompleteConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.CompleteConnect method

The `CompleteConnect` method completes a connection to another pin.

## Syntax


```C++
virtual HRESULT CompleteConnect(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the other pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method is called on both pins at the end of the connection process. The connecting pin calls it from within the [**CBasePin::Connect**](cbasepin-connect.md) method, and the receiving pin calls it from within the [**CBasePin::ReceiveConnection**](cbasepin-receiveconnection.md) method.

In the base class, this method simply returns S\_OK. If a derived class has any requirements for completing a connection, it should override this method. For example, the [**CBaseOutputPin**](cbaseoutputpin.md) class uses this method to decide the memory allocator.

If this method fails, the overall connection attempt also fails, and the pin disconnects from the receiving pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




