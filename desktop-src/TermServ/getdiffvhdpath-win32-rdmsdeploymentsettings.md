---
title: GetDiffVHDPath method of the Win32\_RDMSDeploymentSettings class
description: Retrieves the directory path to which the differencing disks are deployed for a virtual desktop collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4340c817-2276-48a1-a856-b4c9e91ea981'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetDiffVHDPath method Remote Desktop Services", "GetDiffVHDPath method Remote Desktop Services , Win32_RDMSDeploymentSettings class", "Win32_RDMSDeploymentSettings class Remote Desktop Services , GetDiffVHDPath method"]
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetDiffVHDPath
api_location:
- RDMS.dll
api_type:
- COM
---

# GetDiffVHDPath method of the Win32\_RDMSDeploymentSettings class

Retrieves the directory path to which the differencing disks are deployed for a virtual desktop collection.

## Syntax


```mof
uint32 GetDiffVHDPath(
  [out] string DirectoryPath
);
```



## Parameters

<dl> <dt>

*DirectoryPath* \[out\]
</dt> <dd>

Receives the new differencing disk path.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





