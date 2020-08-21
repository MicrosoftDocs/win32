---
title: AUTOCHECKBOX control
description: Defines an automatic check box control.
ms.assetid: 086f5dd3-267f-4ec6-be37-4e9402f7aede
keywords:
- AUTOCHECKBOX control Menus and Other Resources
topic_type:
- apiref
api_name:
- AUTOCHECKBOX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AUTOCHECKBOX control

Defines an automatic check box control. The control is a small rectangle (check box) that has the specified text displayed next to it (typically, to the right). When the user chooses the control, the control highlights the rectangle and sends a message to its parent window.

The **AUTOCHECKBOX** statement can only be used in the body of a [**DIALOG**](dialog-resource.md) or [**DIALOGEX**](dialogex-resource.md) statement.

``` syntax
AUTOCHECKBOX text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles of the control. This value can be a combination of the button class style **BS\_AUTOCHECKBOX** and the **WS\_TABSTOP** and **WS\_GROUP** styles.

If you do not specify a style, the default style is `BS_AUTOCHECKBOX | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## See also

<dl> <dt>

[**AUTO3STATE**](auto3state-control.md)
</dt> <dt>

[Button Styles](../controls/button-styles.md)
</dt> <dt>

[**CHECKBOX**](checkbox-control.md)
</dt> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**STATE3**](state3-control.md)
</dt> </dl>

 

 