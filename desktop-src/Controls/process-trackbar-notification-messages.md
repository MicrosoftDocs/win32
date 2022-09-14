---
title: How to Process Trackbar Notification Messages
description: Trackbars notify their parent window of user actions by sending the parent a WM\_HSCROLL or WM\_VSCROLL message.
ms.assetid: 83F47A3E-E607-49C2-A8B5-BC8A321D90BB
ms.topic: article
ms.date: 05/31/2018
---

# How to Process Trackbar Notification Messages

Trackbars notify their parent window of user actions by sending the parent a [**WM\_HSCROLL**](wm-hscroll.md) or [**WM\_VSCROLL**](wm-vscroll.md) message.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Process Trackbar Notification Messages

The following code example is a function that is called when the trackbar's parent window receives a [**WM\_HSCROLL**](wm-hscroll.md) message. The trackbar in this example has the [**TBS\_ENABLESELRANGE**](trackbar-control-styles.md) style. The position of the slider is compared to the selection range, and the slider is moved to the starting or ending position of the selection range when necessary.


```
// TBNotifications - handles trackbar notifications received 
// in the wParam parameter of WM_HSCROLL. This function simply 
// ensures that the slider remains within the selection range. 

VOID WINAPI TBNotifications( 
    WPARAM wParam,  // wParam of WM_HSCROLL message 
    HWND hwndTrack, // handle of trackbar window 
    UINT iSelMin,   // minimum value of trackbar selection 
    UINT iSelMax)   // maximum value of trackbar selection 
    { 
    DWORD dwPos;    // current position of slider 

    switch (LOWORD(wParam)) { 
    
        case TB_ENDTRACK:
          
            dwPos = SendMessage(hwndTrack, TBM_GETPOS, 0, 0); 
            
            if (dwPos > iSelMax) 
                SendMessage(hwndTrack, TBM_SETPOS, 
                    (WPARAM) TRUE,       // redraw flag 
                    (LPARAM) iSelMax); 
                    
            else if (dwPos < iSelMin) 
                SendMessage(hwndTrack, TBM_SETPOS, 
                    (WPARAM) TRUE,       // redraw flag 
                    (LPARAM) iSelMin); 
            
            break; 

        default: 
        
            break; 
        } 
} 
```



## Remarks

A dialog box that contains a [**TBS\_VERT**](trackbar-control-styles.md) style trackbar can use this function when it receives a [**WM\_VSCROLL**](wm-vscroll.md) message.

## Related topics

<dl> <dt>

[Using Trackbar Controls](using-trackbar-controls.md)
</dt> </dl>

 

 




