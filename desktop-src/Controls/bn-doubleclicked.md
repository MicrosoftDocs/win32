---
title: BN\_DOUBLECLICKED notification code
description: Sent when the user double-clicks a button.
ms.assetid: 2fd7363a-5a02-453c-bfab-df5cbf8e42a5
keywords:
- BN_DOUBLECLICKED notification code Windows Controls
topic_type:
- apiref
api_name:
- BN_DOUBLECLICKED
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

# BN\_DOUBLECLICKED notification code

Sent when the user double-clicks a button. This notification code is sent automatically for [**BS\_USERBUTTON**](https://www.bing.com/search?q=**BS\_USERBUTTON**), [**BS\_RADIOBUTTON**](https://www.bing.com/search?q=**BS\_RADIOBUTTON**), and [**BS\_OWNERDRAW**](https://www.bing.com/search?q=**BS\_OWNERDRAW**) buttons. Other button types send BN\_DOUBLECLICKED only if they have the [**BS\_NOTIFY**](https://www.bing.com/search?q=**BS\_NOTIFY**) style.

The parent window of the button receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
BN_DOUBLECLICKED

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the button's control identifier. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the button.

</dd> </dl>

## Remarks

BN\_DOUBLECLICKED is the same as the [BN\_DBLCLK](bn-dblclk.md) notification code.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





