---
title: How to Implement Multiline Tooltips
description: Multiline tooltips allow text to be displayed on more than one line.
ms.assetid: 62B10B44-C1C2-4C86-8648-AE6B606BACBB
ms.topic: article
ms.date: 05/31/2018
---

# How to Implement Multiline Tooltips

Multiline tooltips allow text to be displayed on more than one line.

They are supported by [version 4.70](common-control-versions.md) and later of the common controls. Your application creates a multiline tooltip by sending a [**TTM\_SETMAXTIPWIDTH**](ttm-setmaxtipwidth.md) message, specifying the width of the display rectangle. Text that exceeds this width wraps to the next line rather than widening the display region. The rectangle height is increased as needed to accommodate the additional lines. The tooltip control wraps the lines automatically, or you can use a carriage return/line feed combination, \\r\\n, to force line breaks at particular locations.

The resulting display is shown in the following illustration.

![screen shot of a dialog box with a tooltip that contains text arranged like a multi-line paragraph](images/tt-multiline.png)

> [!Note]  
> The text buffer specified by the **szText** member of the [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa) structure can accommodate only 80 characters. If you need to use a longer string, point the **lpszText** member of **NMTTDISPINFO** to a buffer containing the desired text.

 

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Implement Multiline Tooltips

The following code fragment is an example of a simple [TTN\_GETDISPINFO](ttn-getdispinfo.md) notification handler. It enables a multiline tooltip by setting the display rectangle to 150 pixels. A manual line break is inserted after the first word to show that line breaks can be hard as well as soft.


```C++
    case WM_NOTIFY:
    {
        switch (((LPNMHDR)lParam)->code)
        {
        case TTN_GETDISPINFO:
            LPNMTTDISPINFO pInfo = (LPNMTTDISPINFO)lParam;
            SendMessage(pInfo->hdr.hwndFrom, TTM_SETMAXTIPWIDTH, 0, 150);
            wcscpy_s(pInfo->szText, ARRAYSIZE(pInfo->szText), 
                L"This\nis a very long text string " \
                L"that must be broken into several lines.");
            break;
        }
        break;
    }
```



## Related topics

<dl> <dt>

[Using Tooltip Controls](using-tooltip-contro.md)
</dt> </dl>

 

 




