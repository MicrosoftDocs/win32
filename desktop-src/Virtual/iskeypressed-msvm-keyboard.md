---
title: IsKeyPressed method of the Msvm\_Keyboard class
description: Retrieves the key state of a key.
ms.assetid: eb1cac54-536b-4de1-9307-255634758b90
keywords:
- IsKeyPressed method Hyper-V
- IsKeyPressed method Hyper-V , Msvm_Keyboard class
- Msvm_Keyboard class Hyper-V , IsKeyPressed method
topic_type:
- apiref
api_name:
- Msvm_Keyboard.IsKeyPressed
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

# IsKeyPressed method of the Msvm\_Keyboard class

Retrieves the key state of a key.

## Syntax


```mof
uint32 IsKeyPressed(
  [in]  uint32  keyCode,
  [out] boolean keyState
);
```



## Parameters

<dl> <dt>

*keyCode* \[in\]
</dt> <dd>

Type: **uint32**

The virtual key code of the key to query. For the list for virtual-key codes, see [**Virtual-Key Codes**](_win32_virtual_key_codes).

</dd> <dt>

*keyState* \[out\]
</dt> <dd>

Type: **boolean**

The current down state of the key. A **TRUE** value means the key is down.

</dd> </dl>

## Return value

Type: **uint32**

A return value of zero indicates success. A nonzero value indicates a failure to query the key state.

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

The **IsKeyPressed** method will always return **FALSE** for the **VK\_MENU** (18), **VK\_CONTROL** (17), and **VK\_SHIFT** (16) because these are not real keys on a keyboard. These virtual key codes are always mapped to **VK\_LMENU** (164), **VK\_LCONTROL** (162), and **VK\_LSHIFT** (160), respectively, by the [**PressKey**](presskey-msvm-keyboard.md) and [**ReleaseKey**](releasekey-msvm-keyboard.md) methods.

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
</dt> <dt>

[**Virtual-Key Codes**](_win32_virtual_key_codes)
</dt> </dl>

 

 





