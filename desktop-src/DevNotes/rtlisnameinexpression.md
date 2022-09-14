---
description: Determines whether a Unicode string matches the specified pattern.
ms.assetid: 9b220cb8-4402-4094-8209-59a9af004b4a
title: RtlIsNameInExpression function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlIsNameInExpression
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlIsNameInExpression function

Determines whether a Unicode string matches the specified pattern.

## Syntax


```C++
 BOOLEAN  RtlIsNameInExpression(
  _In_     PUNICODE_STRING Expression,
  _In_     PUNICODE_STRING Name,
  _In_     BOOLEAN         IgnoreCase,
  _In_opt_ PWCH            UpcaseTable
);
```



## Parameters

<dl> <dt>

*Expression* \[in\]
</dt> <dd>

A pointer to the pattern string. This string can contain wildcard characters. If the *IgnoreCase* parameter is TRUE, the string must contain only uppercase characters.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

A pointer to the string to be compared against the pattern. This string cannot contain wildcard characters.

</dd> <dt>

*IgnoreCase* \[in\]
</dt> <dd>

**TRUE** for case-insensitive matching, or **FALSE** for case-sensitive matching.

</dd> <dt>

*UpcaseTable* \[in, optional\]
</dt> <dd>

An optional pointer to an uppercase character table to use for case-insensitive matching. If this parameter is NULL, the default system uppercase character table is used.

</dd> </dl>

## Return value

Returns **TRUE** if the string matches the pattern. If the string does not match the pattern, this function returns **FALSE**.

## Remarks

This function has no associated header file. The associated import library, Ntdll.lib, is available in the Microsoft Windows Driver Kit (WDK). You can also call this function using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
