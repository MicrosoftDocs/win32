---
description: Converts a locale identifier to a locale name.
ms.assetid: 8e40d097-08a2-43e8-88e8-a4ecaddf449a
title: DownlevelLCIDToLocaleName function (Nlsdl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelLCIDToLocaleName
api_type: 
- DllExport
api_location: 
- NlsMap.dll
---

# DownlevelLCIDToLocaleName function

Converts a [locale identifier](locale-identifiers.md) to a [locale name](locale-names.md).

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires a download package. Applications that run only on Windows Vista and later should call [**LCIDToLocaleName**](/windows/desktop/api/Winnls/nf-winnls-lcidtolocalename) to retrieve a locale name.

 

## Syntax


```C++
int DownlevelLCIDToLocaleName(
  _In_  LCID   Locale,
  _Out_ LPWSTR lpName,
  _In_  int    cchName,
  _In_  DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

The locale identifier to translate. You can use the [**MAKELCID**](/windows/desktop/api/Winnt/nf-winnt-makelcid) macro to create a locale identifier. This function does not support neutral locales or the following specific locale identifier values.

-   [LOCALE\_SYSTEM\_DEFAULT](locale-system-default.md)
-   [LOCALE\_USER\_DEFAULT](locale-user-default.md)
-   [LOCALE\_CUSTOM\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UI\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md)

</dd> <dt>

*lpName* \[out\]
</dt> <dd>

Pointer to a buffer in which this function retrieves the locale name. The function retrieves **NULL** if *cchName* is set to 0.

</dd> <dt>

*cchName* \[in\]
</dt> <dd>

Size, in UTF-16 code points, of the locale name buffer. The application sets this parameter to 0 to return the required size of the locale name buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying the type of name to retrieve. The default value is DOWNLEVEL\_LOCALE\_NAME.

</dd> </dl>

## Return value

Returns the count of UTF-16 code points in the locale name, including the terminating null character, if successful. If the function succeeds and the value of *cchName* is 0, the return value is the required size, in characters (including null characters), for the locale name buffer.

The function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INSUFFICIENT\_BUFFER. A supplied buffer size was not large enough, or it was incorrectly set to **NULL**.
-   ERROR\_INVALID\_FLAGS. The value of *dwFlags* is not valid.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values were invalid.

## Remarks

> [!Note]  
> This function does not support [custom locales](custom-locales.md).

 

The required header file and DLL are part of the "Microsoft NLS Downlevel Data Mapping APIs" download, available at the [Microsoft Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=eb72cda0-834e-4c35-9419-ff14bc349c9d&DisplayLang=en).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                |
| Redistributable<br/>          | Microsoft NLS Downlevel Data Mapping APIs onWindows XP with SP2 and laterorWindows Vista<br/> |
| Header<br/>                   | <dl> <dt>Nlsdl.h</dt> </dl>                  |
| DLL<br/>                      | <dl> <dt>NlsMap.dll</dt> </dl>               |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[Mapping Locale Data](mapping-locale-data.md)
</dt> <dt>

[**LCIDToLocaleName**](/windows/desktop/api/Winnls/nf-winnls-lcidtolocalename)
</dt> </dl>

 

 
