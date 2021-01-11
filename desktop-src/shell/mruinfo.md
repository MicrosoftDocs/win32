---
description: Contains information that defines a new most recently used (MRU) list. Used by CreateMRUListW.
title: MRUINFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _MRUINFO
- MRUINFOA
- MRUINFOW
api_type: 
- NA
api_location: 
ms.assetid: 31d5831d-9a19-4bd9-8439-ce844966c414
api_name: 
 - _MRUINFO
 - MRUINFOA
 - MRUINFOW
api_type: 
 - NA
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# MRUINFO structure

Contains information that defines a new most recently used (MRU) list. Used by [**CreateMRUListW**](createmrulist.md).

## Syntax


```C++
typedef struct {
  DWORD      cbSize;
  UINT       uMax;
  UINT       fFlags;
  HKEY       hKey;
  LPCTSTR    lpszSubKey;
  MRUCMPPROC lpfnCompare;
} _MRUINFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size of the structure.

</dd> <dt>

**uMax**
</dt> <dd>

Type: **UINT**

</dd> <dd>

The maximum number of entries in the MRU list.

</dd> <dt>

**fFlags**
</dt> <dd>

Type: **UINT**

</dd> <dd>

One or more of the following flags.

<dt>

<span id="MRU_BINARY"></span><span id="mru_binary"></span>

<span id="MRU_BINARY"></span><span id="mru_binary"></span>**MRU\_BINARY** (0x0001)


</dt> <dd>

Data is stored in the registry as binary data rather than string data.

</dd> <dt>

<span id="MRU_CACHEWRITE"></span><span id="mru_cachewrite"></span>

<span id="MRU_CACHEWRITE"></span><span id="mru_cachewrite"></span>**MRU\_CACHEWRITE** (0x0002)


</dt> <dd>

Write changes to the version of the MRU stored in the registry only when a new item is added or the MRU list's resources are freed from memory. Note that the active version of the MRU in memory is updated immediately in response to any change in contents or ordering.

</dd> </dl> </dd> <dt>

**hKey**
</dt> <dd>

Type: **HKEY**

</dd> <dd>

A handle to the currently open key, or one of the following predefined values under which to store the MRU data.

<dl><span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span><dt>

**HKEY\_CURRENT\_USER**
</dt><span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span><dt>

**HKEY\_LOCAL\_MACHINE**
</dt> </dl> </dd> <dt>

**lpszSubKey**
</dt> <dd>

Type: **LPCTSTR**

</dd> <dd>

The subkey under which to store the MRU data.

</dd> <dt>

**lpfnCompare**
</dt> <dd>

Type: **[**MRUCMPPROC**](mrucmpproc.md)**

</dd> <dd>

A pointer to an optional data comparison function that can be used to determine whether an item is present in the MRU list. This is useful when the MRU list was created with the **MRU\_BINARY** flag. If this member is **NULL**, standard string comparison functions are used; for binary data, a direct memory comparison is used.

</dd> </dl>

## Remarks

This structure is not defined in a header file. You must define it yourself.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| Unicode and ANSI names<br/>   | **MRUINFOW** (Unicode) and **MRUINFOA** (ANSI)<br/>  |



 

 




