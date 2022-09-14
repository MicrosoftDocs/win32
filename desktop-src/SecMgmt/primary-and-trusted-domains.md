---
description: The following terms describe domains that exist on remote systems.
ms.assetid: a6ce5356-682a-46ae-a101-15227c3b8d1e
title: Primary and Trusted Domains
ms.topic: article
ms.date: 05/31/2018
---

# Primary and Trusted Domains

The following terms describe domains that exist on remote systems.

-   [Primary Domain](#primary-domain)
-   [Trusted Domain](#primary-and-trusted-domains)

## Primary Domain

A primary domain is the domain that is responsible for establishing further trust relationships and performing authentication (or for passing an authentication request on to an appropriate trusted domain). The domain controllers in the primary domain handle or pass along authentication requests that originate at the workstation.

When logon occurs, the LSA checks the built-in and account domains for authentication information. If the account being logged on to is not in either of these domains, the logon request is handed off to the system's primary domain.

## Trusted Domain

A trusted domain is a domain that the local system trusts to authenticate users. In other words, if a user or application is authenticated by a trusted domain, this authentication is accepted by all domains that trust the authenticating domain.

Each subordinate domain automatically has a two-way trust relationship with the main domain. By default, this trust is transitive, meaning that if a system trusts Domain A, it also trusts all domains that Domain A trusts. One-way trusts are also supported for operating systems earlier than Windows 2000, which do not support transitive, two-way trusts.

The [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) has an object type, [**TrustedDomain**](the-trusteddomain-object-type.md), that is used to store information about trust relationships, including the name and [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) of the trusted domain, the account in the domain to use for authentication requests, name and SID translation requests, and the names of domain controllers in the trusted domain.

On domain controllers, the LSA creates an instance of a [**TrustedDomain**](the-trusteddomain-object-type.md) object for each domain trusted by the local system.

For example, if a Windows XP workstation trusts a Windows 2000 domain controller that in turn trusts four other systems, the workstation, connected using transitive trust, will have five [**TrustedDomain**](the-trusteddomain-object-type.md) objects on its local system.

 

 
