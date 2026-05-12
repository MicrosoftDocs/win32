---
description: The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release.
ms.assetid: 2FAF67CD-CEEA-4096-B482-F5E2DF8D6C34
title: Version Helper functions
ms.topic: reference
ms.date: 02/13/2024
---

# Version Helper functions

The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release. These functions provide simple tests that use the [VerifyVersionInfo](/windows/win32/api/Winbase/nf-winbase-verifyversioninfoa) function and the recommended greater than or equal to comparisons that are proven as a robust means to determine the operating system version.

> [!NOTE]
> These APIs are defined by **versionhelpers.h**, which is included in the Windows Software Development Kit (SDK) for Windows 8.1 and later. This file can be used with other Microsoft Visual Studio releases to implement the same functionality for Windows versions prior to Windows 8.1.

> [!NOTE]
> **Versionhelpers.h** requires **windows.h** to be included before it.

| Function | Description |
|----------|-------------|
| [**IsWindowsXPOrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsxporgreater) | Indicates if the current OS version matches, or is greater than, the Windows XP version. |
| [**IsWindowsXPSP1OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp1orgreater) | Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 1 (SP1) version. |
| [**IsWindowsXPSP2OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp2orgreater) | Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 2 (SP2) version. |
| [**IsWindowsXPSP3OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp3orgreater) | Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 3 (SP3) version. |
| [**IsWindowsVistaOrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsvistaorgreater) | Indicates if the current OS version matches, or is greater than, the Windows Vista version. |
| [**IsWindowsVistaSP1OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsvistasp1orgreater) | Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 1 (SP1) version. |
| [**IsWindowsVistaSP2OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsvistasp2orgreater) | Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 2 (SP2) version. |
| [**IsWindows7OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows7orgreater) | Indicates if the current OS version matches, or is greater than, the Windows 7 version. |
| [**IsWindows7SP1OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows7sp1orgreater) | Indicates if the current OS version matches, or is greater than, the Windows 7 with Service Pack 1 (SP1) version. |
| [**IsWindows8OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows8orgreater) | Indicates if the current OS version matches, or is greater than, the Windows 8 version. |
| [**IsWindows8Point1OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows8point1orgreater) | Indicates if the current OS version matches, or is greater than, the Windows 8.1 version.<br/><br/>For Windows 10, [IsWindows8Point1OrGreater](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows8point1orgreater) returns false unless the application contains a manifest that includes a compatibility section that contains the GUIDs that designate Windows 8.1 and/or Windows 10. |
| [**IsWindows10OrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows10orgreater) | Indicates if the current OS version matches, or is greater than, the Windows 10 version.<br/><br/>For Windows 10, [IsWindows10OrGreater](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindows10orgreater) returns false unless the application contains a manifest that includes a compatibility section that contains the GUID that designates Windows 10. |
| [**IsWindowsServer**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsserver) | Indicates if the current OS is a Windows Server release. Applications that need to distinguish between server and client versions of Windows should call this function. |
| [**IsWindowsVersionOrGreater**](/windows/win32/api/VersionHelpers/nf-versionhelpers-iswindowsversionorgreater) | You should only use this function if the other provided version helper functions do not fit your scenario.<br/><br/>Indicates if the current OS version matches, or is greater than, the provided version information. This function is useful in confirming a version of Windows Server that doesn't share a version number with a client release. |

## Example

The inline functions defined in the **VersionHelpers.h** header file let you verify the operating system version by returning a **Boolean** value when testing for a version of Windows.

For example, if your application requires Windows 10 or later, use the following test.

```C++
#include <windows.h>
#include <VersionHelpers.h>
 
if (!IsWindows10OrGreater())
{
   MessageBox(NULL, "You need at least Windows 10", "Version Not Supported", MB_OK);
}
```

## Related topics

- [OSVERSIONINFOEX](/windows/desktop/api/Winnt/ns-winnt-osversioninfoexa)
