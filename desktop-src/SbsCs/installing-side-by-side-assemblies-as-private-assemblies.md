---
description: To install side-by-side assemblies as private assemblies, you can install the assembly as a component of an installer package.
ms.assetid: 1cfd836f-a1b9-4339-8756-5488c88b3c2b
title: Installing Side-by-side Assemblies as Private Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Installing Side-by-side Assemblies as Private Assemblies

To install [side-by-side assemblies](about-side-by-side-assemblies-.md) as [private assemblies](/windows/desktop/Msi/private-assemblies), you can install the assembly as a component of an installer package. This can be the same installation package used to install or update your application. Windows Installer version 2.0 or later is required to install assemblies. For more information, see the [Windows Installer](../msi/windows-installer-portal.md) SDK and the sections under [Installation of Win32 Assemblies](../msi/installation-of-win32-assemblies.md).

As an alternative, you can use the installer to copy a private assembly and manifest into the same folder as the application's executable file.

 

 
