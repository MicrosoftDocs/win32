---
title: About Strings
description: This topic discusses string functions.
ms.assetid: f1799fbf-4619-4b19-998e-b1d2f4c19a35
keywords:
- resources,strings
- strings
- string functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [strcat](http://go.microsoft.com/fwlink/p/?linkid=192489) | [**lstrcat**](/windows/win32/Winbase/nf-winbase-lstrcata?branch=master) | <dl> <dt>[**StringCchCat**](/windows/win32/Strsafe/nf-strsafe-stringcchcata?branch=master)</dt> <dt>[**StringCchCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcatexa?branch=master)</dt> <dt>[**StringCbCat**](/windows/win32/Strsafe/nf-strsafe-stringcbcata?branch=master)</dt> <dt>[**StringCbCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcatexa?branch=master)</dt> </dl>         |
| [strcmp](http://go.microsoft.com/fwlink/p/?linkid=192493) | [**lstrcmp**](/windows/win32/Winbase/nf-winbase-lstrcmpa?branch=master) | (no equivalent function)                                                                                                                                                                                                                                                                                                                                                                                  |
| [strcpy](http://go.microsoft.com/fwlink/p/?linkid=192494) | [**lstrcpy**](/windows/win32/Winbase/nf-winbase-lstrcpya?branch=master) | <dl> <dt>[**StringCchCopy**](/windows/win32/Strsafe/nf-strsafe-stringcchcopya?branch=master)</dt> <dt>[**StringCchCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcopyexa?branch=master)</dt> <dt>[**StringCbCopy**](/windows/win32/Strsafe/nf-strsafe-stringcbcopya?branch=master)</dt> <dt>[**StringCbCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcopyexa?branch=master)</dt> </dl> |
| [strlen](http://go.microsoft.com/fwlink/p/?linkid=192495) | [**lstrlen**](/windows/win32/Winbase/nf-winbase-lstrlena?branch=master) | <dl> <dt>[**StringCchLength**](/windows/win32/Strsafe/nf-strsafe-stringcchlengtha?branch=master)</dt> <dt>[**StringCbLength**](/windows/win32/Strsafe/nf-strsafe-stringcblengtha?branch=master)</dt> </dl>                                                                                                                                                                                       |



 

The **strlen** function, for example, always returns the number of bytes in a string, but the [**lstrlen**](/windows/win32/Winbase/nf-winbase-lstrlena?branch=master) function returns the number of **TCHAR** values, which refers to bytes for ANSI versions of the function or **WCHAR** values for Unicode versions.

The following string functions differ from standard C functions such as **tolower** and **toupper** in that they operate on any character in a character set. By using the [**CharLower**](/windows/win32/Winuser/nf-winuser-charlowera?branch=master) function, for example, an application can convert an uppercase U with an umlaut (Ü) to lowercase (ü). For more information about character sets, see [Single-byte Character Sets](https://msdn.microsoft.com/library/windows/desktop/dd374056).



| Function                               | Description                                   |
|----------------------------------------|-----------------------------------------------|
| [**CharLower**](/windows/win32/Winuser/nf-winuser-charlowera?branch=master)         | Converts a character or string to lowercase.  |
| [**CharLowerBuff**](/windows/win32/Winuser/nf-winuser-charlowerbuffa?branch=master) | Converts a character string to lowercase.     |
| [**CharNext**](/windows/win32/Winuser/nf-winuser-charnexta?branch=master)           | Moves to the next character in a string.      |
| [**CharPrev**](/windows/win32/Winuser/nf-winuser-charpreva?branch=master)           | Moves to the preceding character in a string. |
| [**CharUpper**](/windows/win32/Winuser/nf-winuser-charuppera?branch=master)         | Converts a character or string to uppercase.  |
| [**CharUpperBuff**](/windows/win32/Winuser/nf-winuser-charupperbuffa?branch=master) | Converts a string to uppercase.               |



 

The following string functions make determinations about a character based on the semantics of the language selected by the user. These functions are Unicode enabled.



| Function                                         | Description                                     |
|--------------------------------------------------|-------------------------------------------------|
| [**IsCharAlpha**](/windows/win32/Winuser/nf-winuser-ischaralphaa?branch=master)               | Determines whether a character is alphabetic.   |
| [**IsCharAlphaNumeric**](/windows/win32/Winuser/nf-winuser-ischaralphanumerica?branch=master) | Determines whether a character is alphanumeric. |
| [**IsCharLower**](/windows/win32/Winuser/nf-winuser-ischarlowera?branch=master)               | Determines whether a character is lowercase.    |
| [**IsCharUpper**](/windows/win32/Winuser/nf-winuser-ischaruppera?branch=master)               | Determines whether a character is uppercase.    |



 

The following table shows the Unicode extensions to the standard C run-time (CRT) functions. As mentioned previously, the StrSafe functions enable safer handling of strings and are recommended for better security for your application.



| Standard CRT function                                       | String Function                | StrSafe Function                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [sprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)  | [**wsprintf**](/windows/win32/Winuser/nf-winuser-wsprintfa?branch=master)   | <dl> <dt>[**StringCchPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfa?branch=master)</dt> <dt>[**StringCchPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfexa?branch=master)</dt> <dt>[**StringCbPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfa?branch=master)</dt> <dt>[**StringCbPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfexa?branch=master)</dt> </dl>         |
| [vsprintf](http://go.microsoft.com/fwlink/p/?linkid=192500) | [**wvsprintf**](/windows/win32/Winuser/nf-winuser-wvsprintfa?branch=master) | <dl> <dt>[**StringCchVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfa?branch=master)</dt> <dt>[**StringCchVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfexa?branch=master)</dt> <dt>[**StringCbVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfa?branch=master)</dt> <dt>[**StringCbVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfexa?branch=master)</dt> </dl> |



 

## String Resources

An application that maintains character strings in resources can be translated into new languages with minimum effort. Instead of searching for strings in the source modules, you can simply translate the strings in the resource file and relink the application. In addition, using string resources simplifies creation of Unicode and non-Unicode versions of the application from the same source files.

The [**LoadString**](/windows/win32/Winuser/nf-winuser-loadstringa?branch=master) function loads a string resource from an application's executable file. The [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function loads a string resource and interprets formatting options that may be embedded in the string.

Resources in binary form are stored in Unicode format. When loading resources, applications can use the Unicode version of the resource functions ([**LoadStringW**](/windows/win32/Winuser/nf-winuser-loadstringa?branch=master), for example) to obtain resources as Unicode data.

For 16-bit string resources, 255 characters is the maximum length. For 32-bit string resources, 65535 characters is the maximum length.

 

 




