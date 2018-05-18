---
title: SetInt32Property method of the Win32\_RDSHServer class
description: Updates an integer property value of a Win32\_RDSHServer object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fa8df023-120d-4174-adc1-868f08fdce56'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["SetInt32Property method Remote Desktop Services", "SetInt32Property method Remote Desktop Services , Win32_RDSHServer class", "Win32_RDSHServer class Remote Desktop Services , SetInt32Property method"]
topic_type:
- apiref
api_name:
- Win32_RDSHServer.SetInt32Property
api_location:
- RDMS.dll
api_type:
- COM
---

# SetInt32Property method of the Win32\_RDSHServer class

Updates an integer property value of a [**Win32\_RDSHServer**](win32-rdshserver.md) object.

## Syntax


```mof
uint32 SetInt32Property(
  [in] string Key,
  [in] sint32 Value
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



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDSHServer**](win32-rdshserver.md)
</dt> </dl>

 

 





