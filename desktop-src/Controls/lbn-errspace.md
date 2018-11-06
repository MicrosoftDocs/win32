---
title: LBN_ERRSPACE notification code
description: Notifies the application that the list box cannot allocate enough memory to meet a specific request. The parent window of the list box receives this notification code through the WM\_COMMAND message.
ms.assetid: ff716ad0-cbd8-4ac3-bcaf-d5be81355eaa
keywords:
- LBN_ERRSPACE notification code Windows Controls
topic_type:
- apiref
api_name:
- LBN_ERRSPACE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# LBN\_ERRSPACE notification code

Notifies the application that the list box cannot allocate enough memory to meet a specific request. The parent window of the list box receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
LBN_ERRSPACE

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the identifier of the list box. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the list box.

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

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





