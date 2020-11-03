---
title: How to Create a Button
description: To create buttons dynamically, you use the CreateWindow or CreateWindowEx function. This topic demonstrates how to use the CreateWindow function to create a default push button.
ms.assetid: A8C56D09-90A3-4C70-9907-61390521D1DA
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Button

To create buttons dynamically, you use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function. This topic demonstrates how to use the **CreateWindow** function to create a default push button.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


Use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) function to create a button control.

In the following C++ example, the *m\_hwnd* parameter is the handle to the parent window. The [**BS\_DEFPUSHBUTTON**](button-styles.md) style specifies that a default push button should be created. Note that the size and position values must be specified because using **CW\_USEDEFAULT** for a button sets the values to zero.


```C++
HWND hwndButton = CreateWindow( 
    L"BUTTON",  // Predefined class; Unicode assumed 
    L"OK",      // Button text 
    WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
    10,         // x position 
    10,         // y position 
    100,        // Button width
    100,        // Button height
    m_hwnd,     // Parent window
    NULL,       // No menu.
    (HINSTANCE)GetWindowLongPtr(m_hwnd, GWLP_HINSTANCE), 
    NULL);      // Pointer not needed.
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

 

 