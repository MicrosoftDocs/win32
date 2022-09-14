---
description: Windows Installer runs as a service on computers using 32-bit or 64-bit Windows.
ms.assetid: c02fc401-0c9c-49f6-adcc-ed36bdb18fca
title: About Windows Installer on 64-Bit Operating Systems
ms.topic: article
ms.date: 05/31/2018
---

# About Windows Installer on 64-Bit Operating Systems

Windows Installer runs as a service on computers using 32-bit or 64-bit Windows. Versions of the installer earlier than version 2.0 can install and manage 32-bit Windows Installer Packages only on 32-bit operating systems. Note that you cannot advertise or install a 64-bit application on a 32-bit operating system.

A Windows Installer package must be specified as either a 32-bit or a 64-bit package; it cannot be specified as neutral. On a computer using a 64-bit operating system, the Windows Installer service is hosted in a 64-bit process that installs both 32-bit and 64-bit packages. Windows Installer installs three types of Windows installer packages on a computer running a 64-bit operating system:

-   32-bit packages that contain only 32-bit components.
-   64-bit packages containing some 32-bit components.
-   64-bit packages containing only 64-bit components.

The follow sections describe the two types of Windows Installer packages and the new installer properties provided by Windows Installer for 64-bit packages.

[32-bit Windows Installer Packages](32-bit-windows-installer-packages.md)

[64-bit Windows Installer Packages](64-bit-windows-installer-packages.md)

## Related topics

<dl> <dt>

[Using 64-Bit Windows Installer Packages](using-64-bit-windows-installer-packages.md)
</dt> </dl>

 

 



