---
description: This class implements the IAMStreamControl interface for input and output pins.
ms.assetid: a0ddc2d5-8385-4209-b1c5-9822c30f8a02
title: CBaseStreamControl class (Strmctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseStreamControl class

![cbasestreamcontrol class hierarchy](images/strmctl1.png)

This class implements the [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol) interface for input and output pins. It provides control over starting and stopping an individual pin on the filter. A pin that supports **IAMStreamControl** should inherit from this base class. The following is a typical declaration for an input pin:

``` syntax
class CMyInputPin : public CBaseInputPin, public CBaseStreamControl
```

Be sure to override **NonDelegatingQueryInteface** to expose **IAMStreamControl**. For more information, see [How to Implement IUnknown](how-to-implement-iunknown.md).



| Public Methods                                                        | Description                                                                                          |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**CBaseStreamControl**](cbasestreamcontrol-cbasestreamcontrol.md)   | Constructor method.                                                                                  |
| [**~CBaseStreamControl**](cbasestreamcontrol--cbasestreamcontrol.md) | Destructor method.                                                                                   |
| [**CheckStreamState**](cbasestreamcontrol-checkstreamstate.md)       | Determines whether a media sample should be delivered or discarded.                                  |
| [**Flushing**](cbasestreamcontrol-flushing.md)                       | Notifies the base class that the pin has started or stopped flushing.                                |
| [**NotifyFilterState**](cbasestreamcontrol-notifyfilterstate.md)     | Notifies the pin when the filter's state changes.                                                    |
| [**SetFilterGraph**](cbasestreamcontrol-setfiltergraph.md)           | Specifies the event sink for stream control events.                                                  |
| [**SetSyncSource**](cbasestreamcontrol-setsyncsource.md)             | Notifies the base class of the current reference clock.                                              |
| IAMStreamControl Methods                                              | Description                                                                                          |
| [**GetInfo**](cbasestreamcontrol-getinfo.md)                         | Retrieves information about the current stream-control settings, including the start and stop times. |
| [**StartAt**](cbasestreamcontrol-startat.md)                         | Informs the pin when to start delivering data.                                                       |
| [**StopAt**](cbasestreamcontrol-stopat.md)                           | Informs the pin when to stop delivering data.                                                        |



 

## Remarks

This class requires the pin and the owning filter to notify the class when various events occur, such as the filter joining the graph or receiving a new reference clock. You should call the following class methods:

-   In the filter's [**IMediaFilter::SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) method, call the [**CBaseStreamControl::SetSyncSource**](cbasestreamcontrol-setsyncsource.md) method. This method notifies the class of the current reference clock.
-   In the filter's [**CBaseFilter::JoinFilterGraph**](cbasefilter-joinfiltergraph.md) method, call the [**CBaseStreamControl::SetFilterGraph**](cbasestreamcontrol-setfiltergraph.md) method. This method gives the class a pointer to the Filter Graph Manager, so that the class can send the right stream-control events.
-   Whenever the filter changes state (to running, paused, or stopped), call the [**CBaseStreamControl::NotifyFilterState**](cbasestreamcontrol-notifyfilterstate.md) method.
-   In the pin's [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) and [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) methods, call the [**CBaseStreamControl::Flushing**](cbasestreamcontrol-flushing.md) method.

The `CBaseStreamControl` class uses the filter graph's reference clock to determine which samples the filter should be deliver, and which it should discard. In your pin's [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method, call the [**CBaseStreamControl::CheckStreamState**](cbasestreamcontrol-checkstreamstate.md) method with a pointer to the incoming media sample. If the method returns the value STREAM\_FLOWING, deliver the sample downstream. Otherwise, discard it.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




