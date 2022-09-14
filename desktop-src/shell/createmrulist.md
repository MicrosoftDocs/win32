---
description: Creates a new most recently used (MRU) list.
title: CreateMRUListW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateMRUListW
- CreateMRUListW
api_type: 
- DllExport
api_location: 
- Comctl32.dll
ms.assetid: b2d9e3c7-8151-45ef-9658-bd33a87b4c9c

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

This function is not included in a public header or library. It can be accessed through [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) or extracted from comctl32.dll by its ordinal, which is 400 for **CreateMRUListW**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **CreateMRUListW** (Unicode)<br/>                                                                        |



 

 
