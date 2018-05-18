---
title: GenerateTokenActivationChallenge method of the SoftwareLicensingProduct class
description: Returns token-based activation challenge.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3fb13f7-ddd1-477b-8caa-c3d730ae3f24'
keywords: ["GenerateTokenActivationChallenge method Windows Management Instrumentation", "GenerateTokenActivationChallenge method Windows Management Instrumentation , SoftwareLicensingProduct class", "SoftwareLicensingProduct class Windows Management Instrumentation , GenerateTokenActivationChallenge method"]
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.GenerateTokenActivationChallenge
api_location:
- SppWmi.dll
api_type:
- COM
---

# GenerateTokenActivationChallenge method of the SoftwareLicensingProduct class

Returns token-based activation challenge.

## Syntax


```mof
uint32 GenerateTokenActivationChallenge(
  [out] string Challenge
);
```



## Parameters

<dl> <dt>

*Challenge* \[out\]
</dt> <dd>

Specifies the challenge string that is associated with the token.

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

 

 





