---
title: DIALOGEX resource
description: Defines a dialog box. | DIALOGEX resource
ms.assetid: 3ff28b68-e8b4-444d-8e26-5119ed30e44e
keywords:
- DIALOGEX resource Menus and Other Resources
topic_type:
- apiref
api_name:
- DIALOGEX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DIALOGEX resource

Defines a dialog box. The statement defines the position and dimensions of the dialog box on the screen as well as the dialog box style. It also defines the following:

-   Help IDs on the dialog itself as well as on controls within the dialog box.
-   Use of the [**EXSTYLE**](exstyle-statement.md) statement for the dialog box itself as well as on controls within the dialog box.
-   Font weight and italic settings for the font to be used in the dialog box.
-   Control-specific data for controls within the dialog box.
-   Use of the **BEDIT**, **IEDIT**, and **HEDIT** predefined system class names.

``` syntax
nameID DIALOGEX x, y, width, height [ , helpID] [optional-statements]  {control-statements}
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a unique 16-bit unsigned integer value that identifies the dialog box.

</dd> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

Location on the screen of the left side of the dialog box, in dialog units.

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

Location on the screen of the top of the dialog box, in dialog units.

</dd> <dt>

<span id="width"></span><span id="WIDTH"></span>*width*
</dt> <dd>

Width of the dialog box, in dialog units.

</dd> <dt>

<span id="height"></span><span id="HEIGHT"></span>*height*
</dt> <dd>

Height of the dialog box, in dialog units.

</dd> <dt>

<span id="helpID"></span><span id="helpid"></span><span id="HELPID"></span>*helpID*
</dt> <dd>

Numeric expression indicating the ID used to identify the dialog box during [**WM\_HELP**](../shell/wm-help.md) processing.

</dd> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

Options for the dialog box. This can be zero or more of the following statements.



| Statement                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CAPTION** "*text*"                                              | Caption of the dialog box if it has a title bar. For more information, see [**CAPTION Statement**](caption-statement.md).                                                                                                                                                                                                                                                                                                                                                            |
| **CHARACTERISTICS** *dword*                                       | User-defined **DWORD** value for use by resource tools. This value is not used by the system. For more information, see [**CHARACTERISTICS Statement**](characteristics-statement.md).                                                                                                                                                                                                                                                                                               |
| **CLASS***class*                                                  | A 16-bit unsigned integer or a string, enclosed in double quotation marks ("), that identifies the class of the dialog box. For more information, see [**CLASS Statement**](class-statement.md).                                                                                                                                                                                                                                                                                     |
| **EXSTYLE**= *extended-styles*                                    | Extended window style of the dialog box. For more information, see [**EXSTYLE Statement**](exstyle-statement.md).                                                                                                                                                                                                                                                                                                                                                                    |
| **FONT** *pointsize*, "*typeface*", *weight*, *italic*, *charset* | Point size and typeface for the font. For *weight*, use the **FW\_\*** values defined in WinGDI.h. For *italic*, specify TRUE to use an italic font, FALSE otherwise. For *charset*, use the value defined in the **lfCharSet** member of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure. To get the definitive font for a dialog box, an application should specify *charset* along with other font properties. For more information, see [**FONT Statement**](font-statement.md). |
| **LANGUAGE** *language*, *sublanguage*                            | Language of the dialog box. For more information, see [**LANGUAGE Statement**](language-statement.md).                                                                                                                                                                                                                                                                                                                                                                               |
| **MENU** *menuname*                                               | Menu to be used. This value is either the name of the menu or its integer identifier. For more information, see [**MENU Statement**](menu-statement.md).                                                                                                                                                                                                                                                                                                                             |
| **STYLE** *styles*                                                | Styles of the dialog box. For more information, see [**STYLE Statement**](style-statement.md).                                                                                                                                                                                                                                                                                                                                                                                       |
| **VERSION** *dword*                                               | User-defined **DWORD** value. This statement is intended for use by additional resource tools and is not used by the system. For more information, see [**VERSION Statement**](version-statement.md).                                                                                                                                                                                                                                                                                |



 

</dd> <dt>

<span id="control-statements"></span><span id="CONTROL-STATEMENTS"></span>*control-statements*
</dt> <dd>

Body of the **DIALOGEX** resource is made up of any number of control statements. There are four families of control statements: generic, static, button, and edit. For more information, see Remarks.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

The valid operations that may be contained in any of the numeric expressions in the statements of **DIALOGEX** are as follows:

-   Add ('+')
-   Subtract ('-')
-   Unary minus ('-')
-   Unary NOT ('~')
-   AND ('&')
-   OR ('\|')

The body of the resource is made up of generic, static, button, and edit control statements. While each of these families of statements uses a different syntax for defining specific features of its controls, they all share a common syntax for defining the position, size, extended styles, help identification number, and control-specific data. For more information, see [Common Control Parameters](common-control-parameters.md).

### Generic Control Statements

``` syntax
CONTROL controlText, id, className, style
```

<dl> <dt>

<span id="controlText"></span><span id="controltext"></span><span id="CONTROLTEXT"></span>*controlText*
</dt> <dd>

Window text for the control. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Control identifier. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> <dt>

<span id="className"></span><span id="classname"></span><span id="CLASSNAME"></span>*className*
</dt> <dd>

Name of the class. This may be either a string enclosed in double quotation marks (") or one of the following predefined system classes: **BUTTON**, **STATIC**, **EDIT**, **LISTBOX**, **SCROLLBAR**, or **COMBOBOX**.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Window styles (explicit **WS\_\***, **BS\_\***, **SS\_\***, **ES\_\***, **LBS\_\***, **SBS\_\***, and **CBS\_\*** style values defined in Winuser.H can be used by adding an include to the .rc file: `#include "winuser.h"`). For more information, see [Window Styles](/windows/desktop/winmsg/window-styles).

