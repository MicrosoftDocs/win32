---
title: RADIOBUTTON control
description: Defines a radio-button control.
ms.assetid: af843084-5213-4934-b291-0787b88ef62d
keywords:
- RADIOBUTTON control Menus and Other Resources
topic_type:
- apiref
api_name:
- RADIOBUTTON
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RADIOBUTTON control

Defines a radio-button control. The control is a small circle that has the given text displayed next to it, typically to its right. The control highlights the circle and sends a message to its parent window when the user selects the button. The control removes the highlight and sends a message when the button is next selected.

``` syntax
RADIOBUTTON text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the radio button, which can be a combination of BUTTON-class styles and the following styles: **WS\_TABSTOP**, **WS\_DISABLED**, and **WS\_GROUP**.

If you do not specify a style, the default style is `BS_RADIOBUTTON | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

The following example demonstrates the use of the **RADIOBUTTON** statement:

``` syntax
RADIOBUTTON "Italic", 100, 10, 10, 40, 10
```

## See also

<dl> <dt>

[**GetDialogBaseUnits**](_win32_getdialogbaseunits_cpp)
</dt> <dt>

[Radio Buttons](_win32_Button_Types_and_Styles#radio-buttons)
</dt> </dl>

 

 




