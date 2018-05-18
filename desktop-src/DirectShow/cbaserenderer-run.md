---
Description: 'The Run method runs the filter.'
ms.assetid: '83251137-83f8-45a3-b3f2-d7b45f43f7f8'
title: 'CBaseRenderer.Run method'
---

# CBaseRenderer.Run method

The `Run` method runs the filter.

## Syntax


```C++
HRESULT Run();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method overrides the [**CBaseFilter::Run**](cbasefilter-run.md) method. It performs the following actions:

-   Calls the **CBaseFilter::Run** method.
-   Commits the allocator. (See [**IMemAllocator::Commit**](imemallocator-commit.md).)
-   If the previous state was stopped, the filter releases any sample it is holding. (The sample is no longer valid.)
-   Calls the [**CBaseRenderer::StartStreaming**](cbaserenderer-startstreaming.md) method and returns the result. If a sample is pending, the **StartStreaming** method schedules it for rendering.

If the filter is not connected, it posts an [**EC\_COMPLETE**](ec-complete.md) event immediately.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




