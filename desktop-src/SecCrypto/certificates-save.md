---
description: Saves the Certificate objects in the collection.
ms.assetid: 1d4b7bd5-3ed3-4ace-9894-4e89c5cf844f
title: Certificates.Save method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Save
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificates.Save method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](/previous-versions/windows/embedded/hh424013(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **Save** method saves the [**Certificate**](certificate.md) objects in the collection.

## Syntax


```VB
Certificates.Save( _
  ByVal FileName, _
  [ ByVal Password ], _
  [ ByVal SaveAs ], _
  [ ByVal ExportFlag ] _
)
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

A string that contains the name of the output file where the certificates will be saved.

</dd> <dt>

*Password* \[in, optional\]
</dt> <dd>

A string that contains the [*plaintext*](../secgloss/p-gly.md) password for a [*private key*](../secgloss/p-gly.md) file. The default value is the empty string (""). Up to 32 Unicode characters, including a terminating null character, can be used for the password. For information about protecting the password, see [Handling Passwords](../secbp/handling-passwords.md).

</dd> <dt>

*SaveAs* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_CERTIFICATES\_SAVE\_AS\_TYPE**](capicom-certificates-save-as-type.md) enumeration that specifies the format of the output file. The default is CAPICOM\_CERTIFICATES\_SAVE\_AS\_PFX. The following table shows the possible values.



| Value                                                                                                                                                                                                                                          | Meaning                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="CAPICOM_CERTIFICATES_SAVE_AS_PFX"></span><span id="capicom_certificates_save_as_pfx"></span><dl> <dt>**CAPICOM\_CERTIFICATES\_SAVE\_AS\_PFX**</dt> </dl>                      | The certificates are saved as a PFX.<br/>      |
| <span id="CAPICOM_CERTIFICATES_SAVE_AS_PKCS7"></span><span id="capicom_certificates_save_as_pkcs7"></span><dl> <dt>**CAPICOM\_CERTIFICATES\_SAVE\_AS\_PKCS7**</dt> </dl>                | The certificates are saved as a PKCS \#7.<br/> |
| <span id="CAPICOM_CERTIFICATES_SAVE_AS_SERIALIZED"></span><span id="capicom_certificates_save_as_serialized"></span><dl> <dt>**CAPICOM\_CERTIFICATES\_SAVE\_AS\_SERIALIZED**</dt> </dl> | The certificates are saved as serialized.<br/> |



 

</dd> <dt>

*ExportFlag* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_EXPORT\_FLAG**](capicom-export-flag.md) enumeration that specifies whether any private key export errors are ignored. The default is CAPICOM\_EXPORT\_DEFAULT. The following table shows the possible values.



| Value                                                                                                                                                                                                                                                                                          | Meaning                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="CAPICOM_EXPORT_DEFAULT"></span><span id="capicom_export_default"></span><dl> <dt>**CAPICOM\_EXPORT\_DEFAULT**</dt> </dl>                                                                                                      | Private key export errors are not ignored.<br/> |
| <span id="CAPICOM_EXPORT_IGNORE_PRIVATE_KEY_NOT_EXPORTABLE_ERROR"></span><span id="capicom_export_ignore_private_key_not_exportable_error"></span><dl> <dt>**CAPICOM\_EXPORT\_IGNORE\_PRIVATE\_KEY\_NOT\_EXPORTABLE\_ERROR**</dt> </dl> | Private key export errors are ignored.<br/>     |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method raises CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

The [**Certificate**](certificate.md) objects can be retrieved by using the [**Store.Load**](store-load.md) method.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificates**](certificates.md)
</dt> </dl>

 

 
