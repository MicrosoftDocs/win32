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
ms.date: 05/31/2018
---

# Runtime Registry Entry

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

 

 




