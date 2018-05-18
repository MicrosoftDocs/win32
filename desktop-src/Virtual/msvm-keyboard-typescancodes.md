---
title: TypeScancodes method of the Msvm\_Keyboard class
description: Simulates a key sequence using scan codes.
ms.assetid: '393fb049-63fa-43e1-914d-1786451d878f'
keywords: ["TypeScancodes method Hyper-V", "TypeScancodes method Hyper-V , Msvm_Keyboard class", "Msvm_Keyboard class Hyper-V , TypeScancodes method"]
topic_type:
- apiref
api_name:
- Msvm_Keyboard.TypeScancodes
api_location:
- Root\Virtualization
api_type:
- COM
---

# TypeScancodes method of the Msvm\_Keyboard class

Simulates a key sequence using scan codes.

## Syntax


```mof
uint32 TypeScancodes(
  [in] uint8 Scancodes[]
);
```



## Parameters

<dl> <dt>

*Scancodes* \[in\]
</dt> <dd>

Type: **uint8\[\]**

An array that contains the scan codes to type.

</dd> </dl>

## Return value

Type: **uint32**

This method returns 0 if it succeeds. Any other return value indicates an error. The return value can be one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Remarks

Access to the [**Msvm\_Keyboard**](msvm-keyboard.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_Keyboard**](msvm-keyboard.md)
</dt> </dl>

 

 





