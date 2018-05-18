---
Description: 'The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release.'
ms.assetid: '2FAF67CD-CEEA-4096-B482-F5E2DF8D6C34'
title: Version Helper functions
---

# Version Helper functions

The following functions can be used to determine the current operating system version or identify whether it is a Windows or Windows Server release. These functions provide simple tests that use the [**VerifyVersionInfo**](verifyversioninfo.md) function and the recommended greater than or equal to comparisons that are proven as a robust means to determine the operating system version.

> [!Note]  
> These APIs are defined by **versionhelpers.h**, which is included in the Windows 8.1 software development kit (SDK). This file can be used with other Microsoft Visual Studio releases to implement the same functionality for Windows versions prior to Windows 8.1.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IsWindowsXPOrGreater</strong>](iswindowsxporgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindowsXPSP1OrGreater</strong>](iswindowsxpsp1orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindowsXPSP2OrGreater</strong>](iswindowsxpsp2orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 2 (SP2) version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindowsXPSP3OrGreater</strong>](iswindowsxpsp3orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows XP with Service Pack 3 (SP3) version.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindowsVistaOrGreater</strong>](iswindowsvistaorgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindowsVistaSP1OrGreater</strong>](iswindowsvistasp1orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindowsVistaSP2OrGreater</strong>](iswindowsvistasp2orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows Vista with Service Pack 2 (SP2) version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindows7OrGreater</strong>](iswindows7orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 7 version.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindows7SP1OrGreater</strong>](iswindows7sp1orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 7 with Service Pack 1 (SP1) version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindows8OrGreater</strong>](iswindows8orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 8 version.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindows8Point1OrGreater</strong>](iswindows8-1orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 8.1 version.<br/> For Windows 10, [<strong>IsWindows8Point1OrGreater</strong>](iswindows8-1orgreater.md) returns false unless the application contains a manifest that includes a compatibility section that contains the GUIDs that designate Windows 8.1 and/or Windows 10.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindows10OrGreater</strong>](iswindows10orgreater.md)</td>
<td>Indicates if the current OS version matches, or is greater than, the Windows 10 version.<br/> For Windows 10, [<strong>IsWindows10OrGreater</strong>](iswindows10orgreater.md) returns false unless the application contains a manifest that includes a compatibility section that contains the GUID that designates Windows 10.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsWindowsServer</strong>](iswindowsserver.md)</td>
<td>Indicates if the current OS is a Windows Server release. Applications that need to distinguish between server and client versions of Windows should call this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsWindowsVersionOrGreater</strong>](iswindowsversionorgreater.md)</td>
<td><blockquote>
[!Note]<br />
You should only use this function if the other provided version helper functions do not fit your scenario.
</blockquote>
<br/> Indicates if the current OS version matches, or is greater than, the provided version information. This function is useful in confirming a version of Windows Server that doesn't share a version number with a client release.<br/></td>
</tr>
</tbody>
</table>



 

## Example

The inline functions defined in the **VersionHelpers.h** header file let you verify the operating system version by returning a **Boolean** value when testing for a version of Windows.

For example, if your application requires Windows 8 or later, use the following test.


```C++
#include <VersionHelpers.h>
…
    if (!IsWindows8OrGreater())
    {
       MessageBox(NULL, "You need at least Windows 8", "Version Not Supported", MB_OK);
    }
```



## Related topics

<dl> <dt>

[**OSVERSIONINFOEX**](osversioninfoex-str.md)
</dt> </dl>

 

 




