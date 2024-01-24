---
title: About Strsafe.h
description: Poor buffer handling is implicated in many security issues that involve buffer overruns.
ms.assetid: a104a260-1edb-441a-acf8-e2bd3a7d8235
keywords:
- string functions
- Strsafe.h
- Strsafe functions
ms.topic: article
ms.date: 05/31/2018
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
| <dl> <dt>[**StringCchCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcata)</dt> <dt>[**StringCchCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatexa)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](/cpp/c-runtime-library/reference/strcat-wcscat-mbscat)</dt> <dt>[**lstrcat**](/windows/desktop/api/Winbase/nf-winbase-lstrcata)</dt> <dt>[**StrCat**](/windows/desktop/api/shlwapi/nf-shlwapi-strcatw)</dt> <dt>[**StrCatBuff**](/windows/desktop/api/shlwapi/nf-shlwapi-strcatbuffa)</dt> </dl>                                                                             |
| <dl> <dt>[**StringCchCatN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatna)</dt> <dt>[**StringCchCatNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatnexa)</dt> </dl>             | <dl> <dt>[strncat](/cpp/c-runtime-library/reference/strncat-strncat-l-wcsncat-wcsncat-l-mbsncat-mbsncat-l)</dt> <dt>[**StrNCat**](/windows/desktop/api/shlwapi/nf-shlwapi-strncata)</dt> </dl>                                                                                                                                                                                                                                                                   |
| <dl> <dt>[**StringCchCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopya)</dt> <dt>[**StringCchCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopyexa)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](/cpp/c-runtime-library/reference/strcpy-wcscpy-mbscpy)</dt> <dt>[**lstrcpy**](/windows/desktop/api/Winbase/nf-winbase-lstrcpya)</dt> <dt>[**StrCpy**](/windows/desktop/api/shlwapi/nf-shlwapi-strcpyw)</dt> </dl>                                                                                                                                                                    |
| <dl> <dt>[**StringCchCopyN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopyna)</dt> <dt>[**StringCchCopyNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopynexa)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](/cpp/c-runtime-library/reference/strncpy-strncpy-l-wcsncpy-wcsncpy-l-mbsncpy-mbsncpy-l)</dt> </dl>                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>[**StringCchGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsa)</dt> <dt>[**StringCchGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsexa)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](/cpp/c-runtime-library/gets-getws)</dt> </dl>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>[**StringCchPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfa)</dt> <dt>[**StringCchPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfexa)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](/cpp/c-runtime-library/reference/sprintf-sprintf-l-swprintf-swprintf-l-swprintf-l)</dt> <dt>[**wsprintf**](/windows/desktop/api/Winuser/nf-winuser-wsprintfa)</dt> <dt>[**wnsprintf**](/windows/desktop/api/shlwapi/nf-shlwapi-wnsprintfa)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](/cpp/c-runtime-library/reference/snprintf-snprintf-snprintf-l-snwprintf-snwprintf-l)</dt> </dl>          |
| <dl> <dt>[**StringCchVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfa)</dt> <dt>[**StringCchVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfexa)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](/cpp/c-runtime-library/reference/vsprintf-vsprintf-l-vswprintf-vswprintf-l-vswprintf-l)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](/cpp/c-runtime-library/reference/vsnprintf-vsnprintf-vsnprintf-l-vsnwprintf-vsnwprintf-l)</dt> <dt>[**wvsprintf**](/windows/desktop/api/Winuser/nf-winuser-wvsprintfa)</dt> <dt>[**wvnsprintf**](/windows/desktop/api/shlwapi/nf-shlwapi-wvnsprintfa)</dt> </dl>, |
| <dl> <dt>[**StringCchLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchlengtha)</dt> </dl>                                                                                                         | <dl> <dt>[strlen, wcslen, \_tcslen](/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l)</dt> </dl>                                                                                                                                                                                                                                                                                                                                    |



 

## Byte Count Functions

The following functions use a byte count rather than a character count.



