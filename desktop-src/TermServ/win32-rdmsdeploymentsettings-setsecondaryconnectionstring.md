---
title: SetSecondaryConnectionString method of the Win32_RDMSDeploymentSettings class
description: Sets the deployment level database secondary connection string.
ms.assetid: 154c495e-564e-4d90-a4ff-de683d41aa73
ms.tgt_platform: multiple
keywords:
- SetSecondaryConnectionString method Remote Desktop Services
- SetSecondaryConnectionString method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , SetSecondaryConnectionString method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetSecondaryConnectionString
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSecondaryConnectionString method of the Win32\_RDMSDeploymentSettings class

Sets the deployment level database secondary connection string.

## Syntax


```mof
uint32 SetSecondaryConnectionString(
  [in] string SecondaryConnectionString
);
```



## Parameters

<dl> <dt>

*SecondaryConnectionString* \[in\]
</dt> <dd>

The connection string to set

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





