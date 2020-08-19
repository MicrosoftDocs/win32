---
title: CHECKBOX control (Resource Compiler)
description: Defines a check box control.
ms.assetid: '24ee25e5-9de2-4843-a55e-96b897f6ae8e'
keywords:
- CHECKBOX control Menus and Other Resources
topic_type:
- apiref
api_name:
- CHECKBOX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CHECKBOX control

Defines a check box control. The control is a small rectangle (check box) that has the specified text displayed next to it (typically, to the right). When the user selects the control, the control highlights the rectangle and sends a message to its parent window.

The **CHECKBOX** statement, which can only be used in a [**DIALOGEX**](dialogex-resource.md) statement, defines the text, identifier, dimensions, and attributes of the control.

``` syntax
CHECKBOX text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Text that is to be displayed to the right of the control.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be a combination of the button class style **BS\_CHECKBOX** and the **WS\_TABSTOP** and **WS\_GROUP** styles.

If you do not specify a style, the default style is `BS_CHECKBOX | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

This example defines a check-box control that is labeled Italic:

``` syntax
CHECKBOX "Italic", 3, 10, 10, 40, 10
```

## See also

<dl> <dt>

[**AUTOCHECKBOX**](autocheckbox-control.md)
</dt> <dt>

[**AUTO3STATE**](auto3state-control.md)
</dt> <dt>

[Check Boxes](https://www.bing.com/search?q=Check+Boxes)
</dt> <dt>

[**GetDialogBaseUnits**](/windows/win32/api/winuser/nf-winuser-getdialogbaseunits)
</dt> <dt>

[**STATE3**](state3-control.md)
</dt> </dl>

 

 