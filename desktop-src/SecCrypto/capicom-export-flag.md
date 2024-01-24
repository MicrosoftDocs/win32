---
description: The CAPICOM\_EXPORT\_FLAG enumeration type defines whether any private key export errors are ignored.
ms.assetid: 12e6862b-5c73-4e45-8829-8086048e94f3
title: CAPICOM_EXPORT_FLAG enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_EXPORT_FLAG
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_EXPORT\_FLAG enumeration

The **CAPICOM\_EXPORT\_FLAG** enumeration type defines whether any private key export errors are ignored.

## Members



| Member                                                            | Description                                               | Value |
|-------------------------------------------------------------------|-----------------------------------------------------------|-------|
| **CAPICOM\_EXPORT\_DEFAULT**                                      | Any private key export errors are not ignored.<br/> | 0     |
| **CAPICOM\_EXPORT\_IGNORE\_PRIVATE\_KEY\_NOT\_EXPORTABLE\_ERROR** | Any private key export errors are ignored.<br/>     | 1     |



## Remarks

The CAPICOM\_EXPORT\_FLAG enumeration type is used by the following method:

-   [**Certificates.Save**](certificates-save.md)

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




