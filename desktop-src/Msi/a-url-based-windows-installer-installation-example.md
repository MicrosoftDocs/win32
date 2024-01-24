---
description: This example illustrates how to create a URL-based installation of a Windows Installer package.
ms.assetid: a38a1132-43b4-449d-b134-f351ce370223
title: A URL-Based Windows Installer Installation Example
ms.topic: article
ms.date: 05/31/2018
---

# A URL-Based Windows Installer Installation Example

This example illustrates how to create a URL-based installation of a Windows Installer package. For more information about securing installations and using digital certificates see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).

To reproduce this sample you need the [SignTool](../seccrypto/signtool.md) utility. For details, see the [CryptoAPI Tools Reference](../seccrypto/cryptoapi-tools-reference.md) in the Microsoft Windows Software Development Kit (SDK). You also need [Msistuff.exe](msistuff-exe.md) and Setup.exe utilities from the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). For more information, see [Internet Download Bootstrapping](internet-download-bootstrapping.md).

The example has the following specifications:

-   When users visit your website and click the "MySetup Installation" link, they are presented with the option to save or run from that location. If the user selects to run from that location, the Setup.exe upgrades the version of Windows Installer on their computer, if necessary, verifies the digital signature on the installer package, and installs the package on their computer.
-   There is a digital certificate, Mycert.cer, provided with a private key, Mycert.pvk.
-   The URL of the hypothetical website a customer would visit to install the package is https:\//www.blueyonderairlines.com/Products/MySetup/mysetup.html.
-   The web server layout is as follows. 

    | URL                                                               | File        | Description                                    |
    |-------------------------------------------------------------------|-------------|------------------------------------------------|
    | https:\//www.blueyonderairlines.com/Products/MySetup/               | Setup.exe   | Setup.exe bootstrapper.                        |
    | https:\//www.blueyonderairlines.com/Products/MySetup/               | MySetup.msi | Installation package                           |
    | https:\//www.blueyonderairlines.com/Products/MySetup/               | Cab1.cab    | Source file cabinet \#1                        |
    | https:\//www.blueyonderairlines.com/Products/MySetup/               | Cab2.cab    | Source file cabinet \#2                        |
    | https:\//www.blueyonderairlines.com/Products/Common/InstMsi/Ansi    | Instmsi.exe | ANSI Windows Installer 2.0 redistributable.    |
    | https:\//www.blueyonderairlines.com/Products/Common/InstMsi/Unicode | Instmsi.exe | Unicode Windows Installer 2.0 redistributable. |

    

     

[Continue](configuring-the-setup-exe-resources.md)

 

 
