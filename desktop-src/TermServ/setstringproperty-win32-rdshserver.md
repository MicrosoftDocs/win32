---
title: SetStringProperty method of the Win32_RDSHServer class (Certenroll.h)
description: Updates a string property value of a Win32\_RDSHServer object.
ms.assetid: 9a338872-27fc-4e37-afd6-20a42c7859e5
ms.tgt_platform: multiple
keywords:
- SetStringProperty method Remote Desktop Services
- SetStringProperty method Remote Desktop Services , Win32_RDSHServer class
- Win32_RDSHServer class Remote Desktop Services , SetStringProperty method
topic_type:
- apiref
api_name:
- Win32_RDSHServer.SetStringProperty
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetStringProperty method of the Win32\_RDSHServer class

Updates a string property value of a [**Win32\_RDSHServer**](win32-rdshserver.md) object.

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

The key that identifies the property to update.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The new property value.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

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

[**Win32\_RDSHServer**](win32-rdshserver.md)
</dt> </dl>

 

 





