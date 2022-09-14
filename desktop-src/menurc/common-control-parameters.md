---
title: Common Control Parameters
description: The following describes the general syntax for a control resource-definition statement.
ms.assetid: e7a49a9f-93b5-4221-8006-3d1864b7a6a1
ms.topic: article
ms.date: 05/31/2018
---

# Common Control Parameters

The following describes the general syntax for a control resource-definition statement. The meaning of each parameter is given below. Occasionally, a statement will use a parameter differently, or may ignore a parameter. The statement-specific variation is described in the documentation for the statement.

``` syntax
control [[text,]] id, x, y, width, height[[, style[[, extended-style]]]][, helpId]
[{ data-element-1 [, data-element-2 [,  . . . ]]}]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Text that is to be displayed with the control. The text is positioned within the control or adjacent to the control.

This parameter must contain zero or more characters enclosed in double quotation marks ("). Strings are automatically null-terminated and converted to Unicode in the resulting resource file.

By default, the characters listed between the double quotation marks are ANSI characters, and escape sequences are interpreted as byte escape sequences. If the string is preceded by the "L" prefix, the string is a wide-character string and escape sequences are interpreted as 2-byte escape sequences that specify Unicode characters. If a double quotation mark is required in the text, you must include the double quotation mark twice.

An ampersand (&) character in the text indicates that the following character is used as a mnemonic character for the control. When the control is displayed, the ampersand is not shown, but the mnemonic character is underlined. The user can choose the control by pressing the key corresponding to the underlined mnemonic character. To use the ampersand as a character in a string, insert two ampersands (&&).

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Control identifier. This value must be a 16-bit unsigned integer in the range 0 through 65,535 or a simple arithmetic expression that evaluates to a value in that range.

</dd> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

X-coordinate of the left side of the control relative to the left side of the dialog box. This value must be a 16-bit unsigned integer in the range 0 through 65,535. The coordinate is in dialog units and is relative to the origin of the dialog box, window, or control containing the specified control.

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

Y-coordinate of the top side of the control relative to the top of the dialog box. This value must be a 16-bit unsigned integer in the range 0 through 65,535. The coordinate is in dialog units relative to the origin of the dialog box, window, or control containing the specified control.

</dd> <dt>

<span id="width"></span><span id="WIDTH"></span>*width*
</dt> <dd>

Width of the control. This value must be a 16-bit unsigned integer in the range 1 through 65,535. The width is in 1/4-character units.

</dd> <dt>

<span id="height"></span><span id="HEIGHT"></span>*height*
</dt> <dd>

Height of the control. This value must be a 16-bit unsigned integer in the range 1 through 65,535. The height is in 1/8-character units.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control styles. Use the bitwise OR (\|) operator to combine styles. For more information, see [Window Styles](../winmsg/window-styles.md).

</dd> <dt>

<span id="extended-style"></span><span id="EXTENDED-STYLE"></span>*extended-style*
</dt> <dd>

Extended window styles. You must specify *style* to specify *extended-style*. For more information, see [**EXSTYLE**](exstyle-statement.md).

</dd> <dt>

<span id="helpId"></span><span id="helpid"></span><span id="HELPID"></span>*helpId*
</dt> <dd>

Numeric expression indicating the ID used to identify the control during [**WM\_HELP**](../shell/wm-help.md) processing.

</dd> <dt>

<span id="controlData"></span><span id="controldata"></span><span id="CONTROLDATA"></span>*controlData*
</dt> <dd>

Control-specific data for the control. When a dialog is created, and a control in that dialog which has control-specific data is created, a pointer to that data is passed into the control's window procedure through the *lParam* of the [**WM\_CREATE**](../winmsg/wm-create.md) message for that control.

</dd> </dl>

## Remarks

Horizontal dialog units are 1/4 of the dialog base width unit. Vertical units are 1/8 of the dialog base height unit. The current dialog base units are computed from the height and width of the current system font. The [**GetDialogBaseUnits**](/windows/win32/api/winuser/nf-winuser-getdialogbaseunits) function returns the dialog base units in pixels. The coordinates are relative to the origin of the dialog box.

 

 