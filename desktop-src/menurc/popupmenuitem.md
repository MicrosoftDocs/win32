---
title: POPUPMENUITEM structure
description: Contains information about the menu items in a menu resource that open a menu or a submenu. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: cb8faeb2-bca9-4ff5-8f80-d273c3fca504
keywords:
- POPUPMENUITEM structure Menus and Other Resources
topic_type:
- apiref
api_name:
- POPUPMENUITEM
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# POPUPMENUITEM structure

Contains information about the menu items in a menu resource that open a menu or a submenu. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  DWORD   type;
  DWORD   state;
  DWORD   id;
  WORD    resInfo;
  szOrOrd menuText;
} POPUPMENUITEM;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Describes the menu item. Some of the values this member can have include those shown in the list below.

In addition to the values shown, this member can also be a combination of the type values listed with the **fType** member of the [**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa) structure. The type values are those that begin with MFT\_. To use these predefined MFT\_\* type values, include the following statement in your .rc file:

`#include "winuser.h"`



| Value                                                                                                                                                                                                    | Meaning                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="MF_END"></span><span id="mf_end"></span><dl> <dt>**MF\_END**</dt> <dt>0x80</dt> </dl>       | The menu item is the last on the menu; the flag is used internally by the system. <br/>   |
| <span id="MF_POPUP"></span><span id="mf_popup"></span><dl> <dt>**MF\_POPUP**</dt> <dt>0x01</dt> </dl> | The menu item opens a menu or a submenu; the flag is used internally by the system. <br/> |



 

</dd> <dt>

**state**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Describes the menu item. This member can be a combination of the state values listed with the **dwState** member of the [**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa) structure. The state values are those that begin with MFS\_. To use these predefined MFS\_\* state values, include the following statement in your .rc file:

`#include "winuser.h"`

</dd> <dt>

**id**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A numeric expression that identifies the menu item that is passed in the [**WM\_COMMAND**](wm-command.md) message.

</dd> <dt>

**resInfo**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A set of bit flags that specify the type of menu item. This member can be one of the following values.



| Value                                                                                                                                                                                                       | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="MFR_END"></span><span id="mfr_end"></span><dl> <dt>**MFR\_END**</dt> <dt>0x80</dt> </dl>       | The menu item is the last in this submenu or menu resource; this flag is used internally by the system.<br/> |
| <span id="MFR_POPUP"></span><span id="mfr_popup"></span><dl> <dt>**MFR\_POPUP**</dt> <dt>0x01</dt> </dl> | The menu item opens a menu or a submenu; the flag is used internally by the system.<br/>                     |



 

</dd> <dt>

**menuText**
</dt> <dd>

Type: **szOrOrd**

</dd> <dd>

A null-terminated Unicode string that contains the text for this menu item. There is no fixed limit on the size of this string.

</dd> </dl>

## Remarks

There is one **POPUPMENUITEM** structure for each menu item that opens a menu or a submenu. Identify this type of menu item by setting the **type** member to **MF\_POPUP** and by setting the **MFR\_POPUP** bit in the **resInfo** member to 0x0001. In this case, the final data written to the [**RT\_MENU**](/windows/desktop/menurc/resource-types) resource for the menu or submenu is the [**MENUHELPID**](menuhelpid.md) structure. **MENUHELPID** contains a numeric expression that identifies the menu during [**WM\_HELP**](../shell/wm-help.md) processing.

Additionally, every **POPUPMENUITEM** structure that has the **MFR\_POPUP** bit set in the **resInfo** member will be followed by a [**MENUHELPID**](menuhelpid.md) structure plus an additional number of **POPUPMENUITEM** structures, one for each menu item in that submenu. The last **POPUPMENUITEM** structure in the submenu will have the **MFR\_END** bit set in the **resInfo** member. To find the end of the resource, look for a matching **MFR\_END** for every **MFR\_POPUP** plus one additional **MFR\_END** that matches the outermost set of menu items.

Indicate the last menu item by setting the **type** member to **MF\_END**. Because you can nest submenus, there can be multiple levels of **MF\_END**. In these instances, the menu items are sequential.

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

[**MENUHELPID**](menuhelpid.md)
</dt> <dt>

[**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa)
</dt> <dt>

[**NORMALMENUITEM**](normalmenuitem.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

