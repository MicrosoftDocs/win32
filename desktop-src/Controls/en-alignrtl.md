---
title: EN_ALIGNRTL notification code (Richedit.h)
description: Notifies a rich edit control's parent window that the paragraph direction changed to right-to-left. A rich edit control sends this notification code in the form of a WM\_COMMAND message.
ms.assetid: 2db5fd49-9ecd-49d7-8199-1706648255ca
keywords:
- EN_ALIGNRTL notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_ALIGNRTL
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_ALIGNRTL notification code

Notifies a rich edit control's parent window that the paragraph direction changed to right-to-left. A rich edit control sends this notification code in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
EN_ALIGNRTL

    WPARAM wParam
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](../winmsg/loword.md) contains the identifier of the rich edit control. The [**HIWORD**](../winmsg/hiword.md) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the rich edit control.

</dd> </dl>

## Return value

This notification code does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EN\_ALIGNLTR**](en-alignltr.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](../winmsg/hiword.md)
</dt> <dt>

[**LOWORD**](../winmsg/loword.md)
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

