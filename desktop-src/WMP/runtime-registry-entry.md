---
title: Runtime Registry Entry
description: Runtime Registry Entry
ms.assetid: 3b2880f9-acb9-4a13-8364-67fbe76f8d29
keywords:
- Windows Media Player,runtime registry entries
- Windows Media Player,file name extensions
- Windows Media Player,registry
- registry,file name extensions
- registry,runtime entries
- registry,settings for Windows Media Player
- file name extension registry settings
- runtime registry entries
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Runtime Registry Entry

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player encounters a custom file name extension, it looks for a registry subkey that matches the extension. The subkey is described in [File Name Extension Registry Settings](file-name-extension-registry-settings.md). One of the registry entries that can appear under the extension's subkey is the **Runtime** entry.

The **Runtime** entry specifies the underlying technology that Windows Media Player can use to play or convert digital media files that have the custom extension. The **Runtime** entry has the following form.



|   Name   |   Type         |   Value                                                       |
|----------|----------------|---------------------------------------------------------------|
| Runtime  | **REG\_DWORD** | A positive integer that identifies the underlying technology. |



 

The value of the **Runtime** entry must be one the following.



| **Value (decimal)** | **Description**                                                                            |
|---------------------|--------------------------------------------------------------------------------------------|
| 6                   | Render using the Windows Media Format SDK.                                                 |
| 7                   | Render using Microsoft DirectShow.                                                         |
| 13                  | Convert the file using the specified conversion plug-in. Requires Windows Media Player 11. |



 

The **Runtime** registry entry values 6 and 7 are supported by Windows Media Player 9 Series and later. The value 13 is supported by Windows Media Player 11.

## Related topics

<dl> <dt>

[**ConvertPluginCLSID Subkey**](convertpluginclsid-subkey.md)
</dt> <dt>

[**File Name Extension Registry Settings**](file-name-extension-registry-settings.md)
</dt> </dl>

 

 




