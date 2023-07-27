---
description: COPP Command Reference
ms.assetid: b21db1cf-cac3-41d6-8189-6e01c8f91a7d
title: COPP Command Reference
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# COPP Command Reference

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the Certified Output Protection Protocol (COPP) commands. The following commands are defined.



| Command              | GUID                             |
|----------------------|----------------------------------|
| Set Protection Level | **DXVA\_COPPSetProtectionLevel** |
| Set Signaling        | **DXVA\_COPPSetSignaling**       |



 

Set Protection Level Command

Sets the protection level for a specified output protection mechanism. Depending on the connector, it might be possible to apply more than one protection mechanism on the same connector, with different settings for each mechanism.

**GUID**: DXVA\_COPPSetProtectionLevel

**Input data**: A [**DXVA\_COPPSetProtectionLevelCmdData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppsetprotectionlevelcmddata) structure.

Set Signaling Command

Specifies information about the video signal other than the protection level.

For CGMS-A, certain protection standards require that the televsion signal contains information about the aspect ratio and other information within the same VBI waveform packets as the CGMS-A bits. Televisions may display poorly if the aspect ratio information is not consistent with the video stream. The application can use this command to specify the aspect ratio so that the graphics driver can generate the correct VBI packets.

This command is also designed to be extensible if additional signal information is required in future standards.

**GUID**: DXVA\_COPPSetSignaling

**Input data**: A [**DXVA\_COPPSetSignalingCmdData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppsetsignalingcmddata) structure.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



