---
title: Detecting Windows Media Player from an Application
description: Detecting Windows Media Player from an Application
ms.assetid: 3cf8a619-3b7e-45af-af6b-4711a45c7e07
keywords:
- Windows Media Player,detecting from applications
- detecting Windows Media Player from applications
- registry,detecting Windows Media Player from applications
ms.topic: article
ms.date: 05/31/2018
---

# Detecting Windows Media Player from an Application

You can determine what version of Windows Media Player is installed by checking the following registry key:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Active Setup\\Installed Components**

For Windows Media Player 6.4, look at key **{22d6f312-b0f6-11d0-94ab-0080c74c7e95}**.

For Windows Media Player 7 or later, look at key **{6BF52A52-394A-11d3-B153-00C04F79FAA6}**.

Under either of these keys, if the **IsInstalled**<dl> <dt>

Data type
</dt> <dd>DWORD</dd> </dl> DWORD value is set to 0x1, you can safely use the **Version**<dl> <dt>

Data type
</dt> <dd>string</dd> </dl> string value as the version of Windows Media Player that is installed.

## Related topics

<dl> <dt>

[**Redistributing Windows Media Player Software**](redistributing-windows-media-player-software.md)
</dt> </dl>

 

 




