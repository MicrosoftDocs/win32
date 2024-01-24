---
title: How to Process ComboBoxEx Notifications
description: This topic demonstrates how to process ComboBoxEx notification messages.
ms.assetid: 375634BC-CDD6-4D72-A41E-FCBFCBFE7F03
ms.topic: article
ms.date: 05/31/2018
---

# How to Process ComboBoxEx Notifications

This topic demonstrates how to process ComboBoxEx notification messages.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


A ComboBoxEx control notifies its parent window of events by sending [**WM\_NOTIFY**](wm-notify.md) messages. It also passes the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) notification messages that it receives from the combo box contained within it to the parent window to be processed. Therefore, your application must be prepared to process **WM\_NOTIFY** messages from the ComboBoxEx and **WM\_COMMAND** messages that are forwarded from the ComboBoxEx child combo box control.

The example in this section handles the [**WM\_NOTIFY**](wm-notify.md) and [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages from a ComboBoxEx control by calling a corresponding application-defined function to process these messages.

## Complete example


```C++
LRESULT CALLBACK WndProc (HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch(msg){

        case WM_COMMAND: // notification from the child ComboBox within the ComboBoxEx control.
            if((HWND)lParam == g_hwndCB)
                DoOldNotify(hwnd,  wParam);  
            break;

        case WM_NOTIFY: // notification from the ComboBoxEx control
            return (DoCBEXNotify(hwnd, lParam));

        case WM_PAINT:
            hdc = BeginPaint(hwnd, &ps);
            EndPaint(hwnd, &ps);
            break;

        case WM_DESTROY:
            PostQuitMessage(0);
            break;

        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
            break;
    }

    return FALSE;
}
```



## Related topics

<dl> <dt>

[About ComboBoxEx Controls](comboboxex-controls.md)
</dt> <dt>

[ComboBoxEx Control Reference](bumper-comboboxex-comboboxex-control-reference.md)
</dt> <dt>

[Using ComboBoxEx Controls](/windows/desktop/Controls/using-comboboxex)
</dt> <dt>

[ComboBoxEx](comboboxex-control-reference.md)
</dt> </dl>

 

 