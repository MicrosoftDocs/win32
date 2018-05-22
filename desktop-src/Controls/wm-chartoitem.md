---
title: WM\_CHARTOITEM message
description: Sent by a list box with the LBS\_WANTKEYBOARDINPUT style to its owner in response to a WM\_CHAR message.
ms.assetid: 'f941c00b-b836-4f1b-b8cf-8ac2b0704af3'
keywords: ["WM_CHARTOITEM message Windows Controls"]
topic_type:
- apiref
api_name:
- WM_CHARTOITEM
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_CHARTOITEM message

Sent by a list box with the [**LBS\_WANTKEYBOARDINPUT**](list-box-styles.md#lbs-wantkeyboardinput) style to its owner in response to a [**WM\_CHAR**](https://msdn.microsoft.com/library/windows/desktop/ms646276) message.


```C++
WM_CHARTOITEM

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the character code of the key the user pressed. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the current position of the caret.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the list box.

</dd> </dl>

## Return value

The return value specifies the action that the application performed in response to the message. A return value of –1 or –2 indicates that the application handled all aspects of selecting the item and requires no further action by the list box. A return value of 0 or greater specifies the zero-based index of an item in the list box and indicates that the list box should perform the default action for the keystroke on the specified item.

## Remarks

The [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function returns –1.

Only owner-drawn list boxes that do not have the [**LBS\_HASSTRINGS**](list-box-styles.md#lbs-hasstrings) style can receive this message.

If a dialog box procedure handles this message, it should cast the desired return value to a **BOOL** and return the value directly. The *DWL\_MSGRESULT* value set by the [**SetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633591) function is ignored.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WM\_VKEYTOITEM**](wm-vkeytoitem.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_CHAR**](https://msdn.microsoft.com/library/windows/desktop/ms646276)
</dt> </dl>

 

 





