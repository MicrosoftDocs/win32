---
title: CERT\_VALIDATION\_POLICY
description: The following constants indicate the certificate validation policies supported during certificate validation.
ms.assetid: d39c601d-da44-42eb-8be2-1711cff21368
topic_type:
- apiref
api_name:
- CERT_VALIDATION_POLICY_RESERVED
- CERT_VALIDATION_POLICY_NONE
- CERT_VALIDATION_POLICY_BASIC
- CERT_VALIDATION_POLICY_EXTENDED
api_location:
- EhStorExtensions.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CERT\_VALIDATION\_POLICY

The following constants indicate the certificate validation policies supported during certificate validation.

<dl> <dt>

<span id="CERT_VALIDATION_POLICY_RESERVED"></span><span id="cert_validation_policy_reserved"></span>**CERT\_VALIDATION\_POLICY\_RESERVED**
</dt> <dd> <dl> <dt>

0x00
</dt> <dt>



This value is reserved.


</dt> </dl> </dd> <dt>

<span id="CERT_VALIDATION_POLICY_NONE"></span><span id="cert_validation_policy_none"></span>**CERT\_VALIDATION\_POLICY\_NONE**
</dt> <dd> <dl> <dt>

0x01
</dt> <dt>



The corresponding private key of the stored certificate is used for authentication.


</dt> </dl> </dd> <dt>

<span id="CERT_VALIDATION_POLICY_BASIC"></span><span id="cert_validation_policy_basic"></span>**CERT\_VALIDATION\_POLICY\_BASIC**
</dt> <dd> <dl> <dt>

0x02
</dt> <dt>



The certificate and certificate chain conforms to the basic validation policy.


</dt> </dl> </dd> <dt>

<span id="CERT_VALIDATION_POLICY_EXTENDED"></span><span id="cert_validation_policy_extended"></span>**CERT\_VALIDATION\_POLICY\_EXTENDED**
</dt> <dd> <dl> <dt>

0x03
</dt> <dt>



The certificate chain conforms to the extended validation policy. The use of this validation policy must result in an error condition of the Certificate Silo if it does not support parsing of certificate extensions.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>EhStorExtensions.h</dt> </dl> |



 

 





