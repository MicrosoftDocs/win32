---
title: SetAbsolutePosition method of the Msvm\_SyntheticMouse class
description: Offsets the position of the mouse by the specified horizontal and vertical deltas.
ms.assetid: 96ca50de-3cf9-43de-b21e-29e7a36a9c77
keywords:
- SetAbsolutePosition method Hyper-V
- SetAbsolutePosition method Hyper-V , Msvm_SyntheticMouse class
- Msvm_SyntheticMouse class Hyper-V , SetAbsolutePosition method
topic_type:
- apiref
api_name:
- Msvm_SyntheticMouse.SetAbsolutePosition
api_location:
- dbdao.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetAbsolutePosition method of the Msvm\_SyntheticMouse class

Offsets the position of the mouse by the specified horizontal and vertical deltas.

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

Access to the [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Dbdao.h</dt> </dl>                   |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md)
</dt> </dl>

 

 





