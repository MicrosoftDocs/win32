---
title: DisableKeyManagementServiceActivation method of the SoftwareLicensingService class
description: Disables volume activation through KMS machine.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 307f23cf-4532-48c8-9bb9-0ca8193f610d
keywords:
- DisableKeyManagementServiceActivation method Windows Management Instrumentation
- DisableKeyManagementServiceActivation method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , DisableKeyManagementServiceActivation method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.DisableKeyManagementServiceActivation
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

# DisableKeyManagementServiceActivation method of the SoftwareLicensingService class

Disables volume activation through KMS machine.

## Syntax


```mof
uint32 DisableKeyManagementServiceActivation(
  [in] boolean DisableActivation
);
```



## Parameters

<dl> <dt>

*DisableActivation* \[in\]
</dt> <dd>

Determines whether volume activation is disabled. If this parameter is set to 1, volume activation is disabled. If this parameter is set to 0, volume activation is enabled.

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

 

 





