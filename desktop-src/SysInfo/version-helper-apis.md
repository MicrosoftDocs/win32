---
description: The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release.
ms.assetid: 2FAF67CD-CEEA-4096-B482-F5E2DF8D6C34
title: Version Helper functions
ms.topic: article
ms.date: 05/31/2018
---

# Version Helper functions

The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release. These functions provide simple tests that use the [VerifyVersionInfo](/windows/desktop/api/Winbase/nf-winbase-verifyversioninfoa) function and the recommended greater than or equal to comparisons that are proven as a robust means to determine the operating system version.

> [!Note]  
> These APIs are defined by **versionhelpers.h**, which is included in the Windows 8.1 software development kit (SDK). This file can be used with other Microsoft Visual Studio releases to implement the same functionality for Windows versions prior to Windows 8.1.

<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsxporgreater"><strong>IsWindowsXPOrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP version.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp1orgreater"><strong>IsWindowsXPSP1OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp2orgreater"><strong>IsWindowsXPSP2OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 2 (SP2) version.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsxpsp3orgreater"><strong>IsWindowsXPSP3OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 3 (SP3) version.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsvistaorgreater"><strong>IsWindowsVistaOrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista version.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsvistasp1orgreater"><strong>IsWindowsVistaSP1OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsvistasp2orgreater"><strong>IsWindowsVistaSP2OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 2 (SP2) version.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows7orgreater"><strong>IsWindows7OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 7 version.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows7sp1orgreater"><strong>IsWindows7SP1OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 7 with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows8orgreater"><strong>IsWindows8OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 8 version.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows8point1orgreater"><strong>IsWindows8Point1OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 8.1 version.<br/> For Windows 10, <a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows8point1orgreater"><strong>IsWindows8Point1OrGreater</strong></a> returns false unless the application contains a manifest that includes a compatibility section that contains the GUIDs that designate Windows 8.1 and/or Windows 10.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows10orgreater"><strong>IsWindows10OrGreater</strong></a></td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 10 version.<br/> For Windows 10, <a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindows10orgreater"><strong>IsWindows10OrGreater</strong></a> returns false unless the application contains a manifest that includes a compatibility section that contains the GUID that designates Windows 10.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsserver"><strong>IsWindowsServer</strong></a></td>
<td>Indicates if the current OS is a Windows Server release. Applications that need to distinguish between server and client versions of Windows should call this function.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/VersionHelpers/nf-versionhelpers-iswindowsversionorgreater"><strong>IsWindowsVersionOrGreater</strong></a></td>
<td>

> [!Note]  
> You should only use this function if the other provided version helper functions do not fit your scenario.

Indicates if the current OS version matches, or is greater than, the provided version information. This function is useful in confirming a version of Windows Server that doesn't share a version number with a client release.
</td>
</tr>
</tbody>
</table>

## Example

The inline functions defined in the **VersionHelpers.h** header file let you verify the operating system version by returning a **Boolean** value when testing for a version of Windows.

For example, if your application requires Windows 8 or later, use the following test.

```C++
#include <VersionHelpers.h>
 
    if (!IsWindows8OrGreater())
    {
       MessageBox(NULL, "You need at least Windows 8", "Version Not Supported", MB_OK);
    }
```

## Related topics

- [OSVERSIONINFOEX](/windows/desktop/api/Winnt/ns-winnt-osversioninfoexa)
