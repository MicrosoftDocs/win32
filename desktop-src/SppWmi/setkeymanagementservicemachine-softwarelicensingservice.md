---
title: SetKeyManagementServiceMachine method of the SoftwareLicensingService class
description: Sets the name of the key management service (KMS) machine to use for volume activation.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4172914-cfd4-40cb-9468-3f75bd76b242
keywords:
- SetKeyManagementServiceMachine method Windows Management Instrumentation
- SetKeyManagementServiceMachine method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , SetKeyManagementServiceMachine method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.SetKeyManagementServiceMachine
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

# SetKeyManagementServiceMachine method of the SoftwareLicensingService class

Sets the name of the key management service (KMS) machine to use for volume activation.

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

Specifies the name of the KMS machine.

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

[**SoftwareLicensingService**](softwarelicensingservice.md)
</dt> </dl>

 

 





