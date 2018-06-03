---
title: DisableKeyManagementServiceDnsPublishing method of the SoftwareLicensingService class
description: Disables the DNS publishing on a KMS host computer.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 621a7bd0-4d7b-4c2c-8d4a-65142632db48
keywords:
- DisableKeyManagementServiceDnsPublishing method Windows Management Instrumentation
- DisableKeyManagementServiceDnsPublishing method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , DisableKeyManagementServiceDnsPublishing method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.DisableKeyManagementServiceDnsPublishing
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

# DisableKeyManagementServiceDnsPublishing method of the SoftwareLicensingService class

Disables the DNS publishing on a KMS host computer.

## Syntax


```mof
uint32 DisableKeyManagementServiceDnsPublishing(
  [in] boolean DisablePublishing
);
```



## Parameters

<dl> <dt>

*DisablePublishing* \[in\]
</dt> <dd>

Determines whether DNS publishing on a KMS host computer is enabled. If this parameter is set to 1, DNS publishing is disabled. If this parameter is set to 0, DNS publishing is enabled.

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

 

 





