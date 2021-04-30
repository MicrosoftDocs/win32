---
description: A Win32 assembly can be installed as a private assembly and be exclusively available for use by one application. Private assemblies should be installed by a Windows Installer package used to install or update an application.
ms.assetid: 4c6dac5f-fdd3-4125-b54a-74941ee6b3b4
title: Private Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Private Assemblies

A Win32 assembly can be installed as a private assembly and be exclusively available for use by one application. Private assemblies should be installed by a Windows Installer package used to install or update an application.

On Windows XP, private assemblies are installed as [side-by-side assemblies](side-by-side-assemblies.md). The Windows Installer installs private side-by-side assemblies in a folder private to the application. Commonly the folder that contains the applications executable file. The dependency of the application on the private assembly is specified in an application manifest file. For more information, see [Isolated Applications and Side-by-side Assemblies](../sbscs/isolated-applications-and-side-by-side-assemblies-portal.md).

On operating systems earlier than Windows XP, a copy of the private assembly and a .local file is installed into a private folder for the exclusive use of the application. A version of the assembly is also globally registered on the system and available for any application that binds to it. The global version of the assembly may be the version installed with the application or an earlier version. The global version is determined by the same rules use by [Isolated Components](isolated-components.md).

Note that the Windows Installer cannot install a private assembly in a location having a path that contains more than 234 characters, including the terminating null character.

 

 
