---
description: Provides a list of scripts used in the specified Unicode string.
ms.assetid: 3ad23613-8d0c-432a-b352-637c373a0980
title: DownlevelGetStringScripts function (Idndl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownlevelGetStringScripts
api_type: 
- DllExport
api_location: 
- Idndl.dll
---

# DownlevelGetStringScripts function

Provides a list of scripts used in the specified Unicode string.

> [!Note]  
> This function is used only by applications that run on pre-Windows Vista operating systems. Its use requires the download package. Applications that only run on Windows Vista and later should call [**GetStringScripts**](/windows/desktop/api/Winnls/nf-winnls-getstringscripts).

 

## Syntax


```C++
int DownlevelGetStringScripts(
  _In_  DWORD   dwFlags,
  _In_  LPCWSTR lpString,
  _In_  int     cchString,
  _Out_ LPWSTR  lpScripts,
  _In_  int     cchScripts
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying options for script retrieval.



| Value                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GSS_ALLOW_INHERITED_COMMON"></span><span id="gss_allow_inherited_common"></span><dl> <dt>**GSS\_ALLOW\_INHERITED\_COMMON**</dt> </dl> | Retrieve "Qaii" (INHERITED) and "Zyyy" (COMMON) script information. This value does not affect the processing of unassigned characters. These characters in the input string always cause a "Zzzz" (UNASSIGNED script) to appear in the script string.<br/> |



 

> [!Note]  
> By default, this function ignores any inherited or common characters in the input Unicode string. If GSS\_ALLOW\_INHERITED\_COMMON is not set, neither "Qaii" nor "Zyyy" will appear in the script string, even if the input string contains such characters. If GSS\_ALLOW\_INHERITED\_COMMON is set, and if the input string contains inherited and/or common characters, "Qaii" and/or "Zyyy" appear in the script string. See the Remarks section.

 

</dd> <dt>

*lpString* \[in\]
</dt> <dd>

Pointer to the Unicode string to analyze.

</dd> <dt>

*cchString* \[in\]
</dt> <dd>

Size, in characters, of the Unicode string indicated by *lpString*. The application sets this parameter to -1 if the string is null-terminated. If the application sets this parameter to 0, the function retrieves a null Unicode string (L"\\0") in *lpScripts* and returns 1.

</dd> <dt>

*lpScripts* \[out\]
</dt> <dd>

Pointer to a buffer in which this function retrieves a null-terminated string representing a list of scripts, using the 4-character notation used in [ISO 15924](https://www.unicode.org/iso15924/iso15924-codes.html). Each script name consists of four Latin characters, and the names are retrieved in alphabetical order. Each name, including the last, is followed by a semicolon.

Alternatively, this parameter can contain **NULL** if *cchScripts* set to 0. In this case, the function returns the required size for the script buffer.

</dd> <dt>

*cchScripts* \[in\]
</dt> <dd>

Size, in characters, for the script buffer indicated by *lpScripts*.

Alternatively, the application can set this parameter to 0. In this case, the function retrieves **NULL** in *lpScripts* and returns the required size for the script buffer.

</dd> </dl>

## Return value

Returns the number of characters retrieved in the output buffer, including a terminating null character, if successful and *cchScripts* is set to a nonzero value. The function returns 1 to indicate that no script has been found, for example, when the input string only contains COMMON or INHERITED characters and GSS\_ALLOW\_INHERITED\_COMMON is not set. Given that each found script adds five characters (four characters + delimiter), a simple mathematical operation provides the script count as (return\_code - 1) / 5.

If the function succeeds and the value of *cchScripts* is 0, the return value is the required size, in characters including a terminating null character, for the script buffer. The script count is as described above.

The function returns 0 if it does not succeed. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_BADDB. The function could not access the data. This situation should not normally occur, and typically indicates a bad installation, a disk problem, or the like.
-   ERROR\_INSUFFICIENT\_BUFFER. A supplied buffer size was not large enough, or it was incorrectly set to **NULL**.
-   ERROR\_INVALID\_FLAGS. The values supplied for flags were not valid.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function is useful as part of a strategy to mitigate security issues related to [internationalized domain names (IDNs)](handling-internationalized-domain-names--idns.md).

The script determination is based on the script values published by the Unicode Consortium in <https://www.unicode.org/Public/4.1.0/ucd/Scripts.txt>, except that the unassigned characters have the value "Zzzz" (UNASSIGNED) instead of "Zyyy" (COMMON).

Here are some examples of the behavior of this function:



Input string

*dwFlags*

*lpScripts*

Scripts

Microsoft.com

0

Latn;

Latin

Microsoft.com

GSS\_ALLOW\_INHERITED\_COMMON

Latn;Zyyy;

Latin + Common

${ROWSPAN2}$Niño${REMOVE}$  

004E 0069 0241 006F

${ROWSPAN2}$GSS\_ALLOW\_INHERITED\_COMMON${REMOVE}$  

${ROWSPAN2}$Latn;${REMOVE}$  

${ROWSPAN2}$Latin${REMOVE}$  

Uses LATIN SMALL LETTER N WITH TILDE

${ROWSPAN2}$Niño${REMOVE}$  

004E 0069 006E 0303 006F

${ROWSPAN2}$GSS\_ALLOW\_INHERITED\_COMMON${REMOVE}$  

${ROWSPAN2}$Latn;Qaii;${REMOVE}$  

${ROWSPAN2}$Latin + Inherited${REMOVE}$  

Uses COMBINING TILDE

${ROWSPAN2}$Spооf${REMOVE}$  

0053 0070 043e 043e 0066

${ROWSPAN2}$0${REMOVE}$  

${ROWSPAN2}$Latn;Cyrl;${REMOVE}$  

${ROWSPAN2}$Latin + Cyrillic${REMOVE}$  

Uses CYRILLIC SMALL LETTER O



U+f000

0

Zzzz;

Unassigned



U+f000

GSS\_ALLOW\_INHERITED\_COMMON

Zzzz;

Unassigned



 

The required header file and DLL are part of the ["Microsoft Internationalized Domain Name (IDN) Mitigation APIs"](https://www.microsoft.com/downloads/details.aspx?FamilyID=AD6158D7-DDBA-416A-9109-07607425A815&displaylang=en%0A) download, available at the [MSDN Download Center](https://www.microsoft.com/?ref=go).

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

[**DownlevelGetLocaleScripts**](downlevelgetlocalescripts.md)
</dt> <dt>

[**DownlevelVerifyScripts**](downlevelverifyscripts.md)
</dt> <dt>

[**GetStringScripts**](/windows/desktop/api/Winnls/nf-winnls-getstringscripts)
</dt> </dl>

 

 
