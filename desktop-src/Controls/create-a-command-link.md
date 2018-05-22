---
title: How to Create a Command Link
description: This topic describes one way to create a command link.
ms.assetid: 'F342075B-2D3B-40E0-B657-E1C57EDC2E3A'
---

# How to Create a Command Link

This topic describes one way to create a command link.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Step 1: Create an instance of the command link button.

In the following C++ code example, the style constant [**BS\_COMMANDLINK**](button-styles.md#bs-commandlink) specifies the button as a command link button.


```C++
HWND hwndCommandLink = CreateWindow(
    L"BUTTON",  // Predefined class; Unicode assumed
    L"",        // Text will be defined later
    WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_COMMANDLINK,  // Styles
    200,        // x position 
    10,         // y position 
    100,        // Button width
    100,        // Button height
    m_hwnd,     // Parent window
    NULL,       // No menu
    (HINSTANCE)GetWindowLong(m_hwnd, GWL_HINSTANCE), 
    NULL);      // Pointer not needed
```



### Step 2: Set the command link label and explanation text

Use the [**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950) function to set the command link label and supplementary text via the [**WM\_SETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632644#wm-settext) message and the [**BCM\_SETNOTE**](bcm-setnote.md#bcm-setnote-message) message, respectively.


```C++
SendMessage(hwndCommandLink, WM_SETTEXT, 0, (LPARAM)L"Command link");
SendMessage(hwndCommandLink, BCM_SETNOTE, 0, (LPARAM)L"with note");
```



## Related topics

<dl> <dt>

[About Buttons](about-buttons.md)
</dt> <dt>

[Button Control Reference](bumper-button-button-control-reference.md)
</dt> <dt>

[Using Buttons](using-buttons.md)
</dt> <dt>

[Button](buttons.md)
</dt> </dl>

 

 




