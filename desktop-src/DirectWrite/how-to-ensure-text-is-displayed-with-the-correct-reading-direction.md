---
title: Ensure text is displayed with the correct reading direction
description: Some languages, such as Arabic and Hebrew, require a right-to-left reading direction.
ms.assetid: fa9a3dd6-575a-4877-a488-22845c6726c8
ms.topic: article
ms.date: 05/31/2018
---

# Ensure text is displayed with the correct reading direction

Some languages, such as Arabic and Hebrew, require a right-to-left reading direction. For a [DirectWrite](direct-write-portal.md) text format object, the default reading direction is left-to-right. DirectWrite does not automatically infer the reading direction from the locale, so you must do this yourself.

First, get the extended style flags for the window that the text will be rendered to by using the GetWindowStyleEx macro defined in windowsx.h.


```C++
// Get the window extended style flagsfor the current window.
DWORD dwStyle = GetWindowExStyle(hwnd_);
```



The macro returns a DWORD value made up of several flags combined with bitwise OR operations. You must determine if the specific flags affecting reading direction are there.

There are 2 different flags that are related to the reading direction: WS\_EX\_LAYOUTRTL and WS\_EX\_RTLREADING.

Use the bitwise AND operator (&) with the dwStyle variable and the WS\_EX\_LAYOUTRTL macro to store a BOOL value that indicates if the layout is mirrored.


```C++
// Is the WS_EX_LAYOUTRTL flag present?
BOOL bWSLayout = dwStyle & WS_EX_LAYOUTRTL;
```



Do the same thing for the WS\_EX\_RTLREADING flag.


```C++
// Is the WS_EX_RLTREADING flag present?
BOOL bWSReading = dwStyle & WS_EX_RTLREADING;
```



Set the reading direction by using the [**IDWriteTextFormat::SetReadingDirection**](/windows/win32/api/dwrite/nf-dwrite-idwritetextformat-setreadingdirection) method. The default is left-to-right, so you only need to set the reading direction if it is right-to-left.

> [!Note]  
> WS\_EX\_LAYOUTRTL mirrors the whole layout and implies right-to-left reading direction, so set the reading direction only if one of these flags is present. If both are present, they cancel one another out and the reading direction for the text format should be left-to-right.

 


```C++
// If either the WS_EX_LAYOUTRTL flag or the WS_EX_RLTREADING flag is present,
// but NOT BOTH, set the reading direction to right to left.
if ((bWSLayout && !bWSReading)
||  (!bWSLayout && bWSReading))
{
    pTextFormat_->SetReadingDirection(DWRITE_READING_DIRECTION_RIGHT_TO_LEFT);
}
```



 

 
