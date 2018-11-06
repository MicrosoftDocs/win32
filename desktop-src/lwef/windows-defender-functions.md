---
title: Windows Defender Functions
description: Functions called by apps to request scans, signature updates, or information from Windows Defender.
ms.assetid: BB3DF71E-1085-45D0-B739-F4C272E7098B
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
<td><a href="mperrormessageformat"><strong>MpErrorMessageFormat</strong></a></td>
<td>Returns a formatted error message based on an error code.<br/></td>
</tr>
<tr class="even">
<td><a href="mpfreememory"><strong>MpFreeMemory</strong></a></td>
<td>Frees memory for the malware protection manager.<br/></td>
</tr>
<tr class="odd">
<td><a href="mphandleclose"><strong>MpHandleClose</strong></a></td>
<td>Closes the handle returned by <a href="mpmanageropen"><strong>MpManagerOpen</strong></a>, <a href="mpscanstart"><strong>MpScanStart</strong></a>, <a href="mpthreatopen"><strong>MpThreatOpen</strong></a>, or <a href="mpupdatestart"><strong>MpUpdateStart</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="mpmanageropen"><strong>MpManagerOpen</strong></a></td>
<td>Establishes a connection to the malware protection manager on the local computer.<br/></td>
</tr>
<tr class="odd">
<td><a href="mpmanagerstatusquery"><strong>MpManagerStatusQuery</strong></a></td>
<td><strong>Not supported.</strong> Returns status information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="even">
<td><a href="mpmanagerstatusqueryex"><strong>MpManagerStatusQueryEx</strong></a></td>
<td>Returns status information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="odd">
<td><a href="mpmanagerversionquery"><strong>MpManagerVersionQuery</strong></a></td>
<td>Returns version information about various components of the malware protection manager.<br/></td>
</tr>
<tr class="even">
<td><a href="mpscancontrol"><strong>MpScanControl</strong></a></td>
<td>Allows the control of a scan that was asynchronously initiated via <a href="mpscanstart"><strong>MpScanStart</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="mpscanstart"><strong>MpScanStart</strong></a></td>
<td>Starts a scanning operation.<br/></td>
</tr>
<tr class="even">
<td><a href="mpthreatenumerate"><strong>MpThreatEnumerate</strong></a></td>
<td>Returns information about the next threat in the enumeration list. This function can be called repeatedly until the enumeration of all the threats is complete.<br/></td>
</tr>
<tr class="odd">
<td><a href="mpthreatopen"><strong>MpThreatOpen</strong></a></td>
<td>Returns an enumeration handle for the purpose of retrieving threats. This function can be used to open threats detected by a specific scan, all the active threats in the system, the history of threat disinfection, or all the threats present in the signature database.<br/></td>
</tr>
<tr class="even">
<td><a href="mpthreatquery"><strong>MpThreatQuery</strong></a></td>
<td>Used to query static (such as severity and category) or localized (such as category description and advice) information about a particular threat.<br/></td>
</tr>
<tr class="odd">
<td><a href="mpupdatecontrol"><strong>MpUpdateControl</strong></a></td>
<td>Allows the control of a signature update operation that was asynchronously initiated via <a href="mpupdatestart"><strong>MpUpdateStart</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="mpupdatestart"><strong>MpUpdateStart</strong></a></td>
<td>Starts a signature update operation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable"><strong>WDEnable</strong></a></td>
<td>Changes Windows Defender status to on or off.<br/>
<blockquote>
[!Note]<br />
Beginning in Windows 10, version 1607 and Windows Server 2016, the <a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable"><strong>WDEnable</strong></a> function always returns <strong>E_NOTIMPL</strong>.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdstatus"><strong>WDStatus</strong></a></td>
<td>Returns the current status of Windows Defender.<br/></td>
</tr>
</tbody>
</table>



 

 

 





