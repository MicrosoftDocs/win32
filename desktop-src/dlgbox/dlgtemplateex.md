---
title: DLGTEMPLATEEX structure
description: An extended dialog box template begins with a DLGTEMPLATEEX header that describes the dialog box and specifies the number of controls in the dialog box.
ms.assetid: 9f016cc6-56e2-45d3-8773-1b405fc10d29
keywords:
- DLGTEMPLATEEX structure Dialog Boxes
topic_type:
- apiref
api_name:
- DLGTEMPLATEEX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DLGTEMPLATEEX structure

An extended dialog box template begins with a **DLGTEMPLATEEX** header that describes the dialog box and specifies the number of controls in the dialog box. For each control in a dialog box, an extended dialog box template has a block of data that uses the [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) format to describe the control.

The **DLGTEMPLATEEX** structure is not defined in any standard header file. The structure definition is provided here to explain the format of an extended template for a dialog box.

## Syntax


```C++
typedef struct {
  WORD      dlgVer;
  WORD      signature;
  DWORD     helpID;
  DWORD     exStyle;
  DWORD     style;
  WORD      cDlgItems;
  short     x;
  short     y;
  short     cx;
  short     cy;
  sz_Or_Ord menu;
  sz_Or_Ord windowClass;
  WCHAR     title[titleLen];
  WORD      pointsize;
  WORD      weight;
  BYTE      italic;
  BYTE      charset;
  WCHAR     typeface[stringLen];
} DLGTEMPLATEEX;
```



## Members

<dl> <dt>

**dlgVer**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The version number of the extended dialog box template. This member must be set to 1.

</dd> <dt>

**signature**
</dt> <dd>

Type: **WORD**

</dd> <dd>

Indicates whether a template is an extended dialog box template. If **signature** is 0xFFFF, this is an extended dialog box template. In this case, the **dlgVer** member specifies the template version number. If **signature** is any value other than 0xFFFF, this is a standard dialog box template that uses the [**DLGTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgtemplate) and [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) structures.

</dd> <dt>

