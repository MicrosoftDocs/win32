---
title: AUTORADIOBUTTON control
description: Defines an automatic radio button control. This control automatically performs mutual exclusion with the other AUTORADIOBUTTON controls in the same group. When the button is chosen, the application is notified with BN\_CLICKED.
ms.assetid: af843084-5213-4934-b291-0787b88ef62d
keywords:
- AUTORADIOBUTTON control Menus and Other Resources
topic_type:
- apiref
api_name:
- AUTORADIOBUTTON
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AUTORADIOBUTTON control

Defines an automatic radio button control. This control automatically performs mutual exclusion with the other **AUTORADIOBUTTON** controls in the same group. When the button is chosen, the application is notified with **BN\_CLICKED**.

``` syntax
AUTORADIOBUTTON text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Text that will appear next to the radio button.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the automatic radio button, which can be a combination of BUTTON-class styles and the following styles: **WS\_TABSTOP**, **WS\_DISABLED**, and **WS\_GROUP**.

If you do not specify a style, the default style is `BS_AUTORADIOBUTTON | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## See also

<dl> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[Radio Buttons](https://www.bing.com/search?q=Radio+Buttons)
</dt> <dt>

[**RADIOBUTTON**](radiobutton-control.md)
</dt> </dl>

 

 




