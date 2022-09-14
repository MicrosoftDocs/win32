---
title: How to Process the DTN_WMKEYDOWN Notification
description: This topic demonstrates how to process a DTN\_WMKEYDOWN notification. Handling this notification code allows the owner of the control to provide specific responses to keystrokes within the callback fields of the control.
ms.assetid: CD521C62-CF52-4FFF-A598-E5EBA34471FB
ms.topic: article
ms.date: 05/31/2018
---

# How to Process the DTN\_WMKEYDOWN Notification

This topic demonstrates how to process a [DTN\_WMKEYDOWN](dtn-wmkeydown.md) notification. Handling this notification code allows the owner of the control to provide specific responses to keystrokes within the callback fields of the control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


Date and time picker (DTP) controls send the [DTN\_WMKEYDOWN](dtn-wmkeydown.md) message to report that the user has typed input in a callback field. If you want to emulate the same keyboard responses that are supported for standard DTP fields or provide custom responses, your application must include code to handle this notification.

The following C++ code example is an application-defined function that processes the [DTN\_WMKEYDOWN](dtn-wmkeydown.md) notification.

**Security Warning:** Using **lstrcmp** incorrectly can compromise the security of your application. For example, before calling **lstrcmp** in the following code example, you should make sure the two strings are null-terminated. You should review [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.



```C++
//  DoWMKeydown increments or decrements the day of month according 
//  to user keyboard input.

void WINAPI DoWMKeydown(
 HWND hwndDP,
 LPNMDATETIMEWMKEYDOWN lpDTKeystroke)
{
    int delta =1;
    if(!lstrcmp(lpDTKeystroke->pszFormat,L"XX")){
        switch(lpDTKeystroke->nVirtKey){
            case VK_DOWN:
            case VK_SUBTRACT:
                delta = -1;  // fall through

            case VK_UP:
            case VK_ADD:
                lpDTKeystroke->st.wDay += (WORD) delta;
                break;
        }
    }
}
```



## Related topics

<dl> <dt>

[Using Date and Time Picker Controls](using-date-and-time-picker.md)
</dt> <dt>

[Date and Time Picker Control Reference](bumper-date-and-time-picker-date-and-time-picker-control-reference.md)
</dt> <dt>

[Date and Time Picker](date-and-time-picker-control-reference.md)
</dt> </dl>

 

 




