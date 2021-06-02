---
description: Indicates what is checked when a digital signature is verified.
ms.assetid: e6259c3f-caed-42f4-832c-250365caa0d7
title: CAPICOM_SIGNED_DATA_VERIFY_FLAG enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_SIGNED_DATA_VERIFY_FLAG
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG enumeration

The **CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG** enumeration indicates what is checked when a [*digital signature*](../secgloss/d-gly.md) is verified.

## Members



| Member                                           | Description                                                                                                 | Value |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_VERIFY\_SIGNATURE\_ONLY**             | Only the signature is checked.<br/>                                                                   | 0     |
| **CAPICOM\_VERIFY\_SIGNATURE\_AND\_CERTIFICATE** | Both the signature and the validity of the certificate used to create the signature are checked.<br/> | 1     |



## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
