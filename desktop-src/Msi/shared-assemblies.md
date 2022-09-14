---
description: A Win32 assembly can be installed as a shared assembly and be available for use by multiple applications on the computer. Shared assemblies should be installed by a Windows Installer package used to install or update an application.
ms.assetid: d408b0a9-8dc5-4cd0-93b3-429de7d12b17
title: Shared Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Shared Assemblies

A Win32 assembly can be installed as a shared assembly and be available for use by multiple applications on the computer. Shared assemblies should be installed by a Windows Installer package used to install or update an application.

Shared assemblies are installed as [side-by-side assemblies](side-by-side-assemblies.md). The Windows Installer installs shared side-by-side assemblies into the Winsxs folder. The assemblies are not registered globally on the system, but they are globally available to any application that specifies a dependency on the assembly in a manifest file. For more information, see [Isolated Applications and Side-by-side Assemblies](../sbscs/isolated-applications-and-side-by-side-assemblies-portal.md).

On operating systems earlier than Windows XP, shared assemblies are usually installed in the Windows system folder and registered globally. The latest installed version is available to any application that binds to it.

For information on how to author a Windows Installer package to install a shared assembly, see the following:

-   [Installing Win32 Assemblies for Side-by-Side Sharing on Windows XP](installing-win32-assemblies-for-side-by-side-sharing-on-windows-xp.md)
-   [Installing Win32 Assemblies for the Private Use of an Application on Windows XP](installing-win32-assemblies-for-the-private-use-of-an-application-on-windows-xp.md)

 

 
