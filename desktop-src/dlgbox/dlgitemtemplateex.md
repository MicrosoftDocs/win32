---
title: DLGITEMTEMPLATEEX structure
description: A block of text used by an extended dialog box template to describe the extended dialog box. For a description of the format of an extended dialog box template, see DLGTEMPLATEEX.
ms.assetid: c60fd8db-ee4b-433b-a2fb-68b9a677bac8
keywords:
- DLGITEMTEMPLATEEX structure Dialog Boxes
topic_type:
- apiref
api_name:
- DLGITEMTEMPLATEEX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DLGITEMTEMPLATEEX structure

A block of text used by an extended dialog box template to describe the extended dialog box. For a description of the format of an extended dialog box template, see [**DLGTEMPLATEEX**](dlgtemplateex.md).

## Syntax


```C++
typedef struct {
  DWORD     helpID;
  DWORD     exStyle;
  DWORD     style;
  short     x;
  short     y;
  short     cx;
  short     cy;
  DWORD     id;
  sz_Or_Ord windowClass;
  sz_Or_Ord title;
  WORD      extraCount;
} DLGITEMTEMPLATEEX;
```



## Members

<dl> <dt>

**helpID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The help context identifier for the control. When the system sends a [**WM\_HELP**](../shell/wm-help.md) message, it passes the **helpID** value in the **dwContextId** member of the [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure.

</dd> <dt>

**exStyle**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The extended styles for a window. This member is not used to create controls in dialog boxes, but applications that use dialog box templates can use it to create other types of windows. For a list of values, see [**Extended Window Styles**](/windows/desktop/winmsg/extended-window-styles).

</dd> <dt>

**style**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The style of the control. This member can be a combination of [window style values](/windows/desktop/winmsg/window-styles) (such as **WS\_BORDER**) and one or more of the [control style values](/windows/desktop/Controls/common-control-styles) (such as **BS\_PUSHBUTTON** and **ES\_LEFT**).

</dd> <dt>

**x**
</dt> <dd>

Type: **short**

</dd> <dd>

The x-coordinate, in dialog box units, of the upper-left corner of the control. This coordinate is always relative to the upper-left corner of the dialog box's client area.

</dd> <dt>

**y**
</dt> <dd>

Type: **short**

</dd> <dd>

The y-coordinate, in dialog box units, of the upper-left corner of the control. This coordinate is always relative to the upper-left corner of the dialog box's client area.

</dd> <dt>

**cx**
</dt> <dd>

Type: **short**

</dd> <dd>

The width, in dialog box units, of the control.

</dd> <dt>

**cy**
</dt> <dd>

Type: **short**

</dd> <dd>

The height, in dialog box units, of the control.

</dd> <dt>

**id**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The control identifier.

</dd> <dt>

**windowClass**
</dt> <dd>

Type: **sz\_Or\_Ord**

</dd> <dd>

A variable-length array of 16-bit elements that specifies the window class of the control. If the first element of this array is any value other than 0xFFFF, the system treats the array as a null-terminated Unicode string that specifies the name of a registered window class.

If the first element is 0xFFFF, the array has one additional element that specifies the ordinal value of a predefined system class. The ordinal can be one of the following atom values.



| Value                                                                             | Meaning               |
|-----------------------------------------------------------------------------------|-----------------------|
| <dl> <dt>0x0080</dt> </dl> | Button<br/>     |
| <dl> <dt>0x0081</dt> </dl> | Edit<br/>       |
| <dl> <dt>0x0082</dt> </dl> | Static<br/>     |
| <dl> <dt>0x0083</dt> </dl> | List box<br/>   |
| <dl> <dt>0x0084</dt> </dl> | Scroll bar<br/> |
| <dl> <dt>0x0085</dt> </dl> | Combo box<br/>  |



 

</dd> <dt>

**title**
</dt> <dd>

Type: **sz\_Or\_Ord**

</dd> <dd>

A variable-length array of 16-bit elements that contains the initial text or resource identifier of the control. If the first element of this array is 0xFFFF, the array has one additional element that specifies the ordinal value of a resource, such as an icon, in an executable file. You can use a resource identifier for controls, such as static icon controls, that load and display an icon or other resource rather than text. If the first element is any value other than 0xFFFF, the system treats the array as a null-terminated Unicode string that specifies the initial text.

</dd> <dt>

**extraCount**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of bytes of creation data that follow this member. If this value is greater than zero, the creation data begins at the next **WORD** boundary. This creation data can be of any size and format. The control's window procedure must be able to interpret the data. When the system creates the control, it passes a pointer to this data in the *lParam* parameter of the [**WM\_CREATE**](/windows/desktop/winmsg/wm-create) message that it sends to the control.

</dd> </dl>

## Remarks

An extended template for a dialog box consists of a [**DLGTEMPLATEEX**](dlgtemplateex.md) header followed by a **DLGITEMTEMPLATEEX** structure for each control in the dialog box.

Each **DLGITEMTEMPLATEEX** structure must be aligned on a **DWORD** boundary. The variable-length **windowClass** and **title** arrays must be aligned on **WORD** boundaries. The creation data array, if any, must be aligned on a **WORD** boundary.

If you specify character strings in the **windowClass** and **title** arrays, you must use Unicode strings. Use the [**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar) function to generate Unicode strings from ANSI strings.

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

[**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa)
</dt> <dt>

[**DialogBoxIndirect**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirecta)
</dt> <dt>

[**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama)
</dt> <dt>

[**DLGTEMPLATEEX**](dlgtemplateex.md)
</dt> <dt>

[**MapDialogRect**](/windows/desktop/api/Winuser/nf-winuser-mapdialogrect)
</dt> <dt>

[**WM\_CREATE**](/windows/desktop/winmsg/wm-create)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar)
</dt> <dt>

[**WM\_HELP**](../shell/wm-help.md)
</dt> </dl>

 

