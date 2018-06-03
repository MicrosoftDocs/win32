---
title: SetRelativePosition method of the Msvm\_Ps2Mouse class
description: Offsets the position of the mouse by the specified horizontal and vertical deltas.
ms.assetid: 3e4c7a27-9f7d-4032-abaf-102577bbae8f
keywords:
- SetRelativePosition method Hyper-V
- SetRelativePosition method Hyper-V , Msvm_Ps2Mouse class
- Msvm_Ps2Mouse class Hyper-V , SetRelativePosition method
topic_type:
- apiref
api_name:
- Msvm_Ps2Mouse.SetRelativePosition
api_location:
- mpconfig.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetRelativePosition method of the Msvm\_Ps2Mouse class

Offsets the position of the mouse by the specified horizontal and vertical deltas.

## Syntax


```mof
uint32 SetRelativePosition(
  [in] sint8 horizontalDelta,
  [in] sint8 verticalDelta
);
```



## Parameters

<dl> <dt>

*horizontalDelta* \[in\]
</dt> <dd>

Type: **sint8**

The horizontal change for the mouse position, in pixels.

</dd> <dt>

*verticalDelta* \[in\]
</dt> <dd>

Type: **sint8**

The vertical change for the mouse position, in pixels.

</dd> </dl>

## Return value

Type: **uint32**

A return value of zero indicates success. A nonzero value indicates a failure to alter the mouse position.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Mpconfig.h</dt> </dl>                |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_Ps2Mouse**](msvm-ps2mouse.md)
</dt> </dl>

 

 





