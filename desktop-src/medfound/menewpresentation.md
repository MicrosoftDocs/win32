---
Description: Raised by a media source that provides topologies through the IMFMediaSourceTopologyProvider interface, such as the sequencer source. The source raises the event when it has a new presentation. The Media Session forwards this event to the application.
ms.assetid: c669b2c9-5ece-4045-b691-8a71bbf491e1
title: MENewPresentation event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MENewPresentation event

Raised by a media source that provides topologies through the [**IMFMediaSourceTopologyProvider**](/windows/win32/mfidl/nn-mfidl-imfmediasourcetopologyprovider?branch=master) interface, such as the sequencer source. The source raises the event when it has a new presentation. The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master) interface of the presentation descriptor for the new presentation.<br/> <br/> |



## Remarks

The application can get the topology that corresponds to the presentation descriptor by calling [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](/windows/win32/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology?branch=master) on the media source. The application can then queue the new topology on the Media Session by calling [**IMFMediaSession::SetTopology**](/windows/win32/mfidl/nf-mfidl-imfmediasession-settopology?branch=master).

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

 

 




