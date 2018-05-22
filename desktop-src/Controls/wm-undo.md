---
title: WM\_UNDO message
description: An application sends a WM\_UNDO message to an edit control to undo the last operation. When this message is sent to an edit control, the previously deleted text is restored or the previously added text is deleted.
ms.assetid: 'bb5a3425-bf99-4a08-8747-82c24c5889ad'
keywords: ["WM_UNDO message Windows Controls"]
topic_type:
- apiref
api_name:
- WM_UNDO
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_UNDO message

An application sends a **WM\_UNDO** message to an edit control to undo the last operation. When this message is sent to an edit control, the previously deleted text is restored or the previously added text is deleted.

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

If the message succeeds, the return value is **TRUE**.

If the message fails, the return value is **FALSE**.

## Remarks

**Rich Edit:** It is recommended that [**EM\_UNDO**](em-undo.md) be used instead of **WM\_UNDO**.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**WM\_CLEAR**](https://msdn.microsoft.com/library/windows/desktop/ms649020)
</dt> <dt>

[**WM\_COPY**](https://msdn.microsoft.com/library/windows/desktop/ms649022)
</dt> <dt>

[**WM\_CUT**](https://msdn.microsoft.com/library/windows/desktop/ms649023)
</dt> <dt>

[**WM\_PASTE**](https://msdn.microsoft.com/library/windows/desktop/ms649028)
</dt> </dl>

 

 





