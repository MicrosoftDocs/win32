---
Description: Indicates what is checked when a digital signature is verified.
ms.assetid: e6259c3f-caed-42f4-832c-250365caa0d7
title: CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG enumeration

The **CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG** enumeration indicates what is checked when a [*digital signature*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) is verified.

## Members



| Member                                           | Description                                                                                                 | Value |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_VERIFY\_SIGNATURE\_ONLY**             | Only the signature is checked.<br/>                                                                   | 0     |
| **CAPICOM\_VERIFY\_SIGNATURE\_AND\_CERTIFICATE** | Both the signature and the validity of the certificate used to create the signature are checked.<br/> | 1     |



## Requirements



|                            |                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




