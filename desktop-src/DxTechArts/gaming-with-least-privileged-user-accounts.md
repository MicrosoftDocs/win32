---
title: Gaming with Least-Privileged User Accounts
description: This article describes how games developers can author Microsoft Windows games that work well with least-privileged user accounts (also known as limited-user accounts).
ms.assetid: 1b7cc3c9-b180-14b1-53c8-57f9e545d009
ms.topic: article
ms.date: 05/31/2018
---

# Gaming with Least-Privileged User Accounts

This article describes how games developers can author Microsoft Windows games that work well with least-privileged user accounts (also known as limited-user accounts).

-   [Introduction](#introduction)
-   [File Access for Least-Privileged User Accounts](#file-access-for-least-privileged-user-accounts)
    -   [Scenario 1: Files that do not need to be viewed or altered by users](#scenario-1-files-that-do-not-need-to-be-viewed-or-altered-by-users)
    -   [Scenario 2: Files that need to be viewed or altered by users](#scenario-2-files-that-need-to-be-viewed-or-altered-by-users)
-   [Registry Access for Least-Privileged User Accounts](#registry-access-for-least-privileged-user-accounts)
-   [Patching with Least-Privileged User Accounts](#patching-with-least-privileged-user-accounts)

## Introduction

Windows manages its users with accounts. Today, more than eighty percent of computer users at home share their computer with other family members. When multiple users share a Windows computer, multiple user accounts are created, and each user logs in with an individual account to access the computer. With the increasing awareness for security, more people operate their computers with least-privileged user accounts, also known as limited-user accounts, which do not have complete control over the system. Administrator accounts typically have unrestricted access to every part of the computer. This can affect how Windows-based games work.

There are additional benefits for games developers who write their games to work with least-privileged user accounts. In Windows Vista and later, least-privileged user accounts are enforced, which means that every account on the system, with the exception of the local administrator, is a least-privileged user account. This will affect how games that do not follow the guideline (legacy applications) run on Windows Vista and later. For instance, when an application attempts to write to a folder or a registry value to which it does not have permission, the file write is redirected to a virtual file store for the user. This virtual file store will reside in a folder to which the user has write access. This behavior may not seem as catastrophic as outright failing the write attempt; however, applications that create virtualized files may confuse users because files will not be written to the location users expect. For instance, games that write high score files to the same folder as the executable folder will write these files to a virtualized folder instead. Consequently, one user cannot see the high score achieved by another user because every user has a separate virtualized file store.

Games that follow the guidelines in this article will run with least-privileged user accounts, and consequently will maintain compatibility with Windows Vista and later.

## File Access for Least-Privileged User Accounts

Windows supports two file systems: FAT32 and NTFS. FAT32 is a legacy file system supported only for backward compatibility; NTFS supports more powerful and robust file permissions. The use of NTFS is expanding as retailers are shipping new computers with Windows pre-installed on a NTFS-partitioned hard drive. On an NTFS-based Windows XP system, users with least-privileged user accounts have only limited access to several folders. However, they would have complete access on a FAT32-based Windows XP system.

The following table lists the default location of these folders and their permissions.



| Path                                               | Folder Contents              | Read | Write | Create/Delete |
|----------------------------------------------------|------------------------------|------|-------|---------------|
| &lt;Drive&gt;:\\Windows                            | The Windows operating system | X    |       |               |
| &lt;Drive&gt;:\\Program Files                      | Executable application files | X    |       |               |
| &lt;Drive&gt;:\\Documents and Settings\\Username\* | Each user's files            | X    | X     | X             |
| &lt;Drive&gt;:\\Documents and Settings\\All Users  | All user files               | X    | X     | X             |



 

\* Username is the user's login name.

In a least-privileged user account, you may read, write, create and delete files in either folder: Documents and Settings\\Username or Documents and Settings\\All Users.

What this means is that you should not place save games in \\Program Files, instead they should go in a sub-folder in \\My Documents. Also you should not place temporary application data in \\Program Files or \\My Documents, instead it should be placed in Application Data folder (CSIDL\_LOCAL\_APPDATA).

More specifically, there are two scenarios that each game should handle:

### Scenario 1: Files that do not need to be viewed or altered by users

A typical example would be the game's configuration file, temporary files, and game cache files. These files are typically kept in the Application Data folder. To obtain this folder path, call the [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) function with CSIDL\_APPDATA or CSIDL\_LOCAL\_APPDATA as shown in the following code example.

``` syntax
#include <shlobj.h>
#include <strsafe.h>

#define APPNAME L"MyApp"

WCHAR wszPath[MAX_PATH];

// Local Application Data
SHGetFolderPath( hWnd, CSIDL_LOCAL_APPDATA, NULL, SHGFP_TYPE_CURRENT, wszPath );
StringCchCatW( wszPath, MAX_PATH, L"\\" );
StringCchCatW( wszPath, MAX_PATH, APPNAME );

// Create the folder wszPath
// Then create files in wszPath
// Roaming Application Data
SHGetFolderPath( hWnd, CSIDL_APPDATA, NULL, SHGFP_TYPE_CURRENT, wszPath );
StringCchCatW( wszPath, MAX_PATH, L"\\" );
StringCchCatW( wszPath, MAX_PATH, APPNAME );

// Create the folder wszPath
// Then create files in wszPath
```

The difference between local and roaming Application Data folders is that on Windows 2000 and Windows XP, roaming content is copied to and from the server during the logon/logoff process, while local content is not. For most games, local Application Data is sufficient.

### Scenario 2: Files that need to be viewed or altered by users

A typical example would be a user's saved game files. Store the files in the user's document folder so that they are easily visible to the user. An application gets the user's document folder path by calling [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) with CSIDL\_PERSONAL, as the following code example shows:

``` syntax
#include <shlobj.h>
#include <strsafe.h>

#define APPNAME L"MyApp"

WCHAR wszPath[MAX_PATH];

SHGetFolderPath( hWnd, CSIDL_PERSONAL, NULL, SHGFP_TYPE_CURRENT, wszPath );
StringCchCatW( wszPath, MAX_PATH, L"\\" );
StringCchCatW( wszPath, MAX_PATH, APPNAME );

// Create the folder wszPath
// Then create files in wszPath
```

At times, a game may need to store files that all users are meant to see and use. One example is the high score record, where all users write to the same record file so that high scores are maintained system-wide instead of a separate high score for each user. Other examples are downloaded maps, missions, and game modifications. If these are shared, then only one user has to download them instead of every user. In this scenario, use the document folder under the shared profile folder, as demonstrated in the following code.

``` syntax
#include <shlobj.h>
#include <strsafe.h>

#define APPNAME L"MyApp"

WCHAR wszPath[MAX_PATH];

SHGetFolderPath( hWnd, CSIDL_COMMON_DOCUMENTS, NULL, SHGFP_TYPE_CURRENT, wszPath );
StringCchCatW( wszPath, MAX_PATH, L"\\" );
StringCchCatW( wszPath, MAX_PATH, APPNAME );

// Create the folder wszPath
// Then create files in wszPath
```

## Registry Access for Least-Privileged User Accounts

It is common for applications to use the Windows registry to store information. Similar to file access, administrator and least-privileged user accounts do not have the same permission to the registry. For least-privileged user accounts, the entire HKEY\_LOCAL\_MACHINE node is read-only. For instance, a game can read the default configuration information, but may not write any new information to this node. Consequently, games running in least-privileged user mode that need to write to the registry will need to use the HKEY\_CURRENT\_USER node to store per-user information, as illustrated in the following code.

``` syntax
#define APP_REGISTRY_KEY_PATH L"Software\\MyCompany\\MyApp"

LONG lRetVal;
HKEY hKey;

lRetVal = RegCreateKeyExW( HKEY_CURRENT_USER,
                           APP_REGISTRY_KEY_PATH,
                           0,
                           NULL,
                           REG_OPTION_NON_VOLATILE,
                           KEY_WRITE|KEY_READ,
                           NULL,
                           &hKey,
                           NULL );

if( ERROR_SUCCESS == lRetVal )
{
    // Store information in hKey
}
```

It is worth noting that during installation, registry information should be written to HKEY\_LOCAL\_MACHINE, not HKEY\_CURRENT\_USER. This is because the person running the installation is usually an administrator, and may not be the only person to use the program. In this situation, writing to HKEY\_CURRENT\_USER makes the information unavailable to other users. This is not usually an issue because the information written to the registry during installation is the configuration and default settings that apply to every user of the program.

When uninstalling the game, extra effort is necessary to remove every value that the game has written to the registry. Because the uninstaller is run by one person, usually the administrator, simply deleting the relevant information in HKEY\_LOCAL\_MACHINE and HKEY\_CURRENT\_USER will not remove values for other users. One way to remove the per-user information in the registry is to enumerate the HKEY\_USERS registry hive root. Each subkey under HKEY\_USERS corresponds to the HKEY\_CURRENT\_USER hive for a particular user on the system. By enumerating HKEY\_USERS and removing the game-specific information under each subkey, the uninstaller can ensure that no information is left behind.

## Patching with Least-Privileged User Accounts

Patching a game involves updating the game's files. Therefore, it usually requires write access to the game's program folder. Patching a game is a straightforward process when it is done by an administrator because they have unrestricted access to the game's program folder. Conversely, it has traditionally been difficult, if not impossible, for a least privileged user to patch games because of the access restriction. Now, [Windows Installer](/windows/desktop/Msi/windows-installer-portal) has been enhanced to make least-privileged user account patching possible. To take advantage of this feature, games are encouraged to utilize Windows Installer for installation and patching.

Starting with Windows Installer 3.0, application patches can be applied by least privileged users when certain conditions are met. These conditions are:

-   The application was installed using Windows Installer 3.0.
-   The application was originally installed per-machine.
-   The application is installed from removable media, such a CD-ROM or digital video disc (DVD).
-   The patches are digitally signed by a certificate that is identified by the original installer package (.msi file).
-   The patches can be validated against the digital signature.
-   The original installer package has not disabled least-privileged user account patching.
-   The system administrator has not disabled least-privileged user account patching via system policy.

Normally, a least privileged user cannot modify a game's program files. However, when the above conditions are met and LUA patching is enabled, Windows Installer can update the game's files so that the user gets the latest version.

> [!Note]  
> The information contained in this article relates to pre-release software product, which may be substantially modified before its first commercial release. Accordingly, the information may not accurately describe or reflect the software product when first commercially released. This article is provided for informational purposes only, and Microsoft makes no warranties, express or implied, with respect to this article or the information contained in it.

 

 

 
