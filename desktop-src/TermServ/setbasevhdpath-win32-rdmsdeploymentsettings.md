---
title: SetBaseVHDPath method of the Win32_RDMSDeploymentSettings class
description: Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed. | SetBaseVHDPath method of the Win32_RDMSDeploymentSettings class
ms.assetid: 1ea4cd93-ef17-4ec9-82f9-382c549f189c
ms.tgt_platform: multiple
keywords:
- SetBaseVHDPath method Remote Desktop Services
- SetBaseVHDPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , SetBaseVHDPath method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetBaseVHDPath
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetBaseVHDPath method of the Win32\_RDMSDeploymentSettings class

Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed.

## Syntax


```mof
uint32 SetBaseVHDPath(
  [in] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[in\]
</dt> <dd>

The new VHD deployment path.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





