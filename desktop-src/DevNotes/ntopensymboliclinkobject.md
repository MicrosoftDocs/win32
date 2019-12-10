---
Description: Opens an existing symbolic link.
ms.assetid: 37684707-4f65-4904-8bfc-d0679ebbd924
title: NtOpenSymbolicLinkObject function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtOpenSymbolicLinkObject
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtOpenSymbolicLinkObject function

\[This function may be altered or unavailable in the future.\]

Opens an existing symbolic link.

## Syntax


```C++
NTSTATUS WINAPI NtOpenSymbolicLinkObject(
  _Out_ PHANDLE            LinkHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes
);
```



## Parameters

<dl> <dt>

*LinkHandle* \[out\]
</dt> <dd>

A handle to the newly opened symbolic link object.

</dd> <dt>

*DesiredAccess* \[in\]
</dt> <dd>

An [**ACCESS\_MASK**](https://msdn.microsoft.com/library/Aa374892(v=VS.85).aspx) that specifies the requested access to the directory object. It is typical to use GENERIC\_READ so the handle can be passed to the [**NtQueryDirectoryObject**](ntquerydirectoryobject.md) function.

</dd> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

The attributes for the directory object. To initialize the **OBJECT\_ATTRIBUTES** structure, use the **InitializeObjectAttributes** macro. If the caller is not running in a system thread context, it must specify the **OBJ\_KERNEL\_HANDLE** flag when initializing the structure. For more information, see the documentation for these items in the documentation for the WDK.

</dd> </dl>

## Return value

The function returns **STATUS\_SUCCESS** or an error status.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtQueryDirectoryObject**](ntquerydirectoryobject.md)
</dt> </dl>

 

 




