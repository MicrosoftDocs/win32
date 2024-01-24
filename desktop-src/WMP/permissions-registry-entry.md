---
title: Permissions Registry Entry
description: Permissions Registry Entry
ms.assetid: 01d55d2d-fe29-4006-a34b-9fbc730f9cbc
keywords:
- Windows Media Player,file name extensions
- Windows Media Player,permissions
- Windows Media Player,registry
- registry,file name extensions
- registry,permissions
- registry,settings for Windows Media Player
- file name extension registry settings
- permissions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Permissions Registry Entry

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player encounters a custom file name extension, it looks for a registry subkey that matches the extension. The subkey is described in [File Name Extension Registry Settings](file-name-extension-registry-settings.md). One of the registry entries that can appear under the extension's subkey is the **Permissions** entry.

The **Permissions** entry specifies the actions that Windows Media Player is allowed to perform on files that have the custom extension. The **Permissions** entry has the following form.



| Name        | Type           | Value                                                                  |
|-------------|----------------|------------------------------------------------------------------------|
| Permissions | **REG\_DWORD** | A set of flags, each of which grants permission for a specific action. |



 

The value of the **Permissions** entry is a bitwise **OR** of one or more of the following flags.



| Flag (decimal value) | Description                                                                                                                                                                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                    | Permission for playback. Files having the registered file name extension can be played.                                                                                                                                                                                       |
| 2                    | Permission for folder drop. Files having the registered file name extension will be included in the playlist created when the user drags a folder containing the files and drops it on the user interface of the Player.                                                      |
| 4                    | Permission for media CD. Files having the registered file name extension will be included in the playlist created when a CD containing the files is inserted into the CD-ROM drive.                                                                                           |
| 8                    | Permission for the library. Files having the registered file name extension can be added to the library. Required for conversion plug-ins.                                                                                                                                    |
| 16                   | Permission for HTML streaming. Files having the registered file name extension will be inserted into the Internet Explorer cache when delivered from a Web stream.                                                                                                            |
| 128                  | Permission for transcoding. Files having the registered file name extension can be transcoded to Windows Media Format under certain conditions. See [IWMPTranscodePolicy::allowTranscode](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmptranscodepolicy-allowtranscode). Requires Windows Media Player 10 or later. |



 

When the user attempts to play a media file that has a custom file name extension, Windows Media Player looks for a registry subkey that matches the extension. If no match is found, the Player presents the user with a warning dialog box that prompts the user for permission to attempt to play the file. If you create digital media files with custom file name extensions, you can prevent this warning from appearing on the user's computer by registering the file name extension and providing a **Permissions** entry.

The **Permissions** entry (except for the flag value 128) is supported by Windows Media Player 9 Series and later. The flag value 128 is supported by Windows Media Player 10 and later.

## Related topics

<dl> <dt>

[**File Name Extension Registry Settings**](file-name-extension-registry-settings.md)
</dt> </dl>

 

 




