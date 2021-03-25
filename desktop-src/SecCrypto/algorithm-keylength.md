---
description: Sets or retrieves the length of the key.
ms.assetid: c0176d2d-c000-4529-af45-1cc9060ca56a
title: Algorithm.KeyLength property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Algorithm.KeyLength
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Algorithm.KeyLength property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**AlgorithmIdentifier Class**](/dotnet/api/system.security.cryptography.pkcs.algorithmidentifier?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **KeyLength** property sets or retrieves the length of the key.

This property is read/write.

## Syntax


```VB
Algorithm.KeyLength As CAPICOM_ENCRYPTION_KEY_LENGTH
```



## Property value

A value of the [**CAPICOM\_ENCRYPTION\_KEY\_LENGTH**](capicom-encryption-key-length.md) enumeration that specifies the key length. The following table shows the possible values.



| Value                                                                                                                                                                                                                                        | Meaning                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_MAXIMUM"></span><span id="capicom_encryption_key_length_maximum"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_MAXIMUM**</dt> </dl>     | Use the maximum key length available with the indicated encryption algorithm.<br/> |
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_40_BITS"></span><span id="capicom_encryption_key_length_40_bits"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_40\_BITS**</dt> </dl>    | Use 40-bit keys.<br/>                                                              |
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_56_BITS"></span><span id="capicom_encryption_key_length_56_bits"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_56\_BITS**</dt> </dl>    | Use 56-bit keys if available.<br/>                                                 |
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_128_BITS"></span><span id="capicom_encryption_key_length_128_bits"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_128\_BITS**</dt> </dl> | Use 128-bit keys if available.<br/>                                                |
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_192_BITS"></span><span id="capicom_encryption_key_length_192_bits"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_192\_BITS**</dt> </dl> | Use 192-bit keys. This key length is available only for AES.<br/>                  |
| <span id="CAPICOM_ENCRYPTION_KEY_LENGTH_256_BITS"></span><span id="capicom_encryption_key_length_256_bits"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_256\_BITS**</dt> </dl> | Use 256-bit keys. This key length is available only for AES.<br/>                  |



 

## Remarks

When DES and 3DES encryption algorithms are used, the key lengths are standard and the **KeyLength** property is ignored.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Algorithm**](algorithm.md)
</dt> </dl>

 

 
