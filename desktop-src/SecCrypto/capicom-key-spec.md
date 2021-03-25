---
description: The CAPICOM\_KEY\_SPEC enumeration defines key specifications.
ms.assetid: e4aaaf69-ab28-4e8c-8a8a-6dc662299865
title: CAPICOM_KEY_SPEC enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_KEY_SPEC
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_KEY\_SPEC enumeration

The **CAPICOM\_KEY\_SPEC** enumeration defines key specifications.

## Members



| Member                              | Description                                                | Value |
|-------------------------------------|------------------------------------------------------------|-------|
| **CAPICOM\_KEY\_SPEC\_KEYEXCHANGE** | The key can be used for encryption and signing.<br/> | 1     |
| **CAPICOM\_KEY\_SPEC\_SIGNATURE**   | The key can be used only for signing.<br/>           | 2     |



## Remarks

The **CAPICOM\_KEY\_SPEC** enumeration is used by the following methods and properties:

-   [**PrivateKey.KeySpec**](privatekey-keyspec.md) property.
-   [**PrivateKey.Open**](privatekey-open.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




