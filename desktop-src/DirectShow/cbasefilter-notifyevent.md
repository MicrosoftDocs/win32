---
description: The NotifyEvent method sends an event notification to the filter graph manager.
ms.assetid: 79587b72-4152-4443-9fde-c2746bf06191
title: CBaseFilter.NotifyEvent method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.NotifyEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.NotifyEvent method

The `NotifyEvent` method sends an event notification to the filter graph manager.

## Syntax


```C++
HRESULT NotifyEvent(
   long     EventCode,
   LONG_PTR EventParam1,
   LONG_PTR EventParam2
);
```



## Parameters

<dl> <dt>

*EventCode* 
</dt> <dd>

Event notification code.

</dd> <dt>

*EventParam1* 
</dt> <dd>

First parameter of the event.

</dd> <dt>

*EventParam2* 
</dt> <dd>

Second parameter of the event.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                               | Description                                                                                            |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | The filter graph manager is not accepting event notifications.<br/>                              |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                                                                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Filter does not have a pointer to the [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink) interface.<br/> |



 

## Remarks

For a list of notification codes and parameter values, see [Event Notification Codes](event-notification-codes.md).

In the base class, if the event code is EC\_COMPLETE, the method sets the *EventParam2* parameter to a pointer to the filter's [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




