---
description: Imports a certificate from a file.
ms.assetid: 62c3bf8e-2f52-4342-b3ee-744b032578bf
title: ICertificate2::Load method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.Load
- ICertificate2.Load
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::Load method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Load** method imports a certificate from a file. This method was introduced in CAPICOM 2.0.

## Syntax


```VB
Certificate.Load( _
  ByVal FileName, _
  [ ByVal Password ], _
  [ ByVal KeyStorageFlag ], _
  [ ByVal KeyLocation ] _
)
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

A string that contains the path to a .cer or .pfx file that contains the certificate data.

</dd> <dt>

*Password* \[in, optional\]
</dt> <dd>

A string that contains the [*plaintext*](../secgloss/p-gly.md) password to the [*private key*](../secgloss/p-gly.md) file. The password can contain up to 32 Unicode characters, including a terminating null character. For information about protecting the password, see [Handling Passwords](../secbp/handling-passwords.md).

</dd> <dt>

*KeyStorageFlag* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_KEY\_STORAGE\_FLAG**](capicom-key-storage-flag.md) enumeration that defines key storage flags. The default is CAPICOM\_KEY\_STORAGE\_DEFAULT. The following table shows the possible values.



| Value                                                                                                                                                                                                                           | Meaning                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="CAPICOM_KEY_STORAGE_DEFAULT"></span><span id="capicom_key_storage_default"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_DEFAULT**</dt> </dl>                       | Default key storage.<br/>       |
| <span id="CAPICOM_KEY_STORAGE_EXPORTABLE"></span><span id="capicom_key_storage_exportable"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_EXPORTABLE**</dt> </dl>              | The key is exportable.<br/>     |
| <span id="CAPICOM_KEY_STORAGE_USER_PROTECTED"></span><span id="capicom_key_storage_user_protected"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_USER\_PROTECTED**</dt> </dl> | The key is user protected.<br/> |



 

</dd> <dt>

*KeyLocation* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_KEY\_LOCATION**](capicom-key-location.md) enumeration that defines key location types. The default value is CAPICOM\_CURRENT\_USER\_KEY. The following table shows the possible values.



| Value                                                                                                                                                                                               | Meaning                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| <span id="CAPICOM_CURRENT_USER_KEY"></span><span id="capicom_current_user_key"></span><dl> <dt>**CAPICOM\_CURRENT\_USER\_KEY**</dt> </dl>    | The key is a user key.<br/>    |
| <span id="CAPICOM_LOCAL_MACHINE_KEY"></span><span id="capicom_local_machine_key"></span><dl> <dt>**CAPICOM\_LOCAL\_MACHINE\_KEY**</dt> </dl> | The key is a machine key.<br/> |



 

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



 

 
