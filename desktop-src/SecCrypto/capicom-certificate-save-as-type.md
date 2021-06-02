---
description: Defines the format of a file containing certificate information.
ms.assetid: 417a6d1b-6329-418c-823c-d82b94207fd6
title: CAPICOM_CERTIFICATE_SAVE_AS_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_CERTIFICATE_SAVE_AS_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_CERTIFICATE\_SAVE\_AS\_TYPE enumeration

The **CAPICOM\_CERTIFICATE\_SAVE\_AS\_TYPE** enumeration type defines the format of a file containing certificate information. This enumeration type was introduced by CAPICOM 2.0.

## Members



| Member                                  | Description                                                                                                                                   | Value |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_CERTIFICATE\_SAVE\_AS\_PFX** | The output file will be formatted as a PFX (PKCS 12) file and any associated private keys which are exportable will also be saved.<br/> | 0     |
| **CAPICOM\_CERTIFICATE\_SAVE\_AS\_CER** | The output file will be formatted as a CER file with no private keys saved.<br/>                                                        | 1     |



## Remarks

The **CAPICOM\_CERTIFICATE\_SAVE\_AS\_TYPE** enumeration type is used by the [**Certificate.Save**](certificate-save.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




