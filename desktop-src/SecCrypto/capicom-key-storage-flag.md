---
Description: 'The CAPICOM\_KEY\_STORAGE\_FLAG enumeration defines key storage flags.'
ms.assetid: '326cef75-24a5-4dc9-a7e9-a63dd3d8de54'
title: 'CAPICOM\_KEY\_STORAGE\_FLAG enumeration'
---

# CAPICOM\_KEY\_STORAGE\_FLAG enumeration

The **CAPICOM\_KEY\_STORAGE\_FLAG** enumeration defines key storage flags.

## Members



| Member                                     | Description                           | Value |
|--------------------------------------------|---------------------------------------|-------|
| **CAPICOM\_KEY\_STORAGE\_DEFAULT**         | Default key storage.<br/>       | 0     |
| **CAPICOM\_KEY\_STORAGE\_EXPORTABLE**      | The key is exportable.<br/>     | 1     |
| **CAPICOM\_KEY\_STORAGE\_USER\_PROTECTED** | The key is user protected.<br/> | 2     |



## Remarks

This enumeration is used by the following method:

-   [**Certificate.Load**](certificate-load.md)
-   [**Store.Load**](store-load.md)

## Requirements



|                            |                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




