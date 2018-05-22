---
Description: 'Raised by a content enabler object when the object's enabling action is completed.'
ms.assetid: '5162800c-9c55-40de-be66-a98765324f76'
title: MEEnablerCompleted event
---

# MEEnablerCompleted event

Raised by a content enabler object when the object's enabling action is completed. Objects that expose the [**IMFContentEnabler**](imfcontentenabler.md) interface can raise this event. The event is raised if either of the following occurs:

-   The [**IMFContentEnabler::AutomaticEnable**](imfcontentenabler-automaticenable.md) method completes asynchronously.
-   The application calls [**IMFContentEnabler::MonitorEnable**](imfcontentenabler-monitorenable.md), and then the application completes the HTTP POST request, as described in the **MonitorEnable** method.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

The status code from the event may contain one of the following values.



|                                      |                                                                                                                                                                                 |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **S\_OK**                            | The operation succeeded.                                                                                                                                                        |
| **NS\_E\_DRM\_LICENSE\_NOTACQUIRED** | The DRM license was not acquired. If the previous attempt used [**AutomaticEnable**](imfcontentenabler-automaticenable.md), the application should try non-silent acquisition. |
| **NS\_S\_DRM\_MONITOR\_CANCELLED**   | The [**MonitorEnable**](imfcontentenabler-monitorenable.md) operation was canceled.                                                                                            |



 

To receive this event, query the [**IMFContentEnabler**](imfcontentenabler.md) interface for the [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) interface. Then call [**IMFMediaEventGenerator::BeginGetEvent**](imfmediaeventgenerator-begingetevent.md), as described in the topic [Media Event Generators](media-event-generators.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFContentEnabler**](imfcontentenabler.md)
</dt> <dt>

[Media Event Generators](media-event-generators.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




