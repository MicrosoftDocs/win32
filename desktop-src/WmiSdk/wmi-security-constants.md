---
description: WMI checks access rights for applications and scripts.
ms.assetid: f6808f50-a1fd-434f-8a42-efa3afbe7871
ms.tgt_platform: multiple
title: WMI Security Constants
ms.topic: article
ms.date: 05/31/2018
---

# WMI Security Constants

WMI checks access rights for applications and scripts for objects such as WMI namespaces, printer, services, DCOM applications, files, shares, and other securable objects. Access to theses securable objects is controlled by access control entries (ACE). Each ACE contains lists that designate which groups or users have access. For more information about security and access control lists (ACLs, DACLs, or SACLs), see [Access Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists) and [Security Descriptors](/windows/desktop/SecAuthZ/security-descriptors).

Many provider methods in WMI that affect securable objects require the administrator to enable certain privileges. Which version of the privilege you use depends on the programming language, as shown in [**Privilege Constants**](privilege-constants.md).

The security constants are defined in the following topics:

-   [**Event Security Constants**](event-security-constants.md)
-   [**File and Directory Access Rights Constants**](file-and-directory-access-rights-constants.md)
-   [**Namespace Access Rights Constants**](namespace-access-rights-constants.md)
-   [**Namespace ACE Flag Constants**](namespace-ace-flag-constants.md)
-   [**Namespace ACE Type Constants**](namespace-ace-type-constants.md)
-   [**Privilege Constants**](privilege-constants.md)

 

 
