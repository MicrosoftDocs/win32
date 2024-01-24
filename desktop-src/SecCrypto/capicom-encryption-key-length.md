---
description: Defines the key length to be used in encryption.
ms.assetid: a91e75db-f81e-4908-b795-34be7a1c242d
title: CAPICOM_ENCRYPTION_KEY_LENGTH enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_ENCRYPTION_KEY_LENGTH
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_ENCRYPTION\_KEY\_LENGTH enumeration

The **CAPICOM\_ENCRYPTION\_KEY\_LENGTH** enumeration type defines the [*key length*](../secgloss/k-gly.md) to be used in encryption.

## Members



| Member                                          | Description                                                                               | Value     |
|-------------------------------------------------|-------------------------------------------------------------------------------------------|-----------|
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_MAXIMUM**   | Uses the maximum key length available with the indicated encryption algorithm.<br/> | 0         |
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_40\_BITS**  | Uses 40-bit keys.<br/>                                                              | 1         |
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_56\_BITS**  | Uses 56-bit keys if available.<br/>                                                 | 2         |
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_128\_BITS** | Uses 128-bit keys if available.<br/>                                                | 3         |
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_192\_BITS** | Uses 192-bit keys. This key length is available only for AES.<br/>                  | 4 // v2.0 |
| **CAPICOM\_ENCRYPTION\_KEY\_LENGTH\_256\_BITS** | Uses 256-bit keys. This key length is available only for AES.<br/>                  | 5 // v2.0 |



## Remarks

The **CAPICOM\_ENCRYPTION\_KEY\_LENGTH** enumeration type is used by the [**Algorithm.KeyLength**](algorithm-keylength.md) property.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
