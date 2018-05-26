---
Description: Functions for setting and retrieving an objects security descriptor.
ms.assetid: 22bf0d6b-3ec6-4c28-ace4-49e48714f4bf
title: Low-level Security Descriptor Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Low-level Security Descriptor Functions

There are several pairs of low-level functions for setting and retrieving an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly). Each of these pairs works only with a limited set of Windows objects. For example, one pair works with file objects and another works with registry keys. The following table shows the low-level functions to use with the different types of securable objects.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Object type</th>
<th>Low-level functions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>[Files](https://msdn.microsoft.com/library/windows/desktop/aa364399)</li>
<li>[Directories](https://msdn.microsoft.com/library/windows/desktop/aa364399)</li>
<li>Mailslots</li>
<li>[Named pipes](https://msdn.microsoft.com/library/windows/desktop/aa365600)</li>
</ul></td>
<td>Use the [<strong>GetFileSecurity</strong>](/windows/win32/Winbase/nf-winbase-getfilesecuritya?branch=master) and [<strong>SetFileSecurity</strong>](/windows/win32/Winbase/nf-winbase-setfilesecuritya?branch=master) functions. These functions use character strings to identify the securable object, instead of using handles.</td>
</tr>
<tr class="even">
<td><ul>
<li>[Processes](https://msdn.microsoft.com/library/windows/desktop/ms684880)</li>
<li>[Threads](https://msdn.microsoft.com/library/windows/desktop/ms686769)</li>
<li>[Access tokens](access-rights-for-access-token-objects.md)</li>
<li>[File-mapping objects](https://msdn.microsoft.com/library/windows/desktop/aa366559)</li>
<li>[Semaphores](https://msdn.microsoft.com/library/windows/desktop/ms686670)</li>
<li>[Events](https://msdn.microsoft.com/library/windows/desktop/ms686670)</li>
<li>[Mutexes](https://msdn.microsoft.com/library/windows/desktop/ms686670)</li>
<li>[Waitable timers](https://msdn.microsoft.com/library/windows/desktop/ms686670)</li>
</ul></td>
<td>Use the [<strong>GetKernelObjectSecurity</strong>](getkernelobjectsecurity.md) and [<strong>SetKernelObjectSecurity</strong>](setkernelobjectsecurity.md) functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[Window stations](https://msdn.microsoft.com/library/windows/desktop/ms687391)</li>
<li>[Desktops](https://msdn.microsoft.com/library/windows/desktop/ms682575)</li>
</ul></td>
<td>Use the [<strong>GetUserObjectSecurity</strong>](/windows/win32/Winuser/nf-winuser-getuserobjectsecurity?branch=master) and [<strong>SetUserObjectSecurity</strong>](/windows/win32/Winuser/nf-winuser-setuserobjectsecurity?branch=master) functions.</td>
</tr>
<tr class="even">
<td><ul>
<li>[Registry keys](https://msdn.microsoft.com/library/windows/desktop/ms724878)</li>
</ul></td>
<td>Use the [<strong>RegGetKeySecurity</strong>](/windows/win32/Winreg/nf-winreg-reggetkeysecurity?branch=master) and [<strong>RegSetKeySecurity</strong>](/windows/win32/Winreg/nf-winreg-regsetkeysecurity?branch=master) functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[Windows service objects](https://msdn.microsoft.com/library/windows/desktop/ms685981)</li>
</ul></td>
<td>Use the [<strong>QueryServiceObjectSecurity</strong>](/windows/win32/Winsvc/nf-winsvc-queryserviceobjectsecurity?branch=master) and [<strong>SetServiceObjectSecurity</strong>](/windows/win32/Winsvc/nf-winsvc-setserviceobjectsecurity?branch=master) functions.</td>
</tr>
<tr class="even">
<td><ul>
<li>Printer objects</li>
</ul></td>
<td>Use the [<strong>PRINTER_INFO_2</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162845) structure with the [<strong>GetPrinter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd144911) and [<strong>SetPrinter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd145082) functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[Network shares](https://msdn.microsoft.com/library/windows/desktop/aa370891)</li>
</ul></td>
<td>Use level 502 with the [<strong>NetShareGetInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/bb525388) and [<strong>NetShareSetInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/bb525389) functions.</td>
</tr>
<tr class="even">
<td><ul>
<li>[Private objects (objects private to the creating application)](acl-based-access-control.md)</li>
</ul></td>
<td>Use the [<strong>CreatePrivateObjectSecurity</strong>](createprivateobjectsecurity.md), [<strong>DestroyPrivateObjectSecurity</strong>](destroyprivateobjectsecurity.md), [<strong>GetPrivateObjectSecurity</strong>](getprivateobjectsecurity.md) and [<strong>SetPrivateObjectSecurity</strong>](setprivateobjectsecurity.md) functions.</td>
</tr>
</tbody>
</table>



 

 

 



