---
description: The ReceiveCanBlock method determines whether calls to the IMemInputPin::Receive method might block. This method implements the IMemInputPin::ReceiveCanBlock method.
ms.assetid: db96e389-e1bc-4b38-8d0a-a20f0d3a4460
title: CBaseInputPin.ReceiveCanBlock method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.ReceiveCanBlock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.ReceiveCanBlock method

The `ReceiveCanBlock` method determines whether calls to the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method might block. This method implements the [**IMemInputPin::ReceiveCanBlock**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivecanblock) method.

## Syntax


```C++
HRESULT ReceiveCanBlock();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible value include those listed in the following table.



| Return code                                                                             | Description                                                 |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The pin will not block on a call to **Receive**.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | The pin might block on a call to **Receive**.<br/>    |



 

## Remarks

Return S\_FALSE if calls to the **Receive** method are guaranteed not to block. Otherwise, return S\_OK or an error code. If the **Receive** method calls **Receive** on a downstream pin, the downstream pin might block; `ReceiveCanBlock` must take that factor into account.

An upstream filter can use this method to determine its threading strategy. If the **Receive** method might block, the upstream filter might decide to use a worker thread that buffers data. See the [**COutputQueue**](coutputqueue.md) class for an implementation of this strategy.

In the base class, this method returns S\_OK when any of the following are true:

-   The filter has no output pins.
-   An input pin connected to this filter signals that it might block.
-   An input pin connected to this filter does not support the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




