---
title: LTEXT control
description: Defines a left-aligned text control.
ms.assetid: ef6d7d06-3614-4b54-8a23-684d7ef65115
keywords:
- LTEXT control Menus and Other Resources
topic_type:
- apiref
api_name:
- LTEXT
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LTEXT control

Defines a left-aligned text control. The control is a simple rectangle displaying the given text left-aligned in the rectangle. The text is formatted before it is displayed. Words that would extend past the end of a line are automatically wrapped to the beginning of the next line. Words that are longer than the width of the control are truncated.

The **LTEXT** statement, which can be used only in a [**DIALOGEX**](dialogex-resource.md) statement, defines the text, identifier, dimensions, and attributes of the control.

``` syntax
LTEXT text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be any combination of the **BS\_RADIOBUTTON** style and the following styles: **SS\_LEFT**, **WS\_TABSTOP**, and **WS\_GROUP**.

If you do not specify a style, the default style is `SS_LEFT | WS_GROUP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

This example defines a left-aligned text control that is labeled Filename:

``` syntax
LTEXT "Filename", 101, 10, 10, 100, 100
```

## See also

<dl> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**CTEXT**](ctext-control.md)
</dt> <dt>

[Edit Controls](../controls/about-edit-controls.md)
</dt> <dt>

[**RTEXT**](rtext-control.md)
</dt> </dl>

 

 