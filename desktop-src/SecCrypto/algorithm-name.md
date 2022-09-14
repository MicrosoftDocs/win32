---
description: Sets or retrieves the algorithm used for signing, enveloping, and encrypting operations. This is the default property.
ms.assetid: e1144a9c-a352-4f73-a91c-ea66f3d61608
title: Algorithm.Name property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Algorithm.Name
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Algorithm.Name property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**AlgorithmIdentifier Class**](/dotnet/api/system.security.cryptography.pkcs.algorithmidentifier?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Name** property sets or retrieves the algorithm used for signing, enveloping, and encrypting operations. This is the default property.

This property is read/write.

## Syntax


```VB
Algorithm.Name As CAPICOM_ENCRYPTION_ALGORITHM
```



## Property value

A value of the [**CAPICOM\_ENCRYPTION\_ALGORITHM**](capicom-encryption-algorithm.md) enumeration that specifies which algorithm to use. The following table shows the possible values.



| Value                                                                                                                                                                                                                       | Meaning                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="CAPICOM_ENCRYPTION_ALGORITHM_RC2"></span><span id="capicom_encryption_algorithm_rc2"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_ALGORITHM\_RC2**</dt> </dl>    | Use RC2 encryption.<br/>        |
| <span id="CAPICOM_ENCRYPTION_ALGORITHM_RC4"></span><span id="capicom_encryption_algorithm_rc4"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_ALGORITHM\_RC4**</dt> </dl>    | Use RC4 encryption.<br/>        |
| <span id="CAPICOM_ENCRYPTION_ALGORITHM_DES"></span><span id="capicom_encryption_algorithm_des"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_ALGORITHM\_DES**</dt> </dl>    | Use DES encryption.<br/>        |
| <span id="CAPICOM_ENCRYPTION_ALGORITHM_3DES"></span><span id="capicom_encryption_algorithm_3des"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_ALGORITHM\_3DES**</dt> </dl> | Use triple DES encryption.<br/> |
| <span id="CAPICOM_ENCRYPTION_ALGORITHM_AES"></span><span id="capicom_encryption_algorithm_aes"></span><dl> <dt>**CAPICOM\_ENCRYPTION\_ALGORITHM\_AES**</dt> </dl>    | Use the AES algorithm.<br/>     |



 

## Remarks

When the value of this property is reset, directly or indirectly, the whole state of the object is reset.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
