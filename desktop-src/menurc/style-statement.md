---
title: STYLE statement
description: Defines the window style of the dialog box. The window style specifies whether the box is a pop-up or a child window.
ms.assetid: '5ede57ad-5fa5-414c-9823-e66994826027'
keywords:
- STYLE statement Menus and Other Resources
topic_type:
- apiref
api_name:
- STYLE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# STYLE statement

Defines the window style of the dialog box. The window style specifies whether the box is a pop-up or a child window.

``` syntax
STYLE style
```

<dl> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

The window style. This parameter can be an integer value or a combination of window style values (such as **WS\_CAPTION** and **WS\_SYSMENU**) and dialog box style values (such as **DS\_CENTER**).

</dd> </dl>

For a list of window styles, see [Window Styles](/windows/desktop/winmsg/window-styles). For a list of dialog box styles, see [Dialog Box Template Styles](../dlgbox/about-dialog-boxes.md). If you use the window or dialog box style values, you must include Windows.h.

 

 