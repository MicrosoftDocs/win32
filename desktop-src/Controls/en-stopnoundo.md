---
title: EN\_STOPNOUNDO notification code
description: Notifies a rich edit controls parent window that an action occurred for which the control cannot allocate enough memory to maintain the undo state. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 5608f6dd-83dc-4712-b485-dd9bc17dea24
keywords:
- EN_STOPNOUNDO notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_STOPNOUNDO
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EN\_STOPNOUNDO notification code

Notifies a rich edit control's parent window that an action occurred for which the control cannot allocate enough memory to maintain the undo state. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_STOPNOUNDO

    lpnmhdr = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure.

</dd> </dl>

## Return value

Return zero to continue the **Undo** operation.

Return a nonzero value to stop the **Undo** operation.

## Remarks

The parent window will always get a [**WM\_NOTIFY**](wm-notify.md) message for this event, it does not require a notification mask sent with [**EM\_SETEVENTMASK**](em-seteventmask.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





