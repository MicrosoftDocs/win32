---
title: How to Display Tooltips for Buttons
description: When you specify the TBSTYLE\_TOOLTIPS style, the toolbar creates and manages a tooltip control. The tooltip control is hidden and appears only when users move the pointer over a toolbar button and leave it there for approximately one second.
ms.assetid: 0383DB63-A10E-4235-A974-AB21551E086B
ms.topic: article
ms.date: 05/31/2018
---

# How to Display Tooltips for Buttons

When you specify the [**TBSTYLE\_TOOLTIPS**](toolbar-control-and-button-styles.md) style, the toolbar creates and manages a tooltip control. The tooltip control is hidden and appears only when users move the pointer over a toolbar button and leave it there for approximately one second.

Your application can supply text to the tooltip control in any one of the following ways:

-   Set the tooltip text as the **iString** member of the [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure for each button. You must also send a [**TB\_SETMAXTEXTROWS**](tb-setmaxtextrows.md) message and set the maximum text rows to 0, so that the text does not appear as the button label rather than as a tooltip.
-   Create the toolbar with the [**TBSTYLE\_LIST**](toolbar-control-and-button-styles.md) style and then set the [**TBSTYLE\_EX\_MIXEDBUTTONS**](toolbar-extended-styles.md) extended style. Labels are shown only for buttons that have the [**BTNS\_SHOWTEXT**](toolbar-control-and-button-styles.md) style. For buttons that do not have this style, a tooltip is shown that contains the button text.
-   Respond to the [TTN\_GETDISPINFO](ttn-getdispinfo.md) notification code.
-   Respond to the [TBN\_GETINFOTIP](tbn-getinfotip.md) notification code.

An application that needs to send messages directly to the tooltip control can retrieve the handle to the control by using the [**TB\_GETTOOLTIPS**](tb-gettooltips.md) message. An application can replace the tooltip control of a toolbar with another tooltip control by using the [**TB\_SETTOOLTIPS**](tb-settooltips.md) message.

The most flexible way of supplying tooltip text is to respond to the [TTN\_GETDISPINFO](ttn-getdispinfo.md) or [TBN\_GETINFOTIP](tbn-getinfotip.md) notification code sent by the toolbar control to its parent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. For [TTN\_GETDISPINFO](ttn-getdispinfo.md), the *lParam* parameter includes a pointer to an [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa) structure (also defined as **LPTOOLTIPTEXT**) that specifies the command identifier of the button for which Help text is needed. This identifier is in the **NMTTDISPINFO.hdr.idFrom** member. An application can copy the Help text to the structure, specify the address of a string containing the Help text, or specify the instance handle and resource identifier of a string resource.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Display a Tooltip for a Button

The following example code handles the [TTN\_GETDISPINFO](ttn-getdispinfo.md) tooltip notification code by providing text from resource identifiers.


```C++
case WM_NOTIFY: 
            
    switch (((LPNMHDR) lParam)->code) 
    {
    
    case TTN_GETDISPINFO: 
        { 
            LPTOOLTIPTEXT lpttt = (LPTOOLTIPTEXT)lParam; 
            
            // Set the instance of the module that contains the resource.
            lpttt->hinst = g_hInst; 
            
            UINT_PTR idButton = lpttt->hdr.idFrom;
            
            switch (idButton) 
            { 
            case IDM_NEW: 
                lpttt->lpszText = MAKEINTRESOURCE(IDS_TIPS_NEW); 
                break; 
                
            case IDM_OPEN: 
                lpttt->lpszText = MAKEINTRESOURCE(IDS_TIPS_OPEN); 
                break; 
                
            case IDM_SAVE: 
                lpttt->lpszText = MAKEINTRESOURCE(IDS_TIPS_SAVE); 
                break; 
            } 
            
            break; 
        } 
    }
    return TRUE;
```



## Related topics

<dl> <dt>

[Using Toolbar Controls](using-toolbar-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




