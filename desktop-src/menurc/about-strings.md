---
title: About Strings
description: Describes string functions, which give applications the means to copy, compare, sort, format, and convert character strings.
ms.assetid: f1799fbf-4619-4b19-998e-b1d2f4c19a35
keywords:
- resources,strings
- strings
- string functions
ms.topic: article
ms.date: 05/31/2018
---

# About Strings

The string functions give applications the means to copy, compare, sort, format, and convert character strings as well as the means to determine the character type of each character in a string. All the string functions support the single-byte, double-byte, and Unicode character sets if these character sets are supported by the operating system on which the application is run.

**Security Warning:** The incorrect use of string functions can cause security problems for your application. Typically this involves a buffer overrun which can allow a denial of service attack against your application or the injection of executable code from an attacker. The Strsafe functions enable the safer handling of strings and are recommended for better security for your application. For more information on these functions, see [Using the Strsafe.h Functions](strsafe-ovw.md).

This section discusses the following topics.

-   [Comparison with C Run-Time String Functions](#comparison-with-c-run-time-string-functions)
-   [String Resources](#string-resources)

## Comparison with C Run-Time String Functions

Many string functions duplicate or enhance familiar string functions from the standard C run-time (CRT) library. Many of the enhancements enable the string functions to work with Unicode or extended character sets. The following table shows the CRT functions, the Windows functions (that support Unicode, unlike the CRT functions), and the StrSafe functions.



| CRT String Function                                       | Windows String Function    | StrSafe Function                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [strcat](/cpp/c-runtime-library/reference/strcat-wcscat-mbscat) | [**lstrcat**](/windows/desktop/api/Winbase/nf-winbase-lstrcata) | <dl> <dt>[**StringCchCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcata)</dt> <dt>[**StringCchCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatexa)</dt> <dt>[**StringCbCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcata)</dt> <dt>[**StringCbCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatexa)</dt> </dl>         |
| [strcmp](/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp) | [**lstrcmp**](/windows/desktop/api/Winbase/nf-winbase-lstrcmpa) | (no equivalent function)                                                                                                                                                                                                                                                                                                                                                                                  |
| [strcpy](/cpp/c-runtime-library/reference/strcpy-wcscpy-mbscpy) | [**lstrcpy**](/windows/desktop/api/Winbase/nf-winbase-lstrcpya) | <dl> <dt>[**StringCchCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopya)</dt> <dt>[**StringCchCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopyexa)</dt> <dt>[**StringCbCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopya)</dt> <dt>[**StringCbCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopyexa)</dt> </dl> |
| [strlen](/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) | [**lstrlen**](/windows/desktop/api/Winbase/nf-winbase-lstrlena) | <dl> <dt>[**StringCchLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchlengtha)</dt> <dt>[**StringCbLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcblengtha)</dt> </dl>                                                                                                                                                                                       |



 

The **strlen** function, for example, always returns the number of bytes in a string, but the [**lstrlen**](/windows/desktop/api/Winbase/nf-winbase-lstrlena) function returns the number of **TCHAR** values, which refers to bytes for ANSI versions of the function or **WCHAR** values for Unicode versions.

The following string functions differ from standard C functions such as **tolower** and **toupper** in that they operate on any character in a character set. By using the [**CharLower**](/windows/desktop/api/Winuser/nf-winuser-charlowera) function, for example, an application can convert an uppercase U with an umlaut (Ü) to lowercase (ü). For more information about character sets, see [Single-byte Character Sets](/windows/desktop/Intl/single-byte-character-sets).



| Function                               | Description                                   |
|----------------------------------------|-----------------------------------------------|
| [**CharLower**](/windows/desktop/api/Winuser/nf-winuser-charlowera)         | Converts a character or string to lowercase.  |
| [**CharLowerBuff**](/windows/desktop/api/Winuser/nf-winuser-charlowerbuffa) | Converts a character string to lowercase.     |
| [**CharNext**](/windows/desktop/api/Winuser/nf-winuser-charnexta)           | Moves to the next character in a string.      |
| [**CharPrev**](/windows/desktop/api/Winuser/nf-winuser-charpreva)           | Moves to the preceding character in a string. |
| [**CharUpper**](/windows/desktop/api/Winuser/nf-winuser-charuppera)         | Converts a character or string to uppercase.  |
| [**CharUpperBuff**](/windows/desktop/api/Winuser/nf-winuser-charupperbuffa) | Converts a string to uppercase.               |



 

The following string functions make determinations about a character based on the semantics of the language selected by the user. These functions are Unicode enabled.



| Function                                         | Description                                     |
|--------------------------------------------------|-------------------------------------------------|
| [**IsCharAlpha**](/windows/desktop/api/Winuser/nf-winuser-ischaralphaa)               | Determines whether a character is alphabetic.   |
| [**IsCharAlphaNumeric**](/windows/desktop/api/Winuser/nf-winuser-ischaralphanumerica) | Determines whether a character is alphanumeric. |
| [**IsCharLower**](/windows/desktop/api/Winuser/nf-winuser-ischarlowera)               | Determines whether a character is lowercase.    |
| [**IsCharUpper**](/windows/desktop/api/Winuser/nf-winuser-ischaruppera)               | Determines whether a character is uppercase.    |



 

The following table shows the Unicode extensions to the standard C run-time (CRT) functions. As mentioned previously, the StrSafe functions enable safer handling of strings and are recommended for better security for your application.



| Standard CRT function                                       | String Function                | StrSafe Function                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [sprintf](/cpp/c-runtime-library/reference/sprintf-sprintf-l-swprintf-swprintf-l-swprintf-l)  | [**wsprintf**](/windows/desktop/api/Winuser/nf-winuser-wsprintfa)   | <dl> <dt>[**StringCchPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfa)</dt> <dt>[**StringCchPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfexa)</dt> <dt>[**StringCbPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfa)</dt> <dt>[**StringCbPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfexa)</dt> </dl>         |
| [vsprintf](/cpp/c-runtime-library/reference/vsprintf-vsprintf-l-vswprintf-vswprintf-l-vswprintf-l) | [**wvsprintf**](/windows/desktop/api/Winuser/nf-winuser-wvsprintfa) | <dl> <dt>[**StringCchVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfa)</dt> <dt>[**StringCchVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfexa)</dt> <dt>[**StringCbVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfa)</dt> <dt>[**StringCbVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfexa)</dt> </dl> |



 

## String Resources

An application that maintains character strings in resources can be translated into new languages with minimum effort. Instead of searching for strings in the source modules, you can simply translate the strings in the resource file and relink the application. In addition, using string resources simplifies creation of Unicode and non-Unicode versions of the application from the same source files.

The [**LoadString**](/windows/desktop/api/Winuser/nf-winuser-loadstringa) function loads a string resource from an application's executable file. The [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) function loads a string resource and interprets formatting options that may be embedded in the string.

Resources in binary form are stored in Unicode format. When loading resources, applications can use the Unicode version of the resource functions ([**LoadStringW**](/windows/desktop/api/Winuser/nf-winuser-loadstringa), for example) to obtain resources as Unicode data.

For 16-bit string resources, 255 characters is the maximum length. For 32-bit string resources, 65535 characters is the maximum length.

 

 