---
description: Reset method of the Msvm_Keyboard class - Resets the virtual keyboard.
ms.assetid: 6D4A9F02-53BD-47C2-9C09-F22C3630312F
title: Reset method of the Msvm_Keyboard class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Keyboard.Reset
api_type: 
- COM
api_location: 
- vmms.exe
---

# Reset method of the Msvm\_Keyboard class

Resets the virtual keyboard.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

A return value of zero indicates success. A return value of one indicates a failure because the method is not supported.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not supported** (1)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_Keyboard**](msvm-keyboard.md)
</dt> </dl>

 

 




