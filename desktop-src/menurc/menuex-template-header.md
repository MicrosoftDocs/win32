---
title: MENUEX_TEMPLATE_HEADER structure
description: Defines the header for an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.
ms.assetid: df763349-7127-482e-8613-74e68addde5d
keywords:
- MENUEX_TEMPLATE_HEADER structure Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUEX_TEMPLATE_HEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MENUEX\_TEMPLATE\_HEADER structure

Defines the header for an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD  wVersion;
  WORD  wOffset;
  DWORD dwHelpId;
} MENUEX_TEMPLATE_HEADER;
```



## Members

<dl> <dt>

**wVersion**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The template version number. This member must be 1 for extended menu templates.

</dd> <dt>

**wOffset**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The offset to the first [**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md) structure, relative to the end of this structure member. If the first item definition immediately follows the **dwHelpId** member, this member should be 4.

</dd> <dt>

**dwHelpId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The help identifier of menu bar.

</dd> </dl>

## Remarks

An extended menu template consists of a **MENUEX\_TEMPLATE\_HEADER** structure followed by one or more contiguous [**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md) structures. The **MENUEX\_TEMPLATE\_ITEM** structures, which are variable in length, are aligned on **DWORD** boundaries. To create a menu from an extended menu template in memory, use the [**LoadMenuIndirect**](/windows/desktop/api/Winuser/nf-winuser-loadmenuindirecta) function.

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

[**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Menus](menus.md)
</dt> </dl>

 

 





