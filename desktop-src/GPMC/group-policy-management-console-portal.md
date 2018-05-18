---
title: Group Policy Management Console
description: The Group Policy Management Console (GPMC) unifies Group Policy management across an enterprise.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a8e14771-0a8a-4329-bb8d-d6aa0ec6307c'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["GPMC", "GPMC, start page", "Group Policy Management Console, (See GPMC)"]
---

# Group Policy Management Console

## Purpose

The Group Policy Management Console (GPMC) unifies Group Policy management across an enterprise. Before the GPMC, administrators had to use several tools to manage Group Policy. These tools included the Active Directory Users and Computers snap-in, the Active Directory Sites and Services snap-in, the Resultant Set of Policy snap-in, the GPMC Delegation Wizard, and the ACL Editor. The GPMC integrates the existing Group Policy functionality exposed in these tools into a single console, along with the following new capabilities:

-   A user interface that makes it easier to use and manage Group Policy objects (GPOs).
-   Backup, restore, import, and copy Group Policy objects (GPOs).
-   Simplified management of Group Policy-related security
-   Reporting for GPO settings and Resultant Set of Policy (RSoP) data.
-   [Programmatic access](gpmc-interfaces.md) to the preceding GPO operations. Note that it is not possible to programmatically set individual policy settings within a GPO.

## Where applicable

Windows-based applications can use the Group Policy infrastructure to manage Group Policy in Active Directory. Programmatic access is enabled by the GPMC, which consists of a new Microsoft Management Console (MMC) snap-in and a set of programmable interfaces for managing Group Policy. GPMC and its interfaces can manage domains using Active Directory.

## Developer audience

The GPMC includes a set of programmable interfaces designed for use by administrators who write scripts and for use by C/C++ programmers. Familiarity with Active Directory is required. The [sample scripts](group-policy-management-console-scripting-samples-overview.md) provided when you install the GPMC form the basis for a scripting toolkit that Group Policy administrators can use to manage an organization.

## Run-time requirements

The computer on which the GPMC interfaces are used must be running Windows XP with Service Pack 1 (SP1) or later versions of Windows. To run the GPMC interfaces on Windows XP with SP1, you must also install [hotfix 326469](http://go.microsoft.com/fwlink/p/?linkid=118007) and the Microsoft .NET Framework.

The GPMC is available as a free download from the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=11899) for users with a licensed copy of a Windows Server operating system.

## In this section

-   [About the Group Policy Management Console](about-the-group-policy-management-console.md)
-   [Using the Group Policy Management Console](using-the-group-policy-management-console-interfaces.md)
-   [Group Policy Management Console Reference](group-policy-management-console-reference.md)
-   [GPO Operations Supported by the GPMC](gpo-operations-supported-by-the-gpmc.md)

 

 




