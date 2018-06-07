---
Description: To install side-by-side assemblies as private assemblies, you can install the assembly as a component of an installer package.
ms.assetid: 1cfd836f-a1b9-4339-8756-5488c88b3c2b
title: Installing Side-by-side Assemblies as Private Assemblies
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Installing Side-by-side Assemblies as Private Assemblies

To install [side-by-side assemblies](about-side-by-side-assemblies-.md) as [private assemblies](https://msdn.microsoft.com/library/windows/desktop/aa370850), you can install the assembly as a component of an installer package. This can be the same installation package used to install or update your application. Windows Installer version 2.0 or later is required to install assemblies. For more information, see the [Windows Installer](c90b8cbe-d7a1-44ad-ae65-80115bd55e4f) SDK and the sections under [Installation of Win32 Assemblies](09aecb55-ed45-45b3-b27a-d0946223392a).

As an alternative, you can use the installer to copy a private assembly and manifest into the same folder as the application's executable file.

 

 



