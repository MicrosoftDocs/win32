---
title: GetInt32Property method of the Win32_RDSHCollection class (Microsoft.diagnostics.appanalysis.h)
description: Retrieves an integer property value of a Win32\_RDSHCollection object.
ms.assetid: ab68f357-057d-4a36-ae39-f47198768a49
ms.tgt_platform: multiple
keywords:
- GetInt32Property method Remote Desktop Services
- GetInt32Property method Remote Desktop Services , Win32_RDSHCollection class
- Win32_RDSHCollection class Remote Desktop Services , GetInt32Property method
topic_type:
- apiref
api_name:
- Win32_RDSHCollection.GetInt32Property
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetInt32Property method of the Win32\_RDSHCollection class

Retrieves an integer property value of a [**Win32\_RDSHCollection**](win32-rdshcollection.md) object.

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
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                 |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                                   |
| Header<br/>                   | <dl> <dt>Microsoft.diagnostics.appanalysis.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>                            |



## See also

<dl> <dt>

[**Win32\_RDSHCollection**](win32-rdshcollection.md)
</dt> </dl>

 

 





