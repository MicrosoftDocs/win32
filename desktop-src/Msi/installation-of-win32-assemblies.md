---
description: Install Win32 assemblies by making them a component of Microsoft Windows Installer package that installs or updates your application.
ms.assetid: 09aecb55-ed45-45b3-b27a-d0946223392a
title: Installation of Win32 Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Installation of Win32 Assemblies

Install Win32 assemblies by making them a component of Microsoft Windows Installer package that installs or updates your application. When you author the [MsiAssembly table](msiassembly-table.md) and [MsiAssemblyName table](msiassemblyname-table.md), this identifies the component in the Component\_ column as an assembly. The installer will set the [**MsiWin32AssemblySupport**](msiwin32assemblysupport.md) property to the file version of Sxs.dll on operating systems that can support Win32 assemblies and not set this property otherwise.

In Windows Vista and Windows XP, Windows Installer does not write assembly information into the registry. In addition, shared assemblies, private assemblies, and side-by-side assemblies can be used. For information, see [Shared Assemblies](shared-assemblies.md), [Private Assemblies](private-assemblies.md), and [Side-by-Side Assemblies](side-by-side-assemblies.md).

The following sections describe how to author a Windows Installer package to install Win32 assemblies as shared, private, or side-by-side on different Windows operating systems.

-   [Installing Win32 Assemblies for Side-by-Side Sharing on Windows XP](installing-win32-assemblies-for-side-by-side-sharing-on-windows-xp.md)
-   [Installing Win32 Assemblies for the Private Use of an Application on Windows XP](installing-win32-assemblies-for-the-private-use-of-an-application-on-windows-xp.md)

 

 



