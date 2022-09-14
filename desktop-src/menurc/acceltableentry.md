---
title: ACCELTABLEENTRY structure
description: Describes the data in an individual accelerator table resource. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 510594ae-56ea-49fb-abd3-ec06e51f2e0e
keywords:
- ACCELTABLEENTRY structure Menus and Other Resources
topic_type:
- apiref
api_name:
- ACCELTABLEENTRY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ACCELTABLEENTRY structure

Describes the data in an individual accelerator table resource. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD fFlags;
  WORD wAnsi;
  WORD wId;
  WORD padding;
} ACCELTABLEENTRY;
```



## Members

<dl> <dt>

**fFlags**
</dt> <dd>

Type: **WORD**

</dd> <dd>

Describes keyboard accelerator characteristics. This member can have one or more of the following values from Winuser.h.



| Value                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FVIRTKEY"></span><span id="fvirtkey"></span><dl> <dt>**FVIRTKEY**</dt> <dt>TRUE</dt> </dl>    | The accelerator key is a [virtual-key code](/windows/desktop/inputdev/virtual-key-codes). If this flag is not specified, the accelerator key is assumed to specify an ASCII character code. <br/>                          |
| <span id="FNOINVERT"></span><span id="fnoinvert"></span><dl> <dt>**FNOINVERT**</dt> <dt>0x02</dt> </dl> | A menu item on the menu bar is not highlighted when an accelerator is used. This attribute is obsolete and retained only for backward compatibility with resource files designed for 16-bit Windows.<br/> |
| <span id="FSHIFT"></span><span id="fshift"></span><dl> <dt>**FSHIFT**</dt> <dt>0x04</dt> </dl>          | The accelerator is activated only if the user presses the SHIFT key. This flag applies only to virtual keys. <br/>                                                                                        |
| <span id="FCONTROL"></span><span id="fcontrol"></span><dl> <dt>**FCONTROL**</dt> <dt>0x08</dt> </dl>    | The accelerator is activated only if the user presses the CTRL key. This flag applies only to virtual keys. <br/>                                                                                         |
| <span id="FALT"></span><span id="falt"></span><dl> <dt>**FALT**</dt> <dt>0x10</dt> </dl>                | The accelerator is activated only if the user presses the ALT key. This flag applies only to virtual keys. <br/>                                                                                          |
| <span id="0x80"></span><span id="0X80"></span><dl> <dt>**0x80**</dt> </dl>                                                                          | The entry is last in an accelerator table. <br/>                                                                                                                                                          |



 

</dd> <dt>

**wAnsi**
</dt> <dd>

Type: **WORD**

</dd> <dd>

An ANSI character value or a virtual-key code that identifies the accelerator key.

</dd> <dt>

**wId**
</dt> <dd>

Type: **WORD**

</dd> <dd>

An identifier for the keyboard accelerator. This is the value passed to the window procedure when the user presses the specified key.

</dd> <dt>

**padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of bytes inserted to ensure that the structure is aligned on a **DWORD** boundary.

</dd> </dl>

## Remarks

The **ACCELTABLEENTRY** structure is repeated for all accelerator table entries in the resource. The last entry in the table is flagged with the value 0x0080.

You can compute the number of elements in the table if you divide the length of the resource by eight. Then your application can randomly access the individual fixed-length entries.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CreateAcceleratorTable**](/windows/desktop/api/Winuser/nf-winuser-createacceleratortablea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

