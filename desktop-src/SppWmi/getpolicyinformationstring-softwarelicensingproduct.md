---
title: GetPolicyInformationString method of the SoftwareLicensingProduct class
description: Gets policy information of type string.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43bf5db3-fe84-47ab-9868-c7025e8317b5
keywords:
- GetPolicyInformationString method Windows Management Instrumentation
- GetPolicyInformationString method Windows Management Instrumentation , SoftwareLicensingProduct class
- SoftwareLicensingProduct class Windows Management Instrumentation , GetPolicyInformationString method
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.GetPolicyInformationString
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

# GetPolicyInformationString method of the SoftwareLicensingProduct class

Gets policy information of type string.

## Syntax


```mof
uint32 GetPolicyInformationString(
  [in]  string PolicyName,
  [out] string PolicyValue
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

 

 





