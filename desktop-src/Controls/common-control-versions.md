---
title: Common Control Versions
description: This topic lists the available versions of the Common Control library (ComCtl32.dll), describes how to identify the version that your application is using, and explains how to target your application for a specific version.
ms.assetid: 1B524A91-B433-4968-9546-8A6AFB67E89C
ms.topic: article
ms.date: 05/31/2018
---

# Common Control Versions

This topic lists the available versions of the Common Control library (ComCtl32.dll), describes how to identify the version that your application is using, and explains how to target your application for a specific version.

This topic contains the following sections.

-   [Common Control DLL Versions Numbers](#common-control-dll-versions-numbers)
-   [Structure Sizes for Different Common Control Versions](#structure-sizes-for-different-common-control-versions)
-   [Using DllGetVersion to Determine the Version Number](#using-dllgetversion-to-determine-the-version-number)
-   [Project Versions](#project-versions)
-   [Related topics](#related-topics)

## Common Control DLL Versions Numbers

Support for common controls is provided by ComCtl32.dll, which all 32-bit and 64-bit versions of Windows include. Each successive version of the DLL supports the features and API of earlier versions and adds new features.

Because various versions of ComCtl32.dll were distributed with Internet Explorer, the version that is active is sometimes different from the version that was shipped with the operating system. Therefore, your application must directly determine which version of ComCtl32.dll is present.

In the common controls reference documentation, many programming elements specify a minimum supported DLL version number. This version number indicates that the programming element is implemented in that version and subsequent versions of the DLL unless otherwise specified. If no version number is specified, the programming element is implemented in all existing versions of the DLL.

The following table outlines the different DLL versions and how they were distributed on supported OSes.



ComCtl32.dll

Version

Distribution Platform

5.81

Microsoft Internet Explorer 5.01, Microsoft Internet Explorer 5.5, and Microsoft Internet Explorer 6

5.82

Windows Server 2003, Windows Vista, Windows Server 2008, and Windows 7

6.0

Windows Server 2003

6.10

Windows Vista, Windows Server 2008, and Windows 7



 

## Structure Sizes for Different Common Control Versions

Ongoing enhancements to common controls have resulted in the need to extend many of the structures. For this reason, the size of the structures has changed between different versions of Commctrl.h. Because most of the common control structures take a structure size as one of the parameters, a message or function can fail if the size is not recognized. To remedy this, structure size constants have been defined to aid in targeting different version of ComCtl32.dll. The following list defines the structure size constants.



|    Structure Size Constant                           |     Definition                                                                                         |
|-------------------------------|----------------------------------------------------------------------------------------------|
| HDITEM\_V1\_SIZE              | The size of the [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure in version 4.0.                           |
| IMAGELISTDRAWPARAMS\_V3\_SIZE | The size of the [**IMAGELISTDRAWPARAMS**](/windows/win32/api/commctrl/ns-commctrl-imagelistdrawparams) structure in version 5.9. |
| LVCOLUMN\_V1\_SIZE            | The size of the [**LVCOLUMN**](/windows/win32/api/commctrl/ns-commctrl-lvcolumna) structure in version 4.0.                       |
| LVGROUP\_V5\_SIZE             | The size of the [**LVGROUP**](/windows/win32/api/commctrl/ns-commctrl-lvgroup) structure in version 6.0.                         |
| LVHITTESTINFO\_V1\_SIZE       | The size of the [**LVHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-lvhittestinfo) structure in version 4.0.             |
| LVITEM\_V1\_SIZE              | The size of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure in version 4.0.                           |
| LVITEM\_V5\_SIZE              | The size of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure in version 6.0.                           |
| LVTILEINFO\_V5\_SIZE          | The size of the [**LVTILEINFO**](/windows/win32/api/commctrl/ns-commctrl-lvtileinfo) structure in version 6.0.                   |
| MCHITTESTINFO\_V1\_SIZE       | The size of the [**MCHITTESTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-mchittestinfo) structure in version 4.0.             |
| NMLVCUSTOMDRAW\_V3\_SIZE      | The size of the [**NMLVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmlvcustomdraw) structure in version 4.7.           |
| NMTTDISPINFO\_V1\_SIZE        | The size of the [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa) structure in version 4.0.               |
| NMTVCUSTOMDRAW\_V3\_SIZE      | The size of the [**NMTVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvcustomdraw) structure in version 4.7.           |
| PROPSHEETHEADER\_V1\_SIZE     | The size of the [**PROPSHEETHEADER**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2) structure in version 4.0.         |
| PROPSHEETPAGE\_V1\_SIZE       | The size of the [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/ns-prsht-propsheetpagea_v2) structure in version 4.0.             |
| REBARBANDINFO\_V3\_SIZE       | The size of the [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure in version 4.7.             |
| REBARBANDINFO\_V6\_SIZE       | The size of the [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure in version 6.0.             |
| TTTOOLINFO\_V1\_SIZE          | The size of the [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure in version 4.0.                       |
| TTTOOLINFO\_V2\_SIZE          | The size of the [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure in version 4.7.                       |
| TTTOOLINFO\_V3\_SIZE          | The size of the [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure in version 6.0.                       |
| TVINSERTSTRUCT\_V1\_SIZE      | The size of the [**TVINSERTSTRUCT**](/windows/win32/api/commctrl/ns-commctrl-tvinsertstructa) structure in version 4.0.           |



 

## Using DllGetVersion to Determine the Version Number

The [**DllGetVersion**](/windows/desktop/api/shlwapi/nc-shlwapi-dllgetversionproc) function can be called by an application to determine which DLL version is present on the system.

[**DllGetVersion**](/windows/desktop/api/shlwapi/nc-shlwapi-dllgetversionproc) returns a [**DLLVERSIONINFO2**](/windows/desktop/api/shlwapi/ns-shlwapi-dllversioninfo2) structure. In addition to the information provided through [**DLLVERSIONINFO**](/windows/desktop/api/shlwapi/ns-shlwapi-dllversioninfo), **DLLVERSIONINFO2** also provides the hotfix number that identifies the latest installed service pack, which provides a more robust way to compare version numbers. Because the first member of **DLLVERSIONINFO2** is a **DLLVERSIONINFO** structure, the later structure is backward-compatible.


The following sample function `GetVersion` loads a specified DLL and attempts to call its [**DllGetVersion**](/windows/desktop/api/shlwapi/nc-shlwapi-dllgetversionproc) function. If successful, it uses a macro to pack the major and minor version numbers from the [**DLLVERSIONINFO**](/windows/desktop/api/shlwapi/ns-shlwapi-dllversioninfo) structure into a **DWORD** that is returned to the calling application. If the DLL does not export **DllGetVersion**, the function returns zero. You can modify the function to handle the possibility that **DllGetVersion** returns a [**DLLVERSIONINFO2**](/windows/desktop/api/shlwapi/ns-shlwapi-dllversioninfo2) structure. If so, use the information in that **DLLVERSIONINFO2** structure's **ullVersion** member to compare versions, build numbers, and service pack releases. The [**MAKEDLLVERULL**](/windows/desktop/api/shlwapi/nf-shlwapi-makedllverull) macro simplifies the task of comparing these values to those in **ullVersion**.

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can pose security risks. Refer to the **LoadLibrary** documentation for information on how to correctly load DLLs with different versions of Windows.

 


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

    // For security purposes, LoadLibrary should be provided with a fully qualified 
    // path to the DLL. The lpszDllName variable should be tested to ensure that it 
    // is a fully qualified path before it is used. 
    hinstDll = LoadLibrary(lpszDllName);
    
    if(hinstDll)
    {
        DLLGETVERSIONPROC pDllGetVersion;
        pDllGetVersion = (DLLGETVERSIONPROC)GetProcAddress(hinstDll, "DllGetVersion");

        // Because some DLLs might not implement this function, you must test for 
        // it explicitly. Depending on the particular DLL, the lack of a DllGetVersion 
        // function can be a useful indicator of the version. 

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



The following code example shows how you can use `GetVersion` to test whether ComCtl32.dll is version 6.0 or later.


```C++
LPCTSTR lpszDllName = L"C:\\Windows\\System32\\ComCtl32.dll";
DWORD dwVer = GetVersion(lpszDllName);
DWORD dwTarget = PACKVERSION(6,0);

if(dwVer >= dwTarget)
{
    // This version of ComCtl32.dll is version 6.0 or later.
}
else
{
    // Proceed knowing that version 6.0 or later additions are not available.
    // Use an alternate approach for older the DLL version.
}
```



## Project Versions

To ensure that your application is compatible with different targeted versions of a .dll file, version macros are present in the header files. These macros are used to define, exclude, or redefine certain definitions for different versions of the DLL. See [Using the Windows Headers](/windows/desktop/WinProg/using-the-windows-headers) for an in-depth description of these macros.

For example, the macro name **\_WIN32\_IE** is commonly found in older headers. You are responsible for defining the macro as a hexadecimal number. This version number defines the target version of the application that is using the DLL. The following table shows the available version numbers and the effect each has on your application.



| Version | Description                                                                                                                                           |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0300  | The application is compatible with ComCtl32.dll version 4.70 and later. The application cannot implement features that were added after version 4.70. |
| 0x0400  | The application is compatible with ComCtl32.dll version 4.71 and later. The application cannot implement features that were added after version 4.71. |
| 0x0401  | The application is compatible with ComCtl32.dll version 4.72 and later. The application cannot implement features that were added after version 4.72. |
| 0x0500  | The application is compatible with ComCtl32.dll version 5.80 and later. The application cannot implement features that were added after version 5.80. |
| 0x0501  | The application is compatible with ComCtl32.dll version 5.81 and later. The application cannot implement features that were added after version 5.81. |
| 0x0600  | The application is compatible with ComCtl32.dll version 6.0 and later. The application cannot implement features that were added after version 6.0.   |



 

If you do not define the **\_WIN32\_IE** macro in your project, it is automatically defined as 0x0500. To define a different value, you can add the following to the compiler directives in your make file; substitute the desired version number for 0x0400.


```C++
/D _WIN32_IE=0x0400
```



Another method is to add a line similar to the following in your source code before you include the Shell header files. Substitute the desired version number for 0x0400.


```C++
#define _WIN32_IE 0x0400
#include <commctrl.h>
```



## Related topics

<dl> <dt>

[About Common Controls](common-controls-intro.md)
</dt> </dl>

 

 