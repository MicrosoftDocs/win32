---
title: LVM_SETCOLUMNWIDTH message (Commctrl.h)
description: Changes the width of a column in report-view mode or the width of all columns in list-view mode. You can send this message explicitly or use the ListView\_SetColumnWidth macro.
ms.assetid: 309aebfb-9fed-4c77-acbb-ea905b32b0e2
keywords:
- LVM_SETCOLUMNWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETCOLUMNWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETCOLUMNWIDTH message

Changes the width of a column in report-view mode or the width of all columns in list-view mode. You can send this message explicitly or use the [**ListView\_SetColumnWidth**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setcolumnwidth) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of a valid column. For list-view mode, this parameter must be set to zero.

</dd> <dt>

*lParam* 
</dt> <dd>

New width of the column, in pixels. For report-view mode, the following special values are supported:



| Value                                                                                                                                                                                           | Meaning                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LVSCW_AUTOSIZE"></span><span id="lvscw_autosize"></span><dl> <dt>**LVSCW\_AUTOSIZE**</dt> </dl>                                | Automatically sizes the column.<br/>                                                                                                                                           |
| <span id="LVSCW_AUTOSIZE_USEHEADER"></span><span id="lvscw_autosize_useheader"></span><dl> <dt>**LVSCW\_AUTOSIZE\_USEHEADER**</dt> </dl> | Automatically sizes the column to fit the header text. If you use this value with the last column, its width is set to fill the remaining width of the list-view control.<br/> |



 

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

Assume that you have a 2-column list-view control with a width of 500 pixels. If the width of column zero is set to 200 pixels, and you send this message with *wParam* = 1 and *lParam* = LVSCW\_AUTOSIZE\_USEHEADER, the second (and last) column will be 300 pixels wide.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





