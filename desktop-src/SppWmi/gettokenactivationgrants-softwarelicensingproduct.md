---
title: GetTokenActivationGrants method of the SoftwareLicensingProduct class
description: Returns token-based activation grants.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a424f797-60c9-4a03-a88b-5de28455cc5a'
keywords: ["GetTokenActivationGrants method Windows Management Instrumentation", "GetTokenActivationGrants method Windows Management Instrumentation , SoftwareLicensingProduct class", "SoftwareLicensingProduct class Windows Management Instrumentation , GetTokenActivationGrants method"]
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.GetTokenActivationGrants
api_location:
- SppWmi.dll
api_type:
- COM
---

# GetTokenActivationGrants method of the SoftwareLicensingProduct class

Returns token-based activation grants.

## Syntax


```mof
uint32 GetTokenActivationGrants(
  [out] string Grants[]
);
```



## Parameters

<dl> <dt>

*Grants* \[out\]
</dt> <dd>

Specifies the activation grant that is associated with the token.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingProduct**](softwarelicensingproduct.md)
</dt> </dl>

 

 





