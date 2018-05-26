---
Description: Used to determine whether an item is present in a most recently used (MRU) list.
title: MRUCMPPROC callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MRUCMPPROC callback function

Used to determine whether an item is present in a most recently used (MRU) list.

## Syntax


```C++
int CALLBACK MRUCMPPROC(
   LPCTSTR pString1,
   LPCTSTR pString2
);
```



## Parameters

<dl> <dt>

*pString1* 
</dt> <dd>

Type: **LPCTSTR**

The first string.

</dd> <dt>

*pString2* 
</dt> <dd>

Type: **LPCTSTR**

A second string to compare to the first.

</dd> </dl>

## Return value

Type: **int**

Returns 0 if the items are identical, a nonzero value otherwise.

## Remarks

This function can be optionally specified for use in the [**MRUINFO**](mruinfo.md) structure passed to [**CreateMRUListW**](createmrulist.md). This is useful when the MRU list was created with the **MRU\_BINARY** flag. When this function is not specified, standard string comparison functions are used.

## Requirements



|                                     |                                                                 |
|-------------------------------------|-----------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>            |
| Unicode and ANSI names<br/>   | **MRUCMPPROCW** (Unicode) and **MRUCMPPROCA** (ANSI)<br/> |



 

 




