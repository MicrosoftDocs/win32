---
description: Formats time as a time string for a specified locale.
ms.assetid: 048b209c-f757-4b65-9ce7-282a5c21021f
title: GetTimeFormatWrapW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetTimeFormatWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# GetTimeFormatWrapW function

\[**GetTimeFormatWrapW** is available for use in Windows XP. It may not be available in subsequent versions. You should use [**GetTimeFormatW**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata) in its place.\]

Formats time as a time string for a specified locale. The function formats either a specified time or the local system time.

> [!Note]  
> **GetTimeFormatWrapW** is a wrapper for the **GetTimeFormatW** function. See the [**GetTimeFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata) page for further usage notes.

 

## Syntax


```C++
int GetTimeFormatWrapW(
  _In_        LCID       Locale,
  _In_        DWORD      dwFlags,
  _In_  const SYSTEMTIME *lpTime,
  _In_        LPCWSTR    pwzFormat,
  _Out_       LPWSTR     pwzTimeStr,
  _In_        int        cchTime
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

Type: **LCID**

Specifies the locale for which the time string is to be formatted. If *pwzFormat* is **NULL**, the function formats the string according to the time format for this locale. If *pwzFormat* is not **NULL**, the function uses the locale only for information not specified in the format picture string (for example, the locale's time markers).

This parameter can be a locale identifier created by the [**MAKELCID**](/windows/win32/api/winnt/nf-winnt-makelcid) macro, or one of the following predefined values.

<dt>

<span id="LOCALE_SYSTEM_DEFAULT"></span><span id="locale_system_default"></span>

<span id="LOCALE_SYSTEM_DEFAULT"></span><span id="locale_system_default"></span>**LOCALE\_SYSTEM\_DEFAULT**


</dt> <dd>

Default system locale.

</dd> <dt>

<span id="LOCALE_USER_DEFAULT"></span><span id="locale_user_default"></span>

<span id="LOCALE_USER_DEFAULT"></span><span id="locale_user_default"></span>**LOCALE\_USER\_DEFAULT**


</dt> <dd>

Default user locale.

</dd> </dl> </dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies various function options. You can specify a combination of the following values.

<dt>

<span id="LOCALE_NOUSEROVERRIDE"></span><span id="locale_nouseroverride"></span>

<span id="LOCALE_NOUSEROVERRIDE"></span><span id="locale_nouseroverride"></span>**LOCALE\_NOUSEROVERRIDE**


</dt> <dd>

If set, the function formats the string using the system default time format for the specified locale. If not set, the function formats the string using any user overrides to the locale's default time format. This flag can only be set if *pwzFormat* is **NULL**.

</dd> <dt>

<span id="LOCALE_USE_CP_ACP"></span><span id="locale_use_cp_acp"></span>

<span id="LOCALE_USE_CP_ACP"></span><span id="locale_use_cp_acp"></span>**LOCALE\_USE\_CP\_ACP**


</dt> <dd>

Uses the system ANSI code page for string translation instead of the locale code page.

</dd> <dt>

<span id="TIME_NOMINUTESORSECONDS"></span><span id="time_nominutesorseconds"></span>

<span id="TIME_NOMINUTESORSECONDS"></span><span id="time_nominutesorseconds"></span>**TIME\_NOMINUTESORSECONDS**


</dt> <dd>

Does not use minutes or seconds.

</dd> <dt>

<span id="TIME_NOSECONDS"></span><span id="time_noseconds"></span>

<span id="TIME_NOSECONDS"></span><span id="time_noseconds"></span>**TIME\_NOSECONDS**


</dt> <dd>

Does not use seconds.

</dd> <dt>

<span id="TIME_NOTIMEMARKER"></span><span id="time_notimemarker"></span>

<span id="TIME_NOTIMEMARKER"></span><span id="time_notimemarker"></span>**TIME\_NOTIMEMARKER**


</dt> <dd>

Does not use a time marker.

</dd> <dt>

<span id="TIME_FORCE24HOURFORMAT"></span><span id="time_force24hourformat"></span>

<span id="TIME_FORCE24HOURFORMAT"></span><span id="time_force24hourformat"></span>**TIME\_FORCE24HOURFORMAT**


</dt> <dd>

Always uses a 24-hour time format.

</dd> </dl> </dd> <dt>

*lpTime* \[in\]
</dt> <dd>

Type: **const [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime)\***

A pointer to a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure that contains the time information to be formatted. If this pointer is **NULL**, the function uses the current local system time.

</dd> <dt>

*pwzFormat* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a format to use to form the time string. If *pwzFormat* is **NULL**, the function uses the time format of the specified locale. See [**GetTimeFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata) for more details.

</dd> <dt>

*pwzTimeStr* \[out\]
</dt> <dd>

Type: **LPWSTR**

A pointer to a buffer that receives the formatted time string.

</dd> <dt>

*cchTime* \[in\]
</dt> <dd>

Type: **int**

The size, in characters, of the *pwzTimeStr* buffer. If *cchTime* is zero, the function returns the number of characters required to hold the formatted time string, and the buffer pointed to by *pwzTimeStr* is not used.

</dd> </dl>

## Return value

Type: **int**

If the function succeeds, the return value is the number of characters written to the buffer pointed to by *pwzTimeStr*. If the *cchTime* parameter is zero, the return value is the number of characters required to hold the formatted time string. The count includes the terminating null character.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). **GetLastError** may return one of the following error codes.

<dl> <dt>

**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dt>

**ERROR\_INVALID\_FLAGS**
</dt> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> </dl>

## Remarks

**GetTimeFormatWrapW** provides the ability to use Unicode strings in operating systems earlier than Windows XP. The preferred method is to use [**GetTimeFormatW**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata) in conjunction with the Microsoft Layer for Unicode (MSLU).

**GetTimeFormatWrapW** must be called directly from Shlwapi.dll, using ordinal 310.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**GetTimeFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata)
</dt> </dl>

 

 
