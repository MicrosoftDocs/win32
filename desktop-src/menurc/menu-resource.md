---
title: MENU resource
description: Defines the contents of a menu resource. | MENU resource
ms.assetid: fcb420b6-d42e-4044-89ee-028eed1f21ee
keywords:
- MENU resource Menus and Other Resources
topic_type:
- apiref
api_name:
- MENU
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# MENU resource

Defines the contents of a menu resource. A menu resource is a collection of information that defines the appearance and function of an application menu. A menu is a special input tool that lets a user select commands and open submenus from a list of menu items.

``` syntax
menuID MENU  [optional-statements]  {item-definitions ... }
```

## Parameters

<dl> <dt>

<span id="menuID"></span><span id="menuid"></span><span id="MENUID"></span>*menuID*
</dt> <dd>

Number that identifies the menu. This value is either a unique string or a unique 16-bit unsigned integer value in the range of 1 to 65,535.

</dd> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

This parameter can be zero of more of the following statements.



| Statement                                                        | Description                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CHARACTERISTICS**](characteristics-statement.md) *dword*     | User-defined information about a resource that can be used by tools that read and write resource files. For more information, see [**CHARACTERISTICS**](characteristics-statement.md). |
| [**LANGUAGE**](language-statement.md) *language*, *sublanguage* | Language for the resource. For more information, see [**LANGUAGE**](language-statement.md).                                                                                            |
| [**VERSION**](version-statement.md) *dword*                     | User-defined version number for the resource that can be used by tools that read and write resource files. For more information, see [**VERSION**](version-statement.md).              |



 

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following is an example of a complete **MENU** statement:

``` syntax
sample MENU
{
     MENUITEM "&Soup", 100
     MENUITEM "S&alad", 101
     POPUP "&Entree"
     {
          MENUITEM "&Fish", 200
          MENUITEM "&Chicken", 201, CHECKED
          POPUP "&Beef"
          {
               MENUITEM "&Steak", 301
               MENUITEM "&Prime Rib", 302
          }
     }
     MENUITEM "&Dessert", 103
}
```

## See also

<dl> <dt>

[Using Menus](./using-menus.md)
</dt> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENUEX**](menuex-resource.md)
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

 

 
