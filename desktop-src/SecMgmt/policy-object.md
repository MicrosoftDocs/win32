---
description: The Policy object is used to control access to the Local Security Authority (LSA) database and contains information that applies to the entire system or establishes defaults for the system.
ms.assetid: 4253c7fb-85f5-441d-90bf-492e802ad0f8
title: Policy Object
ms.topic: article
ms.date: 05/31/2018
---

# Policy Object

The **Policy** object is used to control access to the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) database and contains information that applies to the entire system or establishes defaults for the system. Each system has only one **Policy** object. This **Policy** object is created by the LSA when the system starts up, and applications cannot create or destroy it.

The information stored in a **Policy** object includes:

-   System default memory quota. Unless otherwise specified, each user logging on to the system will be assigned this memory quota. Special memory quotas can be assigned to individuals or members of groups or local groups through an [**Account**](account-object.md) object.
-   System-wide security auditing requirements.
-   The name and SID of the account domain of this system.
-   Information about the primary domain of this system. This information includes the name and SID of the primary domain, the name of the account within the primary domain that is to be used for authentication requests, name and SID translations, and obtaining the names of domain controllers within the domain. These names may be out of date and should be taken only as a hint. The order of this list is assumed to be significant and will be maintained. This allows, for example, the first name in the list to represent the last-known primary domain controller.
-   Information about whether the LSA holds the master copy of the policy information or a replica. Only part of the policy information is replicated; the remainder is established on a per-system basis.

The **AccountDomain** and **PrimaryDomain** fields of the **Policy** object are used for different purposes depending upon the type of system and trust relationships:

-   On a system that does not have a primary domain, the **AccountDomain** field contains the name and SID of the system's local account domain, which is the same as the computer name. The **PrimaryDomain** field contains the name of the workgroup this machine is a member of. [**TrustedDomain**](trusteddomain-object.md) objects are ignored with one exception—there cannot be a **TrustedDomain** object with the same name as the workgroup because it will appear as though it is the machine's primary domain.
-   On a system that has a primary domain, the **AccountDomain** field identifies the name and SID of the local account domain, as before. However, the **PrimaryDomain** field contains the name and SID of the primary domain for the system. Additionally, there should be a [**TrustedDomain**](trusteddomain-object.md) object with the name and SID identified in the **PrimaryDomain** field. This **TrustedDomain** object contains the account and server information necessary to establish a secure channel to a domain controller in the primary domain. Any other **TrustedDomain** objects are ignored.
-   On domain controllers, the **AccountDomain** field identifies the local account domain for the system; however, the account name is user assigned rather than being a well-known name. Since the primary domain is the same as the account domain, the **PrimaryDomain** field must contain the same value as the **AccountDomain** field. Furthermore, all [**TrustedDomain**](trusteddomain-object.md) objects are expected to be valid and represent trust relationships with other domains. If the system does not trust any other domains, there should not be any **TrustedDomain** objects.

 

 
