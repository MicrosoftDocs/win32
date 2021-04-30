---
title: NORMALMENUITEM structure
description: Contains information about each item in a menu resource that does not open a menu or a submenu. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: c1b84264-2d7f-4bc3-8e74-7b921a0bfe30
keywords:
- NORMALMENUITEM structure Menus and Other Resources
topic_type:
- apiref
api_name:
- NORMALMENUITEM
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# NORMALMENUITEM structure

Contains information about each item in a menu resource that does not open a menu or a submenu. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD    resInfo;
  szOrOrd menuText;
} NORMALMENUITEM;
```



## Members

<dl> <dt>

**resInfo**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The type of menu item. This member can be one of the following values.



| Value                                                                                                                                                                                                       | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="MFR_END"></span><span id="mfr_end"></span><dl> <dt>**MFR\_END**</dt> <dt>0x80</dt> </dl>       | The menu item is the last in this submenu or menu resource; this flag is used internally by the system.<br/> |
| <span id="MFR_POPUP"></span><span id="mfr_popup"></span><dl> <dt>**MFR\_POPUP**</dt> <dt>0x01</dt> </dl> | The menu item opens a menu or a submenu; the flag is used internally by the system. <br/>                    |



 

</dd> <dt>

**menuText**
</dt> <dd>

Type: **szOrOrd**

</dd> <dd>

A null-terminated Unicode string that contains the text for this menu item. There is no fixed limit on the size of this string.

</dd> </dl>

## Remarks

There is one **NORMALMENUITEM** structure for each menu item that does not open a menu or a submenu. Indicate the last menu item on a menu by setting the **resInfo** member to **MFR\_END**.

A menu separator is a special type of menu item that is inactive but appears as a dividing bar between two active menu items. Indicate a menu separator by leaving the **menuText** member empty.

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

[**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa)
</dt> <dt>

[**POPUPMENUITEM**](popupmenuitem.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

 





