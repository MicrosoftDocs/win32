---
description: Defines the algorithms to be used in encryption and decryption.
ms.assetid: c7aacd1c-02f6-4cf5-9305-50e2330f243c
title: CAPICOM_ENCRYPTION_ALGORITHM enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_ENCRYPTION_ALGORITHM
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_ENCRYPTION\_ALGORITHM enumeration

The **CAPICOM\_ENCRYPTION\_ALGORITHM** enumeration type defines the algorithms to be used in encryption and decryption.

## Members



| Member                                   | Description                                                                                                                                                                                              | Value     |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **CAPICOM\_ENCRYPTION\_ALGORITHM\_RC2**  | Use RSA RC2 encryption.<br/>                                                                                                                                                                       | 0         |
| **CAPICOM\_ENCRYPTION\_ALGORITHM\_RC4**  | Use RSA RC4 encryption.<br/>                                                                                                                                                                       | 1         |
| **CAPICOM\_ENCRYPTION\_ALGORITHM\_DES**  | Use DES encryption.<br/>                                                                                                                                                                           | 2         |
| **CAPICOM\_ENCRYPTION\_ALGORITHM\_3DES** | Use triple DES encryption.<br/>                                                                                                                                                                    | 3         |
| **CAPICOM\_ENCRYPTION\_ALGORITHM\_AES**  | Use the [*Advanced Encryption Standard*](../secgloss/a-gly.md) (AES) algorithm. This value is valid for the [**EncryptedData**](encrypteddata.md) object only.<br/> | 4 // v2.0 |



## Remarks

The **CAPICOM\_ENCRYPTION\_ALGORITHM** enumeration type is used by the [**Algorithm.Name**](algorithm-name.md) property.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
