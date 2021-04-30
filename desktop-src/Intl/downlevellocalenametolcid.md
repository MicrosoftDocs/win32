---
description: Converts a locale name to a locale identifier that can be used to get information from the operating system.
ms.assetid: dc776c41-0376-4222-bebf-86be7e4be122
title: DownlevelLocaleNameToLCID function (Nlsdl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelLocaleNameToLCID
api_type: 
- DllExport
api_location: 
- NlsMap.dll
---

# DownlevelLocaleNameToLCID function

Converts a [locale name](locale-names.md) to a [locale identifier](locale-identifiers.md) that can be used to get information from the operating system.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires a download package. Applications that only run on Windows Vista and later should call [**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid) to retrieve a locale identifier.

 

## Syntax


```C++
LCID DownlevelLocaleNameToLCID(
  _In_ LPWSTR lpName,
  _In_ DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*lpName* \[in\]
</dt> <dd>

Pointer to a null-terminated string representing a [locale name](locale-names.md).

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying the type of name. The default is DOWNLEVEL\_LOCALE\_NAME.

</dd> </dl>

## Return value

Returns the locale identifier that corresponds to the locale name if successful.

The function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INVALID\_FLAGS. The values supplied for flags were not valid.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values were invalid.

## Remarks

> [!Note]  
> This function does not support neutral locales. The equivalent [**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid) function supports [custom locales](custom-locales.md), but only for Windows Vista and later.

 

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

[**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid)
</dt> </dl>

 

 
