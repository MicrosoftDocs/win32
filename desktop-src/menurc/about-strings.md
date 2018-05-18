---
title: About Strings
description: This topic discusses string functions.
ms.assetid: 'f1799fbf-4619-4b19-998e-b1d2f4c19a35'
keywords: ["resources,strings", "strings", "string functions"]
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
| [strcat](http://go.microsoft.com/fwlink/p/?linkid=192489) | [**lstrcat**](lstrcat.md) | <dl> <dt>[**StringCchCat**](stringcchcat.md)</dt> <dt>[**StringCchCatEx**](stringcchcatex.md)</dt> <dt>[**StringCbCat**](stringcbcat.md)</dt> <dt>[**StringCbCatEx**](stringcbcatex.md)</dt> </dl>         |
| [strcmp](http://go.microsoft.com/fwlink/p/?linkid=192493) | [**lstrcmp**](lstrcmp.md) | (no equivalent function)                                                                                                                                                                                                                                                                                                                                                                                  |
| [strcpy](http://go.microsoft.com/fwlink/p/?linkid=192494) | [**lstrcpy**](lstrcpy.md) | <dl> <dt>[**StringCchCopy**](stringcchcopy.md)</dt> <dt>[**StringCchCopyEx**](stringcchcopyex.md)</dt> <dt>[**StringCbCopy**](stringcbcopy.md)</dt> <dt>[**StringCbCopyEx**](stringcbcopyex.md)</dt> </dl> |
| [strlen](http://go.microsoft.com/fwlink/p/?linkid=192495) | [**lstrlen**](lstrlen.md) | <dl> <dt>[**StringCchLength**](stringcchlength.md)</dt> <dt>[**StringCbLength**](stringcblength.md)</dt> </dl>                                                                                                                                                                                       |



 

The **strlen** function, for example, always returns the number of bytes in a string, but the [**lstrlen**](lstrlen.md) function returns the number of **TCHAR** values, which refers to bytes for ANSI versions of the function or **WCHAR** values for Unicode versions.

The following string functions differ from standard C functions such as **tolower** and **toupper** in that they operate on any character in a character set. By using the [**CharLower**](charlower.md) function, for example, an application can convert an uppercase U with an umlaut (Ü) to lowercase (ü). For more information about character sets, see [Single-byte Character Sets](https://msdn.microsoft.com/library/windows/desktop/dd374056).



| Function                               | Description                                   |
|----------------------------------------|-----------------------------------------------|
| [**CharLower**](charlower.md)         | Converts a character or string to lowercase.  |
| [**CharLowerBuff**](charlowerbuff.md) | Converts a character string to lowercase.     |
| [**CharNext**](charnext.md)           | Moves to the next character in a string.      |
| [**CharPrev**](charprev.md)           | Moves to the preceding character in a string. |
| [**CharUpper**](charupper.md)         | Converts a character or string to uppercase.  |
| [**CharUpperBuff**](charupperbuff.md) | Converts a string to uppercase.               |



 

The following string functions make determinations about a character based on the semantics of the language selected by the user. These functions are Unicode enabled.



| Function                                         | Description                                     |
|--------------------------------------------------|-------------------------------------------------|
| [**IsCharAlpha**](ischaralpha.md)               | Determines whether a character is alphabetic.   |
| [**IsCharAlphaNumeric**](ischaralphanumeric.md) | Determines whether a character is alphanumeric. |
| [**IsCharLower**](ischarlower.md)               | Determines whether a character is lowercase.    |
| [**IsCharUpper**](ischarupper.md)               | Determines whether a character is uppercase.    |



 

The following table shows the Unicode extensions to the standard C run-time (CRT) functions. As mentioned previously, the StrSafe functions enable safer handling of strings and are recommended for better security for your application.



| Standard CRT function                                       | String Function                | StrSafe Function                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [sprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)  | [**wsprintf**](wsprintf.md)   | <dl> <dt>[**StringCchPrintf**](stringcchprintf.md)</dt> <dt>[**StringCchPrintfEx**](stringcchprintfex.md)</dt> <dt>[**StringCbPrintf**](stringcbprintf.md)</dt> <dt>[**StringCbPrintfEx**](stringcbprintfex.md)</dt> </dl>         |
| [vsprintf](http://go.microsoft.com/fwlink/p/?linkid=192500) | [**wvsprintf**](wvsprintf.md) | <dl> <dt>[**StringCchVPrintf**](stringcchvprintf.md)</dt> <dt>[**StringCchVPrintfEx**](stringcchvprintfex.md)</dt> <dt>[**StringCbVPrintf**](stringcbvprintf.md)</dt> <dt>[**StringCbVPrintfEx**](stringcbvprintfex.md)</dt> </dl> |



 

## String Resources

An application that maintains character strings in resources can be translated into new languages with minimum effort. Instead of searching for strings in the source modules, you can simply translate the strings in the resource file and relink the application. In addition, using string resources simplifies creation of Unicode and non-Unicode versions of the application from the same source files.

The [**LoadString**](loadstring.md) function loads a string resource from an application's executable file. The [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function loads a string resource and interprets formatting options that may be embedded in the string.

Resources in binary form are stored in Unicode format. When loading resources, applications can use the Unicode version of the resource functions ([**LoadStringW**](loadstring.md), for example) to obtain resources as Unicode data.

For 16-bit string resources, 255 characters is the maximum length. For 32-bit string resources, 65535 characters is the maximum length.

 

 




