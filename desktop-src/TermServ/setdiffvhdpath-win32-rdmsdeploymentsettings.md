---
title: SetDiffVHDPath method of the Win32_RDMSDeploymentSettings class
description: Updates the directory path to which the differencing disks are deployed for a virtual desktop collection.
ms.assetid: 665ffbf9-0250-4956-9bce-f5a6714b47e4
ms.tgt_platform: multiple
keywords:
- SetDiffVHDPath method Remote Desktop Services
- SetDiffVHDPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , SetDiffVHDPath method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetDiffVHDPath
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetDiffVHDPath method of the Win32\_RDMSDeploymentSettings class

Updates the directory path to which the differencing disks are deployed for a virtual desktop collection.

## Syntax


```mof
uint32 SetDiffVHDPath(
  [in] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[in\]
</dt> <dd>

The new differencing disk path.

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

 

 





