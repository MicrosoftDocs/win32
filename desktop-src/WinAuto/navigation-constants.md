---
title: Navigation Constants (Oleacc.h)
description: This topic describes the constant values, defined in oleacc.h, that indicate the spatial (up, down, left, and right) or logical (first child, last, next, and previous) direction observed when clients use IAccessible accNavigate to navigate from one user interface element to another within the same container.
ms.assetid: 5859a7a3-bcd3-443e-8ff0-4952f4639517
topic_type:
- apiref
api_name:
- NAVDIR_DOWN
- NAVDIR_FIRSTCHILD
- NAVDIR_LASTCHILD
- NAVDIR_LEFT
- NAVDIR_NEXT
- NAVDIR_PREVIOUS
- NAVDIR_RIGHT
- NAVDIR_UP
api_location:
- oleacc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Navigation Constants

This topic describes the constant values, defined in oleacc.h, that indicate the *spatial* (up, down, left, and right) or *logical* (first child, last, next, and previous) direction observed when clients use [**IAccessible::accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate) to navigate from one user interface element to another within the same container. For more information, see [Object Navigation Properties and Methods](object-navigation-properties-and-methods.md).

The Microsoft Active Accessibility navigation constants are as follows:



| Constant                                                                                                                                                                  | Description                                                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NAVDIR_DOWN"></span><span id="navdir_down"></span><dl> <dt>**NAVDIR\_DOWN**</dt> </dl>                   | Navigate to the sibling object that is located below the starting object.<br/>                                                                  |
| <span id="NAVDIR_FIRSTCHILD"></span><span id="navdir_firstchild"></span><dl> <dt>**NAVDIR\_FIRSTCHILD**</dt> </dl> | Navigate to the first child of this object. When this flag is used, the **lVal** member of the *varStart* parameter must be CHILDID\_SELF.<br/> |
| <span id="NAVDIR_LASTCHILD"></span><span id="navdir_lastchild"></span><dl> <dt>**NAVDIR\_LASTCHILD**</dt> </dl>    | Navigate to the last child of this object. When using this flag, the **lVal** member of the *varStart* parameter must be CHILDID\_SELF.<br/>    |
| <span id="NAVDIR_LEFT"></span><span id="navdir_left"></span><dl> <dt>**NAVDIR\_LEFT**</dt> </dl>                   | Navigate to the sibling object located to the left of the starting object.<br/>                                                                 |
| <span id="NAVDIR_NEXT"></span><span id="navdir_next"></span><dl> <dt>**NAVDIR\_NEXT**</dt> </dl>                   | Navigate to the next logical object; generally, it is a sibling of the starting object.<br/>                                                    |
| <span id="NAVDIR_PREVIOUS"></span><span id="navdir_previous"></span><dl> <dt>**NAVDIR\_PREVIOUS**</dt> </dl>       | Navigate to the previous logical object; generally, it is a sibling of the starting object.<br/>                                                |
| <span id="NAVDIR_RIGHT"></span><span id="navdir_right"></span><dl> <dt>**NAVDIR\_RIGHT**</dt> </dl>                | Navigate to the sibling object that is located to the right of the starting object.<br/>                                                        |
| <span id="NAVDIR_UP"></span><span id="navdir_up"></span><dl> <dt>**NAVDIR\_UP**</dt> </dl>                         | Navigate to the sibling object that is located above the starting object.<br/>                                                                  |



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Oleacc.h</dt> </dl> |



 

 





