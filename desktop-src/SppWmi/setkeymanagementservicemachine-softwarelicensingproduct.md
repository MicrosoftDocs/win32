---
title: SetKeyManagementServiceMachine method of the SoftwareLicensingProduct class
description: Sets the KMS hostname to use for volume activation.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e123fee4-7c0e-4aff-a42a-c06a2e29cecd
keywords:
- SetKeyManagementServiceMachine method Windows Management Instrumentation
- SetKeyManagementServiceMachine method Windows Management Instrumentation , SoftwareLicensingProduct class
- SoftwareLicensingProduct class Windows Management Instrumentation , SetKeyManagementServiceMachine method
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.SetKeyManagementServiceMachine
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

# SetKeyManagementServiceMachine method of the SoftwareLicensingProduct class

Sets the KMS hostname to use for volume activation.

## Syntax


```mof
uint32 SetKeyManagementServiceMachine(
  [in] string MachineName
);
```



## Parameters

<dl> <dt>

*MachineName* \[in\]
</dt> <dd>

Specifies the KMS hostname.

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

 

 





