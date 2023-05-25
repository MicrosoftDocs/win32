---
title: ConvertPluginCLSID Subkey
description: ConvertPluginCLSID Subkey
ms.assetid: 2bf5b6ad-31e9-40c2-a682-c7ad813e8f7a
keywords:
- Windows Media Player,ConvertPluginCLSID subkey
- Windows Media Player,file name extensions
- Windows Media Player,registry
- registry,file name extensions
- registry,ConvertPluginCLSID subkey
- registry,settings for Windows Media Player
- file name extension registry settings
- ConvertPluginCLSID subkey
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ConvertPluginCLSID Subkey

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player 11 encounters a custom file name extension, it looks for a registry subkey that matches the extension. The subkey is described in [File Name Extension Registry Settings](file-name-extension-registry-settings.md). In some cases, the extension's subkey has a subkey named **ConvertPluginCLSID**.

For example, suppose you have created a custom file format (with file name extension .xyz) and a conversion plug-in that converts the files to a format supported by Windows Media Player Then you would store the class ID of the plug-in in one or both of the following subkeys.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Multimedia\\WMPlayer\\Extensions\\.xyz\\ConvertPluginCLSID**

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Player\\Extensions\\.xyz\\ConvertPluginCLSID**

The **ConvertPluginCLSID** subkey specifies the class IDs of plug-ins that Windows Media Player can use to convert a media file from its custom format to a format supported by the Player.

The **ConvertPluginCLSID** subkey has the following entries.

-   A default entry that represents the default conversion plug-in.
-   A named entry that represents the default conversion plug-in.
-   Additional named entries that represent alternate conversion plug-ins.

For example, suppose a custom file format has a default conversion plug-in and two alternate conversion plug-ins. The registry entries under the **ConvertPluginCLSID** subkey would have the following form.



| Name                                                                          | Type        | Value                                                                |
|-------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------|
| Default                                                                       | **REG\_SZ** | The class ID, in registry format, of the default conversion plug-in. |
| The class ID, in registry format, of the default conversion plug-in.          | **REG\_SZ** | The friendly name of the default conversion plug-in.                 |
| The class ID, in registry format, of the first alternate conversion plug-in.  | **REG\_SZ** | The friendly name of the first alternate conversion plug-in.         |
| The class ID, in registry format, of the second alternate conversion plug-in. | **REG\_SZ** | The friendly name of the second alternate conversion plug-in.        |



 

Note that the default conversion plug-in is represented by two registry entries: the default entry and a named entry. Windows Media Player uses the default entry to determine which plug-in is the default (primary) conversion plug-in. Windows Media Player uses the named entries to obtain friendly names for all conversion plug-ins, including the default plug-in.

The friendly name of a conversion plug-in is determined by the company that creates the plug-in. Windows Media Player might display the friendly name in its user interface.

When Windows Media Player attempts to convert a file from a custom format to a standard format, it first loads the default plug-in. If the default plug-in fails to convert the file and returns NS\_E\_WMP\_CONVERT\_PLUGIN\_UNKNOWN\_FILE\_OWNER, the Player loads each alternate plug-in until a successful conversion happens or there are no more plug-ins to try. The Player does not display a warning message if no conversion plug-in is found for the file name extension.

The **ConvertPluginCLSID** registry entry is supported by Windows Media Player 11.

## Related topics

<dl> <dt>

[**File Name Extension Registry Settings**](file-name-extension-registry-settings.md)
</dt> <dt>

[**Windows Media Player Conversion Plug-ins**](windows-media-player-conversion-plug-ins.md)
</dt> </dl>

 

 




