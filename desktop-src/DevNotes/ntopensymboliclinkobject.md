---
Description: 'Opens an existing symbolic link.'
ms.assetid: '37684707-4f65-4904-8bfc-d0679ebbd924'
title: NtOpenSymbolicLinkObject function
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

An [**ACCESS\_MASK**](security.access_mask) that specifies the requested access to the directory object. It is typical to use GENERIC\_READ so the handle can be passed to the [**NtQueryDirectoryObject**](ntquerydirectoryobject.md) function.

</dd> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

The attributes for the directory object. To initialize the **OBJECT\_ATTRIBUTES** structure, use the **InitializeObjectAttributes** macro. If the caller is not running in a system thread context, it must specify the **OBJ\_KERNEL\_HANDLE** flag when initializing the structure. For more information, see the documentation for these items in the documentation for the WDK.

</dd> </dl>

## Return value

The function returns **STATUS\_SUCCESS** or an error status.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtQueryDirectoryObject**](ntquerydirectoryobject.md)
</dt> </dl>

 

 




