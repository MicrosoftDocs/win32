---
description: Formats a date as a date string for a specified locale.
ms.assetid: e45f6d1c-2890-44f6-8406-022c99c59e02
title: GetDateFormatWrapW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetDateFormatWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# GetDateFormatWrapW function

\[**GetDateFormatWrapW** is available for use in Windows XP. It will not be available in subsequent versions. You should use [**GetDateFormatW**](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformata) in its place.\]

Formats a date as a date string for a specified locale. The function formats either a specified date or the local system date.

> [!Note]  
> **GetDateFormatWrapW** is a wrapper for the **GetDateFormatW** function. See the [**GetDateFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformata) page for further usage notes.

 

## Syntax


```C++
int GetDateFormatWrapW(
  _In_        LCID       Locale,
  _In_        DWORD      dwFlags,
  _In_  const SYSTEMTIME *lpDate,
  _In_        LPCWSTR    pwzFormat,
  _Out_       LPWSTR     pwzDateStr,
  _In_        int        cchDate
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

Type: **LCID**

The locale for which the date string is to be formatted. If *pwzFormat* is **NULL**, the function formats the string according to the date format for this locale. If *pwzFormat* is not **NULL**, the function uses the locale only for information not specified in the format picture string (for example, the locale's day and month names).

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

Specifies various function options. If *pwzFormat* is not **NULL**, this parameter must be zero. If *pwzFormat* is **NULL**, you can specify a combination of the following values. If you do not specify either DATE\_YEARMONTH, DATE\_SHORTDATE, or DATE\_LONGDATE, and *pwzFormat* is **NULL**, then DATE\_SHORTDATE is used as the default.

<dt>

<span id="LOCALE_NOUSEROVERRIDE"></span><span id="locale_nouseroverride"></span>

<span id="LOCALE_NOUSEROVERRIDE"></span><span id="locale_nouseroverride"></span>**LOCALE\_NOUSEROVERRIDE**


</dt> <dd>

If set, the function formats the string using the system default date format for the specified locale. If not set, the function formats the string using any user overrides to the locale's default date format.

</dd> <dt>

<span id="LOCALE_USE_CP_ACP"></span><span id="locale_use_cp_acp"></span>

<span id="LOCALE_USE_CP_ACP"></span><span id="locale_use_cp_acp"></span>**LOCALE\_USE\_CP\_ACP**


</dt> <dd>

Uses the system ANSI code page for string translation instead of the locale's code page.

</dd> <dt>

<span id="DATE_SHORTDATE"></span><span id="date_shortdate"></span>

<span id="DATE_SHORTDATE"></span><span id="date_shortdate"></span>**DATE\_SHORTDATE**


</dt> <dd>

Uses the short date format. This value cannot be used with DATE\_LONGDATE or DATE\_YEARMONTH.

</dd> <dt>

<span id="DATE_LONGDATE"></span><span id="date_longdate"></span>

<span id="DATE_LONGDATE"></span><span id="date_longdate"></span>**DATE\_LONGDATE**


</dt> <dd>

Uses the long date format. This value cannot be used with DATE\_SHORTDATE or DATE\_YEARMONTH.

</dd> <dt>

<span id="DATE_YEARMONTH"></span><span id="date_yearmonth"></span>

<span id="DATE_YEARMONTH"></span><span id="date_yearmonth"></span>**DATE\_YEARMONTH**


</dt> <dd>

Uses the year/month format. This value cannot be used with DATE\_SHORTDATE or DATE\_LONGDATE.

</dd> <dt>

<span id="DATE_USE_ALT_CALENDAR"></span><span id="date_use_alt_calendar"></span>

<span id="DATE_USE_ALT_CALENDAR"></span><span id="date_use_alt_calendar"></span>**DATE\_USE\_ALT\_CALENDAR**


</dt> <dd>

Uses the alternate calendar, if one exists, to format the date string. If this flag is set, the function uses the default format for that alternate calendar, rather than using any user overrides. The user overrides will be used only in the event that there is no default format for the specified alternate calendar.

</dd> <dt>

<span id="DATE_LTRREADING"></span><span id="date_ltrreading"></span>

<span id="DATE_LTRREADING"></span><span id="date_ltrreading"></span>**DATE\_LTRREADING**


</dt> <dd>

Adds marks for left-to-right reading layout. This value cannot be used with DATE\_RTLREADING.

</dd> <dt>

<span id="DATE_RTLREADING"></span><span id="date_rtlreading"></span>

<span id="DATE_RTLREADING"></span><span id="date_rtlreading"></span>**DATE\_RTLREADING**


</dt> <dd>

Adds marks for right-to-left reading layout. This value cannot be used with DATE\_LTRREADING.

</dd> </dl> </dd> <dt>

*lpDate* \[in\]
</dt> <dd>

Type: **const [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime)\***

A pointer to a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure that contains the date information to be formatted. If this pointer is **NULL**, the function uses the current local system date.

</dd> <dt>

*pwzFormat* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a format picture to use to form the date string. If *pwzFormat* is **NULL**, the function uses the date format of the specified locale. See [**GetDateFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformata) for more details.

</dd> <dt>

*pwzDateStr* \[out\]
</dt> <dd>

Type: **LPWSTR**

A pointer to a buffer that receives the formatted date string.

</dd> <dt>

*cchDate* \[in\]
</dt> <dd>

Type: **int**

Specifies the size, in characters, of the *pwzDateStr* buffer. If *cchDate* is zero, the function returns the number of characters required to hold the formatted date string, and the buffer pointed to by *pwzDateStr* is not used.

</dd> </dl>

## Return value

Type: **int**

If the function succeeds, the return value is the number of characters written to the buffer pointed to by *pwzDateStr*. If the *cchDate* parameter is zero, the return value is the number of characters required to hold the formatted date string. The count includes the terminating null character.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). **GetLastError** may return one of the following error codes.

<dl> <dt>

**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dt>

**ERROR\_INVALID\_FLAGS**
</dt> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> </dl>

## Remarks

**GetDateFormatWrapW** provides the ability to use Unicode strings in operating systems earlier than Windows XP. The preferred method is to use [**GetDateFormatW**](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformata) in conjunction with the Microsoft Layer for Unicode (MSLU).

**GetDateFormatWrapW** must be called directly from Shlwapi.dll, using ordinal 311.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**GetDateFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformata)
</dt> </dl>

 

 
