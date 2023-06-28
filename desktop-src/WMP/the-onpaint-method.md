---
title: The OnPaint Method
description: The OnPaint Method
ms.assetid: 4b335362-4430-4b05-8aea-7de8df9cc91f
keywords:
- Windows Media Player plug-ins,OnPaint method
- plug-ins,OnPaint method
- user interface plug-ins,OnPaint method
- UI plug-ins,OnPaint method
- OnPaint method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The OnPaint Method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The OnPaint method is called whenever the plug-in window should paint itself. This occurs when the plug-in window receives a WM\_PAINT message, which is mapped to the OnPaint method in the message map described earlier. The wizard provides an implementation of this method that paints the background black and places the name of the plug-in in the plug-in window. The only modification that is necessary for the Search UI plug-in is the removal of the code that displays the text.

The following code is used to implement this method:


```C++
LRESULT OnPaint(UINT nMsg, WPARAM wParam, 
                         LPARAM lParam, BOOL& bHandled)
{
    PAINTSTRUCT ps;

    HDC hDC = BeginPaint(&ps);

    RECT rc;
    GetClientRect(&rc);

    HBRUSH hNewBrush = ::CreateSolidBrush( RGB(0, 0, 0) );

    if (hNewBrush)
    {
        ::FillRect(hDC, &rc, hNewBrush );
        ::DeleteObject( hNewBrush );
    }

    EndPaint(&ps);
    return 0;
}

```



## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




