---
description: Enumerates the contents of the most recently used (MRU) list. Optionally retrieves an item from the enumeration.
title: EnumMRUListW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumMRUListW
- EnumMRUListW
api_type: 
- DllExport
api_location: 
- Comctl32.dll
ms.assetid: 630e5f27-96bf-4e88-b01a-127b301cc051

---

# EnumMRUListW function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows. \]

Enumerates the contents of the most recently used (MRU) list. Optionally retrieves an item from the enumeration.

## Syntax


```C++
int EnumMRUListW(
  _In_  HANDLE hMRU,
  _In_  int    nItem,
  _Out_ void   *lpData,
  _In_  UINT   uLen
);
```



## Parameters

<dl> <dt>

*hMRU* \[in\]
</dt> <dd>

Type: **HANDLE**

The handle of the MRU list, obtained when the list was created.

</dd> <dt>

*nItem* \[in\]
</dt> <dd>

Type: **int**

The item to return. If this value is less than 0, the function returns the number of items in the MRU list.

</dd> <dt>

*lpData* \[out\]
</dt> <dd>

Type: **void\***

A pointer to a buffer that receives the item requested in *nItem*. If *nItem* is less than 0, the contents of this buffer are unchanged.

</dd> <dt>

*uLen* \[in\]
</dt> <dd>

Type: **UINT**

The size of the buffer, including the terminating null character. If the MRU list was created with the **MRU\_BINARY** flag, this is the size in bytes. Otherwise, it is the size in characters.

</dd> </dl>

## Return value

Type: **int**

Returns one of the following values.

- Returns the number of items in the enumeration, if *nItem* is less than 0.
- Returns -1 if an error occurred.
- Otherwise, returns the size of the string returned in *lpData*, including the terminating null character. If the MRU list was created with the **MRU\_BINARY** flag, this is the size in bytes. Otherwise, it is the size in characters.

## Remarks

This function is not included in a public header or library. It can be accessed through [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) or extracted from comctl32.dll by its ordinal, which is 403 for **EnumMRUListW**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **EnumMRUListW** (Unicode)<br/>                                                                          |



## See also

<dl> <dt>

[**CreateMRUListW**](createmrulist.md)
</dt> <dt>

[**MRUINFO**](mruinfo.md)
</dt> </dl>

 

 
