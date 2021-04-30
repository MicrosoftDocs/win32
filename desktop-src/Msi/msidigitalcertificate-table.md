---
description: The MsiDigitalCertificate table stores certificates in binary stream format and associates each certificate with a primary key.
ms.assetid: 834534b8-540a-48c2-8eb0-3511d5a20cb4
title: MsiDigitalCertificate Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiDigitalCertificate Table

The MsiDigitalCertificate table stores certificates in binary stream format and associates each certificate with a primary key. The primary key is used to share certificates among multiple digitally signed objects. A digital certificate is a credential that provides a means to verify identity. For more information, see [Digital Certificates](../seccrypto/digital-certificates.md) in the [Cryptography](../seccrypto/cryptography-portal.md) section of the Microsoft Windows Software Development Kit (SDK).

The [MsiDigitalSignature](msidigitalsignature-table.md) and MsiDigitalCertificate tables are available starting with Windows Installer version 2.0.

Windows Installer can use digital signatures as a means to detect corrupted resources. Windows Installer version 2.0 can only verify the digital signatures of external cabinets, and only by the use of the [MsiDigitalSignature](msidigitalsignature-table.md) and MsiDigitalCertificate tables.

Beginning with Windows Installer version 3.0, the Windows Installer can verify the digital signatures of patches (.msp files) by using the [MsiPatchCertificate](msipatchcertificate-table.md) and MsiDigitalCertificate tables. For more information, see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [User Account Control (UAC) Patching](user-account-control--uac--patching.md).

The MsiDigitalCertificate table has the following columns.



| Column             | Type                         | Key | Nullable |
|--------------------|------------------------------|-----|----------|
| DigitalCertificate | [Identifier](identifier.md) | Y   | N        |
| CertData           | [Binary](binary.md)         | N   | N        |



 

## Columns

<dl> <dt>

<span id="DigitalCertificate"></span><span id="digitalcertificate"></span><span id="DIGITALCERTIFICATE"></span>DigitalCertificate
</dt> <dd>

Identifies the digital signature certificate. Primary key of table.

</dd> <dt>

<span id="CertData"></span><span id="certdata"></span><span id="CERTDATA"></span>CertData
</dt> <dd>

The binary representation of the digital certificate. The CertData column contains the encoded byte array of a certificate context. This is the **pbCertEncoded** member of the [**CERT\_CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_context) structure. The certificate context can be obtained by calling [**WinVerifyTrust**](/windows/win32/api/wintrust/nf-wintrust-winverifytrust), [**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa), or by importing a .cer file.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE29](ice29.md)  
[ICE32](ice32.md)  
[ICE66](ice66.md)  
[ICE81](ice81.md)  
</dl>

## Related topics

<dl> <dt>

[**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa)
</dt> <dt>

[MsiDigitalSignature table](msidigitalsignature-table.md)
</dt> <dt>

[Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md)
</dt> </dl>

 

 
