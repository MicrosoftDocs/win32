---
title: SetButtonState method of the Msvm\_Ps2Mouse class
description: Sets the current state of the specified device button.
ms.assetid: '91349a09-ee75-4bdc-942e-948f8fdd4d4f'
keywords: ["SetButtonState method Hyper-V", "SetButtonState method Hyper-V , Msvm_Ps2Mouse class", "Msvm_Ps2Mouse class Hyper-V , SetButtonState method"]
topic_type:
- apiref
api_name:
- Msvm_Ps2Mouse.SetButtonState
api_location:
- mmc.h
api_type:
- COM
---

# SetButtonState method of the Msvm\_Ps2Mouse class

Sets the current state of the specified device button.

## Syntax


```mof
uint32 SetButtonState(
  [in] uint32  buttonIndex,
  [in] boolean buttonState
);
```



## Parameters

<dl> <dt>

*buttonIndex* \[in\]
</dt> <dd>

Type: **uint32**

The 1-based index of the button to modify.

</dd> <dt>

*buttonState* \[in\]
</dt> <dd>

Type: **boolean**

The new down state of the button. A **TRUE** value means the button is down.

</dd> </dl>

## Return value

Type: **uint32**

A return value of zero indicates success. A nonzero value indicates a failure to modify the button state.

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

Access to the [**Msvm\_Ps2Mouse**](msvm-ps2mouse.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl>                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_Ps2Mouse**](msvm-ps2mouse.md)
</dt> </dl>

 

 





