---
title: EN\_UPDATE notification code
description: Sent when an edit control is about to redraw itself.
ms.assetid: 59138736-6cc9-4a3f-95f3-ada9cbf253cb
keywords:
- EN_UPDATE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_UPDATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EN\_UPDATE notification code

Sent when an edit control is about to redraw itself. This notification code is sent after the control has formatted the text, but before it displays the text. This makes it possible to resize the edit control window, if necessary. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
EN_UPDATE

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the identifier of the edit control. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the edit control.

</dd> </dl>

## Remarks

**Rich Edit 1.0:** To receive EN\_UPDATE notification codes, specify [**ENM\_UPDATE**](https://www.bing.com/search?q=**ENM\_UPDATE**) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

**Rich Edit 2.0 and later:** The [**ENM\_UPDATE**](https://www.bing.com/search?q=**ENM\_UPDATE**) flag is ignored. The EN\_UPDATE notification code is always received. However, when Microsoft Rich Edit 3.0 emulates Microsoft Rich Edit 1.0, to receive EN\_UPDATE notification codes you must specify **ENM\_UPDATE** in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[EN\_CHANGE](en-change.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





