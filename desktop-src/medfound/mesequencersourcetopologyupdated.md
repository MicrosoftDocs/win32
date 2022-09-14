---
description: Raised by the sequencer source when the IMFSequencerSource::UpdateTopology method completes asynchronously.
ms.assetid: f573cbd0-689c-4bfe-846b-6fc8008101c8
title: MESequencerSourceTopologyUpdated event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESequencerSourceTopologyUpdated event

Raised by the sequencer source when the [**IMFSequencerSource::UpdateTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-updatetopology) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE            | Description                                                                                                                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VT\_UI4<br/> | Sequencer element identifier of the topology that is being updated. The application specifies this value in the *dwId* parameter of the [**UpdateTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-updatetopology) method.<br/> <br/> |



## Remarks

This event signals that the sequencer source has updated the topology, but does not mean that the topology is ready for playback. The application should wait for the [MESessionTopologyStatus](mesessiontopologystatus.md) event.

## Requirements



| Requirement | Value |
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

 

 




