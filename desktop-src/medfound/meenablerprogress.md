---
Description: 'Signals the progress of a content enabler object. Objects that expose the IMFContentEnabler interface can raise this event to notify the application about the progress of the content enabler''s actions.'
ms.assetid: 'ec14ba9b-cfb6-4e32-870e-2436e11c308b'
title: MEEnablerProgress event
---

# MEEnablerProgress event

Signals the progress of a content enabler object. Objects that expose the [**IMFContentEnabler**](imfcontentenabler.md) interface can raise this event to notify the application about the progress of the content enabler's actions.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE               | Description                                                               |
|-----------------------|---------------------------------------------------------------------------|
| VT\_LPWSTR<br/> | Wide-character string that describes the progress.<br/> <br/> |



## Remarks

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

 

 




