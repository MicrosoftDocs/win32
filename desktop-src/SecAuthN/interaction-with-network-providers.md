---
Description: Explains the interactions between Winlogon and network providers.
ms.assetid: 09d0b5ce-e2ac-40d7-bc35-272c5f831788
title: Interaction with Network Providers
ms.topic: article
ms.date: 05/31/2018
---

# Interaction with Network Providers

You can configure a system to support zero or more network providers. Each of these network providers can specify that it requires special interactive authentication processing. This capability allows installed networks to collect identification and authentication information specific to each network, yet allows them to collect it during normal logon and under the secure umbrella of [*Winlogon's*](https://msdn.microsoft.com/library/ms721635(v=VS.85).aspx) [*context*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) and desktop.

Winlogon calls network providers under a number of circumstances. Following a successful logon, Winlogon calls network providers so they can collect [*credentials*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) and authenticate the user for their network. Winlogon also calls network providers when users change their passwords. This lets each user maintain a single password for use on all networks.

The [**WLX\_MPR\_NOTIFY\_INFO**](/windows/desktop/api/Winwlx/ns-winwlx-wlx_mpr_notify_info) structure is used to provide identification and authentication information in the relevant GINA functions. This structure includes the following members.



| Member             | Description                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **pszUserName**    | The account name of the logged-on user.                                                                                                                                                      |
| **pszDomain**      | The domain name of the logged-on user. Not all authentication models have a domain concept (or its equivalent), so this member can be **NULL**.                                              |
| **pszPassword**    | When the user gave a plaintext password during authentication, providing it here lets other network providers use the same password (to achieve single logon) without prompting the user.    |
| **pszOldPassword** | After a password change, providing the original password here and the new password in the **pszPassword** member, lets network providers upgrade their passwords without prompting the user. |



 

A [*GINA*](https://msdn.microsoft.com/library/ms721584(v=VS.85).aspx) does not have to provide this information to network providers. If a **NULL** pointer is passed instead of a valid structure pointer, the network providers will prompt the user for information.

 

 



