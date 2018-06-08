---
title: PUSHBOX control
description: Defines a push-box control, which is identical to a PUSHBUTTON, except that it does not display a button face or frame; only the text appears.
ms.assetid: b4e9d3f5-fcc4-40e1-90af-53d14e4638bf
keywords:
- PUSHBOX control Menus and Other Resources
topic_type:
- apiref
api_name:
- PUSHBOX
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PUSHBOX control

Defines a push-box control, which is identical to a [**PUSHBUTTON**](pushbutton-control.md), except that it does not display a button face or frame; only the text appears.

``` syntax
PUSHBOX text, id, x, y, width, height [, style [, extended-style]]
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Styles for the pushbox, which can be a combination of the **BS\_PUSHBOX** style and the following styles: **WS\_TABSTOP**, **WS\_DISABLED**, and **WS\_GROUP**.

If you do not specify a style, the default style is `BS_PUSHBOX | WS_TABSTOP`.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## See also

<dl> <dt>

[Push Buttons](https://msdn.microsoft.com/windows/desktop/bfc8b88b-0da2-46f6-b8c2-72f693ee1e7b)
</dt> <dt>

[**PUSHBUTTON**](pushbutton-control.md)
</dt> </dl>

 

 




