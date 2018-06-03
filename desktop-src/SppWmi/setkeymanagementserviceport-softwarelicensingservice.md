---
title: SetKeyManagementServicePort method of the SoftwareLicensingService class
description: Sets the TCP port used by a client to make requests of a KMS host.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c804be21-9ed3-4bc8-9bb8-a9cca38a9318
keywords:
- SetKeyManagementServicePort method Windows Management Instrumentation
- SetKeyManagementServicePort method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , SetKeyManagementServicePort method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.SetKeyManagementServicePort
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

# SetKeyManagementServicePort method of the SoftwareLicensingService class

Sets the TCP port used by a client to make requests of a KMS host.

## Syntax


```mof
uint32 SetKeyManagementServicePort(
  [in] uint32 PortNumber
);
```



## Parameters

<dl> <dt>

*PortNumber* \[in\]
</dt> <dd>

Specifies the TCP port to set. If no port is specified, port 1688 is used by default.

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

 

 





