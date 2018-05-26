---
Description: Defines the kind of attribute associated with a signature.
ms.assetid: 94f0dce4-0b32-4c39-ab2e-b01795432acd
title: CAPICOM\_ATTRIBUTE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CAPICOM\_ATTRIBUTE enumeration

The **CAPICOM\_ATTRIBUTE** enumeration type defines the kind of attribute associated with a [*signature*](security.d_gly#-security-digital-signature-gly).

## Members



| Member                                                       | Description                                                                | Value |
|--------------------------------------------------------------|----------------------------------------------------------------------------|-------|
| **CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_SIGNING\_TIME**         | The attribute contains the time that the signature was created.<br/> | 0     |
| **CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_DOCUMENT\_NAME**        | The attribute contains the name of the signed document.<br/>         | 1     |
| **CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_DOCUMENT\_DESCRIPTION** | The attribute contains a description of the signed document.<br/>    | 2     |



## Remarks

The **CAPICOM\_ATTRIBUTE** enumeration type is used by the [**Attribute.Name**](attribute-name.md) property.

## Requirements



|                            |                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




