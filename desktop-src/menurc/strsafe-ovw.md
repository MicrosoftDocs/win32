---
title: About Strsafe.h
description: Poor buffer handling is implicated in many security issues that involve buffer overruns.
ms.assetid: a104a260-1edb-441a-acf8-e2bd3a7d8235
keywords:
- string functions
- Strsafe.h
- Strsafe functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| <dl> <dt>[**StringCchCat**](/windows/win32/Strsafe/nf-strsafe-stringcchcata?branch=master)</dt> <dt>[**StringCchCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcatexa?branch=master)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](http://go.microsoft.com/fwlink/p/?linkid=192489)</dt> <dt>[**lstrcat**](/windows/win32/Winbase/nf-winbase-lstrcata?branch=master)</dt> <dt>[**StrCat**](https://msdn.microsoft.com/library/windows/desktop/bb759925)</dt> <dt>[**StrCatBuff**](https://msdn.microsoft.com/library/windows/desktop/bb759928)</dt> </dl>                                                                             |
| <dl> <dt>[**StringCchCatN**](/windows/win32/Strsafe/nf-strsafe-stringcchcatna?branch=master)</dt> <dt>[**StringCchCatNEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcatnexa?branch=master)</dt> </dl>             | <dl> <dt>[strncat](http://go.microsoft.com/fwlink/p/?linkid=192505)</dt> <dt>[**StrNCat**](https://msdn.microsoft.com/library/windows/desktop/bb759987)</dt> </dl>                                                                                                                                                                                                                                                                   |
| <dl> <dt>[**StringCchCopy**](/windows/win32/Strsafe/nf-strsafe-stringcchcopya?branch=master)</dt> <dt>[**StringCchCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcopyexa?branch=master)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](http://go.microsoft.com/fwlink/p/?linkid=192494)</dt> <dt>[**lstrcpy**](/windows/win32/Winbase/nf-winbase-lstrcpya?branch=master)</dt> <dt>[**StrCpy**](https://msdn.microsoft.com/library/windows/desktop/bb759960)</dt> </dl>                                                                                                                                                                    |
| <dl> <dt>[**StringCchCopyN**](/windows/win32/Strsafe/nf-strsafe-stringcchcopyna?branch=master)</dt> <dt>[**StringCchCopyNEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcopynexa?branch=master)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](http://go.microsoft.com/fwlink/p/?linkid=192506)</dt> </dl>                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>[**StringCchGets**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsa?branch=master)</dt> <dt>[**StringCchGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsexa?branch=master)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](http://go.microsoft.com/fwlink/p/?linkid=192504)</dt> </dl>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>[**StringCchPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfa?branch=master)</dt> <dt>[**StringCchPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfexa?branch=master)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)</dt> <dt>[**wsprintf**](/windows/win32/Winuser/nf-winuser-wsprintfa?branch=master)</dt> <dt>[**wnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773455)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](http://go.microsoft.com/fwlink/p/?linkid=192507)</dt> </dl>          |
| <dl> <dt>[**StringCchVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfa?branch=master)</dt> <dt>[**StringCchVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfexa?branch=master)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](http://go.microsoft.com/fwlink/p/?linkid=192500)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](http://go.microsoft.com/fwlink/p/?linkid=192508)</dt> <dt>[**wvsprintf**](/windows/win32/Winuser/nf-winuser-wvsprintfa?branch=master)</dt> <dt>[**wvnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773458)</dt> </dl>, |
| <dl> <dt>[**StringCchLength**](/windows/win32/Strsafe/nf-strsafe-stringcchlengtha?branch=master)</dt> </dl>                                                                                                         | <dl> <dt>[strlen, wcslen, \_tcslen](http://go.microsoft.com/fwlink/p/?linkid=192495)</dt> </dl>                                                                                                                                                                                                                                                                                                                                    |



 

## Byte Count Functions

The following functions use a byte count rather than a character count.



| Function                                                                                                                                                                                                                  | Replaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>[**StringCbCat**](/windows/win32/Strsafe/nf-strsafe-stringcbcata?branch=master)</dt> <dt>[**StringCbCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcatexa?branch=master)</dt> </dl>                 | <dl> <dt>[strcat, wcscat, \_tcsat](http://go.microsoft.com/fwlink/p/?linkid=192489)</dt> <dt>[**lstrcat**](/windows/win32/Winbase/nf-winbase-lstrcata?branch=master)</dt> <dt>[**StrCat**](https://msdn.microsoft.com/library/windows/desktop/bb759925)</dt> <dt>[**StrCatBuff**](https://msdn.microsoft.com/library/windows/desktop/bb759928)</dt> </dl>                                                                            |
| <dl> <dt>[**StringCbCatN**](/windows/win32/Strsafe/nf-strsafe-stringcbcatna?branch=master)</dt> <dt>[**StringCbCatNEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcatnexa?branch=master)</dt> </dl>             | <dl> <dt>[strncat](http://go.microsoft.com/fwlink/p/?linkid=192505)</dt> <dt>[**StrNCat**](https://msdn.microsoft.com/library/windows/desktop/bb759987)</dt> </dl>                                                                                                                                                                                                                                                                  |
| <dl> <dt>[**StringCbCopy**](/windows/win32/Strsafe/nf-strsafe-stringcbcopya?branch=master)</dt> <dt>[**StringCbCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcopyexa?branch=master)</dt> </dl>             | <dl> <dt>[strcpy, wcscpy, \_tcscpy](http://go.microsoft.com/fwlink/p/?linkid=192494)</dt> <dt>[**lstrcpy**](/windows/win32/Winbase/nf-winbase-lstrcpya?branch=master)</dt> <dt>[**StrCpy**](https://msdn.microsoft.com/library/windows/desktop/bb759960)</dt> </dl>                                                                                                                                                                   |
| <dl> <dt>[**StringCbCopyN**](/windows/win32/Strsafe/nf-strsafe-stringcbcopyna?branch=master)</dt> <dt>[**StringCbCopyNEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcopynexa?branch=master)</dt> </dl>         | <dl> <dt>[strncpy, wcsncpy, \_tcsncpy](http://go.microsoft.com/fwlink/p/?linkid=192506)</dt> </dl>                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>[**StringCbGets**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsa?branch=master)</dt> <dt>[**StringCbGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsexa?branch=master)</dt> </dl>             | <dl> <dt>[gets, \_getws, \_getts](http://go.microsoft.com/fwlink/p/?linkid=192504)</dt> </dl>                                                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>[**StringCbPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfa?branch=master)</dt> <dt>[**StringCbPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfexa?branch=master)</dt> </dl>     | <dl> <dt>[sprintf, swprintf, \_stprintf](http://go.microsoft.com/fwlink/p/?linkid=192497)</dt> <dt>[**wsprintf**](/windows/win32/Winuser/nf-winuser-wsprintfa?branch=master)</dt> <dt>[**wnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773455)</dt> <dt>[\_snprintf, \_snwprintf, \_sntprintf](http://go.microsoft.com/fwlink/p/?linkid=192507)</dt> </dl>         |
| <dl> <dt>[**StringCbVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfa?branch=master)</dt> <dt>[**StringCbVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfexa?branch=master)</dt> </dl> | <dl> <dt>[vsprintf, vswprintf, \_vstprintf](http://go.microsoft.com/fwlink/p/?linkid=192500)</dt> <dt>[vsnprintf, \_vsnwprintf, \_vsntprintf](http://go.microsoft.com/fwlink/p/?linkid=192508)</dt> <dt>[**wvsprintf**](/windows/win32/Winuser/nf-winuser-wvsprintfa?branch=master)</dt> <dt>[**wvnsprintf**](https://msdn.microsoft.com/library/windows/desktop/bb773458)</dt> </dl> |
| <dl> <dt>[**StringCbLength**](/windows/win32/Strsafe/nf-strsafe-stringcblengtha?branch=master)</dt> </dl>                                                                                                       | <dl> <dt>[strlen, wcslen, \_tcslen](http://go.microsoft.com/fwlink/p/?linkid=192495)</dt> </dl>                                                                                                                                                                                                                                                                                                                                   |



 

## Using Strsafe.h

-   To use the Strsafe functions inline, include the header file as shown here, following the **\#include** statements for all other header files.

    `#include <strsafe.h>`

-   To use the functions in library form, include the following statement before including Strsafe.h. However, it is recommended that you use the inline functions.

    `#define STRSAFE_LIB`

    > [!Note]  
    > : The following functions must be used as inline functions: [**StringCbGets**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsa?branch=master), [**StringCbGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsexa?branch=master), [**StringCchGets**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsa?branch=master), and [**StringCchGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsexa?branch=master).

     

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

 

 




