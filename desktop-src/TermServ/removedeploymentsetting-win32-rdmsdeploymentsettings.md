---
title: RemoveDeploymentSetting method of the Win32_RDMSDeploymentSettings class
description: Deletes the deployment settings for a virtual desktop collection.
ms.assetid: 68e102a3-8f3f-4997-bdf0-c2ae3640ed42
ms.tgt_platform: multiple
keywords:
- RemoveDeploymentSetting method Remote Desktop Services
- RemoveDeploymentSetting method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , RemoveDeploymentSetting method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.RemoveDeploymentSetting
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveDeploymentSetting method of the Win32\_RDMSDeploymentSettings class

Deletes the deployment settings for a virtual desktop collection.

## Syntax


```mof
uint32 RemoveDeploymentSetting(
  [in] string Key
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The alias of the virtual desktop collection.

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

 

 





