---
title: GetExportPath method of the Win32_RDMSDeploymentSettings class
description: Retrieves the directory path to which virtual machines are deployed for a virtual desktop collection.
ms.assetid: 8df79e31-b960-46ae-b49c-8052b356e1a8
ms.tgt_platform: multiple
keywords:
- GetExportPath method Remote Desktop Services
- GetExportPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , GetExportPath method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetExportPath
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetExportPath method of the Win32\_RDMSDeploymentSettings class

Retrieves the directory path to which virtual machines are deployed for a virtual desktop collection.

## Syntax


```mof
uint32 GetExportPath(
  [out] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[out\]
</dt> <dd>

Receives the directory path.

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

 

 





