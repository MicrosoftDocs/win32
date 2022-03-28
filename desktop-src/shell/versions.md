---
description: This section describes how to determine which version of the Shell DLLs your application is running on and how to target your application for a specific version.
title: Shell and Shlwapi DLL Versions
ms.topic: article
ms.date: 09/24/2020
ms.assetid: ecfb6484-a1d6-4ace-8457-3940b111a4d2
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell and Shlwapi DLL Versions

This section describes how to determine which version of the Shell DLLs your application is running on and how to target your application for a specific version.

- [DLL Version Numbers](#dll-version-numbers)
- [Using DllGetVersion to Determine the Version Number](#using-dllgetversion-to-determine-the-version-number)
    - [Using DllGetVersion](#using-dllgetversion)
- [Project Versions](#project-versions)

## DLL Version Numbers

All but a handful of the programming elements discussed in the Shell documentation are contained in two DLLs: Shell32.dll and Shlwapi.dll. Because of ongoing enhancements, different versions of these DLLs implement different features. Throughout the Shell reference documentation, each programming element specifies a minimum supported DLL version number. This version number indicates that the programming element is implemented in that version and subsequent versions of the DLL unless otherwise specified. If no version number is specified, the programming element is implemented in all existing versions of the DLL.

Before Windows XP, new Shell32.dll and Shlwapi.dll versions were sometimes provided with new versions of Windows Internet Explorer. As of Windows XP, those DLLs were no longer provided as redistributable files outside of new versions of Windows itself. The following table outlines the different DLL versions and how they were distributed dating back to Microsoft Internet Explorer 3.0, Windows 95, and Microsoft Windows NT 4.0.

Shell32.dll version 4.0 is found in the original versions of Windows 95 and Microsoft Windows NT 4.0. The Shell was not updated with the Internet Explorer 3.0 release, so Shell32.dll does not have a version 4.70. Shell32.dll versions 4.71 and 4.72 were shipped with the corresponding Internet Explorer releases, but they were not necessarily installed (see note 1). For releases subsequent to Microsoft Internet Explorer 4.01 and Windows 98, the version numbers for Shell32.dll and Shlwapi.dll diverge. In general, you should assume that the DLLs have different version numbers and test each one separately.

#### Shell32.dll

| Version | Distribution Platform                                                       |
|---------|-----------------------------------------------------------------------------|
| 4.0     | Windows 95 and Microsoft Windows NT 4.0                                     |
| 4.71    | Microsoft Internet Explorer 4.0. See note 1.                                |
| 4.72    | Internet Explorer 4.01 and Windows 98. See note 1.                          |
| 5.0     | Windows 2000 and Windows Millennium Edition (Windows Me). See note 2.       |
| 6.0     | Windows XP                                                                  |
| 6.0.1   | Windows Vista                                                               |
| 6.1     | Windows 7                                                                   |

#### Shlwapi.dll

| Version | Distribution Platform                                                       |
|---------|-----------------------------------------------------------------------------|
| 4.0     | Windows 95 and Microsoft Windows NT 4.0                                     |
| 4.71    | Internet Explorer 4.0. See note 1.                                          |
| 4.72    | Internet Explorer 4.01 and Windows 98. See note 1.                          |
| 4.7     | Internet Explorer 3.x                                                       |
| 5.0     | Microsoft Internet Explorer 5 and Windows 98 SE. See note 2.                |
| 5.5     | Microsoft Internet Explorer 5.5 and Windows Millennium Edition (Windows Me) |
| 6.0     | Windows XP and Windows Vista                                                |



**Note 1:** All systems with Internet Explorer 4.0 or 4.01 had the associated version of Shlwapi.dll (4.71 or 4.72, respectively). However, for systems prior to Windows 98, Internet Explorer 4.0 and 4.01 can be installed with or without what was known as the *integrated Shell*. If Internet Explorer was installed with the integrated Shell, the associated version of Shell32.dll (4.71 or 4.72) was also installed. If Internet Explorer was installed without the integrated Shell, Shell32.dll remained as version 4.0. In other words, the presence of version 4.71 or 4.72 of Shlwapi.dll on a system does not guarantee that Shell32.dll has the same version number. All Windows 98 systems have version 4.72 of Shell32.dll.

**Note 2:** Version 5.0 of Shlwapi.dll was distributed with Internet Explorer 5 and was found on all systems on which Internet Explorer 5 was installed, with the exception of Windows 2000. Version 5.0 of Shell32.dll was distributed natively with Windows 2000 and Windows Millennium Edition (Windows Me), together with version 5.0 of Shlwapi.dll.

## Using DllGetVersion to Determine the Version Number

Starting with version 4.71, the Shell DLLs, among others, began exporting [**DllGetVersion**](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc). This function can be called by an application to determine which DLL version is present on the system.

> [!Note]  
> DLLs do not necessarily export [**DllGetVersion**](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc). Always test for it before attempting to use it.

For Windows versions earlier than Windows 2000, [**DllGetVersion**](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc) returns a [**DLLVERSIONINFO**](/windows/desktop/api/Shlwapi/ns-shlwapi-dllversioninfo) structure that contains the major and minor version numbers, the build number, and a platform ID. For Windows 2000 and later systems, **DllGetVersion** might instead return a [**DLLVERSIONINFO2**](/windows/desktop/api/Shlwapi/ns-shlwapi-dllversioninfo2) structure. In addition to the information provided through **DLLVERSIONINFO**, **DLLVERSIONINFO2**also provides the hotfix number that identifies the latest installed service pack, which provides a more robust way to compare version numbers. Because the first member of **DLLVERSIONINFO2** is a **DLLVERSIONINFO** structure, the later structure is backward-compatible.

### Using DllGetVersion

The following sample function `GetVersion` loads a specified DLL and attempts to call its [**DllGetVersion**](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc) function. If successful, it uses a macro to pack the major and minor version numbers from the [**DLLVERSIONINFO**](/windows/desktop/api/Shlwapi/ns-shlwapi-dllversioninfo) structure into a **DWORD** that is returned to the calling application. If the DLL does not export **DllGetVersion**, the function returns zero. With Windows 2000 and later systems, you can modify the function to handle the possibility that **DllGetVersion** returns a [**DLLVERSIONINFO2**](/windows/desktop/api/Shlwapi/ns-shlwapi-dllversioninfo2) structure. If so, use the information in that **DLLVERSIONINFO2** structure's **ullVersion** member to compare versions, build numbers, and service pack releases. The [**MAKEDLLVERULL**](/windows/desktop/api/Shlwapi/nf-shlwapi-makedllverull) macro simplifies the task of comparing these values to those in **ullVersion**.

> [!Note]  
> Using [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can pose security risks. Refer to the **LoadLibrary** documentation for information on how to correctly load DLLs with different versions of Windows.


```C++
#include "stdafx.h"
#include "windows.h"
#include "windef.h"
#include "winbase.h"
#include "shlwapi.h"

#define PACKVERSION(major,minor) MAKELONG(minor,major)

DWORD GetVersion(LPCTSTR lpszDllName)
{
    HINSTANCE hinstDll;
    DWORD dwVersion = 0;

    /* For security purposes, LoadLibrary should be provided with a fully qualified 
       path to the DLL. The lpszDllName variable should be tested to ensure that it 
       is a fully qualified path before it is used. */
    hinstDll = LoadLibrary(lpszDllName);
    
    if(hinstDll)
    {
        DLLGETVERSIONPROC pDllGetVersion;
        pDllGetVersion = (DLLGETVERSIONPROC)GetProcAddress(hinstDll, "DllGetVersion");

        /* Because some DLLs might not implement this function, you must test for 
           it explicitly. Depending on the particular DLL, the lack of a DllGetVersion 
           function can be a useful indicator of the version. */

        if(pDllGetVersion)
        {
            DLLVERSIONINFO dvi;
            HRESULT hr;

            ZeroMemory(&dvi, sizeof(dvi));
            dvi.info1.cbSize = sizeof(dvi);

            hr = (*pDllGetVersion)(&dvi);

            if(SUCCEEDED(hr))
            {
               dwVersion = PACKVERSION(dvi.info1.dwMajorVersion, dvi.info1.dwMinorVersion);
            }
        }
        FreeLibrary(hinstDll);
    }
    return dwVersion;
}
```


The following code example illustrates how you can use `GetVersion` to test whether Shell32.dll is version 6.0 or later.


```C++
LPCTSTR lpszDllName = L"C:\\Windows\\System32\\Shell32.dll";
DWORD dwVer = GetVersion(lpszDllName);
DWORD dwTarget = PACKVERSION(6,0);

if(dwVer >= dwTarget)
{
    // This version of Shell32.dll is version 6.0 or later.
}
else
{
    // Proceed knowing that version 6.0 or later additions are not available.
    // Use an alternate approach for older the DLL version.
}
```


## Project Versions

To ensure that your application is compatible with different targeted versions of a .dll file, version macros are present in the header files. These macros are used to define, exclude, or redefine certain definitions for different versions of the DLL. See [Using the Windows Headers](../winprog/using-the-windows-headers.md) for an in-depth description of these macros.

For example, the macro name **\_WIN32\_IE** is commonly found in older headers. You are responsible for defining the macro as a hexadecimal number. This version number defines the target version of the application that is using the DLL. The following table shows the available version numbers and the effect each has on your application.


| Version | Description                                                                                                                                                                                       |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0200  | The application is compatible with Shell32.dll version 4.00 and later. The application cannot implement features that were added after version 4.00.                                              |
| 0x0300  | The application is compatible with Shell32.dll version 4.70 and later. The application cannot implement features that were added after version 4.70.                                              |
| 0x0400  | The application is compatible with Shell32.dll version 4.71 and later. The application cannot implement features that were added after version 4.71.                                              |
| 0x0401  | The application is compatible with Shell32.dll version 4.72 and later. The application cannot implement features that were added after version 4.72.                                              |
| 0x0500  | The application is compatible with Shell32.dll and Shlwapi.dll version 5.0 and later. The application cannot implement features that were added after version 5.0 of Shell32.dll and Shlwapi.dll. |
| 0x0501  | The application is compatible with Shell32.dll and Shlwapi.dll version 5.0 and later. The application cannot implement features that were added after version 5.0 of Shell32.dll and Shlwapi.dll. |
| 0x0600  | The application is compatible with Shell32.dll and Shlwapi.dll version 6.0 and later. The application cannot implement features that were added after version 6.0 of Shell32.dll and Shlwapi.dll. |


If you do not define the **\_WIN32\_IE** macro in your project, it is automatically defined as 0x0500. To define a different value, you can add the following to the compiler directives in your make file; substitute the desired version number for 0x0400.

```
/D _WIN32_IE=0x0400
```

Another method is to add a line similar to the following in your source code before you include the Shell header files. Substitute the desired version number for 0x0400.

```
#define _WIN32_IE 0x0400
#include <commctrl.h>
```
