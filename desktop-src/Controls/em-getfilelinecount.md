---
title: EM_GETFILELINECOUNT message (CommCtrl.h)
description: Gets the number of lines in a multiline edit control, independently of how lines are displayed on the screen.
ms.assetid: 9fe63c10-7395-4f98-a672-14960a70d14f
keywords:
- EM_GETFILELINECOUNT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETFILELINECOUNT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM_GETFILELINECOUNT message (CommCtrl.h)

Gets the number of lines in a multiline edit control, independently of how lines are displayed on the screen.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is an integer specifying the total number of text lines in the multiline edit control, independently of how lines are displayed on the screen. If the control has no text, the return value is 1. The return value will never be less than 1.

## Remarks

The **EM\_GETFILELINECOUNT** message retrieves the total number of text lines, independently of how lines are displayed on the screen, not just the number of lines that are currently visible.

Word-wrap does not change the number of lines this message returns, as this message works independently of how lines are displayed on the screen.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETFILELINE**](em-getfileline.md)
</dt> <dt>

[**EM\_FILELINELENGTH**](em-filelinelength.md)
</dt> <dt>

[**Edit\_GetFileLineCount**](/windows/win32/api/commctrl/nf-commctrl-edit_getfilelinecount)
</dt> </dl>

 

 





