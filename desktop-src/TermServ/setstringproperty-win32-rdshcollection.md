---
title: SetStringProperty method of the Win32_RDSHCollection class (Certenroll.h)
description: Updates a string property value of a Win32\_RDSHCollection object.
ms.assetid: 6981b47a-5480-44f5-90e3-f64d439fa2aa
ms.tgt_platform: multiple
keywords:
- SetStringProperty method Remote Desktop Services
- SetStringProperty method Remote Desktop Services , Win32_RDSHCollection class
- Win32_RDSHCollection class Remote Desktop Services , SetStringProperty method
topic_type:
- apiref
api_name:
- Win32_RDSHCollection.SetStringProperty
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetStringProperty method of the Win32\_RDSHCollection class

Updates a string property value of a [**Win32\_RDSHCollection**](win32-rdshcollection.md) object.

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

[**Win32\_RDSHCollection**](win32-rdshcollection.md)
</dt> </dl>

 

 





