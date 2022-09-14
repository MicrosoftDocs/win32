---
title: EXSTYLE statement
description: Defines extended window styles for a dialog box. In a resource definition, the EXSTYLE statement is placed with the optional statements before the beginning of the body of the resource definition.
ms.assetid: 5dc74bab-e385-457c-80c4-5e04eed589b5
keywords:
- EXSTYLE statement Menus and Other Resources
topic_type:
- apiref
api_name:
- EXSTYLE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EXSTYLE statement

Defines extended window styles for a dialog box. In a resource definition, the **EXSTYLE** statement is placed with the optional statements before the beginning of the body of the resource definition.

``` syntax
EXSTYLE extended-style
```

<dl> <dt>

<span id="extended-style"></span><span id="EXTENDED-STYLE"></span>*extended-style*
</dt> <dd>

Extended window style for the dialog box or control. For a list of extended window styles, see [**Extended Window Styles**](/windows/desktop/winmsg/extended-window-styles).

</dd> </dl>

## Remarks

For controls, extended styles are specified after the *style* option in the control resource-definition statement. For more information, see the resource-definition statement for the individual control.

## See also

<dl> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**DIALOG**](dialog-resource.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**POPUP**](popup-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[User-Defined Resource](user-defined-resource.md)
</dt> </dl>

 

 