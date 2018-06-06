---
Description: Opens an existing symbolic link.
ms.assetid: 37684707-4f65-4904-8bfc-d0679ebbd924
title: NtOpenSymbolicLinkObject function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

An [**ACCESS\_MASK**](https://msdn.microsoft.com/f115ee54-3333-4109-8004-d71904a7a943) that specifies the requested access to the directory object. It is typical to use GENERIC\_READ so the handle can be passed to the [**NtQueryDirectoryObject**](ntquerydirectoryobject.md) function.

</dd> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

The attributes for the directory object. To initialize the **OBJECT\_ATTRIBUTES** structure, use the **InitializeObjectAttributes** macro. If the caller is not running in a system thread context, it must specify the **OBJ\_KERNEL\_HANDLE** flag when initializing the structure. For more information, see the documentation for these items in the documentation for the WDK.

</dd> </dl>

## Return value

The function returns **STATUS\_SUCCESS** or an error status.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtQueryDirectoryObject**](ntquerydirectoryobject.md)
</dt> </dl>

 

 




