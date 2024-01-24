---
title: Library Classification Registry Entries
description: Library Classification Registry Entries
ms.assetid: 3ef7d384-503f-4b8f-9f4b-e0ef3c56616b
keywords:
- Windows Media Player,library
- Windows Media Player,classification registry entries
- Windows Media Player,file name extensions
- Windows Media Player,registry
- registry,file name extensions
- registry,library classification entries
- registry,settings for Windows Media Player
- file name extension registry settings
- library,classification registry entries
- library,registry
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Library Classification Registry Entries

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player encounters a media file that has a custom file name extension, it does not know whether the file should be classified as audio, video, or some other type. By default, Windows Media Player places such files in the Other Media portion of the library.

If your digital media files have a custom format, you can provide Windows Media Player with information about where your files should appear in the Player's library by placing two entries in the registry on the user's computer.

One entry goes in the following subkey.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MediaPlayer\\MLS\\Extensions**

The registry entry has the following format.



| Name                                                  | Data type   | Value                                      |
|-------------------------------------------------------|-------------|--------------------------------------------|
| The file name extension without the dot (.) separator | **REG\_SZ** | A string that specifies a library location |



 

The other registry entry goes in the following subkey that you create.

**HKEY\_CLASSES\_ROOT\\** *customExtension*

where *customExtension* is the file name extension including the dot (.) separator.

The registry entry has the following format.



| Name          | Data type   | Value                                      |
|---------------|-------------|--------------------------------------------|
| PerceivedType | **REG\_SZ** | A string that specifies a library location |



 

Both registry entries must have the same value. Possible values are given in the following table.



| Value | Description                                                                      |
|-------|----------------------------------------------------------------------------------|
| audio | Files that have the custom extension appear in the music portion of the library. |
| video | Files that have the custom extension appear in the video portion of the library. |



 

For example, the following registry entries specify that files having the file name extension .xyz will appear in the music portion of the library:


```C++

HKEY_LOCAL_MACHINE\Software\Microsoft\MediaPlayer\MLS\Extensions
    xyz     REG_SZ     audio

HKEY_CLASSES_ROOT\.xyz
    PerceivedType     REG_SZ     audio

```



Note that any code that attempts to write to the registry on the user's computer can write to the HKEY\_LOCAL\_MACHINE subtree only if the current user has administrative privileges.

Library classification registry entries are supported by the following versions of Windows Media Player.

-   Windows Media Player 9 Series with hotfix 823275
-   Windows Media Player 10 and later

## Related topics

<dl> <dt>

[**File Name Extension Registry Settings**](file-name-extension-registry-settings.md)
</dt> </dl>

 

 




