---
description: A shared assembly is an assembly available for use by multiple applications on the computer.
ms.assetid: E42688E0-83D8-4C64-98A8-1BE82E4348FA
title: About Shared Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# About Shared Assemblies

A shared assembly is an assembly available for use by multiple applications on the computer. On Windows Vista and Windows XP, [side-by-side assemblies](about-side-by-side-assemblies-.md) can be installed as shared assemblies. Shared side-by-side assemblies are not registered globally on the system, but they are globally available to applications that specify a dependence on the assembly in [manifests](manifests.md). Multiple versions of side-by-side assemblies can be shared by different applications running at the same time. For more information, see [About Isolated Applications and Side-by-Side Assemblies](about-isolated-applications-and-side-by-side-assemblies.md). For example, the [supported Microsoft side-by-side assemblies](supported-microsoft-side-by-side-assemblies.md) shipped with Windows XP are typically used as shared assemblies by multiple applications.

Shared side-by-side assemblies are installed in the WinSxS folder. Assembly publishers, applications, and administrators can change the version of side-by-side assembly dependencies after deployment through the [configuration](configuration.md). Shared side-by-side assemblies can be installed by an operating system update, or by a Windows Installer package that installs or updates an application. For more information, see [Installation of Win32 Assemblies](../msi/installation-of-win32-assemblies.md).

Prior to Windows XP, shared assemblies were registered globally and installed in the Windows System folder. In this case, the latest installed version of the assembly is available to any application that binds to it. A side-by-side assembly can also be installed as a private assembly for the exclusive use of an application. For more information, see [Private Assemblies](/windows/desktop/Msi/private-assemblies).

 

 
