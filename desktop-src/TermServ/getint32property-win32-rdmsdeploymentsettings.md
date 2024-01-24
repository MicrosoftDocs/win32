---
title: GetInt32Property method of the Win32_RDMSDeploymentSettings class (Microsoft.diagnostics.appanalysis.h)
description: Retrieves an integer property for the deployment settings of a virtual desktop collection.
ms.assetid: 6b8174bb-ffb7-4699-a3fb-d32ab0b202fc
ms.tgt_platform: multiple
keywords:
- GetInt32Property method Remote Desktop Services
- GetInt32Property method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , GetInt32Property method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetInt32Property
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetInt32Property method of the Win32\_RDMSDeploymentSettings class

Retrieves an integer property for the deployment settings of a virtual desktop collection.

## Syntax


```mof
uint32 GetInt32Property(
  [in]  string Key,
  [out] sint32 Value
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The alias to the virtual desktop collection.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

An integer that receives the retrieved value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                 |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                                   |
| Header<br/>                   | <dl> <dt>Microsoft.diagnostics.appanalysis.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>                            |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





