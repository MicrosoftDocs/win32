---
description: Defines the extended key usage names based on where they can be used.
ms.assetid: 78f9f9cb-46e7-4f81-a16e-503750a0d743
title: CAPICOM_EKU enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_EKU
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_EKU enumeration

The **CAPICOM\_EKU** enumeration type defines the extended key usage names based on where they can be used.

## Members



| Member                                     | Description                                                                                                                                                 | Value |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_EKU\_OTHER**                    | Certificate has uses defined in local policy. This is used if the EKU needed is not predefined and the OID value must be set by the application.<br/> | 0     |
| **CAPICOM\_EKU\_SERVER\_AUTH**             | Certificate can be used to authenticate a server.<br/>                                                                                                | 1     |
| **CAPICOM\_EKU\_CLIENT\_AUTH**             | Certificate can be used to authenticate a client.<br/>                                                                                                | 2     |
| **CAPICOM\_EKU\_CODE\_SIGNING**            | Certificate can be used to create a digital signature.<br/>                                                                                           | 3     |
| **CAPICOM\_EKU\_EMAIL\_PROTECTION**        | Certificate can be used for email protection.<br/>                                                                                                    | 4     |
| **CAPICOM\_EKU\_SMARTCARD\_LOGON**         | Certificate can be used for smart card logon. Introduced in CAPICOM 2.0.<br/>                                                                         | 5     |
| **CAPICOM\_EKU\_ENCRYPTING\_FILE\_SYSTEM** | Certificate can be used for EFS. Introduced in CAPICOM 2.0.<br/>                                                                                      | 6     |



## Remarks

The **CAPICOM\_EKU** enumeration type is used by the [**EKU.Name**](eku-name.md) property.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




