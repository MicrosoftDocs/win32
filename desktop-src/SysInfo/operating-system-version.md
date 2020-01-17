---
Description: The Version API Helper functions are used to determine the version of the operating system that is currently running. For more information, see Getting the System Version.
ms.assetid: 1a70b1d9-ed66-4201-9921-4e26e4001020
title: Operating System Version
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Version

The [Version API Helper functions](version-helper-apis.md) are used to determine the version of the operating system that is currently running. For more information, see [Getting the System Version](getting-the-system-version.md).

The following table summarizes the most recent operating system version numbers.

| Operating system | Version number |
|------------------|----------------|
| Windows 10       | 10.0\*         |
| Windows Server 2019 | 10.0\*      |
| Windows Server 2016 | 10.0\*      |
| Windows 8.1      | 6.3\*          |
| Windows Server 2012 R2 | 6.3\*    |
| Windows 8        | 6.2            |
| Windows Server 2012 | 6.2         |
| Windows 7        | 6.1            |
| Windows Server 2008 R2 | 6.1      |
| Windows Server 2008 | 6.0         |
| Windows Vista    | 6.0            |
| Windows Server 2003 R2 | 5.2      |
| Windows Server 2003 | 5.2         |
| Windows XP 64-Bit Edition | 5.2   |
| Windows XP | 5.1                  |
| Windows 2000     | 5.0            |

**\*** For applications that have been manifested for Windows 8.1 or Windows 10. Applications not manifested for Windows 8.1 or Windows 10 will return the Windows 8 OS version value (6.2). To manifest your applications for Windows 8.1 or Windows 10, refer to [Targeting your application for Windows](targeting-your-application-at-windows-8-1.md).<br/>

Identifying the current operating system is usually not the best way to determine whether a particular operating system feature is present. This is because the operating system may have had new features added in a redistributable DLL. Rather than using the [Version API Helper functions](version-helper-apis.md) to determine the operating system platform or version number, test for the presence of the feature itself.

To determine the best way to test for a feature, refer to the documentation for the feature of interest. The following list discusses some common techniques for feature detection:

- You can test for the presence of the functions associated with a feature. To test for the presence of a function in a system DLL, call the [**LoadLibrary**](https://docs.microsoft.com/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to load the DLL. Then call the [**GetProcAddress**](https://docs.microsoft.com/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) function to determine whether the function of interest is present in the DLL. Use the pointer returned by **GetProcAddress** to call the function. Note that even if the function is present, it may be a stub that just returns an error code such as ERROR\_CALL\_NOT\_IMPLEMENTED.
- You can determine the presence of some features by using the [**GetSystemMetrics**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function. For example, you can detect multiple display monitors by calling **GetSystemMetrics**(SM\_CMONITORS).
- There are several versions of the redistributable DLLs that implement shell and common control features. For information about determining which versions are present on the system your application is running on, see the topic [Shell and Common Controls Versions](https://msdn.microsoft.com/library/Bb776779(v=VS.85).aspx).

If you must require a particular operating system, be sure to use it as a minimum supported version, rather than design the test for the one operating system. This way, your detection code will continue to work on future versions of Windows.

Note that a 32-bit application can detect whether it is running under WOW64 by calling the [**IsWow64Process**](https://docs.microsoft.com/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process) function. It can obtain additional processor information by calling the [**GetNativeSystemInfo**](https://msdn.microsoft.com/library/ms724340(v=VS.85).aspx) function.

 

 




