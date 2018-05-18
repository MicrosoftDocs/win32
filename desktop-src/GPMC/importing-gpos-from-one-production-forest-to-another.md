---
title: Importing GPOs from one Production Forest to Another
description: Importing GPOs from one Production Forest to Another
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '79e8121b-0a5c-4638-a36c-8261a730ce87'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
---

# Importing GPOs from one Production Forest to Another

In this scenario, an administrator wants to copy Group Policy object (GPO) X from production domain B to another production domain C. Trust must exist between the source and target domains. The domains can be in the same production forest. Or, the domains can be in different forests if a trust exists across the domains.

The following figure illustrates this scenario. Security principals, such as users, groups, or computers, are represented in the figure. For example, for the B\\red security principal, the domain is B, and the relative name is red. In this figure A, B, and C are all shown as production domains in the same forest. These domains could also be in separate forests, provided a trust relationship exists across the domains.

There are two techniques by which an administrator can transfer GPO X from production domain B to production domain C. The first technique does not use a [migration table](using-migration-tables.md) and the transferred GPO retains all the references to security principals defined in domain B and applies them in domain C unchanged. The technique way uses a migration table and can change some or all of the references to security principals or to UNC paths during an import or copy operation. (For detailed steps to perform these tasks, see the sample scripts described in [Group Policy Management Console Scripting Samples](group-policy-management-console-scripting-samples.md). After you install the GPMC, you can find the scripts in the %programfiles%\\Gpmc\\Scripts folder.)

The figure illustrates the effect of using a migration table when you copy a GPO from domain B to domain C to update the references to security principals that are defined in domain B. In the destination GPO, these references now point to the security principals in domain C. However, the references to security principals in domain A remain unchanged.

![domain b and domain c in a forest](images/prod-prod.png)

An administrator can also import a GPO from a test environment to a production environment. For more information, see [Importing GPOs from Test to Production Forests](importing-gpos-from-a-test-to-a-production-forest.md) and [Copying and Importing GPOs Across Domains](copying-and-importing-gpos-across-domains.md).

 

 




