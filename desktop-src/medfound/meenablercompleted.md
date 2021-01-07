---
description: Raised by a content enabler object when the objects enabling action is completed.
ms.assetid: 5162800c-9c55-40de-be66-a98765324f76
title: MEEnablerCompleted event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEEnablerCompleted event

Raised by a content enabler object when the object's enabling action is completed. Objects that expose the [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) interface can raise this event. The event is raised if either of the following occurs:

-   The [**IMFContentEnabler::AutomaticEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-automaticenable) method completes asynchronously.
-   The application calls [**IMFContentEnabler::MonitorEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-monitorenable), and then the application completes the HTTP POST request, as described in the **MonitorEnable** method.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

The status code from the event may contain one of the following values.



|                                      |                                                                                                                                                                                 |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **S\_OK**                            | The operation succeeded.                                                                                                                                                        |
| **NS\_E\_DRM\_LICENSE\_NOTACQUIRED** | The DRM license was not acquired. If the previous attempt used [**AutomaticEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-automaticenable), the application should try non-silent acquisition. |
| **NS\_S\_DRM\_MONITOR\_CANCELLED**   | The [**MonitorEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-monitorenable) operation was canceled.                                                                                            |



 

To receive this event, query the [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) interface for the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. Then call [**IMFMediaEventGenerator::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent), as described in the topic [Media Event Generators](media-event-generators.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler)
</dt> <dt>

[Media Event Generators](media-event-generators.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




