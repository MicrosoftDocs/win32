---
description: Retrieves the locale identifier for the parent of the supplied locale.
ms.assetid: 4cfa1787-6b9e-4dd4-8466-7b737e00a4b1
title: DownlevelGetParentLocaleLCID function (Nlsdl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelGetParentLocaleLCID
api_type: 
- DllExport
api_location: 
- NlsMap.dll
---

# DownlevelGetParentLocaleLCID function

Retrieves the [locale identifier](locale-identifiers.md) for the parent of the supplied locale.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires the download package. Applications that only run on Windows Vista and later should call [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) with *LCType* set to [LOCALE\_SPARENT](locale-sparent.md).

 

## Syntax


```C++
LCID DownlevelGetParentLocaleLCID(
  _In_ LCID Locale
);
```



## Parameters

<dl> <dt>

*Locale* \[in\]
</dt> <dd>

Locale identifier of the locale for which to retrieve the parent locale identifier. You can use the [**MAKELCID**](/windows/desktop/api/Winnt/nf-winnt-makelcid) macro to create a locale identifier or use one of the following predefined values.

-   [LOCALE\_INVARIANT](locale-invariant.md)
-   [LOCALE\_SYSTEM\_DEFAULT](locale-system-default.md)
-   [LOCALE\_USER\_DEFAULT](locale-user-default.md)

**Windows Vista and later:** The following custom locale identifiers are also supported.

-   [LOCALE\_CUSTOM\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UI\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md)

</dd> </dl>

## Return value

Returns the parent locale identifier if successful, or 0 otherwise. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

The required header file and DLL are part of the "Microsoft NLS Downlevel Data Mapping APIs" download, available at the [Microsoft Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=eb72cda0-834e-4c35-9419-ff14bc349c9d&DisplayLang=en).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Microsoft NLS Downlevel Data Mapping APIs onWindows XPor Windows Vista<br/>     |
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

 

 
