---
title: Windows Defender Functions
description: Functions called by apps to request scans, signature updates, or information from Windows Defender.
ms.assetid: BB3DF71E-1085-45D0-B739-F4C272E7098B
ms.topic: article
ms.date: 05/31/2018
---

# Windows Defender Functions

Functions called by apps to request scans, signature updates, or information from Windows Defender.




| Function | Description | 
|----------|-------------|
| <a href="mperrormessageformat.md"><strong>MpErrorMessageFormat</strong></a> | Returns a formatted error message based on an error code.<br /> | 
| <a href="mpfreememory.md"><strong>MpFreeMemory</strong></a> | Frees memory for the malware protection manager.<br /> | 
| <a href="mphandleclose.md"><strong>MpHandleClose</strong></a> | Closes the handle returned by <a href="mpmanageropen.md"><strong>MpManagerOpen</strong></a>, <a href="mpscanstart.md"><strong>MpScanStart</strong></a>, <a href="mpthreatopen.md"><strong>MpThreatOpen</strong></a>, or <a href="mpupdatestart.md"><strong>MpUpdateStart</strong></a>.<br /> | 
| <a href="mpmanageropen.md"><strong>MpManagerOpen</strong></a> | Establishes a connection to the malware protection manager on the local computer.<br /> | 
| <a href="mpmanagerstatusquery.md"><strong>MpManagerStatusQuery</strong></a> | <strong>Not supported.</strong> Returns status information about various components of the malware protection manager.<br /> | 
| <a href="mpmanagerstatusqueryex.md"><strong>MpManagerStatusQueryEx</strong></a> | Returns status information about various components of the malware protection manager.<br /> | 
| <a href="mpmanagerversionquery.md"><strong>MpManagerVersionQuery</strong></a> | Returns version information about various components of the malware protection manager.<br /> | 
| <a href="mpscancontrol.md"><strong>MpScanControl</strong></a> | Allows the control of a scan that was asynchronously initiated via <a href="mpscanstart.md"><strong>MpScanStart</strong></a>.<br /> | 
| <a href="mpscanstart.md"><strong>MpScanStart</strong></a> | Starts a scanning operation.<br /> | 
| <a href="mpthreatenumerate.md"><strong>MpThreatEnumerate</strong></a> | Returns information about the next threat in the enumeration list. This function can be called repeatedly until the enumeration of all the threats is complete.<br /> | 
| <a href="mpthreatopen.md"><strong>MpThreatOpen</strong></a> | Returns an enumeration handle for the purpose of retrieving threats. This function can be used to open threats detected by a specific scan, all the active threats in the system, the history of threat disinfection, or all the threats present in the signature database.<br /> | 
| <a href="mpthreatquery.md"><strong>MpThreatQuery</strong></a> | Used to query static (such as severity and category) or localized (such as category description and advice) information about a particular threat.<br /> | 
| <a href="mpupdatecontrol.md"><strong>MpUpdateControl</strong></a> | Allows the control of a signature update operation that was asynchronously initiated via <a href="mpupdatestart.md"><strong>MpUpdateStart</strong></a>.<br /> | 
| <a href="mpupdatestart.md"><strong>MpUpdateStart</strong></a> | Starts a signature update operation.<br /> | 
| <a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable"><strong>WDEnable</strong></a> | Changes Windows Defender status to on or off.<br /><blockquote>[!Note]<br />Beginning in Windows 10, version 1607 and Windows Server 2016, the <a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdenable"><strong>WDEnable</strong></a> function always returns <strong>E_NOTIMPL</strong>.</blockquote><br /><br /> | 
| <a href="/windows/desktop/api/Windowsdefender/nf-windowsdefender-wdstatus"><strong>WDStatus</strong></a> | Returns the current status of Windows Defender.<br /> | 




 

 

 





