---
title: DIALOG resource
description: Defines a dialog box. | DIALOG resource
ms.assetid: d166fb7d-0fe5-4e48-a545-19acc0ff80f1
keywords:
- DIALOG resource Menus and Other Resources
topic_type:
- apiref
api_name:
- DIALOG
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DIALOG resource

Defines a dialog box. The statement defines the position and dimensions of the dialog box on the screen as well as the dialog box style.

> [!Note]  
> **DIALOG** is an obsolete resource ID. New applications should use [**DIALOGEX**](dialogex-resource.md).

 

``` syntax
nameID DIALOG x, y, width, height  [optional-statements] {control-statement  . . . }
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a unique 16-bit unsigned integer value that identifies the dialog box.

</dd> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

Options for the dialog box. This can be zero or more of the following statements.



| Statement                                                        | Description                                                                                                                                                                                  |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAPTION**](caption-statement.md) "*text*"                    | Caption of the dialog box if it has a title bar. For more information, see [**CAPTION**](caption-statement.md).                                                                             |
| [**CHARACTERISTICS**](characteristics-statement.md) *dword*     | User-defined **DWORD** value for use by resource tools. This value is not used by the system. For more information, see [**CHARACTERISTICS**](characteristics-statement.md).                |
| [**CLASS**](class-statement.md) *class*                         | A 16-bit unsigned integer or a string, enclosed in double quotation marks ("), that identifies the class of the dialog box. For more information, see [**CLASS**](class-statement.md).      |
| **EXSTYLE=** *extended-styles*                                   | Extended window style of the dialog box. For more information, see [**EXSTYLE**](exstyle-statement.md).                                                                                     |
| **FONT** *pointsize*, *typeface*                                 | Point size and typeface for the font. For more information, see [**FONT**](font-statement.md).                                                                                              |
| [**LANGUAGE**](language-statement.md) *language*, *sublanguage* | Language of the dialog box. For more information, see [**LANGUAGE**](language-statement.md).                                                                                                |
| **MENU** *menuname*                                              | Menu to be used. This value is either the name of the menu or its integer identifier.                                                                                                        |
| [**STYLE**](style-statement.md) *styles*                        | Styles of the dialog box. For more information, see [**STYLE**](style-statement.md).                                                                                                        |
| [**VERSION**](version-statement.md) *dword*                     | User-defined **DWORD** value. This statement is intended for use by additional resource tools and is not used by the system. For more information, see [**VERSION**](version-statement.md). |



 

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

The [**GetDialogBaseUnits**](/windows/win32/api/winuser/nf-winuser-getdialogbaseunits) function returns the dialog base units in pixels. The exact meaning of the coordinates depends on the style defined by the [**STYLE**](style-statement.md) option statement. For child-style dialog boxes, the coordinates are relative to the origin of the parent window, unless the dialog box has the style **DS\_ABSALIGN**; in that case, the coordinates are relative to the origin of the display screen.

Do not use the **WS\_CHILD** style with a modal dialog box. The [**DialogBox**](/windows/win32/api/winuser/nf-winuser-dialogboxa) function always disables the parent/owner of the newly created dialog box. When a parent window is disabled, its child windows are implicitly disabled. Since the parent window of the child-style dialog box is disabled, the child-style dialog box is too.

If a dialog box has the **DS\_ABSALIGN** style, the dialog coordinates for its upper-left corner are relative to the screen origin instead of to the upper-left corner of the parent window. You would typically use this style when you wanted the dialog box to start in a specific part of the display no matter where the parent window may be on the screen.

The name **DIALOG** can also be used as the class-name parameter to the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) function to create a window with dialog-box attributes.

## Examples

The following demonstrates the usage of the **DIALOG** statement:

``` syntax
#include <windows.h>

ErrorDialog DIALOG  10, 10, 300, 110
STYLE WS_POPUP | WS_BORDER
CAPTION "Error!" 
{
    CTEXT "Select One:", 1, 10, 10, 280, 12
    PUSHBUTTON "&Retry", 2, 75, 30, 60, 12
    PUSHBUTTON "&Abort", 3, 75, 50, 60, 12
    PUSHBUTTON "&Ignore", 4, 75, 80, 60, 12
}
```

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

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 
