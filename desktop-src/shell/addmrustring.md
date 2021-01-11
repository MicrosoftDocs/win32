---
description: Adds a string to the top of the most recently used (MRU) list.
title: AddMRUStringW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddMRUStringW
- AddMRUStringW
api_type: 
- DllExport
api_location: 
- Comctl32.dll
ms.assetid: ad94a442-8492-412c-a4f2-ac6e7c5327d7
api_name: 
 - AddMRUStringW
 - AddMRUStringW
api_type: 
 - DllExport
api_location: 
 - Comctl32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# AddMRUStringW function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows. \]

Adds a string to the top of the most recently used (MRU) list.

## Syntax


```C++
int AddMRUStringW(
  _In_ HANDLE  hMRU,
  _In_ LPCTSTR szString
);
```



## Parameters

<dl> <dt>

*hMRU* \[in\]
</dt> <dd>

Type: **HANDLE**

The handle of the MRU list.

</dd> <dt>

*szString* \[in\]
</dt> <dd>

Type: **LPCTSTR**

A pointer to the data. This can be either a string or, if the MRU list was created with the **MRU\_BINARY** flag, binary data. In the case of binary data, the first **DWORD** indicates its size.

</dd> </dl>

## Return value

Type: **int**

Returns a non-negative value if successful, -1 otherwise.

## Remarks

This function is not included in a public header or library. It can be accessed through [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) or extracted from comctl32.dll by its ordinal, which is 401 for **AddMRUStringW**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **AddMRUStringW** (Unicode)<br/>                                                                         |



 

