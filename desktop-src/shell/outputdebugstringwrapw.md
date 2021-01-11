---
description: Sends a Unicode string to the debugger for display.
ms.assetid: 26cf4750-8ca1-4a9a-8378-d65ed288b358
title: OutputDebugStringWrapW function (Shlwapip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OutputDebugStringWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# OutputDebugStringWrapW function

\[This function is available for use in Windows XP. It may not be available in subsequent versions. Use [**OutputDebugStringW**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) in its place.\]

Sends a Unicode string to the debugger for display.

> [!Note]  
> **OutputDebugStringWrapW** is a wrapper for the **OutputDebugStringW** function. See the [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) page for further usage notes.

 

## Syntax


```C++
void OutputDebugStringWrapW(
  _In_ LPCWSTR lpOutputString
);
```



## Parameters

<dl> <dt>

*lpOutputString* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to the null-terminated Unicode string to be displayed.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

**OutputDebugStringWrapW** provides the ability to use Unicode strings in operating systems prior to Windows XP. The preferred method is to use [**OutputDebugStringW**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) in conjunction with the Microsoft Layer for Unicode (MSLU).

**OutputDebugStringWrapW** must be called directly from Shlwapi.dll, using ordinal 115.

If the application has no debugger, the system debugger displays the string. If the application has no debugger and the system debugger is not active, **OutputDebugStringWrapW** does nothing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shlwapip.h</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa)
</dt> </dl>

 

 
