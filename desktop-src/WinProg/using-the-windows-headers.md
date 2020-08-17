---
title: Using the Windows Headers
description: Use the Windows header files to create applications that use the Windows API.
ms.assetid: a4def563-8ddc-4630-ae8a-86c07cf98374
keywords:
- Windows API, header files
- C2065
- WINVER
- _WIN32_WINDOWS
- _WIN32_WINNT
- _WIN32_IE
- WIN32_LEAN_AND_MEAN
ms.topic: article
ms.date: 01/22/2020
---

# Using the Windows Headers

The header files for the Windows API enable you to create 32- and 64-bit applications. They include declarations for both Unicode and ANSI versions of the API. For more information, see [Unicode in the Windows API](/windows/desktop/Intl/unicode-in-the-windows-api). They use [data types](windows-data-types.md) that enable you to build both 32- and 64-bit versions of your application from a single source code base. For more information, see [Getting Ready for 64-bit Windows](/windows/desktop/WinProg64/getting-ready-for-64-bit-windows). Additional features include [Header Annotations](header-annotations.md) and [STRICT Type Checking](strict-type-checking.md).

-   [Visual C++ and the Windows Header Files](#visual-c-and-the-windows-header-files)
-   [Macros for Conditional Declarations](#macros-for-conditional-declarations)
-   [Setting WINVER or \_WIN32\_WINNT](#setting-winver-or-_win32_winnt)
-   [Controlling Structure Packing](#controlling-structure-packing)
-   [Faster Builds with Smaller Header Files](#faster-builds-with-smaller-header-files)
-   [Related topics](#related-topics)

## Visual C++ and the Windows Header Files

Microsoft Visual C++ includes copies of the Windows header files that were current at the time Visual C++ was released. Therefore, if you install updated header files from an SDK, you may end up with multiple versions of the Windows header files on your computer. If you do not ensure that you are using the latest version of the SDK header files, you will receive the following error code when compiling code that uses features that were introduced after Visual C++ was released: error C2065: undeclared identifier.

## Macros for Conditional Declarations

Certain functions that depend on a particular version of Windows are declared using conditional code. This enables you to use the compiler to detect whether your application uses functions that are not supported on its target version(s) of Windows. To compile an application that uses these functions, you must define the appropriate macros. Otherwise, you will receive the C2065 error message.

The Windows header files use macros to indicate which versions of Windows support many programming elements. Therefore, you must define these macros to use new functionality introduced in each major operating system release. (Individual header files may use different macros; therefore, if compilation problems occur, check the header file that contains the definition for conditional definitions.) For more information, see SdkDdkVer.h.

The following table describes the preferred macros used in the Windows header files. If you define NTDDI\_VERSION, you must also define \_WIN32\_WINNT.



| Minimum system required                       | Value for NTDDI\_VERSION            |
|-----------------------------------------------|-------------------------------------|
| Windows 10 1903 "19H1"                        | **NTDDI\_WIN10\_19H1** (0x0A000007) |
| Windows 10 1809 "Redstone 5"                  | **NTDDI\_WIN10\_RS5** (0x0A000006)  |
| Windows 10 1803 "Redstone 4"                  | **NTDDI\_WIN10\_RS4** (0x0A000005)  |
| Windows 10 1709 "Redstone 3"                  | **NTDDI\_WIN10\_RS3** (0x0A000004)  |
| Windows 10 1703 "Redstone 2"                  | **NTDDI\_WIN10\_RS2** (0x0A000003)  |
| Windows 10 1607 "Redstone 1"                  | **NTDDI\_WIN10\_RS1** (0x0A000002)  |
| Windows 10 1511 "Threshold 2"                 | **NTDDI\_WIN10\_TH2** (0x0A000001)  |
| Windows 10 1507 "Threshold"                   | **NTDDI\_WIN10** (0x0A000000)       |
| Windows 8.1                                   | **NTDDI\_WINBLUE** (0x06030000)     |
| Windows 8                                     | **NTDDI\_WIN8** (0x06020000)        |
| Windows 7                                     | **NTDDI\_WIN7** (0x06010000)        |
| Windows Server 2008                           | **NTDDI\_WS08** (0x06000100)        |
| Windows Vista with Service Pack 1 (SP1)       | **NTDDI\_VISTASP1** (0x06000100)    |
| Windows Vista                                 | **NTDDI\_VISTA** (0x06000000)       |
| Windows Server 2003 with Service Pack 2 (SP2) | **NTDDI\_WS03SP2** (0x05020200)     |
| Windows Server 2003 with Service Pack 1 (SP1) | **NTDDI\_WS03SP1** (0x05020100)     |
| Windows Server 2003                           | **NTDDI\_WS03** (0x05020000)        |
| Windows XP with Service Pack 3 (SP3)          | **NTDDI\_WINXPSP3** (0x05010300)    |
| Windows XP with Service Pack 2 (SP2)          | **NTDDI\_WINXPSP2** (0x05010200)    |
| Windows XP with Service Pack 1 (SP1)          | **NTDDI\_WINXPSP1** (0x05010100)    |
| Windows XP                                    | **NTDDI\_WINXP** (0x05010000)       |



 

The following tables describe other macros used in the Windows header files.



| Minimum system required                           | Minimum value for \_WIN32\_WINNT and WINVER |
|---------------------------------------------------|---------------------------------------------|
| Windows 10                                        | **\_WIN32\_WINNT\_WIN10** (0x0A00)          |
| Windows 8.1                                       | **\_WIN32\_WINNT\_WINBLUE** (0x0603)        |
| Windows 8                                         | **\_WIN32\_WINNT\_WIN8** (0x0602)           |
| Windows 7                                         | **\_WIN32\_WINNT\_WIN7** (0x0601)           |
| Windows Server 2008                               | **\_WIN32\_WINNT\_WS08** (0x0600)           |
| Windows Vista                                     | **\_WIN32\_WINNT\_VISTA** (0x0600)          |
| Windows Server 2003 with SP1, Windows XP with SP2 | **\_WIN32\_WINNT\_WS03** (0x0502)           |
| Windows Server 2003, Windows XP                   | **\_WIN32\_WINNT\_WINXP** (0x0501)          |



 



| Minimum version required          | Minimum value of \_WIN32\_IE      |
|-----------------------------------|-----------------------------------|
| Internet Explorer 11.0            | **\_WIN32\_IE\_IE110** (0x0A00)   |
| Internet Explorer 10.0            | **\_WIN32\_IE\_IE100** (0x0A00)   |
| Internet Explorer 9.0             | **\_WIN32\_IE\_IE90** (0x0900)    |
| Internet Explorer 8.0             | **\_WIN32\_IE\_IE80** (0x0800)    |
| Internet Explorer 7.0             | **\_WIN32\_IE\_IE70** (0x0700)    |
| Internet Explorer 6.0 SP2         | **\_WIN32\_IE\_IE60SP2** (0x0603) |
| Internet Explorer 6.0 SP1         | **\_WIN32\_IE\_IE60SP1** (0x0601) |
| Internet Explorer 6.0             | **\_WIN32\_IE\_IE60** (0x0600)    |
| Internet Explorer 5.5             | **\_WIN32\_IE\_IE55** (0x0550)    |
| Internet Explorer 5.01            | **\_WIN32\_IE\_IE501** (0x0501)   |
| Internet Explorer 5.0, 5.0a, 5.0b | **\_WIN32\_IE\_IE50** (0x0500)    |



 

## Setting WINVER or \_WIN32\_WINNT

You can define these symbols by using the \#define statement in each source file, or by specifying the /D compiler option supported by Visual C++.

For example, to set WINVER in your source file, use the following statement:

`#define WINVER 0x0502`

To set \_WIN32\_WINNT in your source file, use the following statement:

`#define _WIN32_WINNT 0x0502`

To set \_WIN32\_WINNT using the /D compiler option, use the following command:

**cl -c /D\_WIN32\_WINNT=0x0502** _source_**.cpp**

For information on using the /D compiler option, see [/D (preprocessor definitions)](/cpp/build/reference/d-preprocessor-definitions).

Note that some features introduced in the latest version of Windows may be added to a service pack for a previous version of Windows. Therefore, to target a service pack, you may need to define \_WIN32\_WINNT with the value for the next major operating system release. For example, the [**GetDllDirectory**](/windows/desktop/api/winbase/nf-winbase-getdlldirectorya) function was introduced in Windows Server 2003 and is conditionally defined if \_WIN32\_WINNT is 0x0502 or greater. This function was also added to Windows XP with SP1. Therefore, if you were to define \_WIN32\_WINNT as 0x0501 to target Windows XP, you would miss features that are defined in Windows XP with SP1.

## Controlling Structure Packing

Projects should be compiled to use the default structure packing, which is currently 8 bytes because the largest integral type is 8 bytes. Doing so ensures that all structure types within the header files are compiled into the application with the same alignment the Windows API expects. It also ensures that structures with 8-byte values are properly aligned and will not cause alignment faults on processors that enforce data alignment.

For more information, see [/Zp (struct member alignment)](/cpp/build/reference/zp-struct-member-alignment) or [pack](/cpp/preprocessor/pack).

## Faster Builds with Smaller Header Files

You can reduce the size of the Windows header files by excluding some of the less common API declarations as follows:

-   Define WIN32\_LEAN\_AND\_MEAN to exclude APIs such as Cryptography, DDE, RPC, Shell, and Windows Sockets.

    `#define WIN32_LEAN_AND_MEAN`

-   Define one or more of the NO*api* symbols to exclude the API. For example, NOCOMM excludes the serial communication API. For a list of support NO*api* symbols, see Windows.h.

    `#define NOCOMM`

## Related topics

<dl> <dt>

[Windows SDK download site](https://msdn.microsoft.com/windowsserver/bb980924.aspx)
</dt> </dl>

 

 