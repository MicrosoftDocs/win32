---
title: Using a Local User Account as a Service Logon Account
description: A local user account (name format \ 0034;.\\UserName \ 0034;) exists only in the SAM database of the host computer; it does not have a user object in Active Directory Domain Services.
ms.assetid: a36d4d1c-3cfc-4ae1-8f1d-3f2e766f0c4b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Using a Local User Account as a Service Logon Account

A local user account (name format: ".\\*UserName*") exists only in the SAM database of the host computer; it does not have a user object in Active Directory Domain Services. This means that a local account cannot be authenticated by the domain. Consequently, a service that runs in the security context of a local user account does not have access to network resources (except as an anonymous user), and it cannot support Kerberos mutual authentication in which the service is authenticated by its clients. For these reasons, local user accounts are typically inappropriate for directory-enabled services. On the plus side, bugs in the service cannot damage the system. If your service can run under those limitations, it should.

 

 




