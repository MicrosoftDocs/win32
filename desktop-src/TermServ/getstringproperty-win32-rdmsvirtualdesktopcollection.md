---
title: GetStringProperty method of the Win32_RDMSVirtualDesktopCollection class
description: Retrieves a string property from a virtual desktop collection.
ms.assetid: 4a122fc5-1635-4d74-a90d-2347c0714fc7
ms.tgt_platform: multiple
keywords:
- GetStringProperty method Remote Desktop Services
- GetStringProperty method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , GetStringProperty method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.GetStringProperty
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetStringProperty method of the Win32\_RDMSVirtualDesktopCollection class

Retrieves a string property from a virtual desktop collection.

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

A key that identifies the property to retrieve.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

A string that receives the retrieved value.

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

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 





