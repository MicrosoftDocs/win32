---
title: GetPolicyInformationDWord method of the SoftwareLicensingProduct class
description: Gets license policy information of type DWORD.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce6e986d-0ab1-4517-91c0-3fd7b6c83c62
keywords:
- GetPolicyInformationDWord method Windows Management Instrumentation
- GetPolicyInformationDWord method Windows Management Instrumentation , SoftwareLicensingProduct class
- SoftwareLicensingProduct class Windows Management Instrumentation , GetPolicyInformationDWord method
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.GetPolicyInformationDWord
api_location:
- SppWmi.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPolicyInformationDWord method of the SoftwareLicensingProduct class

Gets license policy information of type DWORD.

## Syntax


```mof
uint32 GetPolicyInformationDWord(
  [in]  string PolicyName,
  [out] uint32 PolicyValue
);
```



## Parameters

<dl> <dt>

*PolicyName* \[in\]
</dt> <dd>

Specifies the policy name.

</dd> <dt>

*PolicyValue* \[out\]
</dt> <dd>

Specifies the policy value.

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

 

 





