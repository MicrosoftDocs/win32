---
title: SetStringProperty method of the Win32_RDMSDeploymentSettings class (Certenroll.h)
description: Updates a string property for the deployment settings of a virtual desktop collection.
ms.assetid: 500ab1cb-7336-47a8-adee-790976ea30fe
ms.tgt_platform: multiple
keywords:
- SetStringProperty method Remote Desktop Services
- SetStringProperty method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , SetStringProperty method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.SetStringProperty
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetStringProperty method of the Win32\_RDMSDeploymentSettings class

Updates a string property for the deployment settings of a virtual desktop collection.

## Syntax


```mof
uint32 SetStringProperty(
  [in] string Key,
  [in] string Value
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The alias to the virtual desktop collection.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The new property value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| Header<br/>                   | <dl> <dt>Certenroll.h</dt> </dl>     |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





