---
description: Compares two enumerated lists of scripts.
ms.assetid: 3500ce36-75e4-4d61-8449-a65c99532326
title: DownlevelVerifyScripts function (Idndl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelVerifyScripts
api_type: 
- DllExport
api_location: 
- Idndl.dll
---

# DownlevelVerifyScripts function

Compares two enumerated lists of scripts.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires the download package. Applications that only run on Windows Vista and later should call [**VerifyScripts**](/windows/desktop/api/Winnls/nf-winnls-verifyscripts).

 

## Syntax


```C++
BOOL DownlevelVerifyScripts(
  _In_ DWORD   dwFlags,
  _In_ LPCWSTR lpLocaleScripts,
  _In_ int     cchLocaleScripts,
  _In_ LPCWSTR lpTestScripts,
  _In_ int     cchTestScripts
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying script verification options.



| Value                                                                                                                                                             | Meaning                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="VS_ALLOW_LATIN"></span><span id="vs_allow_latin"></span><dl> <dt>**VS\_ALLOW\_LATIN**</dt> </dl> | Allow "Latn" (Latin script) in the test list, even if it is not in the locale list.<br/> |



 

</dd> <dt>

*lpLocaleScripts* \[in\]
</dt> <dd>

Pointer to the locale list, the enumerated list of scripts for a given locale. This list is typically populated by calling [**DownlevelGetLocaleScripts**](downlevelgetlocalescripts.md).

</dd> <dt>

*cchLocaleScripts* \[in\]
</dt> <dd>

Size, in characters, of the string indicated by *lpLocaleScripts*. The application sets this parameter to -1 if the string is null-terminated. If this parameter is set to 0, the function fails.

</dd> <dt>

*lpTestScripts* \[in\]
</dt> <dd>

Pointer to the test list, a second enumerated list of scripts. This list is typically populated by calling [**DownlevelGetStringScripts**](downlevelgetstringscripts.md).

</dd> <dt>

*cchTestScripts* \[in\]
</dt> <dd>

Size, in characters, of the string indicated by *lpTestScripts*. The application sets this parameter to -1 if the string is null-terminated. If this parameter is set to 0, the function fails.

</dd> </dl>

## Return value

Returns **TRUE** if the test list is non-empty and all items in the list are also included in the locale list. Otherwise, the function returns **FALSE**.

A return value of **FALSE** can indicate that the test list contains an item that is not in the locale list, or it can indicate an error. To distinguish between these two cases, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). If **DownlevelVerifyScripts** has successfully determined that there is an item in the test list that is not in the locale list, **GetLastError** returns ERROR\_SUCCESS. Otherwise, **GetLastError** can return one of the following error codes:

-   ERROR\_INVALID\_FLAGS. The values supplied for flags were not valid.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function compares strings, such as "Latn;Cyrl;", that consist of a series of 4-character script names, with each script name followed by a semicolon. It also has a special case to account for the fact that the Latin script is often used in languages and locales for which it is not native.

This function is useful as part of a strategy to mitigate security issues related to [internationalized domain names (IDNs)](handling-internationalized-domain-names--idns.md).

The following are examples of the return of this function and a subsequent call to [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) in various scenarios. The last two examples illustrate, respectively, a case in which the test list lacks a terminating semicolon (malformed string) and a case in which the test list is empty.



| "Locale" string | "Test" string | *dwFlags*        | Return value | GetLastError return       |
|-----------------|---------------|------------------|--------------|---------------------------|
| Hani;Hira;Kana; | Hani;         | N/A              | **TRUE**     | N/A                       |
| Hani;Hira;Kana; | Hani;Latn;    | 0                | **FALSE**    | ERROR\_SUCCESS            |
| Hani;Hira;Kana; | Hani;Latn;    | VS\_ALLOW\_LATIN | **TRUE**     | N/A                       |
| Hani;Hira;Kana; | Cyrl;         | N/A              | **FALSE**    | ERROR\_SUCCESS            |
| Hani;Hira;Kana; | Cyrl;         | N/A              | **FALSE**    | ERROR\_INVALID\_PARAMETER |
| Hani;Hira;Kana; |               | N/A              | **FALSE**    | ERROR\_SUCCESS            |



 

The required header file and DLL are part of the ["Microsoft Internationalized Domain Name (IDN) Mitigation APIs"](https://www.microsoft.com/downloads/details.aspx?FamilyID=AD6158D7-DDBA-416A-9109-07607425A815&displaylang=en) download, available at the [MSDN Download Center](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                         |
| Redistributable<br/>          | Microsoft Internationalized Domain Name (IDN) Mitigation APIs onWindows XP with SP2,Windows Server 2003 with SP1, orWindows Vista<br/> |
| Header<br/>                   | <dl> <dt>Idndl.h</dt> </dl>                                                           |
| DLL<br/>                      | <dl> <dt>Idndl.dll</dt> </dl>                                                         |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[Handling Internationalized Domain Names (IDNs)](handling-internationalized-domain-names--idns.md)
</dt> <dt>

[**DownlevelGetLocaleScripts**](downlevelgetlocalescripts.md)
</dt> <dt>

[**DownlevelGetStringScripts**](downlevelgetstringscripts.md)
</dt> <dt>

[**VerifyScripts**](/windows/desktop/api/Winnls/nf-winnls-verifyscripts)
</dt> </dl>

 

 
