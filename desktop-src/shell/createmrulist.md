---
Description: Creates a new most recently used (MRU) list.
title: CreateMRUListW function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateMRUListW function

Creates a new most recently used (MRU) list.

## Syntax


```C++
int CreateMRUListW(
  _In_ LPMRUINFO lpmi
);
```



## Parameters

<dl> <dt>

*lpmi* \[in\]
</dt> <dd>

Type: **LPMRUINFO**

A pointer to an [**MRUINFO**](mruinfo.md) structure defining the MRU list.

</dd> </dl>

## Return value

Type: **int**

Returns a handle to the new MRU list, or 0 in case of an error.

## Remarks

This function is not included in a public header or library. It can be accessed through [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) or extracted from comctl32.dll by its ordinal, which is 400 for **CreateMRUListW**.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **CreateMRUListW** (Unicode)<br/>                                                                        |



 

 




