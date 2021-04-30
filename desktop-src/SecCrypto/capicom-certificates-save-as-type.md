---
description: Defines the format of a file containing certificates information.
ms.assetid: 2118746a-9fa4-4e6a-82ce-e57f154f4a94
title: CAPICOM_CERTIFICATES_SAVE_AS_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_CERTIFICATES_SAVE_AS_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_CERTIFICATES\_SAVE\_AS\_TYPE enumeration

The **CAPICOM\_CERTIFICATES\_SAVE\_AS\_TYPE** enumeration type defines the format of a file containing certificates information. This enumeration type was introduced by CAPICOM 2.0.

## Members



| Member                                          | Description                                          | Value |
|-------------------------------------------------|------------------------------------------------------|-------|
| **CAPICOM\_CERTIFICATES\_SAVE\_AS\_SERIALIZED** | The saved certificates are serialized.<br/>    | 0     |
| **CAPICOM\_CERTIFICATES\_SAVE\_AS\_PKCS7**      | The certificates are saved as a PKCS \#7.<br/> | 1     |
| **CAPICOM\_CERTIFICATES\_SAVE\_AS\_PFX**        | The certificates are saved as a PFX.<br/>      | 2     |



## Remarks

The CAPICOM\_CERTIFICATES\_SAVE\_AS\_TYPE enumeration type is used by the [**Certificates.Save**](certificates-save.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




