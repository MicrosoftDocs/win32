---
title: PUSHBUTTON control
description: Defines a push-button control. The control is a round-cornered rectangle containing the given text. The text is centered in the control. The control sends a message to its parent whenever the user chooses the control.
ms.assetid: '17b2ffcb-0611-4d92-9108-bf27b1c07049'
keywords: ["PUSHBUTTON control Menus and Other Resources"]
topic_type:
- apiref
api_name:
- PUSHBUTTON
api_type:
- NA
---

# PUSHBUTTON control

Defines a push-button control. The control is a round-cornered rectangle containing the given text. The text is centered in the control. The control sends a message to its parent whenever the user chooses the control.

``` syntax
PUSHBUTTON text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the pushbutton, which can be a combination of the **BS\_PUSHBUTTON** style and the following styles: **WS\_TABSTOP**, **WS\_DISABLED**, and **WS\_GROUP**.

If you do not specify a style, the default style is `BS_PUSHBUTTON | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

The following example demonstrates the use of the **PUSHBUTTON** statement:

``` syntax
PUSHBUTTON "ON", 7, 10, 10, 20, 10
```

## See also

<dl> <dt>

[**GetDialogBaseUnits**](_win32_getdialogbaseunits_cpp)
</dt> <dt>

[Push Buttons](_win32_Button_Types_and_Styles#push-buttons)
</dt> </dl>

 

 




