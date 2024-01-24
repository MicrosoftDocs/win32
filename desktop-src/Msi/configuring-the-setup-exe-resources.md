---
description: A configurable bootstrap executable (Setup.exe) and configuration tool ( Msistuff.exe) is included in the Windows SDK Components for Windows Installer Developers.
ms.assetid: 95fcea5c-b107-48b7-9ae8-84629353c554
title: Configuring the Setup.exe Resources
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Setup.exe Resources

A configurable bootstrap executable (Setup.exe) and configuration tool ( [Msistuff.exe](msistuff-exe.md)) is included in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). By using Msistuff.exe to configure the resources in Setup.exe, developers can easily create a web installation of a Windows Installer package. For more information see [Internet Download Bootstrapping](internet-download-bootstrapping.md).

Entering the following command line configures the resources for the sample described in [A URL Based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md).

`MsiStuff setup.exe /u https://www.blueyonderairlines.com/Products/MySetup /d MySetup.msi /n MySetup /v 150 /i https://www.blueyonderairlines.com/Products/Common/InstMsi /a Ansi/Instmsi.exe /w Unicode/Instmsi.exe`

[Continue](sign-setup-exe-and-mysetup-msi.md)

 

 



