---
title: Granting Access Rights to the Service Logon Account
description: A primary consideration of installing a service instance is to ensure that the installed service can access the necessary resources.
ms.assetid: 5b756318-f621-4fce-af2b-71ccccbb4e3c
ms.tgt_platform: multiple
keywords:
- Granting Access Rights to the Service Logon Account AD
ms.topic: article
ms.date: 05/31/2018
---

# Granting Access Rights to the Service Logon Account

A primary consideration of installing a service instance is to ensure that the installed service can access the necessary resources. To do this, set ACEs in the security descriptors of objects that the service must access. An ACE can grant or deny access rights to a specified security principal, such as the service user account, or the computer account for a LocalSystem service, or a group to which the service's account belongs. For more information about ACEs, security descriptors, and access control, see [Controlling Access to objects in Active Directory Domain Services](controlling-access-to-objects-in-active-directory-domain-services.md) and [Access Control](/windows/desktop/SecAuthZ/access-control).

For more information and a code example that can be used to set an ACE that enables the service to modify its service connection point, see [Enabling Service Account to Access SCP Properties](enabling-service-account-to-access-scp-properties.md).

In some cases, you must add your service user account as a member of one or more security groups. For example, if you create an administrators group for your service, you might make the service a member of the group. You can then grant access rights to the group rather than granting them explicitly to the service account. For more information about security groups, see [Managing Groups](managing-groups.md).

 

 