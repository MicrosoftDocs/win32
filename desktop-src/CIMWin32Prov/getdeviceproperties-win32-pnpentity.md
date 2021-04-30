---
description: Gets the specified properties of this Plug and Play device.
ms.assetid: 63327a4f-7d4a-4041-b58d-7a852ba08d5b
ms.tgt_platform: multiple
title: GetDeviceProperties method of the Win32_PnPEntity class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PnPEntity.GetDeviceProperties
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetDeviceProperties method of the Win32\_PnPEntity class

Gets the specified properties of this Plug and Play device.

## Syntax


```mof
Uint32 GetDeviceProperties(
  [in, optional] string                  devicePropertyKeys[],
  [out]          Win32_PnPDeviceProperty deviceProperties[]
);
```



## Parameters

<dl> <dt>

*devicePropertyKeys* \[in, optional\]
</dt> <dd>

The properties to return.

</dd> <dt>

*deviceProperties* \[out\]
</dt> <dd>

The requested properties in appropriate subtypes of the [**Win32\_PnPDeviceProperty**](win32-pnpdeviceproperty.md) abstract class.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_PnPEntity**](win32-pnpentity.md)
</dt> </dl>

 

 




