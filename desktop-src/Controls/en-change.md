---
title: EN_CHANGE notification code
description: Sent when the user has taken an action that may have altered text in an edit control.
ms.assetid: 8a04e6fb-ae9d-4d94-8047-6de96df899f5
keywords:
- EN_CHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_CHANGE
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

# EN\_CHANGE notification code

Sent when the user has taken an action that may have altered text in an edit control. Unlike the [EN\_UPDATE](en-update.md) notification code, this notification code is sent after the system updates the screen. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
EN_CHANGE

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

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. To receive EN\_CHANGE notification codes, specify [**ENM\_CHANGE**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

The EN\_CHANGE notification code is not sent when the [**ES\_MULTILINE**](edit-control-styles.md) style is used and the text is sent through [**WM\_SETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632644).

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

[EN\_UPDATE](en-update.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





