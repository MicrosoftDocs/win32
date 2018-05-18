---
title: About Strsafe.h
description: Poor buffer handling is implicated in many security issues that involve buffer overruns.
ms.assetid: 'a104a260-1edb-441a-acf8-e2bd3a7d8235'
keywords: ["string functions", "Strsafe.h", "Strsafe functions"]
---

# About Strsafe.h

Poor buffer handling is implicated in many security issues that involve buffer overruns. The functions defined in Strsafe.h provide additional processing for proper buffer handling in your code. For this reason, they are intended to replace their built-in C/C++ counterparts as well as specific Windows implementations. Strsafe.h is available in the Windows SDK starting with Windows XP with Service Pack 2 (SP2).

The advantages of the Strsafe functions include:

-   The size of the destination buffer is always provided to the function to ensure that the function does not write past the end of the buffer.

-   Buffers are guaranteed to be null-terminated, even if the operation truncates the intended result.

-   All functions return an **HRESULT** value, with only one possible success code (**S\_OK**).

-   Each function is available in a corresponding character count ("cch") or byte count ("cb") version.

-   Most functions have an extended ("Ex") version available for advanced functionality.

See the following sections for details.

-   [Character Count Functions](#character-count-functions)
-   [Byte Count Functions](#byte-count-functions)
-   [Using Strsafe.h](#using-strsafeh)
-   [Related topics](#related-topics)

## Character Count Functions

The following functions use a character count rather than a byte count.



| Function                                                                                                                                                                                                                      | Replaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>[**StringCchCat**](stringcchcat.md)</dt> <dt>[**StringCchCatEx**](stringcchcatex.md)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](http://go.microsoft.com/fwlink/p/?linkid=192489)</dt> <dt>[**lstrcat**](lstrcat.md)</dt> <dt>[**StrCat**](https://msdn.microsoft.com/library/windows/desktop/bb759925)</dt> <dt>[**StrCatBuff**](https://msdn.microsoft.com/library/windows/desktop/bb759928)</dt> </dl>                                                                             |
| <dl> <dt>[**StringCchCatN**](stringcchcatn.md)</dt> <dt>[**StringCchCatNEx**](stringcchcatnex.md)</dt> </dl>             | <dl> <dt>[strncat](http://go.microsoft.com/fwlink/p/?linkid=192505)</dt> <dt>[**StrNCat**](https://msdn.microsoft.com/library/windows/desktop/bb759987)</dt> </dl>                                                                                                                                                                                                                                                                   |
| <dl> <dt>[**StringCchCopy**](stringcchcopy.md)</dt> <dt>[**StringCchCopyEx**](stringcchcopyex.md)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](http://go.microsoft.com/fwlink/p/?linkid=192494)</dt> <dt>[**lstrcpy**](lstrcpy.md)</dt> <dt>[**StrCpy**](https://msdn.microsoft.com/library/windows/desktop/bb759960)</dt> </dl>                                                                                                                                                                    |
| <dl> <dt>[**StringCchCopyN**](stringcchcopyn.md)</dt> <dt>[**StringCchCopyNEx**](stringcchcopynex.md)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](http://go.microsoft.com/fwlink/p/?linkid=192506)</dt> </dl>                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>[**StringCchGets**](stringcchgets.md)</dt> <dt>[**StringCchGetsEx**](stringcchgetsex.md)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](http://go.microsoft.com/fwlink/p/?linkid=192504)</dt> </dl>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>[**StringCchPrintf**](stringcchprintf.md)</dt> <dt>[**StringCchPrintfEx**](stringcchprintfex.md)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)</dt> <dt>[**wsprintf**](wsprintf.md)</dt> <dt>[**wnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773455)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](http://go.microsoft.com/fwlink/p/?linkid=192507)</dt> </dl>          |
| <dl> <dt>[**StringCchVPrintf**](stringcchvprintf.md)</dt> <dt>[**StringCchVPrintfEx**](stringcchvprintfex.md)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](http://go.microsoft.com/fwlink/p/?linkid=192500)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](http://go.microsoft.com/fwlink/p/?linkid=192508)</dt> <dt>[**wvsprintf**](wvsprintf.md)</dt> <dt>[**wvnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773458)</dt> </dl>, |
| <dl> <dt>[**StringCchLength**](stringcchlength.md)</dt> </dl>                                                                                                         | <dl> <dt>[strlen, wcslen, \_tcslen](http://go.microsoft.com/fwlink/p/?linkid=192495)</dt> </dl>                                                                                                                                                                                                                                                                                                                                    |



 

## Byte Count Functions

The following functions use a byte count rather than a character count.



| Function                                                                                                                                                                                                                  | Replaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>[**StringCbCat**](stringcbcat.md)</dt> <dt>[**StringCbCatEx**](stringcbcatex.md)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](http://go.microsoft.com/fwlink/p/?linkid=192489)</dt> <dt>[**lstrcat**](lstrcat.md)</dt> <dt>[**StrCat**](https://msdn.microsoft.com/library/windows/desktop/bb759925)</dt> <dt>[**StrCatBuff**](https://msdn.microsoft.com/library/windows/desktop/bb759928)</dt> </dl>                                                                            |
| <dl> <dt>[**StringCbCatN**](stringcbcatn.md)</dt> <dt>[**StringCbCatNEx**](stringcbcatnex.md)</dt> </dl>             | <dl> <dt>[strncat](http://go.microsoft.com/fwlink/p/?linkid=192505)</dt> <dt>[**StrNCat**](https://msdn.microsoft.com/library/windows/desktop/bb759987)</dt> </dl>                                                                                                                                                                                                                                                                  |
| <dl> <dt>[**StringCbCopy**](stringcbcopy.md)</dt> <dt>[**StringCbCopyEx**](stringcbcopyex.md)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](http://go.microsoft.com/fwlink/p/?linkid=192494)</dt> <dt>[**lstrcpy**](lstrcpy.md)</dt> <dt>[**StrCpy**](https://msdn.microsoft.com/library/windows/desktop/bb759960)</dt> </dl>                                                                                                                                                                   |
| <dl> <dt>[**StringCbCopyN**](stringcbcopyn.md)</dt> <dt>[**StringCbCopyNEx**](stringcbcopynex.md)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](http://go.microsoft.com/fwlink/p/?linkid=192506)</dt> </dl>                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>[**StringCbGets**](stringcbgets.md)</dt> <dt>[**StringCbGetsEx**](stringcbgetsex.md)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](http://go.microsoft.com/fwlink/p/?linkid=192504)</dt> </dl>                                                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>[**StringCbPrintf**](stringcbprintf.md)</dt> <dt>[**StringCbPrintfEx**](stringcbprintfex.md)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)</dt> <dt>[**wsprintf**](wsprintf.md)</dt> <dt>[**wnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773455)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](http://go.microsoft.com/fwlink/p/?linkid=192507)</dt> </dl>         |
| <dl> <dt>[**StringCbVPrintf**](stringcbvprintf.md)</dt> <dt>[**StringCbVPrintfEx**](stringcbvprintfex.md)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](http://go.microsoft.com/fwlink/p/?linkid=192500)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](http://go.microsoft.com/fwlink/p/?linkid=192508)</dt> <dt>[**wvsprintf**](wvsprintf.md)</dt> <dt>[**wvnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773458)</dt> </dl> |
| <dl> <dt>[**StringCbLength**](stringcblength.md)</dt> </dl>                                                                                                       | <dl> <dt>[strlen, wcslen, \_tcslen](http://go.microsoft.com/fwlink/p/?linkid=192495)</dt> </dl>                                                                                                                                                                                                                                                                                                                                   |



 

## Using Strsafe.h

-   To use the Strsafe functions inline, include the header file as shown here, following the **\#include** statements for all other header files.

    `#include <strsafe.h>`

-   To use the functions in library form, include the following statement before including Strsafe.h. However, it is recommended that you use the inline functions.

    `#define STRSAFE_LIB`

    > [!Note]  
    > : The following functions must be used as inline functions: [**StringCbGets**](stringcbgets.md), [**StringCbGetsEx**](stringcbgetsex.md), [**StringCchGets**](stringcchgets.md), and [**StringCchGetsEx**](stringcchgetsex.md).

     

-   When you include Strsafe.h in your file, the older functions replaced by the Strsafe.h functions will be deprecated. Attempts to use these older functions will result in a compiler error telling you to use the newer functions. If you want to override this behavior, include the following statement before including Strsafe.h.

    `#define STRSAFE_NO_DEPRECATE`

-   To allow only character count functions, include the following statement before including Strsafe.h.

    `#define STRSAFE_NO_CB_FUNCTIONS`

-   To allow only byte count functions, include the following statement before including Strsafe.h.

    `#define STRSAFE_NO_CCH_FUNCTIONS`

    > [!Note]  
    > You can define **STRSAFE\_NO\_CB\_FUNCTIONS** or **STRSAFE\_NO\_CCH\_FUNCTIONS**, but not both.

     

-   Some Strsafe functions have locale-aware versions. By default, the header does not declare these functions. To enable these declarations, include the following macro statement before including Strsafe.h.

    `#define STRSAFE_LOCALE_FUNCTIONS`

-   The maximum supported string length is 2,147,483,647 (**STRSAFE\_MAX\_CCH**) characters, either ANSI or Unicode.

## Related topics

<dl> <dt>

[Strsafe Functions](string-overviews.md)
</dt> </dl>

 

 




