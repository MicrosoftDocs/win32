---
title: Application Installation on 64-bit Systems
description: The 64-bit Windows Installer can seamlessly install 32-bit MSI-based applications on 64-bit Windows.
ms.assetid: fb9c5720-9906-4827-9daf-d7caa453e818
keywords:
- application installation 64-bit Windows Programming
- installation 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Application Installation on 64-bit Systems

The [64-bit Windows Installer](/windows/desktop/Msi/windows-installer-on-64-bit-operating-systems) can seamlessly install 32-bit MSI-based applications on 64-bit Windows. For older applications that use a 16-bit stub to launch a 32-bit installation engine, 64-bit Windows recognizes specific 16-bit installer programs and substitutes a ported 32-bit version.

16-bit DOS, Windows, or OS/2 applications often use a 16-bit stub to check the machine type, then launch a 32-bit installation engine to actually perform the installation. To enable installation of applications that use this technique, 64-bit Windows substitutes 32-bit versions for the following 16-bit installer programs:

* Microsoft Setup for Windows 1.2  
* Microsoft Setup for Windows 2.6  
* Microsoft Setup for Windows 3.0  
* Microsoft Setup for Windows 3.01  
* InstallShield 5.x  

The list of substitutions is stored in the registry under the following key: **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\NtVdm64**.

> [!Note]  
> This mechanism is provided only for compatibility with 32-bit applications that use the 16-bit Microsoft installer programs listed in this topic. Addition of third-party installer programs is not supported.

 

> [!Note]  
> This mechanism is not included on Windows 10 on ARM.

 

 

 