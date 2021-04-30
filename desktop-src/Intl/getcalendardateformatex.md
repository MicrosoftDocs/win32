---
description: Deprecated.
ms.assetid: eb2622bc-a98d-42bd-ab59-7a849000d79d
title: GetCalendarDateFormatEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCalendarDateFormatEx
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-calendar-l1-1-0.dll
- kernel32legacy.dll
---

# GetCalendarDateFormatEx function

Deprecated. Retrieves a properly formatted date string for the specified locale using the specified date and calendar. The user can specify the short date format, the long date format, the year month format, or a custom format pattern.

> [!Note]  
> This function can retrieve data that changes between releases, for example, due to a custom locale. If your application must persist or transmit data, see [Using Persistent Locale Data](using-persistent-locale-data.md).

 

## Syntax


```C++
BOOL GetCalendarDateFormatEx(
  _In_        LPCWSTR       lpszLocale,
  _In_        DWORD         dwFlags,
  _In_  const LPCALDATETIME lpCalDateTime,
  _In_        LPCWSTR       lpFormat,
  _Out_       LPWSTR        lpDateStr,
  _In_        int           cchDate
);
```



## Parameters

<dl> <dt>

*lpszLocale* \[in\]
</dt> <dd>

Pointer to a locale name, or one of the following predefined values.

-   [LOCALE\_NAME\_INVARIANT](locale-name-constants.md)
-   [LOCALE\_NAME\_SYSTEM\_DEFAULT](locale-name-constants.md)
-   [LOCALE\_NAME\_USER\_DEFAULT](locale-name-constants.md)

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying date format options. If *lpFormat* is not set to **NULL**, this parameter must be set to 0. If *lpFormat* is set to **NULL**, the application can specify a combination of the following values and [LOCALE\_NOUSEROVERRIDE](locale-nouseroverride.md).



| Value                                                                                                                                                               | Meaning                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <span id="DATE_SHORTDATE"></span><span id="date_shortdate"></span><dl> <dt>**DATE\_SHORTDATE**</dt> </dl>    | Use the short date format. This is the default. This value cannot be used with DATE\_LONGDATE or DATE\_YEARMONTH. <br/> |
| <span id="DATE_LONGDATE"></span><span id="date_longdate"></span><dl> <dt>**DATE\_LONGDATE**</dt> </dl>       | Use the long date format. This value cannot be used with DATE\_SHORTDATE or DATE\_YEARMONTH. <br/>                      |
| <span id="DATE_YEARMONTH"></span><span id="date_yearmonth"></span><dl> <dt>**DATE\_YEARMONTH**</dt> </dl>    | Use the year/month format. This value cannot be used with DATE\_SHORTDATE or DATE\_LONGDATE.<br/>                       |
| <span id="DATE_LTRREADING"></span><span id="date_ltrreading"></span><dl> <dt>**DATE\_LTRREADING**</dt> </dl> | Add marks for left-to-right reading layout. This value cannot be used with DATE\_RTLREADING.<br/>                       |
| <span id="DATE_RTLREADING"></span><span id="date_rtlreading"></span><dl> <dt>**DATE\_RTLREADING**</dt> </dl> | Add marks for right-to-left reading layout. This value cannot be used with DATE\_LTRREADING<br/>                        |



 

</dd> <dt>

*lpCalDateTime* \[in\]
</dt> <dd>

Pointer to a [**CALDATETIME**](caldatetime.md) structure that contains the date and calendar information to format.

</dd> <dt>

*lpFormat* \[in\]
</dt> <dd>

Pointer to a format picture string that is used to form the date string. Possible values for the format picture string are defined in [Day, Month, Year, and Era Format Pictures](day--month--year--and-era-format-pictures.md).

The format picture string must be null-terminated. The function uses the locale only for information not specified in the format picture string, for example, the day and month names for the locale. The application sets this parameter to **NULL** if the function is to use the date format of the specified locale.

</dd> <dt>

*lpDateStr* \[out\]
</dt> <dd>

Pointer to a buffer in which this function receives the formatted date string.

</dd> <dt>

*cchDate* \[in\]
</dt> <dd>

Size, in characters, of the *lpDateStr* buffer. Alternatively, the application can set this parameter to 0. In this case, the function returns the number of characters required to hold the formatted date string, and the *lpDateStr* parameter is not used.

</dd> </dl>

## Return value

Returns the number of characters written to the *lpDateStr* buffer if successful. If the *cchDate* parameter is set to 0, the function returns the number of characters required to hold the formatted date string, including the terminating null character.

This function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_DATE\_OUT\_OF\_RANGE. The specified date was out of range.
-   ERROR\_INSUFFICIENT\_BUFFER. A supplied buffer size was not large enough, or it was incorrectly set to **NULL**.
-   ERROR\_INVALID\_FLAGS. The values supplied for flags were not valid.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

The earliest date supported by this function is January 1, 1601.

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with that module handle and the name of this function to get the function address.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[Day, Month, Year, and Era Format Pictures](day--month--year--and-era-format-pictures.md)
</dt> <dt>

[NLS: Name-based APIs Sample](nls--name-based-apis-sample.md)
</dt> <dt>

[**EnumDateFormatsExEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexex)
</dt> <dt>

[**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata)
</dt> <dt>

[**GetDateFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex)
</dt> <dt>

[**CALDATETIME**](caldatetime.md)
</dt> </dl>

 

 
