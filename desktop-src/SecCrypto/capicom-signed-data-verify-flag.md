---
Description: 'Indicates what is checked when a digital signature is verified.'
ms.assetid: 'e6259c3f-caed-42f4-832c-250365caa0d7'
title: 'CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG enumeration'
---

# CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG enumeration

The **CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG** enumeration indicates what is checked when a [*digital signature*](security.d_gly#-security-digital-signature-gly) is verified.

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



 

 




