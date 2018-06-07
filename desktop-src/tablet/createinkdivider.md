---
Description: Instantiates an implementation of the InkDivider interface and returns its handle.
ms.assetid: 77c8504b-0b63-43dd-b487-bab2a500979b
title: CreateInkDivider function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateInkDivider function

Instantiates an implementation of the [**InkDivider**](/windows/desktop/api/msinkaut15/) interface and returns its handle.

This function is not intended to be used by application code.

## Syntax


```C++
INT_PTR CreateInkDivider(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a handle to the created object.

## Remarks

This class inherits from the [**InkDivider**](/windows/desktop/api/msinkaut15/) base class and implements virtual functions.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




