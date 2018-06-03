---
title: Copying and Importing GPOs Across Domains
description: The Group Policy Management Console (GPMC) enables you to transfer Group Policy objects (GPOs) across domains and across forests using import and copy operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4a14a75-50f2-4f42-9c11-fc15856a469c
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Copying and Importing GPOs Across Domains

The Group Policy Management Console (GPMC) enables you to transfer Group Policy objects (GPOs) across domains and across forests using import and copy operations. This can be useful if you maintain separate test and production environments and need to replicate the content from one environment to the other. You can test complex policy deployments in your test environment and then import or copy these settings into your production environment. You can also transfer GPOs from one production environment to another production environment. In addition, the GPMC enables you to modify certain settings as part of the import or copy operation to suit your test or production environment. Specifically, you can modify references to security principals, such as users, groups, and computers, and to Universal Naming Convention (UNC) paths that exist in the GPO. The modification of security principals and UNC paths in the destination GPO is achieved by using a [migration table](using-migration-tables.md) with the import or copy operation.

To facilitate the migration of GPOs across domains, you may need to use the GPMC to modify certain settings to suit your environment during import or copy operations. The following reasons explain why you may need to do this:

-   When you migrate GPOs from test to production environments, users in the production environment may not have access to the paths that are available in the test environment, and vice versa. By using a migration table, the GPMC enables you to modify references to UNC paths in the destination GPO as part of import and copy operations.
-   When you migrate GPOs across domains, some users, groups, and computers may be referenced in the settings of the GPO or in the access control list (ACL) for the GPO. Security principals do not transfer well across domains for several reasons. Domain local groups are not valid in external domains, but other groups are valid if a trust relationship exists between domains. Even with a trust relationship, it may not always be appropriate to use the exact same group in the new domain. If no trust relationship exists, none of the security principals in the source domain will be available in the destination domain. Using a migration table, the GPMC can be used to modify references to the security principals in the destination GPO across the domains when copying and importing GPOs and so enables you to modify the settings in this case.

[Importing GPOs from a Test to a Production Forest](importing-gpos-from-a-test-to-a-production-forest.md) and [Importing GPOs from one Production Forest to Another](importing-gpos-from-one-production-forest-to-another.md) are tasks that are often encountered by administrators. These tasks can be facilitated by using migration tables and import and copy operations.

 

 




