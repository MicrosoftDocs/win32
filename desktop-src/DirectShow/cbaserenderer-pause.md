---
description: The Pause method pauses the filter.
ms.assetid: 9dfd23d1-bf07-424b-9952-13719358d0a5
title: CBaseRenderer.Pause method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.Pause
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.Pause method

The `Pause` method pauses the filter.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                             | Description                            |
|-----------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The transition is complete.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Transition is not complete.<br/> |



 

## Remarks

This method overrides the [**CBaseFilter::Pause**](cbasefilter-pause.md) method. It performs the following steps:

-   Calls the **CBaseFilter::Pause** method.
-   Commits the allocator. (See [**IMemAllocator::Commit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-commit).)
-   If the previous state was stopped, the filter releases any sample it is holding. (The sample is no longer valid.)
-   Calls the [**CBaseRenderer::CompleteStateChange**](cbaserenderer-completestatechange.md) method and returns the value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