</dd> </dl>

### Static Control Statements

``` syntax
staticClass controlText, id
```

<dl> <dt>

<span id="staticClass"></span><span id="staticclass"></span><span id="STATICCLASS"></span>*staticClass*
</dt> <dd>

**LTEXT**, **RTEXT**, or **CTEXT**.

</dd> <dt>

<span id="controlText"></span><span id="controltext"></span><span id="CONTROLTEXT"></span>*controlText*
</dt> <dd>

Window text for the control. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Control identifier. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> </dl>

### Button Control Statements

``` syntax
buttonClass controlText, id
```

<dl> <dt>

<span id="buttonClass"></span><span id="buttonclass"></span><span id="BUTTONCLASS"></span>*buttonClass*
</dt> <dd>

**AUTO3STATE**, **AUTOCHECKBOX**, **AUTORADIOBUTTON**, **CHECKBOX**, **PUSHBOX**, **PUSHBUTTON**, **RADIOBUTTON**, **STATE3**, or **USERBUTTON**.

</dd> <dt>

<span id="controlText"></span><span id="controltext"></span><span id="CONTROLTEXT"></span>*controlText*
</dt> <dd>

Window text for the control. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Control identifier. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> </dl>

### Edit Control Statements

``` syntax
editClass id
```

<dl> <dt>

<span id="editClass"></span><span id="editclass"></span><span id="EDITCLASS"></span>*editClass*
</dt> <dd>

**EDITTEXT**, **BEDIT**, **HEDIT**, or **IEDIT**.

</dd> <dt>

<span id="id"></span><span id="ID"></span>*id*
</dt> <dd>

Control identifier. For more information, see [Common Control Parameters](common-control-parameters.md).

</dd> </dl>

## See also

<dl> <dt>

[Using Dialog Boxes](../dlgbox/using-dialog-boxes.md)
</dt> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**CONTROL**](control-control.md)
</dt> <dt>

[**CreateDialog**](/windows/win32/api/winuser/nf-winuser-createdialoga)
</dt> <dt>

[**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa)
</dt> <dt>

[**DialogBox**](/windows/win32/api/winuser/nf-winuser-dialogboxa)
</dt> <dt>

[**GetDialogBaseUnits**](/windows/win32/api/winuser/nf-winuser-getdialogbaseunits)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta)
</dt> <dt>

[MENU](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 
