---
title: How to Limit Slider Movement
description: As described in About Trackbar Controls, it is possible to set off part of the trackbar range as a selection range. One purpose of a selection range might be to limit movement of the slider, making some parts of the full range off limits.
ms.assetid: 9DD8BB11-EC6F-4695-BA56-5061F6EA5436
ms.topic: article
ms.date: 05/31/2018
---

# How to Limit Slider Movement

As described in [About Trackbar Controls](trackbar-controls.md), it is possible to set off part of the trackbar range as a selection range. One purpose of a selection range might be to limit movement of the slider, making some parts of the full range off limits.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Limit Slider Movement

The following example code limits movement of the slider by resetting the slider's position whenever it is moved outside the selection range.


```
case WM_HSCROLL:
    {
        HWND hTrackbar = GetDlgItem(hDlg, IDC_SLIDER1);
        
        if (hTrackbar == (HWND)lParam)
        {
            int newPos    = SendMessage(hTrackbar, TBM_GETPOS, 0, 0);
            int selStart  = SendMessage(hTrackbar, TBM_GETSELSTART, 0, 0);
            int selEnd    = SendMessage(hTrackbar, TBM_GETSELEND, 0, 0);
            
            if (newPos > selEnd)
            {
                SendMessage(hTrackbar, TBM_SETPOS, (WPARAM)TRUE, (LPARAM)selEnd);
            }
            
            else if (newPos < selStart)
            {
                SendMessage(hTrackbar, TBM_SETPOS, (WPARAM)TRUE, (LPARAM)selStart);
            }
        }
        
        break;
    }
```



## Remarks

This code snippet would be part of a dialog box's Window Procedure.

## Related topics

<dl> <dt>

[Using Trackbar Controls](using-trackbar-controls.md)
</dt> </dl>

 

 




