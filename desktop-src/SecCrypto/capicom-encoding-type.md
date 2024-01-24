---
description: Indicates the encoding type used.
ms.assetid: 13e78a5e-3a31-44de-b249-28e360e1e087
title: CAPICOM_ENCODING_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_ENCODING_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_ENCODING\_TYPE enumeration

The **CAPICOM\_ENCODING\_TYPE** enumeration type indicates the encoding type used.

## Members



| Member                      | Description                                                                                                                                                                                 | Value      |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **CAPICOM\_ENCODE\_ANY**    | Data is saved as a base64-encoded string or a pure binary sequence. This encoding type is used only for input data that has an unknown encoding type. Introduced in CAPICOM 2.0.<br/> | 0xffffffff |
| **CAPICOM\_ENCODE\_BASE64** | Data is saved as a base64-encoded string.<br/>                                                                                                                                        | 0          |
| **CAPICOM\_ENCODE\_BINARY** | Data is saved as a pure binary sequence.<br/>                                                                                                                                         | 1          |



## Remarks

This enumeration type is used by the following CAPICOM methods and properties:

-   [**Certificate.Export**](certificate-export.md) method
-   [**EncodedData.Value**](encodeddata-value.md) property
-   [**EncryptedData.Encrypt**](encrypteddata-encrypt.md) method
-   [**EnvelopedData.Encrypt**](envelopeddata-encrypt.md) method
-   [**ExtendedProperty.Value**](extendedproperty-value.md) property
-   [**SignedData.Sign**](signeddata-sign.md) method
-   [**SignedData.CoSign**](signeddata-cosign.md) method
-   [**Store.Export**](store-export.md) method
-   [**Utilities.GetRandom**](utilities-getrandom.md) method

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




