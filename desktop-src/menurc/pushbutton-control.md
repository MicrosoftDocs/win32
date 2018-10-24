---
title: PUSHBUTTON control
description: Defines a push-button control. The control is a round-cornered rectangle containing the given text. The text is centered in the control. The control sends a message to its parent whenever the user chooses the control.
ms.assetid: 'c5fbcfb7-1b7d-4199-acac-d11bfd899298'
keywords:
- PUSHBUTTON control Menus and Other Resources
topic_type:
- apiref
api_name:
- PUSHBUTTON
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[**GetDialogBaseUnits**](https://msdn.microsoft.com/library/ms645475(v=VS.85).aspx)
</dt> <dt>

[Push Buttons](https://www.bing.com/search?q=Push+Buttons)
</dt> </dl>

 

 




