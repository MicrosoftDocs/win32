---
description: The CBaseInputPin method begins a flush operation. This method implements the IPin::BeginFlush method.
ms.assetid: 3f149d4f-765b-44c1-87e5-6313f6a4d50d
title: CBaseInputPin.BeginFlush method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.BeginFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.BeginFlush method

The `CBaseInputPin` method begins a flush operation. This method implements the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method.

## Syntax


```C++
HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CBaseInputPin::m\_bFlushing**](cbaseinputpin-m-bflushing.md) flag to **TRUE**, which causes the [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method to reject any more samples.

The derived class must override this method and perform the following steps:

1.  Call the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method on downstream input pins. If the pin has not yet delivered any media samples downstream, you can skip this step. If your output pins derive from the [**CBaseOutputPin**](cbaseoutputpin.md) class, you can call the [**CBaseOutputPin::DeliverBeginFlush**](cbaseoutputpin-deliverbeginflush.md) method.
2.  Call the base class method.
3.  Begin discarding queued data.
4.  Return from any blocked calls to the **Receive** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