| Function                                                                                                                                                                                                                  | Replaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>[**StringCbCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcata)</dt> <dt>[**StringCbCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatexa)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](/cpp/c-runtime-library/reference/strcat-wcscat-mbscat)</dt> <dt>[**lstrcat**](/windows/desktop/api/Winbase/nf-winbase-lstrcata)</dt> <dt>[**StrCat**](/windows/desktop/api/shlwapi/nf-shlwapi-strcatw)</dt> <dt>[**StrCatBuff**](/windows/desktop/api/shlwapi/nf-shlwapi-strcatbuffa)</dt> </dl>                                                                            |
| <dl> <dt>[**StringCbCatN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatna)</dt> <dt>[**StringCbCatNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatnexa)</dt> </dl>             | <dl> <dt>[strncat](/cpp/c-runtime-library/reference/strncat-strncat-l-wcsncat-wcsncat-l-mbsncat-mbsncat-l)</dt> <dt>[**StrNCat**](/windows/desktop/api/shlwapi/nf-shlwapi-strncata)</dt> </dl>                                                                                                                                                                                                                                                                  |
| <dl> <dt>[**StringCbCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopya)</dt> <dt>[**StringCbCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopyexa)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](/cpp/c-runtime-library/reference/strcpy-wcscpy-mbscpy)</dt> <dt>[**lstrcpy**](/windows/desktop/api/Winbase/nf-winbase-lstrcpya)</dt> <dt>[**StrCpy**](/windows/desktop/api/shlwapi/nf-shlwapi-strcpyw)</dt> </dl>                                                                                                                                                                   |
| <dl> <dt>[**StringCbCopyN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopyna)</dt> <dt>[**StringCbCopyNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopynexa)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](/cpp/c-runtime-library/reference/strncpy-strncpy-l-wcsncpy-wcsncpy-l-mbsncpy-mbsncpy-l)</dt> </dl>                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>[**StringCbGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsa)</dt> <dt>[**StringCbGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsexa)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](/cpp/c-runtime-library/gets-getws)</dt> </dl>                                                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>[**StringCbPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfa)</dt> <dt>[**StringCbPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfexa)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](/cpp/c-runtime-library/reference/sprintf-sprintf-l-swprintf-swprintf-l-swprintf-l)</dt> <dt>[**wsprintf**](/windows/desktop/api/Winuser/nf-winuser-wsprintfa)</dt> <dt>[**wnsprintf**](/windows/desktop/api/shlwapi/nf-shlwapi-wnsprintfa)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](/cpp/c-runtime-library/reference/snprintf-snprintf-snprintf-l-snwprintf-snwprintf-l)</dt> </dl>         |
| <dl> <dt>[**StringCbVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfa)</dt> <dt>[**StringCbVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfexa)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](/cpp/c-runtime-library/reference/vsprintf-vsprintf-l-vswprintf-vswprintf-l-vswprintf-l)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](/cpp/c-runtime-library/reference/vsnprintf-vsnprintf-vsnprintf-l-vsnwprintf-vsnwprintf-l)</dt> <dt>[**wvsprintf**](/windows/desktop/api/Winuser/nf-winuser-wvsprintfa)</dt> <dt>[**wvnsprintf**](/windows/desktop/api/shlwapi/nf-shlwapi-wvnsprintfa)</dt> </dl> |
| <dl> <dt>[**StringCbLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcblengtha)</dt> </dl>                                                                                                       | <dl> <dt>[strlen, wcslen, \_tcslen](/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l)</dt> </dl>                                                                                                                                                                                                                                                                                                                                   |



 

## Using Strsafe.h

-   To use the Strsafe functions inline, include the header file as shown here, following the **\#include** statements for all other header files.

    `#include <strsafe.h>`

-   To use the functions in library form, include the following statement before including Strsafe.h. However, it is recommended that you use the inline functions.

    `#define STRSAFE_LIB`

    > [!Note]  
    > : The following functions must be used as inline functions: [**StringCbGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsa), [**StringCbGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsexa), [**StringCchGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsa), and [**StringCchGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsexa).

     

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

 

 