---
title: GROUPBOX control (Menus and Other Resources)
description: Defines a group box control. The control is a rectangle that groups other controls together. The controls are grouped by drawing a border around them and displaying the given text in the upper-left corner.
ms.assetid: ffca7b68-0326-4fbe-8330-7d1151abb14a
keywords:
- GROUPBOX control Menus and Other Resources
topic_type:
- apiref
api_name:
- GROUPBOX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# GROUPBOX control

Defines a group box control. The control is a rectangle that groups other controls together. The controls are grouped by drawing a border around them and displaying the given text in the upper-left corner.

The **GROUPBOX** statement, which you can use only in a [**DIALOGEX**](dialogex-resource.md) statement, defines the text, identifier, dimensions, and attributes of a control window.

``` syntax
GROUPBOX text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be a combination of the button class style **BS\_GROUPBOX** and the **WS\_TABSTOP** and **WS\_DISABLED** styles.

If you do not specify a style, the default style is **BS\_GROUPBOX**.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Remarks

When the style contains **WS\_TABSTOP** or the text specifies an accelerator, tabbing or pressing the accelerator key moves the focus to the first control within the group.

## Examples

This example defines a group-box control that is labeled Options:

``` syntax
GROUPBOX "Options", 101, 10, 10, 100, 100
```

## See also

<dl> <dt>

[Group Boxes](https://www.bing.com/search?q=Group+Boxes)
</dt> </dl>

 

 




