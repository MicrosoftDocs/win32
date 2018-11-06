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
ms.date: 05/31/2018
---

# The OnPaint Method

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

 

 




