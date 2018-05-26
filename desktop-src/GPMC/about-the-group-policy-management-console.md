---
title: About the Group Policy Management Console
description: Integrates the Group Policy functionality provided by Active Directory Users and Computers, Active Directory Sites and Services, Resultant Set of Policy, ACL Editor, and Delegation Wizard into a single console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0f53731-dbf9-406f-830f-21b77e5485b2
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- Group Policy Management Console, about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# About the Group Policy Management Console

The Group Policy Management Console (GPMC) integrates the Group Policy functionality provided by the following tools into a single console:

-   Active Directory Users and Computers
-   Active Directory Sites and Services
-   Resultant Set of Policy
-   ACL Editor
-   GPMC Delegation Wizard

Administrators can perform core Group Policy tasks by using the GPMC instead of these other tools. The GPMC provides a comprehensive set of COM interfaces that can be used to programmatically access many of the operations supported by the console.

The GPMC does not replace the Active Directory Users and Computers snap-in and the Active Directory Sites and Services snap-in. The GPMC is intended for Group Policy administration, whereas the Active Directory snap-ins are intended for directory administration tasks such as creating user, computer, and group objects.

The GPMC provides a unified view of Group Policy objects (GPOs), organizational units (OUs), domains, and sites across an enterprise. To edit policy settings within an individual GPO, the GPMC provides direct access to the original Group Policy snap-in. To clarify this relationship, the existing snap-in has been renamed the Group Policy Object Editor snap-in.

For more information, see the following topics:

-   [GPMC Features and Functionality](gpmc-features-and-functionality.md)
-   [GPO Operations Supported by the GPMC](gpo-operations-supported-by-the-gpmc.md)
-   [System Requirements for the Group Policy Management Console](system-requirements-for-the-group-policy-management-console.md)
-   [Group Policy Management Console Scripting Samples Overview](group-policy-management-console-scripting-samples-overview.md)

 

 




