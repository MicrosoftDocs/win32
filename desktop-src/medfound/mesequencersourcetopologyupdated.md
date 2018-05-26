---
Description: Raised by the sequencer source when the IMFSequencerSourceUpdateTopology method completes asynchronously.
ms.assetid: f573cbd0-689c-4bfe-846b-6fc8008101c8
title: MESequencerSourceTopologyUpdated event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MESequencerSourceTopologyUpdated event

Raised by the sequencer source when the [**IMFSequencerSource::UpdateTopology**](/windows/win32/mfidl/nf-mfidl-imfsequencersource-updatetopology?branch=master) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE            | Description                                                                                                                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VT\_UI4<br/> | Sequencer element identifier of the topology that is being updated. The application specifies this value in the *dwId* parameter of the [**UpdateTopology**](/windows/win32/mfidl/nf-mfidl-imfsequencersource-updatetopology?branch=master) method.<br/> <br/> |



## Remarks

This event signals that the sequencer source has updated the topology, but does not mean that the topology is ready for playback. The application should wait for the [MESessionTopologyStatus](mesessiontopologystatus.md) event.

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

 

 




