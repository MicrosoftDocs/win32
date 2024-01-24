---
description: AppInit_DLLs in Windows 7 and Windows Server 2008 R2
ms.assetid: 6d1f9703-6dc9-4fdc-b52f-e6bb60a2fe8d
title: AppInit_DLLs in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# AppInit\_DLLs in Windows 7 and Windows Server 2008 R2

## Platform

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

AppInit\_DLLs is a mechanism that allows an arbitrary list of DLLs to be loaded into each user mode process on the system. Microsoft is modifying the AppInit DLLs facility in Windows 7 and Windows Server 2008 R2 to add a new code-signing requirement. This will help improve the system reliability and performance, as well as improve visibility into the origin of software.

## Configuration

Values stored under the HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion \\Windows key in the registry determine the behavior of the AppInit\_DLLs infrastructure. The table below describes these registry values:



<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
<th>Sample Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">LoadAppInit_DLLs (REG_DWORD)${REMOVE}$<br />
</td>
<td rowspan="2">Globally enables or disables AppInit_DLLs.${REMOVE}$<br />
</td>
<td>0x0 – AppInit_DLLs are disabled.</td>
</tr>
<tr class="even">
<td>0x1 – AppInit_DLLs are enabled.</td>


</tr>
<tr class="odd">
<td>AppInit_DLLs (REG_SZ)</td>
<td>Space or comma delimited list of DLLs to load. The complete path to the DLL should be specified using Short Names.</td>
<td>C:\ PROGRA~1\WID288~1\MICROS~1.DLL</td>
</tr>
<tr class="even">
<td rowspan="2">RequireSignedAppInit_DLLs (REG_DWORD)${REMOVE}$<br />
</td>
<td rowspan="2">Only load code-signed DLLs.${REMOVE}$<br />
</td>
<td>0x0 – Load any DLLs.</td>
</tr>
<tr class="odd">
<td>0x1 – Load only code-signed DLLs.</td>


</tr>
</tbody>
</table>



 

**Windows 7**

All DLLs that are loaded by the AppInit\_DLLs infrastructure should be code-signed. In the interests of application compatibility, the Windows 7 Operating System will load all AppInit DLLs. However, Microsoft recommends that all application developers code-sign their DLLs to help improve the reliability of Windows and prepare for code-signing enforcement in future versions of Windows. The RequireSignedAppInit\_DLLs registry key controls this behavior and its value on Windows 7 is set to 0 by default.

**Windows Server 2008 R2**

All DLLs that are loaded by the AppInit\_DLLs infrastructure must be code-signed. The RequireSignedAppInit\_DLLs registry key controls this behavior and its value on Windows Server 2008 R2 is set to 1 by default.

## Links to Other Resources

<dl>

[AppInit DLLs in Windows 7 and Windows Server 2008 R2](/windows-hardware/drivers/install/)  
</dl>

 

 
