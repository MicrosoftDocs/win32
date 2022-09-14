---
title: MENUEX resource
description: Defines the contents of a menu resource. | MENUEX resource
ms.assetid: a83e1e78-2af4-4257-906e-7eb6d98bcbc8
keywords:
- MENUEX resource Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUEX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# MENUEX resource

Defines the contents of a menu resource. A menu resource is a collection of information that defines the appearance and function of an application menu. A menu is a special input tool that lets a user select commands and open submenus from a list of menu items. It also defines the following:

-   Help identifiers on menus.
-   Identifiers on menus.
-   Use of the **MFT\_\*** type flags and **MFS\_\*** state flags. For more information on these flags, see the [**MENUITEMINFO**](/windows/win32/api/winuser/ns-winuser-menuiteminfoa) structure.

``` syntax
menuID MENUEX{ [{[MENUITEM itemText [,[id][, [type][, state]]]] | 
    POPUP itemText [,[id][, [type][, [state][, helpID]]]] { popupBody } } . . .]}
```

## Parameters

<dl> <dt>

<span id="MENUITEM"></span><span id="menuitem"></span>[**MENUITEM**](menuitem-statement.md)
</dt> <dd>

Defines a menu item.

<dl> <dt>

<span id="itemText"></span><span id="itemtext"></span><span id="ITEMTEXT"></span>*itemText*
</dt> <dd>

String containing the text for the menu item. For more information, see [**MENUITEM**](menuitem-statement.md).

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Numeric expression indicating the identifier of the menu item.

</dd> <dt>

<span id="type"></span><span id="TYPE"></span>*type*
</dt> <dd>

Numeric expression indicating the type of the menu item To use the predefined MFT\_\* type values, include the following statement in your .rc file: `#include "winuser.h"`

</dd> <dt>

<span id="state"></span><span id="STATE"></span>*state*
</dt> <dd>

Numeric expression indicating the state of the menu item To use the predefined MFS\_\* state values, include the following statement in your .RC file: `#include "winuser.h"`

</dd> </dl> </dd> <dt>

<span id="POPUP"></span><span id="popup"></span>[**POPUP**](popup-resource.md)
</dt> <dd>

Defines a menu item that has a submenu associated with it.

<dl> <dt>

<span id="itemText"></span><span id="itemtext"></span><span id="ITEMTEXT"></span>*itemText*
</dt> <dd>

String containing the text for the menu item.

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Numeric expression indicating the identifier of the menu item.

</dd> <dt>

<span id="type"></span><span id="TYPE"></span>*type*
</dt> <dd>

Numeric expression indicating the type of the menu item To use the predefined MFT\_\* type values, include the following statement in your .RC file: `#include "winuser.h"`

</dd> <dt>

<span id="state"></span><span id="STATE"></span>*state*
</dt> <dd>

Numeric expression indicating the state of the menu item To use the predefined MFS\_\* state values, include the following statement in your .rc file: `#include "winuser.h"`

</dd> <dt>

<span id="helpID"></span><span id="helpid"></span><span id="HELPID"></span>*helpID*
</dt> <dd>

Numeric expression indicating the identifier used to identify the menu during [**WM\_HELP**](../shell/wm-help.md) processing.

</dd> </dl> </dd> <dt>

<span id="popupBody"></span><span id="popupbody"></span><span id="POPUPBODY"></span>*popupBody*
</dt> <dd>

Contains any combination of the [**MENUITEM**](menuitem-statement.md) and [**POPUP**](popup-resource.md) statements.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

The valid arithmetic and Boolean operations that can be contained in any of the numeric expressions in the statements of **MENUEX** are as follows:

-   Add ('+')
-   Subtract ('-')
-   Unary minus ('-')
-   Unary NOT ('~')
-   AND ('&')
-   OR ('\|')

## See also

<dl> <dt>

[Using Menus](./using-menus.md)
</dt> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**DIALOG**](dialog-resource.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**MENUITEM**](menuitem-statement.md)
</dt> <dt>

[**POPUP**](popup-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 
