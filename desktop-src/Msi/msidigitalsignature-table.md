---
description: The MsiDigitalSignature table contains the signature information for every digitally signed object in the installation database.
ms.assetid: 63d62152-4f01-454f-bdea-550f2a9f6b14
title: MsiDigitalSignature Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiDigitalSignature Table

The MsiDigitalSignature table contains the signature information for every digitally signed object in the installation database.

The MsiDigitalSignature and [MsiDigitalCertificate](msidigitalcertificate-table.md) tables are available starting with Windows Installer version 2.0.

Windows Installer version can use digital signatures as a means to detect corrupted resources. Windows Installer 2.0 can only verify the digital signatures of external cabinets, and only by the use of the MsiDigitalSignature and [MsiDigitalCertificate](msidigitalcertificate-table.md) tables.

Beginning with Windows Installer 3.0, the Windows Installer can verify the digital signatures of patches (.msp files) by using the [MsiPatchCertificate](msipatchcertificate-table.md) and MsiDigitalCertificate tables. For more information, see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [User Account Control (UAC) Patching](user-account-control--uac--patching.md).

The MsiDigitalSignature table has the following columns.



| Column               | Type                         | Key | Nullable |
|----------------------|------------------------------|-----|----------|
| Table                | [Identifier](identifier.md) | Y   | N        |
| SignObject           | [Text](text.md)             | Y   | N        |
| DigitalCertificate\_ | [Identifier](identifier.md) | N   | N        |
| Hash                 | [Binary](binary.md)         | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

With the Windows Installer version 2.0, the entry in this field must be "Media" for the [Media table](media-table.md). The installer only verifies the digital signatures on external cabinet media entries. This column and the SignObject column together specify the resource that is digitally signed.

</dd> <dt>

<span id="SignObject"></span><span id="signobject"></span><span id="SIGNOBJECT"></span>SignObject
</dt> <dd>

A foreign key into the primary key of the table specified by the Table column. This column and the Table column together specify the resource that is digitally signed.

</dd> <dt>

<span id="DigitalCertificate_"></span><span id="digitalcertificate_"></span><span id="DIGITALCERTIFICATE_"></span>DigitalCertificate\_
</dt> <dd>

A foreign key into the [MsiDigitalCertificate table](msidigitalcertificate-table.md). This identifies the certificate that must exist on the file for the associated action to succeed. The resource (or object) is always required to match this certificate in the MsiDigitalCertificate table.

</dd> <dt>

<span id="Hash"></span><span id="hash"></span><span id="HASH"></span>Hash
</dt> <dd>

In this field enter the reference hash of the resource (or object) that is to be checked against the actual hash of the resource (or object) obtained at run-time. If only the certificate needs to be verified, the Hash field may be null. Note that the format of the hash depends on the type of the resource (or object) being signed.

The Hash column contains the binary representation of the hash. The actual content is the **pbData** member of the [**CRYPT\_HASH\_BLOB**](/windows/win32/api/dpapi/ns-dpapi-crypt_integer_blob) structure, which is part of the **CRYPTOAPI\_BLOB** structure. This may be obtained by calling [WinVerifyTrust](/windows/win32/api/wintrust/nf-wintrust-winverifytrust) or [**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa).

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

[MsiDigitalCertificate table](msidigitalcertificate-table.md)
</dt> <dt>

[Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md)
</dt> </dl>

 

 
