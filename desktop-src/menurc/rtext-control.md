---
title: RTEXT control
description: Defines a right-aligned text control.
ms.assetid: 66b890db-598e-4255-9d65-a21647005f8e
keywords:
- RTEXT control Menus and Other Resources
topic_type:
- apiref
api_name:
- RTEXT
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# RTEXT control

Defines a right-aligned text control. The control is a simple rectangle displaying the given text right-aligned in the rectangle. The text is formatted before it is displayed. Words that would extend past the end of a line are automatically wrapped to the beginning of the next line. Words that are longer than the width of the control are truncated.

The **RTEXT** statement, which can be used only in a [**DIALOGEX**](dialogex-resource.md) statement, defines the text, identifier, dimensions, and attributes of the control.

``` syntax
RTEXT text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the text control, which can be any combination of the following: **WS\_TABSTOP** and **WS\_GROUP**.

If you do not specify a style, the default style is `SS_RIGHT | WS_GROUP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

The following example demonstrates the use of the **RTEXT** statement:

``` syntax
RTEXT "Number of Messages", 4, 30, 50, 100, 10
```

## See also

<dl> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**CTEXT**](ctext-control.md)
</dt> <dt>

[Edit Controls](../controls/about-edit-controls.md)
</dt> <dt>

[**LTEXT**](ltext-control.md)
</dt> </dl>

 

 