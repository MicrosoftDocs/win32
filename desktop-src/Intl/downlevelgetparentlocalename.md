---
description: Retrieves the locale name for the parent of the supplied locale.
ms.assetid: a8db8107-822c-4bbc-acb8-40b25d2b41c4
title: DownlevelGetParentLocaleName function (Nlsdl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelGetParentLocaleName
api_type: 
- DllExport
api_location: 
- NlsMap.dll
---

# DownlevelGetParentLocaleName function

Retrieves the [locale name](locale-names.md) for the parent of the supplied locale.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires the download package. Applications that only run on Windows Vista and later should call [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) with *LCType* set to [LOCALE\_SPARENT](locale-sparent.md).

 

## Syntax


```C++
int DownlevelGetParentLocaleName(
  _In_  LCID   Locale,
  _Out_ LPWSTR lpName,
  _In_  int    cchName
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

[Locale identifier](locale-identifiers.md) of the locale. You can use the [**MAKELCID**](/windows/desktop/api/Winnt/nf-winnt-makelcid) macro to create a locale identifier or use one of the following predefined values.

-   [LOCALE\_INVARIANT](locale-invariant.md)
-   [LOCALE\_SYSTEM\_DEFAULT](locale-system-default.md)
-   [LOCALE\_USER\_DEFAULT](locale-user-default.md)

**Windows Vista and later:** The following custom locale identifiers are also supported.

-   [LOCALE\_CUSTOM\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UI\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md)

</dd> <dt>

*lpName* \[out\]
</dt> <dd>

Pointer to a buffer in which the function retrieves the parent locale name, or one of the following predefined values. This parameter is set to **NULL** if *cchName* is set to 0.

-   [LOCALE\_NAME\_INVARIANT](locale-name-constants.md)
-   [LOCALE\_NAME\_SYSTEM\_DEFAULT](locale-name-constants.md)
-   [LOCALE\_NAME\_USER\_DEFAULT](locale-name-constants.md)

</dd> <dt>

*cchName* \[in\]
</dt> <dd>

Size of the buffer indicated by *lpName*, in UTF-16 code points. A value of 0 for this parameter causes the function to ignore the *lpName* buffer and return the size of the buffer, in characters (null characters included), required to contain the parent locale name.

</dd> </dl>

## Return value

Returns the count of UTF-16 code points in the locale name, including the terminating null character, if successful.

This function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INSUFFICIENT\_BUFFER. A supplied buffer size was not large enough, or it was incorrectly set to **NULL**.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

The required header file and DLL are part of the "Microsoft NLS Downlevel Data Mapping APIs" download, available at the [Microsoft Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=eb72cda0-834e-4c35-9419-ff14bc349c9d&DisplayLang=en).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Microsoft NLS Downlevel Data Mapping APIs onWindows XP with SP2 and later<br/>  |
| Header<br/>                   | <dl> <dt>Nlsdl.h</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>NlsMap.dll</dt> </dl> |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[Mapping Locale Data](mapping-locale-data.md)
</dt> <dt>

[**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa)
</dt> </dl>

 

 
