---
Description: 'Raised by a media source that provides topologies through the IMFMediaSourceTopologyProvider interface, such as the sequencer source. The source raises the event when it has a new presentation. The Media Session forwards this event to the application.'
ms.assetid: 'c669b2c9-5ece-4045-b691-8a71bbf491e1'
title: MENewPresentation event
---

# MENewPresentation event

Raised by a media source that provides topologies through the [**IMFMediaSourceTopologyProvider**](imfmediasourcetopologyprovider.md) interface, such as the sequencer source. The source raises the event when it has a new presentation. The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFPresentationDescriptor**](imfpresentationdescriptor.md) interface of the presentation descriptor for the new presentation.<br/> <br/> |



## Remarks

The application can get the topology that corresponds to the presentation descriptor by calling [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](imfmediasourcetopologyprovider-getmediasourcetopology.md) on the media source. The application can then queue the new topology on the Media Session by calling [**IMFMediaSession::SetTopology**](imfmediasession-settopology.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 




