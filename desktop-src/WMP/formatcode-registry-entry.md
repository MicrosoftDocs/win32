---
title: FormatCode Registry Entry
description: FormatCode Registry Entry
ms.assetid: cc444eaa-6898-48ab-9573-9e7d5e25d6db
keywords:
- Windows Media Player,FormatCode registry entries
- Windows Media Player,file name extensions
- Windows Media Player,registry
- registry,file name extensions
- registry,FormatCode entries
- registry,settings for Windows Media Player
- file name extension registry settings
- FormatCode registry entries
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# FormatCode Registry Entry

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player encounters a custom file name extension, it looks for a registry subkey that matches the extension. The subkey is described in [File Name Extension Registry Settings](file-name-extension-registry-settings.md). One of the registry entries that can appear under the extension's subkey is the **FormatCode** entry.

The **FormatCode** registry entry specifies the Media Transport Protocol (MTP) format code for files that have the custom extension. The **FormatCode** registry entry has the following form.



| Name       | Type           | Value                                                             |
|------------|----------------|-------------------------------------------------------------------|
| FormatCode | **REG\_DWORD** | A 16-bit positive integer that identifies the format of the file. |



 

When the user attempts to copy a digital media file that has a custom file name extension to a portable device, Windows Media Player looks in the registry to find a format code associated with the custom file name extension. If Windows Media Player finds a format code, it uses MTP to determine whether the device supports the custom file format. If the device supports the format, the media file is copied to the device without being transcoded.

A device that supports MTP can supply Windows Media Player with a DeviceInfo dataset, which contains, among other things, a list of format codes supported by the device.

If you are in the process of developing a custom file format, you can request a format code from Microsoft. For information about how to request a format code, see the Microsoft Media Transport Protocol Porting Kit, which is available at the [Microsoft Windows Media Developer Center](https://msdn.microsoft.com/windowsmedia/default.aspx).

## Related topics

<dl> <dt>

[**File Name Extension Registry Settings**](file-name-extension-registry-settings.md)
</dt> </dl>

 

 




