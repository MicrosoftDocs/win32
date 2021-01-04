---
title: SetStringArrayDeploymentSetting method of the Win32_RDMSDeploymentSettings class
description: Updates the deployment settings for a virtual desktop collection.
ms.assetid: 386594bd-a793-4e5d-ad2c-217951bee9f6
ms.tgt_platform: multiple
keywords:
- SetStringArrayDeploymentSetting method Remote Desktop Services
- SetStringArrayDeploymentSetting method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , SetStringArrayDeploymentSetting method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetStringArrayDeploymentSetting
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetStringArrayDeploymentSetting method of the Win32\_RDMSDeploymentSettings class

Updates the deployment settings for a virtual desktop collection.

## Syntax


```mof
uint32 SetStringArrayDeploymentSetting(
  [in] string Key,
  [in] string Value[]
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The alias of the virtual desktop collection.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

An array of strings that contains the new deployment settings.

</dd> </dl>

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

 

 





