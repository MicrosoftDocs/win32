---
title: SetScrollPosition method of the Msvm\_SyntheticMouse class
description: Adjusts the z-coordinate of the wheel control of the pointing device.
ms.assetid: ee28bb4b-627f-40bc-848f-2b049cb0a8b9
keywords:
- SetScrollPosition method Hyper-V
- SetScrollPosition method Hyper-V , Msvm_SyntheticMouse class
- Msvm_SyntheticMouse class Hyper-V , SetScrollPosition method
topic_type:
- apiref
api_name:
- Msvm_SyntheticMouse.SetScrollPosition
api_location:
- Root\Virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetScrollPosition method of the Msvm\_SyntheticMouse class

Adjusts the z-coordinate of the wheel control of the pointing device. Values written to this property are always relative coordinate offsets.

## Syntax


```mof
uint32 SetScrollPosition(
  [in] sint32 scrollPositionDelta
);
```



## Parameters

<dl> <dt>

*scrollPositionDelta* \[in\]
</dt> <dd>

Type: **sint32**

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

Access to the [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md)
</dt> </dl>

 

 





