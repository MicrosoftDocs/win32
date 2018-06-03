---
title: Windows Defender Functions
description: Functions called by apps to request scans, signature updates, or information from Windows Defender.
ms.assetid: BB3DF71E-1085-45D0-B739-F4C272E7098B
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Defender Functions

Functions called by apps to request scans, signature updates, or information from Windows Defender.



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
<td>[<strong>MpErrorMessageFormat</strong>](mperrormessageformat.md)</td>
<td>Returns a formatted error message based on an error code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpFreeMemory</strong>](mpfreememory.md)</td>
<td>Frees memory for the malware protection manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpHandleClose</strong>](mphandleclose.md)</td>
<td>Closes the handle returned by [<strong>MpManagerOpen</strong>](mpmanageropen.md), [<strong>MpScanStart</strong>](mpscanstart.md), [<strong>MpThreatOpen</strong>](mpthreatopen.md), or [<strong>MpUpdateStart</strong>](mpupdatestart.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpManagerOpen</strong>](mpmanageropen.md)</td>
<td>Establishes a connection to the malware protection manager on the local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpManagerStatusQuery</strong>](mpmanagerstatusquery.md)</td>
<td><strong>Not supported.</strong> Returns status information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpManagerStatusQueryEx</strong>](mpmanagerstatusqueryex.md)</td>
<td>Returns status information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpManagerVersionQuery</strong>](mpmanagerversionquery.md)</td>
<td>Returns version information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpScanControl</strong>](mpscancontrol.md)</td>
<td>Allows the control of a scan that was asynchronously initiated via [<strong>MpScanStart</strong>](mpscanstart.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpScanStart</strong>](mpscanstart.md)</td>
<td>Starts a scanning operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpThreatEnumerate</strong>](mpthreatenumerate.md)</td>
<td>Returns information about the next threat in the enumeration list. This function can be called repeatedly until the enumeration of all the threats is complete.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpThreatOpen</strong>](mpthreatopen.md)</td>
<td>Returns an enumeration handle for the purpose of retrieving threats. This function can be used to open threats detected by a specific scan, all the active threats in the system, the history of threat disinfection, or all the threats present in the signature database.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpThreatQuery</strong>](mpthreatquery.md)</td>
<td>Used to query static (such as severity and category) or localized (such as category description and advice) information about a particular threat.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MpUpdateControl</strong>](mpupdatecontrol.md)</td>
<td>Allows the control of a signature update operation that was asynchronously initiated via [<strong>MpUpdateStart</strong>](mpupdatestart.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MpUpdateStart</strong>](mpupdatestart.md)</td>
<td>Starts a signature update operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WDEnable</strong>](/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable)</td>
<td>Changes Windows Defender status to on or off.<br/>
<blockquote>
[!Note]<br />
Beginning in Windows 10, version 1607 and Windows Server 2016, the [<strong>WDEnable</strong>](/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable) function always returns <strong>E_NOTIMPL</strong>.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>WDStatus</strong>](/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdstatus)</td>
<td>Returns the current status of Windows Defender.<br/></td>
</tr>
</tbody>
</table>



 

 

 





