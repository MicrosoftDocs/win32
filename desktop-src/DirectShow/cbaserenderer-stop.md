---
description: The Stop method stops the filter.
ms.assetid: 80eac207-5db3-4b06-bbae-eca72e37d09d
title: CBaseRenderer.Stop method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.Stop
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.Stop method

The `Stop` method stops the filter.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method overrides the [**CBaseFilter::Stop**](cbasefilter-stop.md) method. It performs the following actions:

-   Calls [**CBaseFilter::Stop**](cbasefilter-stop.md).
-   Decommits the allocator. (See [**IMemAllocator::Decommit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-decommit).)
-   Cancels any scheduled rendering and releases the streaming thread.
-   Waits for any pending **Receive** call to complete.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




