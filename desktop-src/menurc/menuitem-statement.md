---
title: MENUITEM statement
description: Defines a menu item.
ms.assetid: b154211a-5267-4dcf-9e70-ac36671d10d3
keywords:
- MENUITEM statement Menus and Other Resources
topic_type:
- apiref
api_name:
- MENUITEM
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# MENUITEM statement

Defines a menu item.

``` syntax
MENUITEM text, result, [optionlist]  
MENUITEM SEPARATOR
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

The name of the menu item.

The string can contain the escape characters **\\t** and **\\a**. The **\\t** character inserts a tab in the string and is used to align text in columns. Tab characters should be used only in menus, not in menu bars. (For information on menus, see [**POPUP Resource**](popup-resource.md).) The **\\a** character aligns all text that follows it flush right to the menu bar or pop-up menu.

</dd> <dt>

<span id="result"></span><span id="RESULT"></span>*result*
</dt> <dd>

A number that specifies the result generated when the user selects the menu item. This parameter takes an integer value. Menu-item results are always integers; when the user clicks the menu-item name, the result is sent to the window that owns the menu.

</dd> <dt>

<span id="optionlist"></span><span id="OPTIONLIST"></span>*optionlist*
</dt> <dd>

The appearance of the menu item. This optional parameter takes one or more of the following redefined menu options, separated by commas or spaces.



| Option           | Description                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CHECKED**      | Menu item has a check mark next to it.                                                                                                                                |
| **GRAYED**       | Menu item is initially inactive and appears on the menu in gray or a lightened shade of the menu-text color. This option cannot be used with the **INACTIVE** option. |
| **HELP**         | Identifies a help item. This option has no effect on the appearance of the menu item.                                                                                 |
| **INACTIVE**     | Menu item is displayed but it cannot be selected. This option cannot be used with the **GRAYED** option.                                                              |
| **MENUBARBREAK** | Same as **MENUBREAK** except that for pop-up menus, it separates the new column from the old column with a vertical line.                                             |
| **MENUBREAK**    | Places the menu item on a new line for static menu-bar items. For menus, it places the menu item in a new column with no dividing line between the columns.           |



 

</dd> <dt>

<span id="MENUITEM_SEPARATOR"></span><span id="menuitem_separator"></span>**MENUITEM SEPARATOR**
</dt> <dd>

The **MENUITEM SEPARATOR** form of the **MENUITEM** statement creates an inactive menu item that serves as a dividing bar between two active menu items on a menu. Note that this form works inside a **MENU** block, whereas **MENUITEM**'s inside a **MENUEX** instead require the form `MENUITEM "", -1, MFT_SEPARATOR`.

</dd> </dl>

## Examples

The following example demonstrates the use of the **MENUITEM** and **MENUITEM SEPARATOR** statements:

``` syntax
MENUITEM "&Roman", 206, CHECKED, GRAYED
MENUITEM SEPARATOR
MENUITEM "&Blackletter", 301
```

## See also

<dl> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**POPUP**](popup-resource.md)
</dt> </dl>

 

 




