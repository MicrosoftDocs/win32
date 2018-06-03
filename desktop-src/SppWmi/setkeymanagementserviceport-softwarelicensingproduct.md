---
title: SetKeyManagementServicePort method of the SoftwareLicensingProduct class
description: Sets the TCP port used by a client to make requests of a KMS host.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9d123d7d-c471-4d4e-9d67-942c0ec1b662
keywords:
- SetKeyManagementServicePort method Windows Management Instrumentation
- SetKeyManagementServicePort method Windows Management Instrumentation , SoftwareLicensingProduct class
- SoftwareLicensingProduct class Windows Management Instrumentation , SetKeyManagementServicePort method
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.SetKeyManagementServicePort
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

# SetKeyManagementServicePort method of the SoftwareLicensingProduct class

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

Specifies the port number to use for the requests. If no port is specified, port 1688 is used by default.

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

 

 





