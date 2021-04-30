---
description: Sent to an application by the IME to notify the application of a key release and to keep message order. A window receives this message through its WindowProc function.
ms.assetid: 652f951f-4e9f-407c-844c-b250b6a9e6f5
title: WM_IME_KEYUP message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_KEYUP message

Sent to an application by the IME to notify the application of a key release and to keep message order. A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,       
  WM_IME_KEYUP,    
  WPARAM wParam,   
  LPARAM lParam    
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*wParam* 
</dt> <dd>

Virtual key code of the key.

</dd> <dt>

*lParam* 
</dt> <dd>

Repeat count, scan code, extended key flag, context code, previous key state flag, and transition state flag, as shown below.



| Bit   | Meaning                                                                     |
|-------|-----------------------------------------------------------------------------|
| 0-15  | Repeat count. This value is always 1.                                       |
| 16-23 | Scan code.                                                                  |
| 24    | Extended key. This value is 1 if it is an extended key. Otherwise, it is 0. |
| 25-28 | Not used.                                                                   |
| 29    | Context code. This value is always 0.                                       |
| 30    | Previous key state. This value is always 1.                                 |
| 31    | Transition state. This value is always 1.                                   |



 

</dd> </dl>

## Return value

An application should return 0 if it processes this message.

## Remarks

An application can process this message or pass it to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)  function to generate a matching [**WM\_KEYUP**](../inputdev/wm-keyup.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Messages](input-method-manager-messages.md)
</dt> </dl>

 

 
