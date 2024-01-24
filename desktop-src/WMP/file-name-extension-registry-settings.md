---
title: File Name Extension Registry Settings
description: File Name Extension Registry Settings
ms.assetid: a5c31cf7-e1e1-4f1a-8e94-ed08f99ad973
keywords:
- Windows Media Player,registry
- Windows Media Player,file name extensions
- registry,file name extensions
- registry,settings for Windows Media Player
- file name extension registry settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# File Name Extension Registry Settings

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If your digital media files have a custom format, you can provide Windows Media Player with information about your custom format by placing entries in the registry on the user's computer. Windows Media Player inspects your registry entries to determine how it should handle your files. The following list shows several of the things you can do by creating registry entries that pertain to your custom media file format.

-   Grant permission for the Player to play, copy, or transcode your files.
-   Specify the underlying technology that the Player should use to play your files.
-   Specify where the Player should display your files in its library view.
-   Specify a plug-in that the Player should use to convert your files to a standard format.
-   Specify a Media Transport Protocol (MTP) format code that the Player can use to determine whether a particular portable device supports your file format.

Most of the entries that you provide will be under a subkey that is associated with your custom file name extension. You can create that subkey in the HKEY\_LOCAL\_MACHINE subtree and in the HKEY\_CURRENT\_USER subtree. Windows Media Player looks first in the HKEY\_LOCAL\_MACHINE subtree. If it doesn't find what it needs there, it looks in the HKEY\_CURRENT\_USER subtree. Note that any code that attempts to write to the registry on the user's computer can write to the HKEY\_LOCAL\_MACHINE subtree only if the current user has administrative privileges.

To write information about your custom file format to the HKEY\_LOCAL\_MACHINE subtree, create the following subkey.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Multimedia\\WMPlayer\\Extensions\\** *customExtension*

where *customExtension* is the file name extension including the dot (.) separator. For example, if the extension for your custom file format is .xyz, create the following subkey.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Multimedia\\WMPlayer\\Extensions\\.xyz**

To write information about your custom file format to the HKEY\_CURRENT\_USER subtree, create the following subkey.

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Player\\Extensions\\** *customExtension*

You can write one or more of the following entries in your *customExtension* subkey.

-   **Permissions**
-   **Runtime**
-   **FormatCode**

To specify conversion plug-ins for your custom media file format, create a **ConvertPluginCLSID** subkey in your *customExtension* subkey.

To specify where Windows Media Player should display your files in its library view, write an entry that represents your custom file format in the following subkey.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MediaPlayer\\MLS\\Extensions**

The following topics describe the registry subkeys and entries that provide Windows Media Player with information about custom media file formats.

-   [Permissions Registry Entry](permissions-registry-entry.md)
-   [Runtime Registry Entry](runtime-registry-entry.md)
-   [FormatCode Registry Entry](formatcode-registry-entry.md)
-   [Library Classification Registry Entries](library-classification-registry-entries.md)
-   [ConvertPluginCLSID Subkey](convertpluginclsid-subkey.md)

## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> <dt>

[**Windows Media Player Conversion Plug-ins**](windows-media-player-conversion-plug-ins.md)
</dt> </dl>

 

 




