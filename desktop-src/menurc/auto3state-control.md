---
title: AUTO3STATE control
description: Defines an automatic three-state check box.
ms.assetid: 8b27367c-30d0-4591-93d0-756c65255b26
keywords:
- AUTO3STATE control Menus and Other Resources
topic_type:
- apiref
api_name:
- AUTO3STATE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AUTO3STATE control

Defines an automatic three-state check box. The control is an open box with the given text positioned to the right of the box. When chosen, the box automatically advances between three states: checked, unchecked, and disabled (grayed). The control sends a message to its parent whenever the user chooses the control.

``` syntax
AUTO3STATE text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the control, which can be a combination of the **BS\_AUTO3STATE** style and the following styles: **WS\_TABSTOP**, **WS\_DISABLED**, and **WS\_GROUP**.

If you do not specify a style, the default style is `BS_AUTO3STATE | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## See also

<dl> <dt>

[**AUTOCHECKBOX**](autocheckbox-control.md)
</dt> <dt>

[Check Boxes](https://www.bing.com/search?q=Check+Boxes)
</dt> <dt>

[**CHECKBOX**](checkbox-control.md)
</dt> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**STATE3**](state3-control.md)
</dt> <dt>

[Window Styles](/windows/desktop/winmsg/window-styles)
</dt> </dl>

 

 