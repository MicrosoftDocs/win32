---
title: Importing GPOs from a Test to a Production Forest
description: Importing GPOs from a Test to a Production Forest
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 04f2bce6-e279-4b80-bc15-2a988abee486
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Importing GPOs from a Test to a Production Forest

In this scenario, separate forests exist for the test and production environments. An administrator wants to import the settings in Group Policy object (GPO) X from domain B in the test forest to domain E in the production forest. GPO X contains security settings, such as User Rights Assignment, that reference security principals in the test forest. In this scenario, assume no trust exists between the forests. This means that after GPO X is imported to the production forest, the original references to security principals in the test forest are no longer valid. Furthermore, the Universal Naming Convention (UNC) paths in the test forest will not be accessible to users in the production forest. It is therefore necessary to migrate all the references to security principals and to UNC paths in the GPO when you import it to the production forest. This can be achieved by using an import operation and a [migration table](using-migration-tables.md).

The following figure illustrates the scenario. Security principals, such as users, groups, or computers, are represented in the figure. For example, in the A\\red security principal, the domain is A, and the relative name is red.

![test forest diagram compared with production forest diagram](images/test-prod.png)

To transfer the settings in GPO X from domain B in the test forest to a GPO in domain E in the production forest, the administrator must use an import operation and a [migration table](using-migration-tables.md) because trust does not exist between domain B and domain E. If trust did exist, it would also be possible to do this with a copy operation. When you use a migration table together with the import or copy operation, the Group Policy Management Console (GPMC) enables the administrator to update the settings in the destination GPO to the new values that are appropriate for the destination domain.

An administrator can also import a GPO from one production environment to another production environment. For more information, see [Importing GPOs from one Production Forest to Another](importing-gpos-from-one-production-forest-to-another.md) and [Copying and Importing GPOs Across Domains](copying-and-importing-gpos-across-domains.md).

For detailed steps to perform these tasks, see the sample scripts described in [Group Policy Management Console Scripting Samples](group-policy-management-console-scripting-samples.md). After you install the GPMC, you can find the scripts in the %programfiles%\\Gpmc\\Scripts folder.

 

 




