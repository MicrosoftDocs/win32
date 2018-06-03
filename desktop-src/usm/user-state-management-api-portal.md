---
title: User State Management API
description: The User State Management provider exposes a management and reporting API for enterprise scenarios.
ms.assetid: 4905f093-419c-4efb-ac3b-b97753c9eea0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User State Management API

## Purpose

The Windows user state management components—Folder Redirection, Offline Files, and Roaming Profiles—offer the following benefits to the enterprise:

-   Consolidate user data and settings from all corporate client computers to a file server,
    -   Enabling enterprise ownership of user data and settings by making it easier to enforce data management and information protection policies.
    -   Reducing administrative costs for management tasks such as backup.
-   Provide users with a consistent view of their data and settings from multiple computers.
-   Enable easy computer replacement.

The User State Management API provides a unified way to configure and retrieve current status for these components.

Application developers can use this API to provide enhanced management and reporting experiences for enterprise scenarios.

## In this section

-   [**Win32\_FolderRedirection**](win32-folderredirection.md)
-   [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md)
-   [**Win32\_FolderRedirectionHealthConfiguration**](win32-folderredirectionhealthconfiguration.md)
-   [**Win32\_FolderRedirectionUserConfiguration**](win32-folderredirectionuserconfiguration.md)
-   [**Win32\_OfflineFilesBackgroundSync**](win32-offlinefilesbackgroundsync.md)
-   [**Win32\_OfflineFilesDiskSpaceLimit**](win32-offlinefilesdiskspacelimit.md)
-   [**Win32\_OfflineFilesHealth**](win32-offlinefileshealth.md)
-   [**Win32\_OfflineFilesMachineConfiguration**](win32-offlinefilesmachineconfiguration.md)
-   [**Win32\_OfflineFilesUserConfiguration**](win32-offlinefilesuserconfiguration.md)
-   [**Win32\_RoamingProfileBackgroundUploadParams**](win32-roamingprofilebackgrounduploadparams.md)
-   [**Win32\_RoamingProfileMachineConfiguration**](win32-roamingprofilemachineconfiguration.md)
-   [**Win32\_RoamingProfileSlowLinkParams**](win32-roamingprofileslowlinkparams.md)
-   [**Win32\_RoamingProfileUserConfiguration**](win32-roamingprofileuserconfiguration.md)
-   [**Win32\_RoamingUserHealthConfiguration**](win32-roaminguserhealthconfiguration.md)
-   [**Win32\_UserProfile**](win32-userprofile.md)
-   [**Win32\_UserStateConfigurationControls**](win32-userstateconfigurationcontrols.md)

## Developer audience

The User State Management API is designed for WMI developers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. Familiarity with COM programming is helpful but not required. For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582).

## Run-time requirements

The User State Management API is included in Windows 8 and Windows Server 2012 and later.

 

 




