---
title: TITLEBAR_TYPE enumeration (Softkbdc.h)
description: Elements of the TITLEBAR\_TYPE enumeration are used to specify types of titlebars that are available for a soft keyboard window.
ms.assetid: 10d9b1c0-fd52-4f62-9268-cb8903a4c2db
keywords:
- TITLEBAR_TYPE enumeration Text Services Framework
topic_type:
- apiref
api_name:
- TITLEBAR_TYPE
api_location:
- Softkbdc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TITLEBAR\_TYPE enumeration

Elements of the **TITLEBAR\_TYPE** enumeration are used to specify types of titlebars that are available for a soft keyboard window.

## Syntax


```C++
typedef enum tagTITLEBAR_TYPE { 
  TITLEBAR_NONE                = 0,
  TITLEBAR_GRIPPER_HORIZ_ONLY  = 1,
  TITLEBAR_GRIPPER_VERTI_ONLY  = 2,
  TITLEBAR_GRIPPER_BUTTON      = 3
} TITLEBAR_TYPE;
```



## Constants

<dl> <dt>

<span id="TITLEBAR_NONE"></span><span id="titlebar_none"></span>**TITLEBAR\_NONE**
</dt> <dd>

The soft keyboard window uses no titlebar.

</dd> <dt>

<span id="TITLEBAR_GRIPPER_HORIZ_ONLY"></span><span id="titlebar_gripper_horiz_only"></span>**TITLEBAR\_GRIPPER\_HORIZ\_ONLY**
</dt> <dd>

The soft keyboard window uses a horizontal gripper bar only.

</dd> <dt>

<span id="TITLEBAR_GRIPPER_VERTI_ONLY"></span><span id="titlebar_gripper_verti_only"></span>**TITLEBAR\_GRIPPER\_VERTI\_ONLY**
</dt> <dd>

The soft keyboard window uses a vertical gripper bar only.

</dd> <dt>

<span id="TITLEBAR_GRIPPER_BUTTON"></span><span id="titlebar_gripper_button"></span>**TITLEBAR\_GRIPPER\_BUTTON**
</dt> <dd>

The soft keyboard window uses a gripper button only.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |



 

 





