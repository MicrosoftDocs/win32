---
description: Contains information about a button that a File Manager extension DLL is adding to the toolbar of File Manager.
title: EXT_BUTTON structure (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXT_BUTTON
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 8cd29a06-0f38-4285-9092-647a391b72d7

---

# EXT\_BUTTON structure

Contains information about a button that a File Manager extension DLL is adding to the toolbar of File Manager.

## Syntax


```C++
typedef struct tagEXT_BUTTON {
  WORD idCommand;
  WORD idsHelp;
  WORD fsStyle;
} EXT_BUTTON, *LPEXT_BUTTON;
```



## Members

<dl> <dt>

**idCommand**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A command identifier for the button.

</dd> <dt>

**idsHelp**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The identifier of the Help string for the button.

</dd> <dt>

**fsStyle**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The style of the button.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMEVENT\_TOOLBARLOAD**](fmevent-toolbarload.md)
</dt> <dt>

[**FMS\_TOOLBARLOAD**](fms-toolbarload.md)
</dt> </dl>

 

 




