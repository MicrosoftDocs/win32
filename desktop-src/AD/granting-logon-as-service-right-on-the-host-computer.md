---
title: Granting Logon as Service Right on the Host Computer
description: When installing a service to run under a domain user account, the account must have the right to logon as a service on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '1b217650-4397-4e28-b53e-8b03f3caf903'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Granting Logon as Service Right on the Host Computer

When installing a service to run under a domain user account, the account must have the right to logon as a service on the local computer. Be aware that this logon right applies only to the local computer and must be granted in the local LSA policy of each host computer. This step is not required if your service runs as LocalSystem, which, by default, is granted this right.

For more information on how to programmatically grant logon as a service right, see the [LSAPrivs sample code](https://www.google.com/#q=LSAPrivs).

 

 




