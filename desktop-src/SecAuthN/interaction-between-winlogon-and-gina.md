---
Description: Winlogon and the GINA must communicate initialization information, handle secure attention sequence (SAS) monitoring and notification, and permit logoff and shutdown activities.
ms.assetid: ea45cd5f-9cb0-41bb-99bf-f84781ae9604
title: Interaction Between Winlogon and GINA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interaction Between Winlogon and GINA

[*Winlogon*](https://www.bing.com/search?q=*Winlogon*) and the [*GINA*](https://www.bing.com/search?q=*GINA*) must communicate initialization information, handle [*secure attention sequence*](https://www.bing.com/search?q=*secure attention sequence*) (SAS) monitoring and notification, and permit logoff and shutdown activities. The state of Winlogon determines which GINA function is called to process any given SAS event. Communications occur in the order shown here.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Workstation boot</td>
<td><ol>
<li>Winlogon calls the GINA's [<strong>WlxNegotiate</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate) function to notify the GINA about the version of Winlogon in use.</li>
<li>Winlogon calls the GINA's [<strong>WlxInitialize</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxinitialize) function to give the GINA the addresses of the support functions, a handle to Winlogon, and to obtain the [<em>context</em>](https://www.bing.com/search?q=<em>context</em>) information for the GINA (to be used in all future calls to the GINA).<br/> Winlogon is in the logged-out state.<br/></li>
</ol></td>
</tr>
<tr class="even">
<td>No one is logged on</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls Winlogon's [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function when a SAS event has been received.</li>
<li>Winlogon calls the GINA's [<strong>WlxLoggedOutSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas) function, allowing the GINA to process a user's identification and authentication information.<br/> When logon is successful, Winlogon is in the logged-on state.<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls Winlogon's [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function when a SAS event has been received.</li>
<li>Winlogon calls the GINA's [<strong>WlxLoggedOnSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas) function, allowing the GINA to present options to the user who is currently logged on.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on and wants to lock computer</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxLoggedOnSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas) function.</li>
<li>The GINA returns WLX_SAS_ACTION_LOCK_WKSTA.<br/> Winlogon is in the workstation-locked state.<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on, the workstation is locked, and the user wants to unlock computer</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxWkstaLockedSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxwkstalockedsas) function.</li>
<li>The GINA returns WLX_SAS_ACTION_UNLOCK_WKSTA.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on, and the program calls the [<strong>ExitWindowsEx</strong>](https://msdn.microsoft.com/windows/desktop/f44ccb66-10bd-4ee6-93e1-16948cf10e50) function</td>
<td>Winlogon calls the GINA's [<strong>WlxLogoff</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff) function.</td>
</tr>
<tr class="odd">
<td>The user is logged on and wants to log off by using SAS</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxLoggedOnSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas) function.</li>
<li>The GINA returns WLX_SAS_ACTION_LOGOFF.</li>
<li>Winlogon calls the GINA's [<strong>WlxLogoff</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff) function.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on and wants to log off and shut down by using [<strong>ExitWindowsEx</strong>](https://msdn.microsoft.com/windows/desktop/f44ccb66-10bd-4ee6-93e1-16948cf10e50)</td>
<td><ol>
<li>Winlogon calls the GINA's [<strong>WlxLogoff</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxShutdown</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxshutdown) function.</li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on and wants to log off and shut down by using SAS</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the [<strong>WlxSasNotify</strong>](/windows/desktop/api/wlxutil/) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxLoggedOnSAS</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas) function.</li>
<li>The GINA returns WLX_SAS_ACTION_SHUTDOWN.</li>
<li>Winlogon calls the GINA's [<strong>WlxLogoff</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff) function.</li>
<li>Winlogon calls the GINA's [<strong>WlxShutdown</strong>](/windows/desktop/api/Winwlx/nf-winwlx-wlxshutdown) function.</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 




