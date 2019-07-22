---
title: CBN_ERRSPACE notification code
description: Sent when a combo box cannot allocate enough memory to meet a specific request. The parent window of the combo box receives this notification code through the WM\_COMMAND message.
ms.assetid: c1c19c40-fc88-47d0-9676-7a267a48ae98
keywords:
- CBN_ERRSPACE notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_ERRSPACE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# CBN\_ERRSPACE notification code

Sent when a combo box cannot allocate enough memory to meet a specific request. The parent window of the combo box receives this notification code through the [**WM\_COMMAND**](https://docs.microsoft.com/windows/desktop/menurc/wm-command) message.


```C++
CBN_ERRSPACE

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the control identifier of the combo box. The [**HIWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the combo box.

</dd> </dl>

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**WM\_COMMAND**](https://docs.microsoft.com/windows/desktop/menurc/wm-command)
</dt> </dl>

 

 





