---
title: Appendix F Object Identifier Values for OBJID_QUERYCLASSNAMEIDX
description: When OLEACC sends a WM\_GETOBJECT message with the lParam parameter set to OBJIDQUERYCLASSNAMEIDX, many standard USER or common controls (COMCTL) return one of the following values.
ms.assetid: 2a54973c-7dfa-49af-8fd0-925fafa256ad
ms.topic: article
ms.date: 05/31/2018
---

# Appendix F: Object Identifier Values for OBJID\_QUERYCLASSNAMEIDX

When OLEACC sends a [**WM\_GETOBJECT**](wm-getobject.md) message with the *lParam* parameter set to OBJIDQUERYCLASSNAMEIDX, many standard USER or common controls (COMCTL) return one of the following values.



| USER or common control | Return value |
|------------------------|--------------|
| Listbox                | 65536+0      |
| Button                 | 65536+2      |
| Static                 | 65536+3      |
| Edit                   | 65536+4      |
| Combobox               | 65536+5      |
| Scrollbar              | 65536+10     |
| Status                 | 65536+11     |
| Toolbar                | 65536+12     |
| Progress               | 65536+13     |
| Animate                | 65536+14     |
| Tab                    | 65536+15     |
| Hotkey                 | 65536+16     |
| Header                 | 65536+17     |
| Trackbar               | 65536+18     |
| Listview               | 65536+19     |
| Updown                 | 65536+22     |
| ToolTips               | 65536+24     |
| Treeview               | 65536+25     |
| RichEdit               | 65536+28     |



 

Only USER and Windows common controls (COMCTL) will return one of the values from the table. If a window returns 0 in response to this message, the window may be one of the following:

-   A custom control
-   A control other than one of the controls in the previous table
-   An old version of a system control that does not recognize the [**WM\_GETOBJECT**](wm-getobject.md) message

If a window returns 0, clients may need to use [**RealGetWindowClass**](/windows/win32/api/winuser/nf-winuser-realgetwindowclassw) or [**GetClassName**](/windows/win32/api/winuser/nf-winuser-getclassname). You can use these functions to determine the type of control based on class name.

In general, clients can use the information provided by OLEACC.

 

 