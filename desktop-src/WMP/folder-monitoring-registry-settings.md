---
title: Folder Monitoring Registry Settings
description: Folder Monitoring Registry Settings
ms.assetid: 563aeaec-0759-4b0c-a8e9-a9a2b3092515
keywords:
- Windows Media Player,folder monitoring registry settings
- Windows Media Player,file folder monitoring registry settings
- Windows Media Player,registry
- registry,folder monitoring settings
- registry,file folder monitoring settings
- registry,settings for Windows Media Player
- folder monitoring registry settings
- file folder monitoring registry settings
ms.topic: article
ms.date: 05/31/2018
---

# Folder Monitoring Registry Settings

Windows Media Player 9 Series or later can monitor file folders for new digital media files. When the Player detects a new file in a monitored folder, it automatically adds the file to the library. For Windows Media Player 9 through Windows Media Player 11, users can change the list of monitored folders by clicking **Monitor Folders** on the library tab of the **Options** dialog box. For Windows Media Player 12, a user can change the list of monitored folders by following the instructions in the topic [Add items to the Windows Media Player Library](https://windows.microsoft.com/windows7/Add-items-to-the-Windows-Media-Player-Library). For Windows Media Player 9 through Windows Media Player 11, you can programmatically add a folder to be monitored by adding a value to the registry. For Windows Media Player 12, you cannot use the registry to programmatically add or remove folders to be monitored.

For Windows Media Player 9 through Windows Media Player 11, to add a folder for monitoring you must first create or modify two values in the following registry key:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Preferences\\**

The new values must be named as follows.



| Name                           | Type           | Description                                                                                                                                                                                                                                                                    |
|--------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TrackFoldersDirectories**    | **REG\_DWORD** | A **DWORD** value that represents the count of folders to monitor. This must match the count of **TrackFoldersDirectories***X* values.                                                                                                                                         |
| **TrackFoldersDirectories***X* | **REG\_SZ**    | A string value that represents the path of the folder to monitor. Each folder to monitor requires a separate value. The suffix *X* is an integer that should always begin at 0 and then increment by 1. Windows Media Player also monitors subfolders of the specified folder. |



 

For example, to add the first folder to monitor, add the following value:


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Preferences]
"TrackFoldersDirectories0" = "c:\MyPath\MyFolder"

```



Then, create the count value:


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Preferences]
"TrackFoldersDirectories" = dword:00000001

```



To add a second folder to monitor, add the following value:


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Preferences]
"TrackFoldersDirectories1" = "c:\MyPath\MyFolder2"

```



Then, increment the count value:


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Preferences]
"TrackFoldersDirectories" = dword:00000002

```



## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> </dl>

 

 




