---
description: Windows Resource Protection (WRP) prevents the replacement of essential system files, folders, and registry keys that are installed as part of the operating system.
ms.assetid: 39069f57-d9f6-4890-ba87-37175184d7a2
title: About Windows Resource Protection
ms.topic: article
ms.date: 05/31/2018
---

# About Windows Resource Protection

Windows Resource Protection (WRP) prevents the replacement of essential system files, folders, and registry keys that are installed as part of the operating system. It became available starting with Windows Server 2008 and Windows Vista. Permission for full access to modify WRP-protected resources is restricted to TrustedInstaller. WRP-protected resources can only be changed using the [Supported Resource Replacement Mechanisms](supported-file-replacement-mechanisms.md) with the Windows Modules Installer service. Protecting these resources prevents application and operating system failures.

Applications should not attempt to modify WRP-protected resources because these are used by Windows and other applications. If an application attempts to modify a WRP-protected resource, it can have the following results.

-   Application installers that attempt to replace, modify, or delete critical Windows files or registry keys may fail to install the application and will receive an error message stating that access to the resource was denied.
-   Applications that attempt to add or remove sub-keys or change the values of protected registry keys may fail and will receive an error message stating that access to the resource was denied.
-   Applications that rely on writing any information into protected registry keys, folders, or files may fail.

WRP is the new name for Windows File Protection (WFP). WRP protects registry keys and folders as well as essential system files. WFP was available in Microsoft Windows Server 2003 and Windows XP. WRP replaces WFP in Windows Server 2008 and Windows Vista.

The following topics describe WRP:

-   [Protected Resource List](protected-file-list.md)
-   [Detecting Resource Replacement](detecting-file-replacement.md)
-   [Supported Resource Replacement Mechanisms](supported-file-replacement-mechanisms.md)
-   [System File Checker](system-file-checker.md)
-   [Remote Administration Considerations](remote-administration-considerations.md)

 

 



