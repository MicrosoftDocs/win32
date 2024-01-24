---
title: EM_SETCUEBANNER message (Commctrl.h)
description: Sets the textual cue, or tip, that is displayed by the edit control to prompt the user for information.
ms.assetid: 1b1ff5e7-e0b8-40c1-8b7e-7003e9ef959b
keywords:
- EM_SETCUEBANNER message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETCUEBANNER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETCUEBANNER message

Sets the textual cue, or tip, that is displayed by the edit control to prompt the user for information.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

**TRUE** if the cue banner should show even when the edit control has focus; otherwise, **FALSE**. **FALSE** is the default behavior the cue banner disappears when the user clicks in the control.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to a Unicode string that contains the text to display as the textual cue.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

An edit control that is used to begin a search may display "Enter search here" in gray text as a textual cue. When the user clicks the text, the text goes away and the user can type.

You cannot set a cue banner on a multiline edit control or on a rich edit control.

> [!Note]  
> To use this API, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**Edit\_SetCueBannerText**](/windows/desktop/api/Commctrl/nf-commctrl-edit_setcuebannertext)
</dt> </dl>

 

 





