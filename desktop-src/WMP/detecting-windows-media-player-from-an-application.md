---
title: Detecting Windows Media Player from an Application
description: Detecting Windows Media Player from an Application
ms.assetid: 3cf8a619-3b7e-45af-af6b-4711a45c7e07
keywords:
- Windows Media Player,detecting from applications
- detecting Windows Media Player from applications
- registry,detecting Windows Media Player from applications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Detecting Windows Media Player from an Application

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




