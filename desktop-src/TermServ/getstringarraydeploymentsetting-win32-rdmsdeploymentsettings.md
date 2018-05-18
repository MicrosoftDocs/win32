---
title: GetStringArrayDeploymentSetting method of the Win32\_RDMSDeploymentSettings class
description: Retrieves the deployment settings for a virtual desktop collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ab380618-560e-425b-9bf0-a7de6b30d01a'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetStringArrayDeploymentSetting method Remote Desktop Services", "GetStringArrayDeploymentSetting method Remote Desktop Services , Win32_RDMSDeploymentSettings class", "Win32_RDMSDeploymentSettings class Remote Desktop Services , GetStringArrayDeploymentSetting method"]
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetStringArrayDeploymentSetting
api_location:
- RDMS.dll
api_type:
- COM
---

# GetStringArrayDeploymentSetting method of the Win32\_RDMSDeploymentSettings class

Retrieves the deployment settings for a virtual desktop collection.

## Syntax


```mof
uint32 GetStringArrayDeploymentSetting(
  [in]  string Key,
  [out] string Value[]
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The alias of the virtual desktop collection.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

Receives an array of strings that contains the deployment settings.

</dd> </dl>

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

 

 





