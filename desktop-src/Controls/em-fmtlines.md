---
title: EM_FMTLINES message (Winuser.h)
description: Sets a flag that determines whether a multiline edit control includes soft line-break characters. A soft line break consists of two carriage returns and a line feed and is inserted at the end of a line that is broken because of wordwrapping.
ms.assetid: bfc08062-b0a7-4ba7-8858-00cb20895c77
keywords:
- EM_FMTLINES message Windows Controls
topic_type:
- apiref
api_name:
- EM_FMTLINES
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FMTLINES message

Sets a flag that determines whether a multiline edit control includes soft line-break characters. A soft line break consists of two carriage returns and a line feed and is inserted at the end of a line that is broken because of wordwrapping.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether soft line-break characters are to be inserted. A value of **TRUE** inserts the characters; a value of **FALSE** removes them.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is identical to the *wParam* parameter.

## Remarks

This message affects only the buffer returned by the [**EM\_GETHANDLE**](em-gethandle.md) message and the text returned by the [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext) message. It has no effect on the display of the text within the edit control.

The **EM\_FMTLINES** message does not affect a line that ends with a hard line break. A hard line break consists of one carriage return and a line feed.

> [!Note]  
> The size of the text changes when this message is processed.

 

**Rich Edit:** The **EM\_FMTLINES** message is not supported.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETHANDLE**](em-gethandle.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)
</dt> </dl>

 

