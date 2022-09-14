---
description: Determines the location of a resource with the specified type and name, in the specified module.
ms.assetid: d8322430-5064-407e-8b89-b86b75bf139e
title: FindResourceWrapW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindResourceWrapW
- FindResourceWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# FindResourceWrapW function

\[**FindResourceWrapW** is available for use in Windows XP. It may not be available in subsequent versions. You should use [**FindResourceW**](/windows/win32/api/winbase/nf-winbase-findresourcea) instead.\]

Determines the location of a resource with the specified type and name, in the specified module.

> [!Note]  
> **FindResourceWrapW** is a wrapper for the **FindResourceW** function. See [**FindResource**](/windows/win32/api/winbase/nf-winbase-findresourcea) for further usage notes.

 

## Syntax


```C++
HRSRC FindResourceWrapW(
  _In_ HMODULE hModule,
  _In_ LPCWSTR lpName,
  _In_ LPCWSTR lpType
);
```



## Parameters

<dl> <dt>

*hModule* \[in\]
</dt> <dd>

Type: **HMODULE**

A handle to the module whose executable file contains the resource. A value of **NULL** specifies the module handle associated with the image file that the operating system used to create the current process.

</dd> <dt>

*lpName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The name of the resource. For more information, see [**FindResource**](/windows/win32/api/winbase/nf-winbase-findresourcea).

</dd> <dt>

*lpType* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a string that specifies the resource type. For more information, see [**FindResource**](/windows/win32/api/winbase/nf-winbase-findresourcea).

</dd> </dl>

## Return value

Type: **HRSRC**

If the function succeeds, the return value is a handle to the specified resource's information block. To obtain a handle to the resource, pass this handle to the [**LoadResource**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadresource) function.

If the function fails, the return value is **NULL**. To get extended error information, call the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

## Remarks

If you need to specify a particular localization, use the [**FindResourceEx**](/windows/win32/api/winbase/nf-winbase-findresourceexa) function rather than **FindResourceWrapW**.

**FindResourceWrapW** provides the ability to use Unicode strings in older operating systems. The preferred method is to use [**FindResourceW**](/windows/win32/api/winbase/nf-winbase-findresourcea) in conjunction with the Microsoft Layer for Unicode (MSLU).

**FindResourceWrapW** must be called directly from Shlwapi.dll, using ordinal 66.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>None</dt> </dl>                               |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **FindResourceWrapW** (Unicode)<br/>                                                                    |



## See also

<dl> <dt>

[**FindResource**](/windows/win32/api/winbase/nf-winbase-findresourcea)
</dt> </dl>

 

 
