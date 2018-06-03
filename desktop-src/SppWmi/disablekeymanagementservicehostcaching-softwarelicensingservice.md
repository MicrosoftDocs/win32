---
title: DisableKeyManagementServiceHostCaching method of the SoftwareLicensingService class
description: Disables the caching of the KMS hostname and port value on a volume activation client.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3db3185e-da8d-4135-91a2-8eec1cf0494f
keywords:
- DisableKeyManagementServiceHostCaching method Windows Management Instrumentation
- DisableKeyManagementServiceHostCaching method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , DisableKeyManagementServiceHostCaching method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.DisableKeyManagementServiceHostCaching
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

# DisableKeyManagementServiceHostCaching method of the SoftwareLicensingService class

Disables the caching of the KMS hostname and port value on a volume activation client.

## Syntax


```mof
uint32 DisableKeyManagementServiceHostCaching(
  [in] boolean DisableCaching
);
```



## Parameters

<dl> <dt>

*DisableCaching* \[in\]
</dt> <dd>

Determines whether KMS hostname and port values are cached. If this parameter is set to 1, caching is disabled. If this parameter is set to 0, caching is enabled.

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

 

 





