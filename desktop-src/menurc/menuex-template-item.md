---
title: MENUEX_TEMPLATE_ITEM structure
description: Defines a menu item in an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.
ms.assetid: f6e2fd0a-16b8-48e3-8597-341085a7adbd
keywords:
- MENUEX_TEMPLATE_ITEM structure Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUEX_TEMPLATE_ITEM
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MENUEX\_TEMPLATE\_ITEM structure

Defines a menu item in an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.

## Syntax

```C++
typedef struct {
  DWORD dwType;
  DWORD dwState;
  UINT  uId;
  WORD  wFlags;
  WCHAR szText[1];
} MENUEX_TEMPLATE_ITEM;
```

## Members

<dl> <dt>

**dwType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The menu item type. This member can be a combination of the type (beginning with MFT) values listed with the [**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa) structure.

</dd> <dt>

**dwState**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The menu item state. This member can be a combination of the state (beginning with MFS) values listed with the [**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa) structure.

</dd> <dt>

**uId**
</dt> <dd>

Type: **UINT**

</dd> <dd>

The menu item identifier. This is an application-defined value that identifies the menu item. In an extended menu resource, items that open drop-down menus or submenus as well as command items can have identifiers.

</dd> <dt>

**wFlags**
</dt> <dd>

Type: **WORD**

</dd> <dd>

Specifies whether the menu item is the last item in the menu bar, drop-down menu, submenu, or shortcut menu and whether it is an item that opens a drop-down menu or submenu. This member can be zero or more of these values. For 32-bit applications, this member is a word; for 16-bit applications, it is a byte.

<dt>

0x80
</dt> <dd>

The structure defines the last menu item in the menu bar, drop-down menu, submenu, or shortcut menu.

</dd> <dt>

0x01
</dt> <dd>

The structure defines a item that opens a drop-down menu or submenu. Subsequent structures define menu items in the corresponding drop-down menu or submenu.

</dd> </dl> </dd> <dt>

**szText**
</dt> <dd>

Type: **WCHAR**

</dd> <dd>

The menu item text. This member is a null-terminated Unicode string, aligned on a word boundary. The size of the menu item definition varies depending on the length of this string.

</dd> </dl>

## Remarks

An extended menu template consists of a [**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md) structure followed by one or more contiguous **MENUEX\_TEMPLATE\_ITEM** structures. The **MENUEX\_TEMPLATE\_ITEM** structures, which are variable in length, are aligned on **DWORD** boundaries. To create a menu from an extended menu template in memory, use the [**LoadMenuIndirect**](/windows/desktop/api/Winuser/nf-winuser-loadmenuindirecta) function.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**LoadMenuIndirect**](/windows/desktop/api/Winuser/nf-winuser-loadmenuindirecta)
</dt> <dt>

[**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md)
</dt> <dt>

[**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Menus](menus.md)
</dt> </dl>

 

 





