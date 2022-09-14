---
description: Sets or retrieves the type of hashing algorithm used.
ms.assetid: 3f8e83f2-0e46-494b-ac63-658e663680ea
title: HashedData.Algorithm property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- HashedData.Algorithm
api_type:
- COM
api_location:
- Capicom.dll
---

# HashedData.Algorithm property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**HashAlgorithm Class**](/previous-versions/windows/) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Algorithm** property sets or retrieves the type of hashing algorithm used.

## Syntax


```VB
HashedData.Algorithm As CAPICOM_HASH_ALGORITHM
```



## Property value

A value of the [**CAPICOM\_HASH\_ALGORITHM**](capicom-hash-algorithm.md) enumeration that defines a hash algorithm. The default value is CAPICOM\_HASH\_ALGORITHM\_SHA1. The following table shows the possible values.



| Value                                                                                                                                                                                                               | Meaning                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_HASH_ALGORITHM_SHA1"></span><span id="capicom_hash_algorithm_sha1"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_SHA1**</dt> </dl>           | SHA1 hashing algorithm.<br/>                                                                          |
| <span id="CAPICOM_HASH_ALGORITHM_MD2"></span><span id="capicom_hash_algorithm_md2"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_MD2**</dt> </dl>              | MD2 hashing algorithm.<br/>                                                                           |
| <span id="CAPICOM_HASH_ALGORITHM_MD4"></span><span id="capicom_hash_algorithm_md4"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_MD4**</dt> </dl>              | MD4 hashing algorithm.<br/>                                                                           |
| <span id="CAPICOM_HASH_ALGORITHM_MD5"></span><span id="capicom_hash_algorithm_md5"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_MD5**</dt> </dl>              | MD5 hashing algorithm.<br/>                                                                           |
| <span id="CAPICOM_HASH_ALGORITHM_SHA_256"></span><span id="capicom_hash_algorithm_sha_256"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_SHA\_256**</dt> </dl> | SHA-256 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/> |
| <span id="CAPICOM_HASH_ALGORITHM_SHA_384"></span><span id="capicom_hash_algorithm_sha_384"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_SHA\_384**</dt> </dl> | SHA-384 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/> |
| <span id="CAPICOM_HASH_ALGORITHM_SHA_512"></span><span id="capicom_hash_algorithm_sha_512"></span><dl> <dt>**CAPICOM\_HASH\_ALGORITHM\_SHA\_512**</dt> </dl> | SHA-512 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/> |



 

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**HashedData**](hasheddata.md)
</dt> </dl>

 

 
