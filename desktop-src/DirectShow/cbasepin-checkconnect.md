---
description: CBasePin.CheckConnect method - The CheckConnect method determines whether a pin connection is suitable.
ms.assetid: 511a1594-f3f8-4725-afcd-f14f3a4ebf20
title: CBasePin.CheckConnect method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CheckConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.CheckConnect method

The `CheckConnect` method determines whether a pin connection is suitable.

## Syntax


```C++
virtual HRESULT CheckConnect(
   IPin *pPin
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the other pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                               | Description                                   |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success.<br/>                           |
| <dl> <dt>**VFW\_E\_INVALID\_DIRECTION**</dt> </dl> | Pin directions are not compatible.<br/> |



 

## Remarks

This method is called on both pins at the start of the connection process. The connecting pin calls it from within the [**CBasePin::Connect**](cbasepin-connect.md) method, and the receiving pin calls it from within the [**CBasePin::ReceiveConnection**](cbasepin-receiveconnection.md) method.

Use this method to determine whether the pin specified by the *pPin* parameter is suitable for a connection. The base class returns an error if both pins have the same direction (both input, or both output). Derived classes can override this method to verify other features in the pin. For example, the [**CBaseOutputPin**](cbaseoutputpin.md) class queries the input pin for its [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface.

If this method fails, the connection fails and the pin calls the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method. Use **BreakConnect** to free any resources obtained in `CheckConnect`. For example, if `CheckConnect` calls the **QueryInterface** method, **BreakConnect** must release the interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




