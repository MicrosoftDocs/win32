---
description: Operating System Versioning
ms.assetid: 974650d9-504a-4f19-bc71-90fbc92672d9
title: Operating System Versioning
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Versioning

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - High  
**Frequency** - High  









## Description

The internal version number for Windows 7 and Windows Server 2008 R2 is 6.1. The GetVersion function will now return this version number to applications when queried. This is especially important for AntiVirus, backup, utility applications, and copy protection.

## Manifestation of Impact

The manifestation of this change is application-specific. This means that any application that specifically checks for the operating system version will get a higher version number, which can lead to one or more of the following situations:

-   Application installers might be unable to install the application, and applications might be unable to start
-   Applications might become unstable or crash
-   Applications might generate error messages, but continue to function properly

## Mitigation

Most applications will function properly on Windows 7 and Windows Server 2008 R2 because the application compatibility in Windows 7 and Windows Server 2008 R2 is very high. However, Windows 7 and Windows Server 2008 R2 include a Compatibility View for installers and applications that check for operating system version.

To enable the compatibility view, users can right-click the shortcut or the executable file, and then apply the Windows XP SP2 or Windows Vista Compatibility View from the Compatibility tab. In most cases, this should enable the application to operate properly without the need for any changes to the application.

IT Professionals can also apply any of the applicable VersionLie compatibility fixes, by using the Compatibility Administrator tool, which installs with the Application Compatibility Toolkit (ACT). For example, if an application fails to function because it is checking for, but not finding, the Windows XP® with Service Pack 2 (SP2) version information, the WinXPSP2VersionLie can be applied to return the proper version number information to the application, regardless of the actual operating system version that is running on the computer. The available VersionLie compatibility fixes are:

-   Win95VersionLie
-   Win98VersionLie
-   WinNT4SP5VersionLie
-   Win2000VersionLie
-   Win2000SP1VersionLie
-   Win2000SP2VersionLie
-   Win2000SP3VersionLie
-   WinXPVersionLie
-   WinXPSP1VersionLie
-   WinXPSP2VersionLie
-   VistaRTMVersionLie
-   VistaSP1VersionLie
-   VistaSP2VersionLie
-   Win2K3RTMVersionLie
-   Win2K3SP1VersionLie

## Solution

Generally, applications should not perform operating system version checks. If an application needs a specific feature, it is preferable to try to find the feature, and fail only if the needed feature is missing. At a minimum, applications should always accept version numbers greater than or equal to the lowest supported version of the operating system. Exceptions should occur only if there is a specific legal, business, or system-component requirement.

## Links to Other Resources

-   [Application Compatibility Toolkit Download](/windows-hardware/get-started/adk-install)
-   [Known Compatibility Fixes, Compatibility Modes, and AppHelp Messages](/previous-versions/windows/it-pro/windows-7/cc765984(v=ws.10))

 

 
