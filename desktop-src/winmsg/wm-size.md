---
Description: Sent to a window after its size has changed.
ms.assetid: e3e14dcd-9236-48bd-a692-6985d8146f81
title: WM_SIZE message (Winuser.h)
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# WM\_SIZE message

Sent to a window after its size has changed.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca) function.


```C++
#define WM_SIZE                         0x0005
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of resizing requested. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="SIZE_MAXHIDE"></span><span id="size_maxhide"></span><dl> <dt>**SIZE\_MAXHIDE**</dt> <dt>4</dt> </dl>       | Message is sent to all pop-up windows when some other window is maximized.<br/>                              |
| <span id="SIZE_MAXIMIZED"></span><span id="size_maximized"></span><dl> <dt>**SIZE\_MAXIMIZED**</dt> <dt>2</dt> </dl> | The window has been maximized.<br/>                                                                          |
| <span id="SIZE_MAXSHOW"></span><span id="size_maxshow"></span><dl> <dt>**SIZE\_MAXSHOW**</dt> <dt>3</dt> </dl>       | Message is sent to all pop-up windows when some other window has been restored to its former size.<br/>      |
| <span id="SIZE_MINIMIZED"></span><span id="size_minimized"></span><dl> <dt>**SIZE\_MINIMIZED**</dt> <dt>1</dt> </dl> | The window has been minimized.<br/>                                                                          |
| <span id="SIZE_RESTORED"></span><span id="size_restored"></span><dl> <dt>**SIZE\_RESTORED**</dt> <dt>0</dt> </dl>    | The window has been resized, but neither the **SIZE\_MINIMIZED** nor **SIZE\_MAXIMIZED** value applies.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies the new width of the client area.

The high-order word of *lParam* specifies the new height of the client area.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Example

```cpp
/******************************************************************
*                                                                 *
*  SimpleText::OnResize                                           *
*                                                                 *
*  If the application receives a WM_SIZE message, this method     *
*  resize the render target appropriately.                        *
*                                                                 *
******************************************************************/

void SimpleText::OnResize(UINT width, UINT height)
{
    if (pRT_)
    {
        D2D1_SIZE_U size;
        size.width = width;
        size.height = height;
        pRT_->Resize(size);
    }
}

LRESULT CALLBACK SimpleText::WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
   
    SimpleText *pSimpleText = reinterpret_cast<SimpleText *>(
                ::GetWindowLongPtr(hwnd, GWLP_USERDATA));

    if (pSimpleText)
    {
        switch(message)
        {
        case WM_SIZE:
            {
                UINT width = LOWORD(lParam);
                UINT height = HIWORD(lParam);
                pSimpleText->OnResize(width, height);
            }
            return 0;

// ...

```

Example from [Windows classic samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/multimedia/DirectWrite/HelloWorld/SimpleText.cpp) on GitHub.

## Remarks

If the [**SetScrollPos**](https://msdn.microsoft.com/library/Cc411085(v=MSDN.10).aspx) or [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow) function is called for a child window as a result of the **WM\_SIZE** message, the *bRedraw* or *bRepaint* parameter should be nonzero to cause the window to be repainted.

Although the width and height of a window are 32-bit values, the *lParam* parameter contains only the low-order 16 bits of each.

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function
sends the **WM\_SIZE** and **WM\_MOVE** messages when it processes
the [**WM\_WINDOWPOSCHANGED**](wm-windowposchanged.md) message.
The **WM\_SIZE** and **WM\_MOVE** messages are not sent if an application handles
the **WM\_WINDOWPOSCHANGED** message without calling **DefWindowProc**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow)
</dt> <dt>

[**WM\_WINDOWPOSCHANGED**](wm-windowposchanged.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**SetScrollPos**](https://msdn.microsoft.com/library/Cc411085(v=MSDN.10).aspx)
</dt> </dl>

 

 
