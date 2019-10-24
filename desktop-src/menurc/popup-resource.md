---
title: POPUP resource
description: Defines a menu item that can contain menu items and submenus.
ms.assetid: afca21c7-605e-4354-b6ec-576b81389b69
keywords:
- POPUP resource Menus and Other Resources
topic_type:
- apiref
api_name:
- POPUP
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# POPUP resource

Defines a menu item that can contain menu items and submenus.

``` syntax
POPUP text, [optionlist] {item-definitions ...}
```

## Parameters

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

String that contains the name of the menu. This string must be enclosed in double quotation marks (**"**).

</dd> <dt>

<span id="optionlist"></span><span id="OPTIONLIST"></span>*optionlist*
</dt> <dd>

This parameter specifies redefined menu options that specify the appearance of the menu item. This optional parameter can be one or more of the following.



| Option           | Description                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CHECKED**      | Menu item has a check mark next to it. This option is not valid for a top-level menu.                                                                                 |
| **GRAYED**       | Menu item is initially inactive and appears on the menu in gray or a lightened shade of the menu-text color. This option cannot be used with the **INACTIVE** option. |
| **HELP**         | Identifies a help item. The menu item is place at the right-most position on the menu bar.                                                                            |
| **INACTIVE**     | Menu item is displayed but it cannot be selected. This option cannot be used with the **GRAYED** option.                                                              |
| **MENUBARBREAK** | Same as **MENUBREAK** except that for pop-up menus, it separates the new column from the old column with a vertical line.                                             |
| **MENUBREAK**    | Places the menu item on a new line for static menu-bar items. For menus, it places the menu item in a new column with no dividing line between the columns.           |



 

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following example demonstrates the use of the **POPUP** statement:

``` syntax
chem MENU
{
    POPUP "&Elements"
    {
         MENUITEM "&Oxygen", 200
         MENUITEM "&Carbon", 201, CHECKED
         MENUITEM "&Hydrogen", 202
         MENUITEM SEPARATOR
         MENUITEM "&Sulfur", 203
         MENUITEM "Ch&lorine", 204
    } 
    POPUP "&Compounds"
    {
         POPUP "&Sugars"
         {
            MENUITEM "&Glucose", 301
            MENUITEM "&Sucrose", 302, CHECKED
            MENUITEM "&Lactose", 303, MENUBREAK
            MENUITEM "&Fructose", 304
         }
         POPUP "&Acids"
         {
              "&Hydrochloric", 401
              "&Sulfuric", 402
         }
    }
}
```

## See also

<dl> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**MENUITEM**](menuitem-statement.md)
</dt> </dl>

 

 




