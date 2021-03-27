---
description: The FileSignatureInfo method of the Installer object takes the path to a file and returns a SAFEARRAY of bytes that represent the hash or the encoded certificate.
ms.assetid: ab34bc46-8a8f-4b48-a1d1-d824ff36a9cc
title: Installer.FileSignatureInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FileSignatureInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FileSignatureInfo method

The **FileSignatureInfo** method of the [**Installer**](installer-object.md) object takes the path to a file and returns a SAFEARRAY of bytes that represent the hash or the encoded certificate. The values can then be used to populate the [MsiDigitalSignature](msidigitalsignature-table.md), [MsiPatchCertificate](msipatchcertificate-table.md), and [MsiDigitalCertificate](msidigitalcertificate-table.md) tables.

For more information, see the [**SAFEARRAY Data Type**](/windows/win32/api/oaidl/ns-oaidl-safearray).

## Syntax


```JScript
Installer.FileSignatureInfo(
  FilePath,
  Options,
  Format
)
```



## Parameters

<dl> <dt>

*FilePath* 
</dt> <dd>

Full path to a file that is digitally signed.

When populating the [MsiDigitalSignature](msidigitalsignature-table.md) and [MsiDigitalCertificate](msidigitalcertificate-table.md) tables, *FilePath* points to a digitally signed cabinet. When populating the [MsiPatchCertificate](msipatchcertificate-table.md) and MsiDigitalCertificate tables, *FilePath* points to a digitally signed patch.

</dd> <dt>

*Options* 
</dt> <dd>

Special error case flags.



| Flag                                                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiSignatureOptionInvalidHashFatal"></span><span id="msisignatureoptioninvalidhashfatal"></span><span id="MSISIGNATUREOPTIONINVALIDHASHFATAL"></span><dl> <dt>**msiSignatureOptionInvalidHashFatal**</dt> <dt>1</dt> </dl> | With *Options* set to msiSignatureOptionInvalidHashFatal, **FileSignatureInfo** always returns a fatal error for an invalid hash. <br/> If *Options* is not set to msiSignatureOptionInvalidHashFatal and *Format* is set to msiSignatureInfoCertificate, **FileSignatureInfo** does not return an error for an invalid hash.<br/> |



 

</dd> <dt>

*Format* 
</dt> <dd>

The requested signature information.



| Flag                                                                                                                                                                                                                                                                                                        | Meaning                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="msiSignatureInfoCertificate"></span><span id="msisignatureinfocertificate"></span><span id="MSISIGNATUREINFOCERTIFICATE"></span><dl> <dt>**msiSignatureInfoCertificate**</dt> <dt>0</dt> </dl> | Returns a SAFEARRAY of bytes that represent the encoded certificate.<br/> |
| <span id="msiSignatureInfoHash"></span><span id="msisignatureinfohash"></span><span id="MSISIGNATUREINFOHASH"></span><dl> <dt>**msiSignatureInfoHash**</dt> <dt>1</dt> </dl>                             | Returns a SAFEARRAY of bytes that represent the hash.<br/>                |



 

</dd> </dl>

## Return value

If successful, the method returns a [SAFEARRAY](/windows/win32/api/oaidl/ns-oaidl-safearray) of bytes that contain either the hash or encoded certificate.

## Remarks

To author a fully verified signed installation by using automation, use the **FileSignatureInfo** method to populate the [MsiDigitalCertificate](msidigitalcertificate-table.md), [MsiPatchCertificate](msipatchcertificate-table.md), and [MsiDigitalSignature](msidigitalsignature-table.md) tables. For more information, see [Authoring a Fully Verified Signed Installation Using Automation](authoring-a-fully-verified-signed-installation-using-automation.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[Authoring a Fully Verified Signed Installation Using Automation](authoring-a-fully-verified-signed-installation-using-automation.md)
</dt> <dt>

[Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md)
</dt> <dt>

[**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa)
</dt> </dl>

 

 
