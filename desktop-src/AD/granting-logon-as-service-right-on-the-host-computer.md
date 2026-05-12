---
title: Granting Logon as Service Right on the Host Computer
description: When installing a service to run under a domain user account, the account must have the right to logon as a service on the local computer.
ms.assetid: 1b217650-4397-4e28-b53e-8b03f3caf903
ms.tgt_platform: multiple
ms.topic: concept-article
ms.date: 02/13/2024
---

# Granting Logon as Service Right on the Host Computer

When installing a service to run under a domain user account, the account must have the right to logon as a service on the local computer. Be aware that this logon right applies only to the local computer and must be granted in the local LSA policy of each host computer. This step is not required if your service runs as LocalSystem, which is granted this right by default.

For more information on how to programmatically grant logon as a service right, see the [LSAPrivs sample code](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/security/lsapolicy/lsaprivs).
