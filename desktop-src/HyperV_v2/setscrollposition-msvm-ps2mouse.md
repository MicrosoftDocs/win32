---
description: Adjusts the z-coordinate of the wheel control of the pointing device.
ms.assetid: FF1929EE-4A2D-4761-8919-488369FAEE1F
title: SetScrollPosition method of the Msvm_Ps2Mouse class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Ps2Mouse.SetScrollPosition
api_type: 
- COM
api_location: 
- vmms.exe
---

# SetScrollPosition method of the Msvm\_Ps2Mouse class

Adjusts the z-coordinate of the wheel control of the pointing device. Values written to this property are always relative coordinate offsets.

## Syntax


```mof
uint32 SetScrollPosition(
  [in] sint8 scrollPositionDelta
);
```



## Parameters

<dl> <dt>

*scrollPositionDelta* \[in\]
</dt> <dd>

Type: **sint8**

The delta of the scroll position.

</dd> </dl>

## Return value

Type: **uint32**

A return value of zero indicates success. A nonzero value indicates a failure to alter the scroll position.

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

Access to the [**Msvm\_Ps2Mouse**](msvm-ps2mouse.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_Ps2Mouse**](msvm-ps2mouse.md)
</dt> </dl>

 

