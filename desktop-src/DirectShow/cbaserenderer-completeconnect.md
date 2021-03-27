---
description: The CompleteConnect method completes the input pin's connection to another pin.
ms.assetid: 8dfc1a50-bc73-436a-a471-d8d3218410d3
title: CBaseRenderer.CompleteConnect method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CompleteConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.CompleteConnect method

The `CompleteConnect` method completes the input pin's connection to another pin.

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

Pointer to the output pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The filter's input pin calls this method from inside its own `CompleteConnect` method, which is called in order to complete a pin connection. (For more information, see [**CBasePin::CompleteConnect**](cbasepin-completeconnect.md).) The filter calls the [**CBaseRenderer::SetRepaintStatus**](cbaserenderer-setrepaintstatus.md) method to enable [**EC\_REPAINT**](ec-repaint.md) events.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




