---
title: Silent Acquisition Registry Setting
description: Silent Acquisition Registry Setting
ms.assetid: 50e0b27e-ddf8-441f-adcd-d88d36f3edaf
ms.topic: article
ms.date: 05/31/2018
---

# Silent Acquisition Registry Setting

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

 

 




