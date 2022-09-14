---
title: MENUHELPID structure
description: Contains the final data written to the RT\_MENU resource for a menu or submenu if the resInfo member of the POPUPMENUITEM structure is set to MFR\_POPUP.
ms.assetid: f17fdaaa-b37c-4902-bad4-a1181ffee9f9
keywords:
- MENUHELPID structure Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUHELPID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MENUHELPID structure

Contains the final data written to the [**RT\_MENU**](/windows/desktop/menurc/resource-types) resource for a menu or submenu if the **resInfo** member of the [**POPUPMENUITEM**](popupmenuitem.md) structure is set to **MFR\_POPUP**. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  DWORD helpID;
} MENUHELPID;
```



## Members

<dl> <dt>

**helpID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The identifier used to identify the menu during [**WM\_HELP**](/windows/desktop/shell/wm-help) processing.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**MENUHEADER**](menuheader.md)
</dt> <dt>

[**POPUPMENUITEM**](popupmenuitem.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

