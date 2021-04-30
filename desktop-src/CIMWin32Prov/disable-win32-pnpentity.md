---
description: Disables this Plug and Play device.
ms.assetid: 88d60218-7282-4d0e-9a2c-0ad1a8c96650
ms.tgt_platform: multiple
title: Disable method of the Win32_PnPEntity class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PnPEntity.Disable
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Disable method of the Win32\_PnPEntity class

Disables this Plug and Play device.

## Syntax


```mof
Uint32 Disable(
  [out] boolean rebootNeeded
);
```



## Parameters

<dl> <dt>

*rebootNeeded* \[out\]
</dt> <dd>

Whether a reboot is needed.

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

 

 




