---
description: Enables the middle mouse button to toggle the presence of a scrolling compass on a window.
title: EnterReaderModeHelper function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnterReaderModeHelper
api_type: 
- DllExport
api_location: 
- user32.dll
---

# EnterReaderModeHelper function

Enables the middle mouse button to toggle the presence of a scrolling compass cursor on a scrollable window.

## Syntax


```C++
LONG EnterReaderModeHelper(
    HANDLE hwnd
);
```



## Parameters

### hwnd

A handle to the window for which the scrolling compass cursor is enabled.

## Return value

A value evaluating to FALSE if the passed window handle is invalid; otherwise, TRUE.

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from user32.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows 10 |
| DLL | user32.dll |



## See also



 

 
