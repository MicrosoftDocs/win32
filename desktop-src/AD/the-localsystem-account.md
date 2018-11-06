---
title: Using the LocalSystem Account as a Service Logon Account
description: One advantage of running under the LocalSystem account is that the service has complete unrestricted access to local resources.
ms.assetid: 2bc2e16d-bd25-4ec6-91a2-8d03052df021
ms.tgt_platform: multiple
keywords:
- localsystem account
- localsystem
ms.topic: article
ms.date: 05/31/2018
---

# Using the LocalSystem Account as a Service Logon Account

One advantage of running under the LocalSystem account is that the service has complete unrestricted access to local resources. This is also the disadvantage of LocalSystem because a LocalSystem service can do things that would bring down the entire system. In particular, a service running as LocalSystem on a domain controller (DC) has unrestricted access to Active Directory Domain Services. This means that bugs in the service, or security attacks on the service, can damage the system or, if the service is on a DC, damage the entire enterprise network.

For these reasons, domain administrators at sensitive installations will be cautious about allowing services to run as LocalSystem. In fact, they may have policies against it, especially on DCs. If your service must run as LocalSystem, the documentation for your service should justify to domain administrators the reasons for granting the service the right to run at elevated privileges. Services should never run as LocalSystem on a domain controller. For more information and a code example that shows how a service or service installer can determine if it is running on a domain controller, see [Testing Whether Running on a Domain Controller](testing-whether-running-on-a-domain-controller.md).

When a service runs under the LocalSystem account on a computer that is a domain member, the service has whatever network access is granted to the computer account, or to any groups of which the computer account is a member. Be aware that in Windows 2000, a domain computer account is a service principal, similar to a user account. This means that a computer account can be in a security group, and an ACE in a security descriptor can grant access to a computer account. Be aware that adding computer accounts to groups is not recommended for two reasons:

-   Computer accounts are subject to deletion and re-creation if the computer leaves and then rejoins the domain.
-   If you add a computer account to a group, all services running as LocalSystem on that computer are permitted the access rights of the group. This is because all LocalSystem services share the computer account of their host server. For this reason, it is particularly important that computer accounts not be made members of any domain administrator groups.

Computer accounts typically have few privileges and do not belong to groups. The default ACL protection in Active Directory Domain Services permits minimal access for computer accounts. Consequently, services running as LocalSystem, on computers other than DCs, have only minimal access to Active Directory Domain Services.

If your service runs under LocalSystem, you must test your service on a member server to ensure that your service has sufficient rights to read/write to Active Directory Domain Controllers. A domain controller should not be the only Windows computer on which you test your service. Be aware that a service running under LocalSystem on a Windows domain controller has complete access to Active Directory Domain Services and that a member server runs in the context of the computer account which has substantially fewer rights.

 

 




