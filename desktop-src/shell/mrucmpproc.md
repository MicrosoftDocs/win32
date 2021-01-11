---
description: Used to determine whether an item is present in a most recently used (MRU) list.
title: MRUCMPPROC callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MRUCMPPROC
- MRUCMPPROCA
- MRUCMPPROCW
api_type: 
- UserDefined
api_location: 
ms.assetid: 00f31d6b-2a96-4abd-9647-24a6e66aa22f
api_name: 
 - MRUCMPPROC
 - MRUCMPPROCA
 - MRUCMPPROCW
api_type: 
 - UserDefined
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

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



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>            |
| Unicode and ANSI names<br/>   | **MRUCMPPROCW** (Unicode) and **MRUCMPPROCA** (ANSI)<br/> |



 

 




