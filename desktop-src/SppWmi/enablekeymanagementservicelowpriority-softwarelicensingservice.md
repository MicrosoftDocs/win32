---
title: EnableKeyManagementServiceLowPriority method of the SoftwareLicensingService class
description: Enables the KMS service to run with low priority.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3c644dc8-b612-49f2-a1e6-855b5498fc14'
keywords: ["EnableKeyManagementServiceLowPriority method Windows Management Instrumentation", "EnableKeyManagementServiceLowPriority method Windows Management Instrumentation , SoftwareLicensingService class", "SoftwareLicensingService class Windows Management Instrumentation , EnableKeyManagementServiceLowPriority method"]
topic_type:
- apiref
api_name:
- SoftwareLicensingService.EnableKeyManagementServiceLowPriority
api_location:
- SppWmi.dll
api_type:
- COM
---

# EnableKeyManagementServiceLowPriority method of the SoftwareLicensingService class

Enables the KMS service to run with low priority.

## Syntax


```mof
uint32 EnableKeyManagementServiceLowPriority(
  [in] boolean EnableLowPriority
);
```



## Parameters

<dl> <dt>

*EnableLowPriority* \[in\]
</dt> <dd>

Determines whether the KMS service is running with low priority. If this parameter is set to 1, the KMS service is running with low priority.

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

[**SoftwareLicensingService**](softwarelicensingservice.md)
</dt> </dl>

 

 





