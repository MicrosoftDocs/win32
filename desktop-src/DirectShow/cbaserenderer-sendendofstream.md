---
description: If end-of-stream was reached, the SendEndOfStream method schedules an EC\_COMPLETE event for the filter graph manager.
ms.assetid: 3c10c956-e352-4796-a8cd-cc69a02066f2
title: CBaseRenderer.SendEndOfStream method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SendEndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.SendEndOfStream method

If end-of-stream was reached, the `SendEndOfStream` method schedules an EC\_COMPLETE event for the filter graph manager.

## Syntax


```C++
virtual HRESULT SendEndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                             | Description                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The filter graph manager is not accepting event notifications.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                                       |



 

## Remarks

The filter might receive an end-of-stream notification before the current sample's stop time. If so, the filter should wait before posting an [**EC\_COMPLETE**](ec-complete.md) notification to the filter graph manager.

Therefore:

-   If the filter has received an early end-of-stream (EOS) notification, this method schedules a timer event. When the timer event is activated, the filter posts the EC\_COMPLETE event.
-   If the filter has received an EOS notification that was not early, this method posts the EC\_COMPLETE event immediately.
-   If the filter does not have any pending EOS notification, the method returns without doing anything.

The timer callback method is [**CBaseRenderer::TimerCallback**](cbaserenderer-timercallback.md). To deliver the EC\_COMPLETE event, the filter calls the [**CBaseRenderer::NotifyEndOfStream**](cbaserenderer-notifyendofstream.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




