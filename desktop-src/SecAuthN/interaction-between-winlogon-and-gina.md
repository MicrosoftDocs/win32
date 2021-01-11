---
description: Winlogon and the GINA must communicate initialization information, handle secure attention sequence (SAS) monitoring and notification, and permit logoff and shutdown activities.
ms.assetid: ea45cd5f-9cb0-41bb-99bf-f84781ae9604
title: Interaction Between Winlogon and GINA
ms.topic: article
ms.date: 05/31/2018
---

# Interaction Between Winlogon and GINA

[*Winlogon*](../secgloss/w-gly.md) and the [*GINA*](../secgloss/g-gly.md) must communicate initialization information, handle [*secure attention sequence*](../secgloss/s-gly.md) (SAS) monitoring and notification, and permit logoff and shutdown activities. The state of Winlogon determines which GINA function is called to process any given SAS event. Communications occur in the order shown here.

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
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate"><strong>WlxNegotiate</strong></a> function to notify the GINA about the version of Winlogon in use.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxinitialize"><strong>WlxInitialize</strong></a> function to give the GINA the addresses of the support functions, a handle to Winlogon, and to obtain the <a href="/windows/desktop/SecGloss/c-gly"><em>context</em></a> information for the GINA (to be used in all future calls to the GINA).<br/> Winlogon is in the logged-out state.<br/></li>
</ol></td>
</tr>
<tr class="even">
<td>No one is logged on</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls Winlogon's <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function when a SAS event has been received.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas"><strong>WlxLoggedOutSAS</strong></a> function, allowing the GINA to process a user's identification and authentication information.<br/> When logon is successful, Winlogon is in the logged-on state.<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls Winlogon's <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function when a SAS event has been received.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas"><strong>WlxLoggedOnSAS</strong></a> function, allowing the GINA to present options to the user who is currently logged on.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on and wants to lock computer</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas"><strong>WlxLoggedOnSAS</strong></a> function.</li>
<li>The GINA returns WLX_SAS_ACTION_LOCK_WKSTA.<br/> Winlogon is in the workstation-locked state.<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on, the workstation is locked, and the user wants to unlock computer</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxwkstalockedsas"><strong>WlxWkstaLockedSAS</strong></a> function.</li>
<li>The GINA returns WLX_SAS_ACTION_UNLOCK_WKSTA.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on, and the program calls the <a href="/windows/desktop/api/winuser/nf-winuser-exitwindowsex"><strong>ExitWindowsEx</strong></a> function</td>
<td>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff"><strong>WlxLogoff</strong></a> function.</td>
</tr>
<tr class="odd">
<td>The user is logged on and wants to log off by using SAS</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas"><strong>WlxLoggedOnSAS</strong></a> function.</li>
<li>The GINA returns WLX_SAS_ACTION_LOGOFF.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff"><strong>WlxLogoff</strong></a> function.</li>
</ol></td>
</tr>
<tr class="even">
<td>The user is logged on and wants to log off and shut down by using <a href="/windows/desktop/api/winuser/nf-winuser-exitwindowsex"><strong>ExitWindowsEx</strong></a></td>
<td><ol>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff"><strong>WlxLogoff</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxshutdown"><strong>WlxShutdown</strong></a> function.</li>
</ol></td>
</tr>
<tr class="odd">
<td>The user is logged on and wants to log off and shut down by using SAS</td>
<td>(The GINA monitors devices for SAS events).
<ol>
<li>The GINA calls the <a href="/windows/desktop/api/winwlx/nc-winwlx-pwlx_sas_notify"><strong>WlxSasNotify</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas"><strong>WlxLoggedOnSAS</strong></a> function.</li>
<li>The GINA returns WLX_SAS_ACTION_SHUTDOWN.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff"><strong>WlxLogoff</strong></a> function.</li>
<li>Winlogon calls the GINA's <a href="/windows/desktop/api/Winwlx/nf-winwlx-wlxshutdown"><strong>WlxShutdown</strong></a> function.</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 
