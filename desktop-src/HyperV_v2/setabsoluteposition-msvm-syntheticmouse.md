---
description: Sets the horizontal and vertical position of the mouse cursor.
ms.assetid: 7845E10A-7F61-4134-BF81-AED5483F36AD
title: SetAbsolutePosition method of the Msvm_SyntheticMouse class (Dbdao.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SyntheticMouse.SetAbsolutePosition
api_type: 
- COM
api_location: 
- vmms.exe
---

# SetAbsolutePosition method of the Msvm\_SyntheticMouse class

Sets the horizontal and vertical position of the mouse cursor.

## Syntax


```mof
uint32 SetAbsolutePosition(
  [in] sint32 horizontalPosition,
  [in] sint32 verticalPosition
);
```



## Parameters

<dl> <dt>

*horizontalPosition* \[in\]
</dt> <dd>

Type: **sint32**

The new horizontal position of the mouse cursor, in pixels.

</dd> <dt>

*verticalPosition* \[in\]
</dt> <dd>

Type: **sint32**

The new vertical position of the mouse cursor, in pixels.

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

Access to the [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Dbdao.h</dt> </dl>                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md)
</dt> </dl>

 

