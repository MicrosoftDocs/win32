---
Description: Explains the interactions between Winlogon and network providers.
ms.assetid: 09d0b5ce-e2ac-40d7-bc35-272c5f831788
title: Interaction with Network Providers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interaction with Network Providers

You can configure a system to support zero or more network providers. Each of these network providers can specify that it requires special interactive authentication processing. This capability allows installed networks to collect identification and authentication information specific to each network, yet allows them to collect it during normal logon and under the secure umbrella of [*Winlogon's*](security.w_gly#-security-winlogon-gly) [*context*](security.c_gly#-security-context-gly) and desktop.

Winlogon calls network providers under a number of circumstances. Following a successful logon, Winlogon calls network providers so they can collect [*credentials*](security.c_gly#-security-credentials-gly) and authenticate the user for their network. Winlogon also calls network providers when users change their passwords. This lets each user maintain a single password for use on all networks.

The [**WLX\_MPR\_NOTIFY\_INFO**](/windows/win32/Winwlx/ns-winwlx-_wlx_mpr_notify_info?branch=master) structure is used to provide identification and authentication information in the relevant GINA functions. This structure includes the following members.



| Member             | Description                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **pszUserName**    | The account name of the logged-on user.                                                                                                                                                      |
| **pszDomain**      | The domain name of the logged-on user. Not all authentication models have a domain concept (or its equivalent), so this member can be **NULL**.                                              |
| **pszPassword**    | When the user gave a plaintext password during authentication, providing it here lets other network providers use the same password (to achieve single logon) without prompting the user.    |
| **pszOldPassword** | After a password change, providing the original password here and the new password in the **pszPassword** member, lets network providers upgrade their passwords without prompting the user. |



 

A [*GINA*](security.g_gly#-security-gina-gly) does not have to provide this information to network providers. If a **NULL** pointer is passed instead of a valid structure pointer, the network providers will prompt the user for information.

 

 



