---
description: Windows Installer can use digital signatures to detect corrupted resources.
ms.assetid: 49f1c1f9-d342-47e0-8888-2eadc5dbd000
title: Digital Signatures and External Cabinet Files
ms.topic: article
ms.date: 05/31/2018
---

# Digital Signatures and External Cabinet Files

Windows Installer can use digital signatures to detect corrupted resources. When installing an external resource, the signer certificate belonging to the resource may be verified against a reference signer certificate authored in the package. The installer cannot verify signatures for internal cabinets. It can only verify digital signatures by using the [MsiDigitalSignature table](msidigitalsignature-table.md) and [MsiDigitalCertificate table](msidigitalcertificate-table.md).

Windows Installer does the following when installing a file stored in an external cabinet:

-   The installer checks to see whether the media entry for that external cabinet is listed in the [MsiDigitalSignature table](msidigitalsignature-table.md). A file stored in an external cabinet is identified by having an entry in the Cabinet column of the [Media table](media-table.md) that is not prefixed by a '\#' character.
-   Before opening the external cabinet, the installer calls WinVerifyTrust to extract the current certificate and hash information. If there is a mismatch between the current signature information on the cabinet and the signature information authored in the package, the installation fails. The installation fails because the cabinet may have been compromised and cannot be trusted.

For more information regarding the use of digital signatures, digital certificates, and [**WinVerifyTrust**](/windows/desktop/api/wintrust/nf-wintrust-winverifytrust), see the [Security](https://msdn.microsoft.com/library/cc527452.aspx) section of the Microsoft Windows Software Development Kit (SDK).

For more information, see [**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa), [MsiDigitalCertificate table](msidigitalcertificate-table.md), and [MsiDigitalSignature table](msidigitalsignature-table.md).

 

 
