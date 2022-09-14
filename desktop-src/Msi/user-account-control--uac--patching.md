---
description: User Account Control (UAC) patching enables the authors of Windows Installer installations to identify digitally-signed patches that can be applied in the future by non-administrator users.
ms.assetid: f7d64f61-24c8-4037-a10b-d68d0e9e3c42
title: User Account Control (UAC) Patching
ms.topic: article
ms.date: 05/31/2018
---

# User Account Control (UAC) Patching

[*User Account Control*](u-gly.md) (UAC) patching enables the authors of Windows Installer installations to identify digitally-signed patches that can be applied in the future by non-administrator users.

If the digital signature does not match the certificate, Windows Vista displays a UAC dialog box requesting administrator authorization before installing the patch. On systems earlier than Windows Vista, the installer will not apply a signed patch that does not match the certificate.

If a non-administrator attempts to apply a patch to an application, and the following conditions have not been met, Windows Vista will notify the user that administrator authorization is required before installing the patch. A non-administrator can continue installing the patch, without needing to obtain additional administrator authorization, provided the following conditions are met.

-   The application was installed on Windows Vista or Windows XP using Windows Installer 3.0 or later.

    **Windows Server 2008:** Not supported.

-   If the application was installed on Windows XP, the application must also have been installed from removable media, such a CD-ROM or DVD disk. This restriction does not apply if the application was installed on Windows Vista.
-   The application was not installed from an [administrative installation](administrative-installation.md) source image.
-   The application was originally installed per-machine. For information about how to enable non-administrators to apply patches to per-user-managed applications after the patch has been approved as trusted by an administrator, see [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).
-   The [MsiPatchCertificate table](msipatchcertificate-table.md) is present in the Window Installer package (.msi file) and contains the information needed to enable UAC. The table and information may have been be included in the original installation package or added to the package by a Windows Installer patch file (.msp file).
-   The patches are digitally signed by a certificate listed in the [MsiPatchCertificate table](msipatchcertificate-table.md). For more information about digital signature certificates, see [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).
-   The digital signature on the patch package can be verified against the certificate in the [MsiPatchCertificate table](msipatchcertificate-table.md). For more information about the use of digital signatures, digital certificates, and [**WinVerifyTrust**](/windows/win32/api/wintrust/nf-wintrust-winverifytrust), see the [Security](https://msdn.microsoft.com/library/cc527452.aspx) section of the Microsoft Windows Software Development Kit (SDK).
-   The signer certificate used to verify the digital signature on the patch package is valid and has not been revoked.
    > [!Note]  
    > Although you cannot sign a patch using an expired certificate, evaluation of a digital signature on a patch does not fail if the certificate has expired. Evaluation uses the current [MsiPatchCertificate table](msipatchcertificate-table.md), which consists of the MsiPatchCertificate table in the original package and any changes to the table by patches sequenced prior to the current one. A patch can add new certificates to the MsiPatchCertificate table to evaluate patches sequenced after the current patch. A revoked certificate is always rejected.

     

-   Least-privilege patching has not been disabled by setting the [**MSIDISABLELUAPATCHING**](msidisableluapatching.md) property or the [DisableLUAPatching](disableluapatching.md) policy.

A patch that has been applied using UAC patching can also be removed by a non-administrator.

Administrators can apply patches to per-machine installed products regardless of the application's UAC setting.

You can determine whether least-privilege patching is enabled for an application by using the [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa) function to query for the INSTALLPROPERTY\_AUTHORIZED\_LUA\_APP property, or by using the [**ProductInfo**](installer-productinfo.md) method to query for the "AuthorizedLUAApp" property. If the value of either property is 1, the application is enabled for least-privilege user account patching.

An administrator can disable least-privilege patching on the computer by setting the [DisableLUAPatching](disableluapatching.md) policy to 1. You can set the [**MSIDISABLELUAPATCHING**](msidisableluapatching.md) property to 1 during the initial installation of an application to prevent least-privilege patching for that application only.

This functionality is available beginning with Windows Installer version 3.0. User Account Control (UAC) patching was called least-privilege user account (LUA) patching in Windows XP. LUA patching is not available on Windows 2000 and Windows Server 2003.

For more information about application compatibility and developing applications that are compatible with User Account Control (UAC), see the UAC information that is provided on [Microsoft Technet](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc709691(v=ws.10)).

 

 
