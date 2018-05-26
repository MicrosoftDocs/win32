---
title: How to Implement Tooltips for Status Bar Icons
description: A nonintrusive way to display an explanatory message for a status bar icon is to implement a tooltip. The tooltip disappears when clicked, but you can also specify a time-out value.
ms.assetid: AA7F17F2-63A4-4954-9DAB-788B73984628
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Implement Tooltips for Status Bar Icons

A nonintrusive way to display an explanatory message for a status bar icon is to implement a tooltip. The tooltip disappears when clicked, but you can also specify a time-out value.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Implement Tooltips for Status Bar Icons

The following code fragment illustrates how to add a balloon tooltip to a status bar icon.


```C++
#define ARRAYSIZE(a) (sizeof(a)/sizeof(a[0]))

NOTIFYICONDATA IconData = {0};

IconData.cbSize = sizeof(IconData);
IconData.hWnd   = hwndNI;
IconData.uFlags = NIF_INFO;

HRESULT hr = StringCchCopy(IconData.szInfo, 
                           ARRAYSIZE(IconData.szInfo), 
                           TEXT("Your message text goes here."));

if(FAILED(hr))
{
  // TODO: Write an error handler in case the call to StringCchCopy fails.
}
IconData.uTimeout = 15000; // in milliseconds

Shell_NotifyIcon(NIM_MODIFY, &amp;IconData);
            
```



## Remarks

For a detailed discussion of the status bar, see [The Taskbar](https://msdn.microsoft.com/library/windows/desktop/cc144179).

To display a balloon tooltip, you need to set the NIF\_INFO flag in the [**NOTIFYICONDATA**](https://msdn.microsoft.com/library/windows/desktop/bb773352) structure, and use the **szInfo** and **uTimeout** members to specify the tooltip text and time-out duration.

## Related topics

<dl> <dt>

[Using Tooltip Controls](using-tooltip-contro.md)
</dt> </dl>

 

 




