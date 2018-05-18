---
title: SetConnectionString method of the Win32\_RDMSDeploymentSettings class
description: Sets the deployment-level database connection string.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c8902ab9-72a6-4d69-ab22-f6074205deb4'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["SetConnectionString method Remote Desktop Services", "SetConnectionString method Remote Desktop Services , Win32_RDMSDeploymentSettings class", "Win32_RDMSDeploymentSettings class Remote Desktop Services , SetConnectionString method"]
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetConnectionString
api_location:
- RDMS.dll
api_type:
- COM
---

# SetConnectionString method of the Win32\_RDMSDeploymentSettings class

Sets the deployment-level database connection string.

## Syntax


```mof
uint32 SetConnectionString(
  [in] string ConnectionString
);
```



## Parameters

<dl> <dt>

*ConnectionString* \[in\]
</dt> <dd>

The connection string to set

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





