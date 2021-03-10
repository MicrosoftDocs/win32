---
description: Topology Attributes
ms.assetid: 50102096-a29f-4c00-a685-179ba5d71089
title: Topology Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Topology Attributes

The following attributes apply to topologies.



| Attribute                                                                                                | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MF\_TOPOLOGY\_DXVA\_MODE](mf-topology-dxva-mode.md)                                                    | Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology.                                                                                                                         |
| [MF\_TOPOLOGY\_DYNAMIC\_CHANGE\_NOT\_ALLOWED](mf-topology-dynamic-change-not-allowed.md)                | Specifies whether the Media Session attempts to modify the topology when the format of a stream changes.                                                                                                                           |
| [MF\_TOPOLOGY\_ENABLE\_XVP\_FOR\_PLAYBACK](mf-topology-enable-xvp-for-playback.md)                | Specifies whether the topology loader enables the Transcode Video Processor (XVP). for conversions, enabling hardware accelerated color conversion.                                                                                        |
| [MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES](mf-topology-enumerate-source-types.md)                         | Specifies whether the topology loader enumerates the media types provided by the media source.                                                                                                                                     |
| [MF\_TOPOLOGY\_HARDWARE\_MODE](mf-topology-hardware-mode.md)                                            | Specifies whether to include hardware-based transforms in the topology.                                                                                                                                                            |
| [**MF\_TOPOLOGY\_NO\_MARKIN\_MARKOUT**](mf-topology-no-markin-markout-attribute.md)                     | Specifies whether the pipeline trims samples.                                                                                                                                                                                      |
| [MF\_TOPOLOGY\_PLAYBACK\_FRAMERATE](mf-topology-playback-framerate.md)                                  | Specifies the monitor refresh rate.                                                                                                                                                                                                |
| [MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS](mf-topology-playback-max-dims.md)                                   | Specifies the size of the destination window for video playback.                                                                                                                                                                   |
| [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md)                                 | Specifies the topology start time within the current segment, in 100-nanosecond units.                                                                                                                                             |
| [**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md)                                   | Specifies the topology stop time within the current segment, in 100-nanosecond units.                                                                                                                                              |
| [**MF\_TOPOLOGY\_RESOLUTION\_STATUS**](mf-topology-resolution-status-attribute.md)                      | Specifies the status of an attempt to resolve a topology.                                                                                                                                                                          |
| [MF\_TOPOLOGY\_START\_TIME\_ON\_PRESENTATION\_SWITCH](mf-topology-start-time-on-presentation-switch.md) | Specifies the start time for presentations that are queued after the first presentation.                                                                                                                                           |
| [MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS](mf-topology-static-playback-optimizations.md)           | Enables static optimizations in the video pipeline.                                                                                                                                                                                |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md)                                | Contains an [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer, which is used to unlock an MFT with field-of-use restrictions. For more information, see [Field of Use Restrictions](field-of-use-restrictions.md). |



 

## Related topics

<dl> <dt>

[**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 



