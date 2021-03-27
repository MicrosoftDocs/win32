---
description: The Run method notifies the pin that the filter is now running. This method overrides the CBasePin::Run method.
ms.assetid: ee0285aa-9afd-464a-b8b4-d8b7faa49dbd
title: CRenderedInputPin.Run method (Amextra.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRenderedInputPin.Run
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRenderedInputPin.Run method

The `Run` method notifies the pin that the filter is now running. This method overrides the [**CBasePin::Run**](cbasepin-run.md) method.

## Syntax


```C++
HRESULT Run(
   REFERENCE_TIME tStart
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

The start time that was passed to the filter's [**IMediaFilter::Run**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-run) method.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amextra.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRenderedInputPin Class**](crenderedinputpin.md)
</dt> </dl>

 

 