**helpID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The help context identifier for the dialog box window. When the system sends a [**WM\_HELP**](../shell/wm-help.md) message, it passes this value in the **wContextId** member of the [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure.

</dd> <dt>

**exStyle**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The extended windows styles. This member is not used when creating dialog boxes, but applications that use dialog box templates can use it to create other types of windows. For a list of values, see [**Extended Window Styles**](/windows/desktop/winmsg/extended-window-styles).

</dd> <dt>

**style**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The style of the dialog box. This member can be a combination of [window style values](/windows/desktop/winmsg/window-styles) and [dialog box style values](dialog-box-styles.md).

If **style** includes the **DS\_SETFONT** or **DS\_SHELLFONT** dialog box style, the **DLGTEMPLATEEX** header of the extended dialog box template contains four additional members ( **pointsize**, **weight**, **italic**, and **typeface**) that describe the font to use for the text in the client area and controls of the dialog box. If possible, the system creates a font according to the values specified in these members. Then the system sends a [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont) message to the dialog box and to each control to provide a handle to the font.

For more information, see [Dialog Box Fonts](about-dialog-boxes.md).

</dd> <dt>

**cDlgItems**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of controls in the dialog box.

</dd> <dt>

**x**
</dt> <dd>

Type: **short**

</dd> <dd>

The x-coordinate, in dialog box units, of the upper-left corner of the dialog box.

</dd> <dt>

**y**
</dt> <dd>

Type: **short**

</dd> <dd>

The y-coordinate, in dialog box units, of the upper-left corner of the dialog box.

</dd> <dt>

**cx**
</dt> <dd>

Type: **short**

</dd> <dd>

The width, in dialog box units, of the dialog box.

</dd> <dt>

**cy**
</dt> <dd>

Type: **short**

</dd> <dd>

The height, in dialog box units, of the dialog box.

</dd> <dt>

**menu**
</dt> <dd>

Type: **sz\_Or\_Ord**

</dd> <dd>

A variable-length array of 16-bit elements that identifies a menu resource for the dialog box. If the first element of this array is 0x0000, the dialog box has no menu and the array has no other elements. If the first element is 0xFFFF, the array has one additional element that specifies the ordinal value of a menu resource in an executable file. If the first element has any other value, the system treats the array as a null-terminated Unicode string that specifies the name of a menu resource in an executable file.

</dd> <dt>

**windowClass**
</dt> <dd>

Type: **sz\_Or\_Ord**

</dd> <dd>

A variable-length array of 16-bit elements that identifies the window class of the dialog box. If the first element of the array is 0x0000, the system uses the predefined dialog box class for the dialog box and the array has no other elements. If the first element is 0xFFFF, the array has one additional element that specifies the ordinal value of a predefined system window class. If the first element has any other value, the system treats the array as a null-terminated Unicode string that specifies the name of a registered window class.

</dd> <dt>

**title**
</dt> <dd>

Type: **WCHAR\[titleLen\]**

</dd> <dd>

The title of the dialog box. If the first element of this array is 0x0000, the dialog box has no title and the array has no other elements.

</dd> <dt>

**pointsize**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The point size of the font to use for the text in the dialog box and its controls.

This member is present only if the **style** member specifies **DS\_SETFONT** or **DS\_SHELLFONT**.

</dd> <dt>

**weight**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The weight of the font. Note that, although this can be any of the values listed for the **lfWeight** member of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure, any value that is used will be automatically changed to **FW\_NORMAL**.

This member is present only if the **style** member specifies **DS\_SETFONT** or **DS\_SHELLFONT**.

</dd> <dt>

**italic**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

Indicates whether the font is italic. If this value is **TRUE**, the font is italic.

This member is present only if the **style** member specifies **DS\_SETFONT** or **DS\_SHELLFONT**.

</dd> <dt>

**charset**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The character set to be used. For more information, see the **lfcharset** member of [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta).

This member is present only if the **style** member specifies **DS\_SETFONT** or **DS\_SHELLFONT**.

</dd> <dt>

**typeface**
</dt> <dd>

Type: **WCHAR\[stringLen\]**

</dd> <dd>

The name of the typeface for the font.

This member is present only if the **style** member specifies **DS\_SETFONT** or **DS\_SHELLFONT**.

</dd> </dl>

## Remarks

You can use an extended dialog box template instead of a standard dialog box template in the [**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama), [**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama), [**CreateDialogIndirect**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirecta), and [**DialogBoxIndirect**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirecta) functions.

Following the **DLGTEMPLATEEX** header in an extended dialog box template is one or more [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) structures that describe the controls of the dialog box. The **cDlgItems** member of the **DLGITEMTEMPLATEEX** structure specifies the number of **DLGITEMTEMPLATEEX** structures that follow in the template.

Each [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) structure in the template must be aligned on a **DWORD** boundary. If the **style** member specifies the **DS\_SETFONT** or **DS\_SHELLFONT** style, the first **DLGITEMTEMPLATEEX** structure begins on the first **DWORD** boundary after the **typeface** string. If these styles are not specified, the first structure begins on the first **DWORD** boundary after the **title** string.

The **menu**, **windowClass**, **title**, and **typeface** arrays must be aligned on **WORD** boundaries.

If you specify character strings in the **menu**, **windowClass**, **title**, and **typeface** arrays, you must use Unicode strings. Use the [**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar) function to generate these Unicode strings from ANSI strings.

The **x**, **y**, **cx**, and **cy** members specify values in dialog box units. You can convert these values to screen units (pixels) by using the [**MapDialogRect**](/windows/desktop/api/Winuser/nf-winuser-mapdialogrect) function.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CreateDialogIndirect**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirecta)
</dt> <dt>

[**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama)
</dt> <dt>

[**DialogBoxIndirect**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirecta)
</dt> <dt>

[**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama)
</dt> <dt>

[**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md)
</dt> <dt>

[**MapDialogRect**](/windows/desktop/api/Winuser/nf-winuser-mapdialogrect)
</dt> <dt>

[**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta)
</dt> <dt>

[**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar)
</dt> </dl>

 

