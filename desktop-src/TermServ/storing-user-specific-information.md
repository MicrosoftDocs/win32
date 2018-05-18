---
title: Storing user-specific information
description: Applications should store user-specific information in user-specific locations, separately from global information that applies to all users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '32bd1d24-1d2e-4c0a-acdb-0cc67f275e6e'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Storing user-specific information

In a Remote Desktop Services environment, applications should store user-specific information in user-specific locations, separately from global information that applies to all users. This rule applies to information stored in the registry, as well as information stored in files. In general, do not assume that one computer is equivalent to one user.

Store user-specific registry information under the **HKEY\_CURRENT\_USER** registry key. Remote Desktop Services loads the current user's personal registry hive into **HKEY\_CURRENT\_USER** when the user logs on. Of course, Remote Desktop Services manages the registry to ensure that each of the logged-on clients detects the correct user hive under **HKEY\_CURRENT\_USER**. For more information about registry keys, see [Registry Key Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/ms724878) and [Registry Hives](https://msdn.microsoft.com/library/windows/desktop/ms724877).

In contrast, all users share the **HKEY\_LOCAL\_MACHINE** hive. Use **HKEY\_LOCAL\_MACHINE** to store computer-specific information, not user-specific information.

Store user-preference files or other user-specific files in the user's root directory or in a user-specified directory. This consideration applies to temporary files used to store interim information (such as cached data) or to pass data on to another application. User-specific temporary files must also be stored on a per-user basis.

You can use the [**SHGetSpecialFolderLocation**](https://msdn.microsoft.com/library/windows/desktop/bb762203) function with the CSIDL\_PERSONAL flag to get the location of the user's personal files directory. You can also use the [**GetWindowsDirectory**](https://msdn.microsoft.com/library/windows/desktop/ms724454) function to retrieve the path of the Windows directory. In a Remote Desktop Services environment, the Windows directory is guaranteed to be private for each user. Do not store user-specific files under the system directory, such as WINDOWS, or program directory, such as Program Files.

To avoid conflicts among users' information and preferences, applications should store per-user temporary information in user-specific temporary files. User-specific temporary files also prevent application failures caused by file-locking conflicts. To specify the path for storing temporary information, use the [**GetTempPath**](https://msdn.microsoft.com/library/windows/desktop/aa364992) function.

 

 




