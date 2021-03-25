---
description: Provides properties and methods to establish the content to be signed with a digital signature, to sign or cosign data digitally, and to verify the digital signature of signed data. The signed message is in PKCS \#7 format.
ms.assetid: 500437e8-a637-4e89-9ac9-aa3ea20d437f
title: SignedData object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SignedData
api_type:
- COM
api_location:
- Capicom.dll
---

# SignedData object

\[The **SignedData** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**SignedCms Class**](/dotnet/api/system.security.cryptography.pkcs.signedcms?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **SignedData** object provides properties and methods to establish the content to be signed with a [*digital signature*](../secgloss/d-gly.md), to sign or cosign data digitally, and to verify the digital signature of signed data. The signed message is in PKCS \#7 format.

A data signature, if verified, proves the association between a signer and data and shows that the data was not changed in any way after the signature was created.

## Members

The **SignedData** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SignedData** object has these methods.



| Method                              | Description                                                         |
|:------------------------------------|:--------------------------------------------------------------------|
| [**CoSign**](signeddata-cosign.md) | Cosigns an already signed message.<br/>                       |
| [**Sign**](signeddata-sign.md)     | Creates a digital signature on the content to be signed.<br/> |
| [**Verify**](signeddata-verify.md) | Determines the validity of a signature or signatures.<br/>    |



 

### Properties

The **SignedData** object has these properties.



| Property                                                   | Access type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-----------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Certificates**](signeddata-certificates.md)<br/> | Read-only<br/>  | Retrieves the [**Certificates**](certificates.md) collection of the signed data.<br/>                                                                                                                                                                                                                                                                                                                                                          |
| [**Content**](signeddata-content.md)<br/>           | Read/write<br/> | Data to be signed. This property must be initialized before the [**Sign**](signeddata-sign.md) method is called.<br/> When the value of this property is reset, directly or indirectly, the whole [*state*](../secgloss/s-gly.md) of the object is reset, and any signature that was associated with the object before the property was changed is lost.<br/> This is the default property.<br/> |
| [**Signers**](signeddata-signers.md)<br/>           | Read-only<br/>  | Retrieves the [**Signers**](signers.md) collection that represents the signature creators of the data.<br/>                                                                                                                                                                                                                                                                                                                                    |



 

## Remarks

The **SignedData** object can be created, and it is safe for scripting. The ProgID for the **SignedData** object is CAPICOM.SignedData.1.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
