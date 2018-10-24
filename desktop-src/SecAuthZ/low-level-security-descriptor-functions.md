---
Description: Functions for setting and retrieving an objects security descriptor.
ms.assetid: 22bf0d6b-3ec6-4c28-ace4-49e48714f4bf
title: Low-level Security Descriptor Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<li><a href="https://msdn.microsoft.com/library/windows/desktop/aa364399">Files</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/aa364399">Directories</a></li>
<li>Mailslots</li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/aa365600">Named pipes</a></li>
</ul></td>
<td>Use the <a href="/windows/desktop/api/Winbase/nf-winbase-getfilesecuritya"><strong>GetFileSecurity</strong></a> and <a href="/windows/desktop/api/Winbase/nf-winbase-setfilesecuritya"><strong>SetFileSecurity</strong></a> functions. These functions use character strings to identify the securable object, instead of using handles.</td>
</tr>
<tr class="even">
<td><ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms684880">Processes</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms686769">Threads</a></li>
<li><a href="access-rights-for-access-token-objects">Access tokens</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/aa366559">File-mapping objects</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms686670">Semaphores</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms686670">Events</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms686670">Mutexes</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms686670">Waitable timers</a></li>
</ul></td>
<td>Use the <a href="https://msdn.microsoft.com/en-us/library/Aa446641(v=VS.85).aspx"><strong>GetKernelObjectSecurity</strong></a> and <a href="https://msdn.microsoft.com/en-us/library/Aa379578(v=VS.85).aspx"><strong>SetKernelObjectSecurity</strong></a> functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms687391">Window stations</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms682575">Desktops</a></li>
</ul></td>
<td>Use the <a href="/windows/desktop/api/Winuser/nf-winuser-getuserobjectsecurity"><strong>GetUserObjectSecurity</strong></a> and <a href="/windows/desktop/api/Winuser/nf-winuser-setuserobjectsecurity"><strong>SetUserObjectSecurity</strong></a> functions.</td>
</tr>
<tr class="even">
<td><ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms724878">Registry keys</a></li>
</ul></td>
<td>Use the <a href="/windows/desktop/api/Winreg/nf-winreg-reggetkeysecurity"><strong>RegGetKeySecurity</strong></a> and <a href="/windows/desktop/api/Winreg/nf-winreg-regsetkeysecurity"><strong>RegSetKeySecurity</strong></a> functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms685981">Windows service objects</a></li>
</ul></td>
<td>Use the <a href="/windows/desktop/api/Winsvc/nf-winsvc-queryserviceobjectsecurity"><strong>QueryServiceObjectSecurity</strong></a> and <a href="/windows/desktop/api/Winsvc/nf-winsvc-setserviceobjectsecurity"><strong>SetServiceObjectSecurity</strong></a> functions.</td>
</tr>
<tr class="even">
<td><ul>
<li>Printer objects</li>
</ul></td>
<td>Use the <a href="https://msdn.microsoft.com/library/windows/desktop/dd162845"><strong>PRINTER_INFO_2</strong></a> structure with the <a href="https://msdn.microsoft.com/library/windows/desktop/dd144911"><strong>GetPrinter</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd145082"><strong>SetPrinter</strong></a> functions.</td>
</tr>
<tr class="odd">
<td><ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/aa370891">Network shares</a></li>
</ul></td>
<td>Use level 502 with the <a href="https://msdn.microsoft.com/library/windows/desktop/bb525388"><strong>NetShareGetInfo</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/bb525389"><strong>NetShareSetInfo</strong></a> functions.</td>
</tr>
<tr class="even">
<td><ul>
<li><a href="acl-based-access-control">Private objects (objects private to the creating application)</a></li>
</ul></td>
<td>Use the <a href="https://msdn.microsoft.com/en-us/library/Aa376405(v=VS.85).aspx"><strong>CreatePrivateObjectSecurity</strong></a>, <a href="https://msdn.microsoft.com/en-us/library/Aa446613(v=VS.85).aspx"><strong>DestroyPrivateObjectSecurity</strong></a>, <a href="https://msdn.microsoft.com/en-us/library/Aa446646(v=VS.85).aspx"><strong>GetPrivateObjectSecurity</strong></a> and <a href="https://msdn.microsoft.com/en-us/library/Aa379580(v=VS.85).aspx"><strong>SetPrivateObjectSecurity</strong></a> functions.</td>
</tr>
</tbody>
</table>



 

 

 



