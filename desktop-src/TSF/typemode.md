---
title: TYPEMODE enumeration (Softkbdc.h)
description: Elements of the TYPEMODE enumeration are used to specify type modes that are available for a soft keyboard.
ms.assetid: '7db0a4dd-0ee2-455d-aeb8-11cd1249134c'
keywords:
- TYPEMODE enumeration Text Services Framework
topic_type:
- apiref
api_name:
- TYPEMODE
api_location:
- Softkbdc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TYPEMODE enumeration

Elements of the **TYPEMODE** enumeration are used to specify type modes that are available for a soft keyboard.

## Syntax


```C++
typedef enum tagTYPEMODE { 
  ClickMouse  = 0,
  Hover       = 1,
  Scanning    = 2
} TYPEMODE;
```



## Constants

<dl> <dt>

<span id="ClickMouse"></span><span id="clickmouse"></span><span id="CLICKMOUSE"></span>**ClickMouse**
</dt> <dd>

The user can click the on-screen keys to type text.

</dd> <dt>

<span id="Hover"></span><span id="hover"></span><span id="HOVER"></span>**Hover**
</dt> <dd>

The user can point to a key for a predefined period of time, and the selected character is typed automatically.

</dd> <dt>

<span id="Scanning"></span><span id="scanning"></span><span id="SCANNING"></span>**Scanning**
</dt> <dd>

The soft keyboard continually scans the input area and highlights regions where the user can press a shortcut key or use a switch-input device.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |



 

 





