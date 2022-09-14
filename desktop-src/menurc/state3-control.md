---
title: STATE3 control
description: Defines a three-state check box control. The control is identical to a CHECKBOX, except that it has three states checked, unchecked, and disabled (grayed).
ms.assetid: 74659827-ce46-4d36-a5e2-3a97e8fd1c04
keywords:
- STATE3 control Menus and Other Resources
topic_type:
- apiref
api_name:
- STATE3
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# STATE3 control

Defines a three-state check box control. The control is identical to a [**CHECKBOX**](checkbox-control.md), except that it has three states: checked, unchecked, and disabled (grayed).

``` syntax
STATE3 text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Text that is to be displayed to the right of the control.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. This value can be a combination of the button class style **BS\_3STATE** and the **WS\_TABSTOP** and **WS\_GROUP** styles.

If you do not specify a style, the default style is `BS_3STATE | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## See also

<dl> <dt>

[**AUTOCHECKBOX**](autocheckbox-control.md)
</dt> <dt>

[Check Boxes](https://www.bing.com/search?q=Check+Boxes)
</dt> <dt>

[**CHECKBOX**](checkbox-control.md)
</dt> <dt>

[**CONTROL**](control-control.md)
</dt> </dl>

 

 




