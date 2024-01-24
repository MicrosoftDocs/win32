---
description: The CAPICOM\_HASH\_ALGORITHM enumeration defines a hash algorithm.
ms.assetid: 5373b6cc-944a-4d83-ac71-59edcb2af94e
title: CAPICOM_HASH_ALGORITHM enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_HASH_ALGORITHM
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_HASH\_ALGORITHM enumeration

The **CAPICOM\_HASH\_ALGORITHM** enumeration defines a hash algorithm.

## Members



| Member                                 | Description                                                                                                                                                                 | Value |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_HASH\_ALGORITHM\_SHA1**     | [*Secure Hash Algorithm*](../secgloss/s-gly.md) (SHA) that generates a 160-bit message digest.<br/> | 0     |
| **CAPICOM\_HASH\_ALGORITHM\_MD2**      | MD2 hashing algorithm.<br/>                                                                                                                                           | 1     |
| **CAPICOM\_HASH\_ALGORITHM\_MD4**      | MD4 hashing algorithm.<br/>                                                                                                                                           | 2     |
| **CAPICOM\_HASH\_ALGORITHM\_MD5**      | MD5 hashing algorithm.<br/>                                                                                                                                           | 3     |
| **CAPICOM\_HASH\_ALGORITHM\_SHA\_256** | SHA-256 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/>                                                                 | 4     |
| **CAPICOM\_HASH\_ALGORITHM\_SHA\_384** | SHA-384 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/>                                                                 | 5     |
| **CAPICOM\_HASH\_ALGORITHM\_SHA\_512** | SHA-512 hash algorithm.<br/> **CAPICOM 2.0.0.3 and earlier:** This value is not supported.<br/>                                                                 | 6     |



## Remarks

The **CAPICOM\_HASH\_ALGORITHM** enumeration is used by the [**HashedData.Algorithm**](hasheddata-algorithm.md) property.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
