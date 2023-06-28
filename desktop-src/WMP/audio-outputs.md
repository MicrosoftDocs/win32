---
title: Audio Outputs
description: Audio Outputs
ms.assetid: 2bedf804-c9fd-4a44-9289-e36a50517b7f
keywords:
- Windows Media Player,audio outputs
- Windows Media Player,Default DirectSound Device
- Windows Media Player,eConsole
- Windows Media Player,eMultimedia
- Windows Media Player,eCommunications
- audio outputs
- Default DirectSound Device
- eConsole
- eMultimedia
- eCommunications
- Windows Media Player ActiveX control,audio outputs
- Windows Media Player ActiveX control,Default DirectSound Device
- Windows Media Player ActiveX control,eConsole
- Windows Media Player ActiveX control,eMultimedia
- Windows Media Player ActiveX control,eCommunications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Outputs

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Control Panel in Windows XP enables the user to assign the name Default DirectSound Device to a particular audio output device. In Windows Vista, the Control Panel lets the user assign each of three names (eConsole, eMultimedia, and eCommunications) to an audio output device. These names can all be assigned to different devices, or multiple names can be assigned to the same device. The following table shows how Windows Media Player and the Windows Media Player ActiveX control choose default audio output devices.



|       &nbsp;                               | Windows XP                                                                                                                                                                                | Windows Vista                                                                                                                                                              |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media Player                 | By default, the Player uses the audio device designated as Default DirectSound Device. The Player provides a dialog box that lets the user switch the Player to a different audio device. | By default, the Player uses the audio device designated as eMultimedia. The Player provides a dialog box that lets the user switch the Player to a different audio device. |
| Windows Media Player ActiveX control | By default, the Player control uses the audio device designated as Default DirectSound Device. The audio output device cannot be changed programmatically.                                | By default, the Player control uses the audio device designated as eMultimedia. The audio output device cannot be changed programmatically.                                |



 

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




