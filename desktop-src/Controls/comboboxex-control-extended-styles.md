---
title: ComboBoxEx Control Extended Styles (CommCtrl.h)
description: Support the extended styles that are listed in this section as well as most standard combo box control styles.
ms.assetid: 4741ac5e-1c46-4fd3-9174-b4ceb479261f
topic_type:
- apiref
api_name:
- CBES_EX_CASESENSITIVE
- CBES_EX_NOEDITIMAGE
- CBES_EX_NOEDITIMAGEINDENT
- CBES_EX_NOSIZELIMIT
- CBES_EX_PATHWORDBREAKPROC
- CBES_EX_TEXTENDELLIPSIS
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ComboBoxEx Control Extended Styles

Support the extended styles that are listed in this section as well as most standard combo box control styles.



| Constant                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CBES_EX_CASESENSITIVE"></span><span id="cbes_ex_casesensitive"></span><dl> <dt>**CBES\_EX\_CASESENSITIVE**</dt> </dl>             | **BSTR** searches in the list will be case sensitive. This includes searches as a result of text being typed in the edit box and the CB\_FINDSTRINGEXACT message.<br/>                                                                                                                                                          |
| <span id="CBES_EX_NOEDITIMAGE"></span><span id="cbes_ex_noeditimage"></span><dl> <dt>**CBES\_EX\_NOEDITIMAGE**</dt> </dl>                   | The edit box and the dropdown list will not display item images. <br/>                                                                                                                                                                                                                                                          |
| <span id="CBES_EX_NOEDITIMAGEINDENT"></span><span id="cbes_ex_noeditimageindent"></span><dl> <dt>**CBES\_EX\_NOEDITIMAGEINDENT**</dt> </dl> | The edit box and the dropdown list will not display item images. <br/>                                                                                                                                                                                                                                                          |
| <span id="CBES_EX_NOSIZELIMIT"></span><span id="cbes_ex_nosizelimit"></span><dl> <dt>**CBES\_EX\_NOSIZELIMIT**</dt> </dl>                   | Allows the ComboBoxEx control to be vertically sized smaller than its contained combo box control. If the ComboBoxEx is sized smaller than the combo box, the combo box will be clipped. <br/>                                                                                                                                  |
| <span id="CBES_EX_PATHWORDBREAKPROC"></span><span id="cbes_ex_pathwordbreakproc"></span><dl> <dt>**CBES\_EX\_PATHWORDBREAKPROC**</dt> </dl> | Windows NT only. The edit box will use the slash (/), backslash (\), and period (.) characters as word delimiters. This makes keyboard shortcuts for word-by-word cursor movement effective in path names and URLs.<br/>                                                                                                       |
| <span id="CBES_EX_TEXTENDELLIPSIS"></span><span id="cbes_ex_textendellipsis"></span><dl> <dt>**CBES\_EX\_TEXTENDELLIPSIS**</dt> </dl>       | **Windows Vista and later.** Causes items in the drop-down list and the edit box (when the edit box is read only) to be truncated with an ellipsis ("...") rather than just clipped by the edge of the control. This is useful when the control needs to be set to a fixed width, yet the entries in the list may be long.<br/> |



## Remarks

You set and retrieve the combobox extended styles by using [**CBEM\_SETEXTENDEDSTYLE**](cbem-setextendedstyle.md) and [**CBEM\_GETEXTENDEDSTYLE**](cbem-getextendedstyle.md) messages.

> [!Note]  
> If you try to set an extended style for a ComboBoxEx control created with the [**CBS\_SIMPLE**](combo-box-styles.md) style, it might not repaint properly. The **CBS\_SIMPLE** style also does not work properly with the CBES\_EX\_PATHWORDBREAKPROC extended style.

 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





