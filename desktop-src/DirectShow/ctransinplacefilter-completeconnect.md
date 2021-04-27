---
description: CTransInPlaceFilter.CompleteConnect method - The CompleteConnect method completes a pin connection.
ms.assetid: 0c02c455-dbd0-4606-b1b1-f965c2a5805b
title: CTransInPlaceFilter.CompleteConnect method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.CompleteConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.CompleteConnect method

The `CompleteConnect` method completes a pin connection.

## Syntax


```C++
HRESULT CompleteConnect(
   PIN_DIRECTION direction,
   IPin          *pReceivePin
);
```



## Parameters

<dl> <dt>

*direction* 
</dt> <dd>

Member of the [**PIN\_DIRECTION**](/windows/win32/api/strmif/ne-strmif-pin_direction) enumerated type, specifying which pin on the filter is making the connection.

</dd> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the other pin in this connection attempt.

</dd> </dl>

## Return value

Returns an **HRESULT**. Possible values include those shown in the following table.



| Return code                                                                                           | Description                                     |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                             |
| <dl> <dt>**VFW\_E\_NOT\_IN\_GRAPH**</dt> </dl> | The filter is not in a filter graph.<br/> |



 

## Remarks

This method overrides the [**CTransformFilter::CompleteConnect**](ctransformfilter-completeconnect.md) method.

The behavior of the filter depends on the order of the pin connections:

-   If the input pin is connected first, the connection uses a temporary allocator. When the output pin is connected, the filter reconnects the input pin. Reconnecting the input pin causes the upstream filter to renegotiate the allocator. At that point, the input pin proposes an allocator from the downstream filter. For more information, see [**CTransInPlaceInputPin::GetAllocator**](ctransinplaceinputpin-getallocator.md).
-   If the output pin is connected first, the output pin does not select an allocator. When the input pin is connected, it negotiates an allocator for both connections. If the input and output media types are not the same, the filter reconnects the output pin using the input type.

The filter performs all pin reconnections by calling the [**CBaseFilter::ReconnectPin**](cbasefilter-reconnectpin.md) method. The **ReconnectPin** method, in turn, calls the [**IFilterGraph2::ReconnectEx**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph2-reconnectex) method on the filter graph manager.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




