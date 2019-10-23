---
title: DEFPUSHBUTTON control
description: Defines a default push-button control.
ms.assetid: 17b2ffcb-0611-4d92-9108-bf27b1c07049
keywords:
- DEFPUSHBUTTON control Menus and Other Resources
topic_type:
- apiref
api_name:
- DEFPUSHBUTTON
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DEFPUSHBUTTON control

Defines a default push-button control. The control is a small rectangle with a bold outline that represents the default response for the user. The given text is displayed inside the button. The control highlights the button in the usual way when the user clicks the mouse in it and sends a message to its parent window.

``` syntax
DEFPUSHBUTTON text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Text that is to be centered in the rectangular area of the control.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be a combination of the following styles: **BS\_DEFPUSHBUTTON**, **WS\_TABSTOP**, **WS\_GROUP**, and **WS\_DISABLED**.

If you do not specify a style, the default style is `BS_DEFPUSHBUTTON | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

This example defines a default push-button control that is labeled Cancel:

``` syntax
DEFPUSHBUTTON "Cancel", 101, 10, 10, 24, 50
```

## See also

<dl> <dt>

[Push Buttons](https://www.bing.com/search?q=Push+Buttons)
</dt> <dt>

[**PUSHBUTTON**](pushbutton-control.md)
</dt> <dt>

[**RADIOBUTTON**](radiobutton-control.md)
</dt> </dl>

 

 




