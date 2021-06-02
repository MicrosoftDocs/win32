---
description: The WM\_PALETTEISCHANGING message informs applications that an application is going to realize its logical palette.
ms.assetid: 64ec1042-0ab5-496f-9a88-2f293b412704
title: WM_PALETTEISCHANGING message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PALETTEISCHANGING message

The **WM\_PALETTEISCHANGING** message informs applications that an application is going to realize its logical palette.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd, 
  UINT  uMsg, 
  WPARAM wParam, 
  LPARAM lParam     
);
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window that is going to realize its logical palette.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

The application changing its palette does not wait for acknowledgment of this message before changing the palette and sending the [**WM\_PALETTECHANGED**](wm-palettechanged.md) message. As a result, the palette may already be changed by the time an application receives this message.

If the application either ignores or fails to process this message and a second application realizes its palette while the first is using palette indexes, there is a strong possibility that the user will see unexpected colors during subsequent drawing operations.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Colors Overview](colors.md)
</dt> <dt>

[Color Messages](color-messages.md)
</dt> <dt>

[**WM\_PALETTECHANGED**](wm-palettechanged.md)
</dt> <dt>

[**WM\_QUERYNEWPALETTE**](wm-querynewpalette.md)
</dt> </dl>

 

 
