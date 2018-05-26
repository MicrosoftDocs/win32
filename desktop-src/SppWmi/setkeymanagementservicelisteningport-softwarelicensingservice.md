---
title: SetKeyManagementServiceListeningPort method of the SoftwareLicensingService class
description: Sets the TCP port used by a KMS host to listen for activation requests. This method applies to KMS hosts only.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62a47bf8-7112-4ccd-b2d2-17bd663dec03
keywords:
- SetKeyManagementServiceListeningPort method Windows Management Instrumentation
- SetKeyManagementServiceListeningPort method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , SetKeyManagementServiceListeningPort method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.SetKeyManagementServiceListeningPort
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

# SetKeyManagementServiceListeningPort method of the SoftwareLicensingService class

Sets the TCP port used by a KMS host to listen for activation requests. This method applies to KMS hosts only.

## Syntax


```mof
uint32 SetKeyManagementServiceListeningPort(
  [in] uint32 PortNumber
);
```



## Parameters

<dl> <dt>

*PortNumber* \[in\]
</dt> <dd>

Specifies the TCP port number to set. If no port is specified, 1688 is used by default.

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

 

 





