---
title: TDM_UPDATE_ELEMENT_TEXT message (Commctrl.h)
description: TDM_UPDATE_ELEMENT_TEXT message - Updates a text element in a task dialog.
ms.assetid: 2df446c8-db87-42b5-b5bd-40fadbf9d45b
keywords:
- TDM_UPDATE_ELEMENT_TEXT message Windows Controls
topic_type:
- apiref
api_name:
- TDM_UPDATE_ELEMENT_TEXT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_UPDATE\_ELEMENT\_TEXT message

Updates a text element in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Indicates the element to update. (For an illustration of the elements, see [About Task Dialogs](task-dialogs-overview.md).) This parameter must be one of the following values:



| Value                                                                                                                                                                                           | Meaning                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="TDE_CONTENT"></span><span id="tde_content"></span><dl> <dt>**TDE\_CONTENT**</dt> </dl>                                         | Content.<br/>              |
| <span id="TDE_EXPANDED_INFORMATION"></span><span id="tde_expanded_information"></span><dl> <dt>**TDE\_EXPANDED\_INFORMATION**</dt> </dl> | Expanded information.<br/> |
| <span id="TDE_FOOTER"></span><span id="tde_footer"></span><dl> <dt>**TDE\_FOOTER**</dt> </dl>                                            | Footer text.<br/>          |
| <span id="TDE_MAIN_INSTRUCTION"></span><span id="tde_main_instruction"></span><dl> <dt>**TDE\_MAIN\_INSTRUCTION**</dt> </dl>             | Main instruction.<br/>     |



 

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Pointer to a Unicode string that contains the new text.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

To avoid clipping, the new text must be no longer than the existing text. Setting the text to a shorter string does not cause the dialog box to resize.

If the **pszExpandedInformation** member of the [**TASKDIALOGCONFIG**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialogconfig) structure used to create the task dialog was **NULL**, and you send a **TDM\_UPDATE\_ELEMENT\_TEXT** message with TDE\_EXPANDED\_INFORMATION, nothing will happen.

The above also applies to the footer and TDE\_FOOTER.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TDM\_SET\_ELEMENT\_TEXT**](tdm-set-element-text.md)
</dt> </dl>

 

 





