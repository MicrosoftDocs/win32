---
description: Imports certificates from a file into the store.
ms.assetid: 884326b4-77ca-43d4-bda9-127d823ce9bc
title: Store.Load method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Load
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Load method

\[The **Load** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/dotnet/api/system.security.cryptography.x509certificates.x509store) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Load** method imports certificates from a file into the store.

## Syntax


```VB
Store.Load( _
  ByVal FileName, _
  [ ByVal Password ], _
  [ ByVal KeyStorageFlag ] _
)
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

The string that contains the path to a .cer, .sst, .spc, .p7s, or .pfx file, or any Authenticode signed file.

</dd> <dt>

*Password* \[in, optional\]
</dt> <dd>

The string that contains the plaintext password to the file. Up to 32 Unicode characters, including a terminating null character, can be used for the password. For information about protecting the password, see [Handling Passwords](../secbp/handling-passwords.md).

</dd> <dt>

*KeyStorageFlag* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_KEY\_STORAGE\_FLAG**](capicom-key-storage-flag.md) enumeration that defines key storage flags. The default is CAPICOM\_KEY\_STORAGE\_DEFAULT. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="CAPICOM_KEY_STORAGE_DEFAULT"></span><span id="capicom_key_storage_default"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_DEFAULT**</dt> </dl>                       | Default key storage.<br/>       |
| <span id="CAPICOM_KEY_STORAGE_EXPORTABLE"></span><span id="capicom_key_storage_exportable"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_EXPORTABLE**</dt> </dl>              | The key is exportable.<br/>     |
| <span id="CAPICOM_KEY_STORAGE_USER_PROTECTED"></span><span id="capicom_key_storage_user_protected"></span><dl> <dt>**CAPICOM\_KEY\_STORAGE\_USER\_PROTECTED**</dt> </dl> | The key is user protected.<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the **Load** method is called on a memory store, any key containers that are created will be deleted when the memory store is deleted. For example, if a .pfx file is loaded into a memory store and later added to a system store (such as the My store) from the memory store, the certificate in the My store will not contain a key. In this case, the .pfx file should be loaded directly into the My store.

This method raises CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

If the password fails to decrypt the private key file, then the default [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) should be queried. If the default CSP is the Microsoft Base Cryptographic Provider and the decrypt operation fails, then the decrypt operation should be tried again with the Microsoft Strong Cryptographic Provider or Microsoft Enhanced Cryptographic Provider, whichever is available.

If the certificate being loaded into the store is the same as one that is already there, the **Load** method will delete the existing certificate from the store and then add the new certificate. The new certificate will inherit properties from the existing certificate. The existing private key container is replaced by the new private key container.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> </dl>

 

 
