---
description: Compares two Unicode character strings, using a specified locale.
ms.assetid: dff16c1b-d329-40de-b8d7-91edb36ce198
title: CompareStringWrapW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CompareStringWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# CompareStringWrapW function

\[**CompareStringWrapW** is available for use in Windows XP. It will not be available in subsequent versions. You should use [**CompareStringW**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) in its place.\]

Compares two Unicode character strings, using a specified locale.

> [!Note]  
> **CompareStringWrapW** is a wrapper for the **CompareStringW** function. See the [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) page for further usage notes.

 

## Syntax


```C++
int CompareStringWrapW(
  _In_ LCID    Locale,
  _In_ DWORD   dwCmpFlags,
  _In_ LPCWSTR lpString1,
  _In_ int     cchCount1,
  _In_ LPCWSTR lpString2,
  _In_ int     cchCount2
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

Type: **LCID**

A locale identifier used for the comparison. This parameter can be one of the following predefined locale identifiers or a locale identifier created by the [**MAKELCID**](/windows/win32/api/winnt/nf-winnt-makelcid) macro.

<dt>

<span id="LOCALE_SYSTEM_DEFAULT"></span><span id="locale_system_default"></span>

<span id="LOCALE_SYSTEM_DEFAULT"></span><span id="locale_system_default"></span>**LOCALE\_SYSTEM\_DEFAULT**


</dt> <dd>

The system's default locale.

</dd> <dt>

<span id="LOCALE_USER_DEFAULT"></span><span id="locale_user_default"></span>

<span id="LOCALE_USER_DEFAULT"></span><span id="locale_user_default"></span>**LOCALE\_USER\_DEFAULT**


</dt> <dd>

The current user's default locale.

</dd> </dl> </dd> <dt>

*dwCmpFlags* \[in\]
</dt> <dd>

Type: **DWORD**

The flags that indicate how the function compares the two strings. By default, these flags are not set. Set to zero to get the default behavior or to any combination of the following values.

<dt>

<span id="NORM_IGNORECASE"></span><span id="norm_ignorecase"></span>

<span id="NORM_IGNORECASE"></span><span id="norm_ignorecase"></span>**NORM\_IGNORECASE**


</dt> <dd>

Ignore case.

</dd> <dt>

<span id="NORM_IGNOREKANATYPE"></span><span id="norm_ignorekanatype"></span>

<span id="NORM_IGNOREKANATYPE"></span><span id="norm_ignorekanatype"></span>**NORM\_IGNOREKANATYPE**


</dt> <dd>

Do not differentiate between Hiragana and Katakana characters. Corresponding Hiragana and Katakana characters compare as equal.

</dd> <dt>

<span id="NORM_IGNORENONSPACE"></span><span id="norm_ignorenonspace"></span>

<span id="NORM_IGNORENONSPACE"></span><span id="norm_ignorenonspace"></span>**NORM\_IGNORENONSPACE**


</dt> <dd>

Ignore nonspacing characters.

</dd> <dt>

<span id="NORM_IGNORESYMBOLS"></span><span id="norm_ignoresymbols"></span>

<span id="NORM_IGNORESYMBOLS"></span><span id="norm_ignoresymbols"></span>**NORM\_IGNORESYMBOLS**


</dt> <dd>

Ignore symbols.

</dd> <dt>

<span id="NORM_IGNOREWIDTH"></span><span id="norm_ignorewidth"></span>

<span id="NORM_IGNOREWIDTH"></span><span id="norm_ignorewidth"></span>**NORM\_IGNOREWIDTH**


</dt> <dd>

Do not differentiate between a single-byte character and the same character as a double-byte character.

</dd> <dt>

<span id="SORT_STRINGSORT"></span><span id="sort_stringsort"></span>

<span id="SORT_STRINGSORT"></span><span id="sort_stringsort"></span>**SORT\_STRINGSORT**


</dt> <dd>

Treat punctuation the same as symbols.

</dd> </dl> </dd> <dt>

*lpString1* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to the first Unicode string to be compared.

</dd> <dt>

*cchCount1* \[in\]
</dt> <dd>

Type: **int**

The number of characters in the string pointed to by the *lpString1* parameter. The count does not include the terminating null character. If this parameter is a negative value, the string is assumed to be null-terminated and the length is calculated automatically.

</dd> <dt>

*lpString2* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to the second Unicode string to be compared.

</dd> <dt>

*cchCount2* \[in\]
</dt> <dd>

Type: **int**

The number of characters in the string pointed to by the *lpString2* parameter. The count does not include the terminating null character. If this parameter is a negative value, the string is assumed to be null-terminated and the length is calculated automatically.

</dd> </dl>

## Return value

Type: **int**

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). **GetLastError** may return one of the following error codes.

-   ERROR\_INVALID\_FLAGS
-   ERROR\_INVALID\_PARAMETER

If the function succeeds, the return value is one of the following values. 

| Requirement | Value |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| CSTR\_LESS\_THAN    | The string pointed to by the *lpString1* parameter is less in lexical value than the string pointed to by the *lpString2* parameter. |
| CSTR\_EQUAL         | The string pointed to by *lpString1* is equal in lexical value to the string pointed to by *lpString2*.                              |
| CSTR\_GREATER\_THAN | The string pointed to by *lpString1* is greater in lexical value than the string pointed to by *lpString2*                           |



 

## Remarks

**Security Warning:** Using this function incorrectly can compromise the security of your application. Strings that are not compared correctly can produce invalid input. Test strings to make sure they are valid before using them and provide error handlers. For more information, see [Security Considerations: International Features](../intl/security-considerations--international-features.md)

The preferred method is to use [**CompareStringW**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) in conjunction with the Microsoft Layer for Unicode (MSLU).

**CompareStringWrapW** must be called directly from Shlwapi.dll, using ordinal 45.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>None</dt> </dl>                               |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw)
</dt> </dl>

 

 
