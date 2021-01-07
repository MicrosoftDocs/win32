---
description: Provides a list of scripts for the specified locale.
ms.assetid: 0cedcf6c-bab4-4e0f-ab8f-04aa8e51602f
title: DownlevelGetLocaleScripts function (Idndl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelGetLocaleScripts
api_type: 
- DllExport
api_location: 
- Idndl.dll
---

# DownlevelGetLocaleScripts function

Provides a list of scripts for the specified locale.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires the download package. Applications that only run on Windows Vista and later should call [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) with *LCType* set to [LOCALE\_SSCRIPTS](locale-sscripts.md).

 

## Syntax


```C++
int DownlevelGetLocaleScripts(
  _In_  LPCWSTR lpLocaleName,
  _Out_ LPWSTR  lpScripts,
  _In_  int     cchScripts
);
```



## Parameters

<dl> <dt>

*lpLocaleName* \[in\]
</dt> <dd>

Pointer to a null-terminated [locale name](locale-names.md).

</dd> <dt>

*lpScripts* \[out\]
</dt> <dd>

Pointer to a buffer in which this function retrieves a null-terminated string representing a list of scripts, using the 4-character notation used in [ISO 15924](https://www.unicode.org/iso15924/iso15924-codes.html). Each script name consists of four Latin characters, and the names are retrieved in alphabetical order. Each of them, including the last, is followed by a semicolon.

Alternatively, this parameter can contain **NULL** if *cchScripts* is set to 0. In this case, the function returns the required size for the script buffer.

</dd> <dt>

*cchScripts* \[in\]
</dt> <dd>

Size, in characters, for the script buffer indicated by *lpScripts*.

Alternatively, the application can set this parameter to 0. In this case, the function retrieves **NULL** in *lpScripts* and returns the required size for the script buffer.

</dd> </dl>

## Return value

Returns the number of characters retrieved in the script buffer, including the terminating null character. If the function succeeds and the value of *cchScripts* is 0, the return value is the required size, in characters including a terminating null character, for the script buffer.

This function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_BADDB. The function could not access the data. This situation should not normally occur, and typically indicates a bad installation, a disk problem, or the like.
-   ERROR\_INSUFFICIENT\_BUFFER. A supplied buffer size was not large enough, or it was incorrectly set to **NULL**.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function is useful as part of a strategy to mitigate security issues related to [internationalized domain names (IDNs)](handling-internationalized-domain-names--idns.md).

Here are some examples of inputs and outputs for this function, assuming a sufficient buffer size:



| Locale                  | *lpLocaleName* | *lpScripts*     |
|-------------------------|----------------|-----------------|
| English (United States) | en-US          | Latn;           |
| Hindi (India)           | hi-IN          | Deva;           |
| Japanese (Japan)        | ja-JP          | Hani;Hira;Kana; |



 

The list does not contain the Latin script unless it is an essential part of the writing system used for a locale. However, Latin characters are often used in the context of locales for which they are not native, as for a foreign business name. In the example above for Hindi in India, the only script retrieved is "Deva" (for Devanagari), although Latin characters can also appear in Hindi text. The [**DownlevelVerifyScripts**](downlevelverifyscripts.md) function has a special flag to address that case.

The required header file and DLL are part of the ["Microsoft Internationalized Domain Name (IDN) Mitigation APIs"](https://www.microsoft.com/downloads/details.aspx?FamilyID=AD6158D7-DDBA-416A-9109-07607425A815&displaylang=en) download, available at the [MSDN Download Center](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                        |
| Redistributable<br/>          | Microsoft Internationalized Domain Name (IDN) Mitigation APIs on Windows XP (SP2 or later), Windows Server 2003 (SP1 or later), or Windows Vista<br/> |
| Header<br/>                   | <dl> <dt>Idndl.h</dt> </dl>                                                                          |
| DLL<br/>                      | <dl> <dt>Idndl.dll</dt> </dl>                                                                        |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[Handling Internationalized Domain Names (IDNs)](handling-internationalized-domain-names--idns.md)
</dt> <dt>

[**DownlevelGetStringScripts**](downlevelgetstringscripts.md)
</dt> <dt>

[**DownlevelVerifyScripts**](downlevelverifyscripts.md)
</dt> <dt>

[**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa)
</dt> </dl>

 

 
