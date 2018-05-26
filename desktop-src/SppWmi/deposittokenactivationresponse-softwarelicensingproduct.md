---
title: DepositTokenActivationResponse method of the SoftwareLicensingProduct class
description: Deposits the token-based activation response.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8924ad7-a39b-406e-ba40-d575b5b216bb
keywords:
- DepositTokenActivationResponse method Windows Management Instrumentation
- DepositTokenActivationResponse method Windows Management Instrumentation , SoftwareLicensingProduct class
- SoftwareLicensingProduct class Windows Management Instrumentation , DepositTokenActivationResponse method
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.DepositTokenActivationResponse
api_location:
- SppWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DepositTokenActivationResponse method of the SoftwareLicensingProduct class

Deposits the token-based activation response.

## Syntax


```mof
uint32 DepositTokenActivationResponse(
  [in] string Challenge,
  [in] string Response,
  [in] string CertChain
);
```



## Parameters

<dl> <dt>

*Challenge* \[in\]
</dt> <dd>

Specifies the challenge string that is associated with the token.

</dd> <dt>

*Response* \[in\]
</dt> <dd>

Specifies the response string that is associated with the token.

</dd> <dt>

*CertChain* \[in\]
</dt> <dd>

Specifies the certificate chain that is associated with the token.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingProduct**](softwarelicensingproduct.md)
</dt> </dl>

 

 





