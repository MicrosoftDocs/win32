---
title: GetBaseVHDPath method of the Win32_RDMSDeploymentSettings class
description: Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed. | GetBaseVHDPath method of the Win32_RDMSDeploymentSettings class
ms.assetid: d3629a08-ef16-4aab-b74b-f837a8ba00d0
ms.tgt_platform: multiple
keywords:
- GetBaseVHDPath method Remote Desktop Services
- GetBaseVHDPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , GetBaseVHDPath method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetBaseVHDPath
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetBaseVHDPath method of the Win32\_RDMSDeploymentSettings class

Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed.

## Syntax


```mof
uint32 GetBaseVHDPath(
  [out] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[out\]
</dt> <dd>

Receives the VHD deployment path.

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

 

 





