---
title: TDM_SET_ELEMENT_TEXT message (Commctrl.h)
description: TDM_SET_ELEMENT_TEXT message - Updates a text element in a task dialog.
ms.assetid: e3f15805-5d48-4549-9959-69ec01345e57
keywords:
- TDM_SET_ELEMENT_TEXT message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_ELEMENT_TEXT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_SET\_ELEMENT\_TEXT message

Updates a text element in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Indicates the element to update. (For an illustration, see [About Task Dialogs](task-dialogs-overview.md).) This parameter must be one of the following values.



| Value                                                                                                                                                                                           | Meaning                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="TDE_CONTENT"></span><span id="tde_content"></span><dl> <dt>**TDE\_CONTENT**</dt> </dl>                                         | Content.<br/>              |
| <span id="TDE_EXPANDED_INFORMATION"></span><span id="tde_expanded_information"></span><dl> <dt>**TDE\_EXPANDED\_INFORMATION**</dt> </dl> | Expanded information.<br/> |
| <span id="TDE_FOOTER"></span><span id="tde_footer"></span><dl> <dt>**TDE\_FOOTER**</dt> </dl>                                            | Footer text.<br/>          |
| <span id="TDE_MAIN_INSTRUCTION"></span><span id="tde_main_instruction"></span><dl> <dt>**TDE\_MAIN\_INSTRUCTION**</dt> </dl>             | Main instruction.<br/>     |



 

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The new text to use.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

The size or layout of the task dialog may change to accommodate the new text.

## Examples

The following example code shows how to set the footer text in the task dialog represented by *hwnd*.


```C++
SendMessage(hwnd, TDM_SET_ELEMENT_TEXT, (WPARAM)TDE_FOOTER, (LPARAM)L"New footer text.");
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TDM\_UPDATE\_ELEMENT\_TEXT**](tdm-update-element-text.md)
</dt> </dl>

 

 





