---
title: Crash Dump Analysis
description: This technical article provides info about how to write and use a minidump.
ms.assetid: 575c4716-18c2-7b11-7308-aa2e3d8efac7
ms.topic: article
ms.date: 05/31/2018
---

# Crash Dump Analysis

Not all bugs can be found prior to release, which means not all bugs that throw exceptions can be found before release. Fortunately, Microsoft has included in the Platform SDK a function to help developers collect information on exceptions that are discovered by users. The [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) function writes the necessary crash dump information to a file without saving the whole process space. This crash dump information file is called a minidump. This technical article provides info about how to write and use a minidump.

-   [Writing a Minidump](#writing-a-minidump)
-   [Thread safety](#thread-safety)
-   [Writing a Minidump with Code](#writing-a-minidump-with-code)
-   [Using Dumpchk.exe](#using-dumpchkexe)
-   [Analyzing a Minidump](#analyzing-a-minidump)
    -   [Using the Microsoft Public Symbol Server](#using-the-microsoft-public-symbol-server)
    -   [Debugging a Minidump with WinDbg](#debugging-a-minidump-with-windbg)
    -   [Using Copy-Protection Tools with Minidumps](#using-copy-protection-tools-with-minidumps)
-   [Summary](#summary)

## Writing a Minidump

The basic options for writing a minidump are as follows:

-   Do nothing. Windows automatically generates a minidump whenever a program throws an unhandled exception. Automatic generation of a minidump is available since Windows XP. If the user allows it, the minidump will be sent to Microsoft, and not to the developer, through Windows Error Reporting (WER). Developers can gain access to these minidumps through the [Windows Desktop Application Program](../appxpkg/windows-desktop-application-program.md).

    Use of WER requires:

    -   Developers to sign their applications using Authenticode
    -   Applications have valid VERSIONINFO resource in every executable and DLL

    If you implement a custom routine for unhandled exceptions, you are strongly urged to use the [**ReportFault**](/windows/desktop/api/errorrep/nf-errorrep-reportfault) function in the exception handler to also send an automated minidump to WER. The **ReportFault** function handles all of the issues of connecting to and sending the minidump to WER. Not sending minidumps to WER violates the requirements of Games for Windows.

    For more information on how WER works, see [How Windows Error Reporting Works](https://www.microsoft.com/whdc/maintain/WER/WERWorks.mspx). For an explanation of registration details, see [Introducing Windows Error Reporting](https://msdn.microsoft.com/) on MSDN's [ISV Zone](https://msdn.microsoft.com/).

-   Use a product from the Microsoft Visual Studio Team System. On the **Debug** menu, click **Save Dump As** to save a copy of a dump. Use of a locally saved dump is only an option for in-house testing and debugging.
-   Add code to your project. Add the [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) function and the appropriate exception handling code to save and send a minidump directly to the developer. This article demonstrates how to implement this option. However, note that **MiniDumpWriteDump** does not currently work with managed code and is only available on Windows XP, Windows Vista, Windows 7.

## Thread safety

[**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) is part of the DBGHELP library. This library is not thread-safe, so any program that uses **MiniDumpWriteDump** should synchronize all threads before attempting to call **MiniDumpWriteDump**.

## Writing a Minidump with Code

The actual implementation is straightforward. The following is a simple example of how to use [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump).


```C++
#include <dbghelp.h>
#include <shellapi.h>
#include <shlobj.h>

int GenerateDump(EXCEPTION_POINTERS* pExceptionPointers)
{
    BOOL bMiniDumpSuccessful;
    WCHAR szPath[MAX_PATH]; 
    WCHAR szFileName[MAX_PATH]; 
    WCHAR* szAppName = L"AppName";
    WCHAR* szVersion = L"v1.0";
    DWORD dwBufferSize = MAX_PATH;
    HANDLE hDumpFile;
    SYSTEMTIME stLocalTime;
    MINIDUMP_EXCEPTION_INFORMATION ExpParam;

    GetLocalTime( &stLocalTime );
    GetTempPath( dwBufferSize, szPath );

    StringCchPrintf( szFileName, MAX_PATH, L"%s%s", szPath, szAppName );
    CreateDirectory( szFileName, NULL );

    StringCchPrintf( szFileName, MAX_PATH, L"%s%s\\%s-%04d%02d%02d-%02d%02d%02d-%ld-%ld.dmp", 
               szPath, szAppName, szVersion, 
               stLocalTime.wYear, stLocalTime.wMonth, stLocalTime.wDay, 
               stLocalTime.wHour, stLocalTime.wMinute, stLocalTime.wSecond, 
               GetCurrentProcessId(), GetCurrentThreadId());
    hDumpFile = CreateFile(szFileName, GENERIC_READ|GENERIC_WRITE, 
                FILE_SHARE_WRITE|FILE_SHARE_READ, 0, CREATE_ALWAYS, 0, 0);

    ExpParam.ThreadId = GetCurrentThreadId();
    ExpParam.ExceptionPointers = pExceptionPointers;
    ExpParam.ClientPointers = TRUE;

    bMiniDumpSuccessful = MiniDumpWriteDump(GetCurrentProcess(), GetCurrentProcessId(), 
                    hDumpFile, MiniDumpWithDataSegs, &ExpParam, NULL, NULL);

    return EXCEPTION_EXECUTE_HANDLER;
}


void SomeFunction()
{
    __try
    {
        int *pBadPtr = NULL;
        *pBadPtr = 0;
    }
    __except(GenerateDump(GetExceptionInformation()))
    {
    }
}
```



This example demonstrates the basic usage of [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) and the minimum information necessary to call it. The name of the dump file is up to the developer; however, to avoid file name collisions, it is advisable to generate the file name from the application's name and version number, the process and thread IDs, and the date and time. This will also help to keep the minidumps grouped by application and version. It is up to the developer to decide how much information is used to differentiate minidump file names.

It should be noted that the path name in the preceding example was generated by calling the [**GetTempPath**](/windows/desktop/api/fileapi/nf-fileapi-gettemppatha) function to retrieve the path of the directory designated for temporary files. Use of this directory works even with least-privileged user accounts, and it also prevents the minidump from taking up hard drive space after it is no longer needed.

If you archive the product during your daily build process, also be sure to include symbols for the build so that you can debug an old version of the product, if necessary. You also need to take steps to maintain full compiler optimizations while generating symbols. This can be done by opening your project's properties in the development environment and, for the release configuration, doing the following:

1.  On the left side of the project's property page, click C/C++. By default, this displays **General** settings. On the right side of the project's property page, set **Debug Information Format** to **Program Database (/Zi)**.
2.  On the left side of the property page, expand **Linker**, and then click **Debugging**. On the right side of the property page, set **Generate Debug Info** to **Yes (/DEBUG)**.
3.  Click **Optimization**, and set **References** to E**liminate Unreferenced Data (/OPT:REF)**.
4.  Set **Enable COMDAT Folding** to **Remove Redundant COMDATs (/OPT:ICF)**.

MSDN has more detailed information on the [**MINIDUMP\_EXCEPTION\_INFORMATION**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-minidump_exception_information) structure and the [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) function.

## Using Dumpchk.exe

Dumpchk.exe is a command-line utility that can be used to verify that a dump file was created correctly. If Dumpchk.exe generates an error, then the dump file is corrupt and cannot be analyzed. For information on using Dumpchk.exe, see [How to Use Dumpchk.exe to Check a Memory Dump File](https://support.microsoft.com/kb/315271/).

Dumpchk.exe is included on the Windows XP product CD and can be installed to System Drive\\Program Files\\Support Tools\\ by running Setup.exe in the Support\\Tools\\ folder on the Windows XP product CD. You can also get the latest version of Dumpchk.exe by download and installing the debugging tools available from [Windows Debugging Tools](https://www.microsoft.com/whdc/devtools/debugging/) on [Windows Hardware Developer Central](https://www.microsoft.com/whdc/).

## Analyzing a Minidump

Opening a minidump for analysis is as easy as creating one.

**To analyze a minidump**

1.  Open Visual Studio.
2.  On the **File** menu, click **Open Project**.
3.  Set **Files of type** to **Dump Files**, navigate to the dump file, select it, and click **Open.**
4.  Run the debugger.

The debugger will create a simulated process. The simulated process will be halted at the instruction that caused the crash.

### Using the Microsoft Public Symbol Server

To get the stack for driver- or system-level crashes, it might be necessary to configure Visual Studio to point to the Microsoft public symbol server.

**To set a path to the Microsoft symbol server**

1.  On the **Debug** menu, click **Options**.
2.  In the **Options** dialog box, open the **Debugging** node, and click **Symbols**.
3.  Make sure **Search the above locations only when symbols are loaded manually** is not selected, unless you want to load symbols manually when you debug.
4.  If you are using symbols on a remote symbol server, you can improve performance by specifying a local directory that symbols can be copied to. To do this, enter a path for **Cache symbols from symbol server to this directory**. To connect to the Microsoft public symbol server, you need to enable this setting. Note that if you are debugging a program on a remote computer, the cache directory refers to a directory on the remote computer.
5.  Click **OK**.
6.  Because you are using the Microsoft public symbol server, an End User License Agreement dialog box appears. Click **Yes** to accept the agreement and download symbols to your local cache.

### Debugging a Minidump with WinDbg

You can also use WinDbg, a debugger that is part of the Windows Debugging Tools, to debug a minidump. WinDbg allows you to debug without having to use Visual Studio. To download Windows Debugging Tools, see [Windows Debugging Tools](https://www.microsoft.com/whdc/devtools/debugging/) on [Windows Hardware Developer Central](https://www.microsoft.com/whdc/).

After installing Windows Debugging Tools, you must enter the symbol path in WinDbg.

**To enter a symbol path in WinDbg**

1.  On the **File** menu, click **Symbol Path**.
2.  In the **Symbol Search Path** window, enter the following:

    `"srv\*c:\\cache\*https://msdl.microsoft.com/download/symbols;"`

### Using Copy-Protection Tools with Minidumps

Developers also need to be aware of how their copy-protection scheme might affect the minidump. Most copy-protection schemes have their own descramble tools, and it is up to the developer to learn how to use those tools with [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump).

## Summary

The [**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump) function can be an extremely useful tool in collecting and solving bugs after the product has been released. Writing a custom exception handler that uses **MiniDumpWriteDump** allows the developer to customize the information collection and improve the debugging process. The function is flexible enough to be used in any C++-based project and should be considered part of any project's stability process.

 

 
