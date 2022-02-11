---
title: Local Security Policy
description: The local security policy of a system is a set of information about the security of a local computer.
ms.assetid: 9cef073f-a38f-4808-8dc9-3fabc3413eb2
ms.topic: article
ms.date: 01/25/2022
ms.custom: seo-windows-dev
---

# Local security policy

The local security policy of a system is a set of information about the security of a local computer.

The local security policy information includes the following:

* The domains trusted to authenticate logon attempts.
* Which user accounts may access the system and how. For example, interactively, through a network, or as a service.
* The rights and [*privileges*](/windows/desktop/SecGloss/p-gly) assigned to accounts.
* The security auditing policy.

The [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) stores the local policy information in a set of [LSA Policy Objects](lsa-policy-objects.md).
