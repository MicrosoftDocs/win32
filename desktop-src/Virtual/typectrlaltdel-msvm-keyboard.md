---
title: TypeCtrlAltDel method of the Msvm\_Keyboard class
description: Simulates a CTRL+ALT+DEL key sequence.
ms.assetid: 82f3b8d1-20fb-4201-9135-896da43ce66c
keywords:
- TypeCtrlAltDel method Hyper-V
- TypeCtrlAltDel method Hyper-V , Msvm_Keyboard class
- Msvm_Keyboard class Hyper-V , TypeCtrlAltDel method
topic_type:
- apiref
api_name:
- Msvm_Keyboard.TypeCtrlAltDel
api_location:
- Root\Virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TypeCtrlAltDel method of the Msvm\_Keyboard class

Simulates a CTRL+ALT+DEL key sequence.

## Syntax


```mof
uint32 TypeCtrlAltDel();
```



## Parameters

This method has no parameters.

## Return value

Type: **uint32**

A return value of zero indicates success. A nonzero value indicates a failure to send.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_Keyboard**](msvm-keyboard.md)
</dt> </dl>

 

 





