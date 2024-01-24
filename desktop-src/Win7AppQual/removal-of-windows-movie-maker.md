---
description: Removal of Windows Movie Maker
ms.assetid: af55e570-0f24-4376-905a-3b879d5f3a1c
title: Removal of Windows Movie Maker
ms.topic: article
ms.date: 05/31/2018
---

# Removal of Windows Movie Maker

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - High  
**Frequency** - Medium  


## Description

Microsoft is deprecating and removing the Windows Movie Maker utility. This includes:

-   All entry points to Windows Movie Maker (for example, Start Menu, Start > Run)
-   All binaries that were used by Windows Movie Maker (everything that was in %ProgramFiles%\\Movie Maker)

However, a user's Movie Maker project files will remain on the system and be accessible to other applications that support this file format.

## Manifestation

Remove of Windows Movie Maker results in the following:

-   Any attempt to launch Windows Movie Maker with its command line arguments will fail
-   Any plug-ins that were installed to enable new transforms and animations will remain installed but will not be exposed to the end user

## Solution

To have such functionality in the future, a user will need to install a similar application from Microsoft or another software provider.

 

 



