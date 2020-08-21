---
title: COMBOBOX control (Menus and Other Resources)
description: Defines a combination box control (a combo box).
ms.assetid: 0a0fcfa8-b65c-44c1-89d8-f5020af10f0f
keywords:
- COMBOBOX control Menus and Other Resources
topic_type:
- apiref
api_name:
- COMBOBOX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# COMBOBOX control

Defines a combination box control (a combo box). A combo box consists of either a static text box or an edit box combined with a list box. The list box can be displayed at all times or pulled down by the user. If the combo box contains a static text box, the text box always displays the selection (if any) in the list box portion of the combo box. If it uses an edit box, the user can type in the desired selection; the list box highlights the first item (if any) that matches what the user has entered in the edit box. The user can then select the item highlighted in the list box to complete the choice. In addition, the combo box can be owner-drawn and of fixed or variable height.

``` syntax
COMBOBOX id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be a combination of the COMBOBOX class styles and any of the following styles: **WS\_TABSTOP**, **WS\_GROUP**, **WS\_VSCROLL**, and **WS\_DISABLED**.

If you do not specify a style, the default style is `CBS_SIMPLE | WS_TABSTOP`.

</dd> </dl>

The *height* parameter applies to the height of a combo box with a drop-down list fully expanded.

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

This example defines a combo-box control with a vertical scroll bar:

``` syntax
COMBOBOX 777, 10, 10, 50, 54, CBS_SIMPLE | WS_VSCROLL | WS_TABSTOP 
```

## See also

<dl> <dt>

[Combo Boxes](../controls/about-combo-boxes.md)
</dt> </dl>

 

 