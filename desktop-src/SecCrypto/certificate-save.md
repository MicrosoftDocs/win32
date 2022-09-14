---
description: Saves the certificate to a file.
ms.assetid: 2012b39b-47fd-4071-9752-98bb10954fc0
title: ICertificate2::Save method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.Save
- ICertificate2.Save
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::Save method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Save** method saves the certificate to a file. This method was introduced in CAPICOM 2.0.

## Syntax


```VB
Certificate.Save( _
  ByVal FileName, _
  [ ByVal Password ], _
  [ ByVal SaveAs ], _
  [ ByVal IncludeOption ] _
)
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

A string that contains the name of the output file where the certificate will be saved.

</dd> <dt>

*Password* \[in, optional\]
</dt> <dd>

A string that contains the [*plaintext*](../secgloss/p-gly.md) password for a [*private key*](../secgloss/p-gly.md) file. The password can contain up to 32 Unicode characters, including a terminating null character. For information about protecting the password, see [Handling Passwords](../secbp/handling-passwords.md).

</dd> <dt>

*SaveAs* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_CERTIFICATE\_SAVE\_AS\_TYPE**](capicom-certificate-save-as-type.md) enumeration that specifies the format of the output file. The default is **CAPICOM\_CERTIFICATE\_SAVE\_AS\_CER**. The following table shows the possible values.



| Value                                                                                                                                                                                                                  | Meaning                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_CERTIFICATE_SAVE_AS_CER"></span><span id="capicom_certificate_save_as_cer"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_SAVE\_AS\_CER**</dt> </dl> | The output file will be formatted as a .cer file with no private keys saved.<br/>                                                         |
| <span id="CAPICOM_CERTIFICATE_SAVE_AS_PFX"></span><span id="capicom_certificate_save_as_pfx"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_SAVE\_AS\_PFX**</dt> </dl> | The output file will be formatted as a .pfx (PKCS \#12) file and any associated private keys that are exportable will also be saved.<br/> |



 

</dd> <dt>

*IncludeOption* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_CERTIFICATE\_INCLUDE\_OPTION**](capicom-certificate-include-option.md) enumeration that specifies how many certificates in the chain are saved to the output file. The default is CAPICOM\_CERTIFICATE\_INCLUDE\_END\_ENTITY\_ONLY. The following table shows the possible values.



| Value                                                                                                                                                                                                                                                             | Meaning                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="CAPICOM_CERTIFICATE_INCLUDE_CHAIN_EXCEPT_ROOT"></span><span id="capicom_certificate_include_chain_except_root"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_INCLUDE\_CHAIN\_EXCEPT\_ROOT**</dt> </dl> | Saves all certificates in the chain with the exception of the root entity<br/> |
| <span id="CAPICOM_CERTIFICATE_INCLUDE_WHOLE_CHAIN"></span><span id="capicom_certificate_include_whole_chain"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_INCLUDE\_WHOLE\_CHAIN**</dt> </dl>                    | Saves the complete certificate chain<br/>                                      |
| <span id="CAPICOM_CERTIFICATE_INCLUDE_END_ENTITY_ONLY"></span><span id="capicom_certificate_include_end_entity_only"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_INCLUDE\_END\_ENTITY\_ONLY**</dt> </dl>       | Saves only the end entity certificate<br/>                                     |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method raises CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
