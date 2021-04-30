---
description: The Windows Installer can use digital signatures to detect corrupted resources.
ms.assetid: 68f2c686-cbe0-495d-a448-a7d2ca1df47b
title: Digital Signatures and Windows Installer
ms.topic: article
ms.date: 05/31/2018
---

# Digital Signatures and Windows Installer

The Windows Installer can use digital signatures to detect corrupted resources. A signer certificate may be compared to the signer certificate of an external resource to be installed by the package. For more information regarding the use of digital signatures, digital certificates, and [**WinVerifyTrust**](/windows/desktop/api/wintrust/nf-wintrust-winverifytrust), see the [Security](https://msdn.microsoft.com/library/cc527452.aspx) section of the Microsoft Windows Software Development Kit (SDK).

With Windows Installer, digital signatures can be used with Windows Installer packages, transforms, patches, merge modules, and external cabinet files. Windows Installer is integrated with Software Restriction Policy on Microsoft Windows XP. Policies can be created to allow or prevent installations based upon different criteria, including a particular signer certificate or publisher. The Windows Installer can perform signature validation of external cabinet files on all platforms where CryptoAPI version 2.0 is installed.

Note that the sample Setup.exe bootstrap provided with the Windows Installer SDK performs a signature check on a Windows Installer package prior to initiating the installation.

Performing an [administrative installation](administrative-installation.md) removes the digital signature from the package. An administrative installation modifies the installation package in order to add the AdminProperties stream, which would invalidate the original digital signature. An administrator can resign the package.

Applying a patch to an administrative installation also removes the digital signature from the package. The reason is because the changes persist in the patched installation package of the administrative installation. An administrator can resign the package.

Starting with Windows Installer version 3.0, [User Account Control (UAC) Patching](user-account-control--uac--patching.md) enables non-administrator users to patch applications installed in the per-machine context. UAC patching is enabled by providing a signer certificate in the [MsiPatchCertificate](msipatchcertificate-table.md) table and signing patches with the same certificate.

For more information, see [Digital Signatures and External Cabinet Files](digital-signatures-and-external-cabinet-files.md), [Windows Installer and Software Restriction Policy](windows-installer-and-software-restriction-policy.md), [Authoring a Fully Verified Signed Installation](authoring-a-fully-verified-signed-installation.md), and [A URL based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md).

 

 
