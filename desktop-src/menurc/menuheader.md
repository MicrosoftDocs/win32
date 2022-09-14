---
title: MENUHEADER structure
description: Contains version information for the menu resource. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 1e34b0b6-18ff-4cb6-901e-a2aabad0df74
keywords:
- MENUHEADER structure Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUHEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MENUHEADER structure

Contains version information for the menu resource. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD wVersion;
  WORD cbHeaderSize;
} MENUHEADER;
```



## Members

<dl> <dt>

**wVersion**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The version number of the menu template. This member must be equal to zero to indicate that this is an [**RT\_MENU**](/windows/desktop/menurc/resource-types) created with a standard menu template.

</dd> <dt>

**cbHeaderSize**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The size of the menu template header. This value is zero for menus you create with a standard menu template.

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

[**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md)
</dt> <dt>

[**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md)
</dt> <dt>

[**MENUITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-menuitemtemplate)
</dt> <dt>

[**MENUITEMTEMPLATEHEADER**](/windows/desktop/api/Winuser/ns-winuser-menuitemtemplateheader)
</dt> <dt>

[**NORMALMENUITEM**](normalmenuitem.md)
</dt> <dt>

[**POPUPMENUITEM**](popupmenuitem.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

