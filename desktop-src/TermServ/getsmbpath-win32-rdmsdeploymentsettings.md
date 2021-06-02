---
title: GetSMBPath method of the Win32_RDMSDeploymentSettings class
description: Retrieves the UNC path to the SMB share to which virtual machines of the virtual desktop collection are deployed.
ms.assetid: 0a5d3c11-6a77-48f7-a3ea-6f82725ff01f
ms.tgt_platform: multiple
keywords:
- GetSMBPath method Remote Desktop Services
- GetSMBPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , GetSMBPath method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetSMBPath
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetSMBPath method of the Win32\_RDMSDeploymentSettings class

Retrieves the UNC path to the SMB share to which virtual machines of the virtual desktop collection are deployed.

## Syntax


```mof
uint32 GetSMBPath(
  [out] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[out\]
</dt> <dd>

Receives a UNC formatted path to the SMB share.

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

 

 





