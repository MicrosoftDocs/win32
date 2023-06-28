---
title: Silent Acquisition Registry Setting
description: Silent Acquisition Registry Setting
ms.assetid: 50e0b27e-ddf8-441f-adcd-d88d36f3edaf
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Silent Acquisition Registry Setting

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft Windows Media Player uses the following registry value to determine whether to enable silent acquisition, a state in which the player downloads usage rights automatically when the user plays or syncs protected content.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**MediaPlayer**\\**Preferences**\\**SilentAcquisition**

The SilentAcquisition value has the following form:



| Name              | Type           | Description                                                                                                       |
|-------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| SilentAcquisition | **REG\_DWORD** | Set this value to 1 to enable silent acquisition, or set it to 0 to disable silent acquisition. The default is 1. |



 

To specify a value, the user can start Windows Media Player, open the **Options** dialog box, click the **Privacy** tab, and then select or clear the **Download usage rights automatically when I play or sync a file** check box. Selecting this check box sets SilentAcquisition to 1; clearing the check box sets it to 0.

## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> </dl>

 

 




