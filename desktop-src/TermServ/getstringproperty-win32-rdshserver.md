---
title: GetStringProperty method of the Win32_RDSHServer class
description: Retrieves a string property value of a Win32\_RDSHServer object.
ms.assetid: 136cd213-86a6-472a-8853-8d05f992309a
ms.tgt_platform: multiple
keywords:
- GetStringProperty method Remote Desktop Services
- GetStringProperty method Remote Desktop Services , Win32_RDSHServer class
- Win32_RDSHServer class Remote Desktop Services , GetStringProperty method
topic_type:
- apiref
api_name:
- Win32_RDSHServer.GetStringProperty
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetStringProperty method of the Win32\_RDSHServer class

Retrieves a string property value of a [**Win32\_RDSHServer**](win32-rdshserver.md) object.

## Syntax


```mof
uint32 GetStringProperty(
  [in]  string Key,
  [out] string Value
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The key that identifies the property to retrieve.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

Receives the retrieved property value.

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

[**Win32\_RDSHServer**](win32-rdshserver.md)
</dt> </dl>

 

 





