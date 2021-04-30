---
description: The CAPICOM\_KEY\_USAGE enumeration defines the ways in which a key can be used. Introduced in CAPICOM 2.0.
ms.assetid: 7143567b-5882-44a3-ae30-fb8965fb7997
title: CAPICOM_KEY_USAGE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_KEY_USAGE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_KEY\_USAGE enumeration

The **CAPICOM\_KEY\_USAGE** enumeration defines the ways in which a key can be used. Introduced in CAPICOM 2.0.

## Members



| Member                                      | Description                                                                                                                      | Value      |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------|
| **CAPICOM\_DIGITAL\_SIGNATURE\_KEY\_USAGE** | The key can be used to create a digital signature.<br/>                                                                    | 0x00000080 |
| **CAPICOM\_NON\_REPUDIATION\_KEY\_USAGE**   | The key can be used for [*nonrepudiation*](../secgloss/n-gly.md).<br/> | 0x00000040 |
| **CAPICOM\_KEY\_ENCIPHERMENT\_KEY\_USAGE**  | The key can be used to encrypt a key.<br/>                                                                                 | 0x00000020 |
| **CAPICOM\_DATA\_ENCIPHERMENT\_KEY\_USAGE** | The key can be used to encrypt data.<br/>                                                                                  | 0x00000010 |
| **CAPICOM\_KEY\_AGREEMENT\_KEY\_USAGE**     | The key can be used for key agreement.<br/>                                                                                | 0x00000008 |
| **CAPICOM\_KEY\_CERT\_SIGN\_KEY\_USAGE**    | The key can be used for key certificate signing. This value is equivalent to CAPICOM\_OFFLINE\_CRL\_SIGN\_KEY\_USAGE.<br/> | 0x00000004 |
| **CAPICOM\_OFFLINE\_CRL\_SIGN\_KEY\_USAGE** | The key can be used for key certificate signing. This value is equivalent to CAPICOM\_KEY\_CERT\_SIGN\_KEY\_USAGE.<br/>    | 0x00000002 |
| **CAPICOM\_CRL\_SIGN\_KEY\_USAGE**          | The key can be used for signing.<br/>                                                                                      | 0x00000002 |
| **CAPICOM\_ENCIPHER\_ONLY\_KEY\_USAGE**     | The key can only be used to encrypt.<br/>                                                                                  | 0x00000001 |
| **CAPICOM\_DECIPHER\_ONLY\_KEY\_USAGE**     | The key can only be used to decrypt.<br/>                                                                                  | 0x00008000 |



## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
