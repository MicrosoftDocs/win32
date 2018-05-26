---
title: Using Migration Tables
description: Migration tables are files that are created by an administrator.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2c3632e0-8d24-4965-8529-85b6efb6c651
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Migration Tables

*Migration tables* are files that are created by an administrator. They are used to implement the advanced capabilities of Group Policy object (GPO) import and copy operations. A migration table can contain information about references to security principals, to Universal Naming Convention (UNC) paths, or to both. By using a migration table, an administrator can modify references to security principals and to UNC paths during import and copy operations.

A sample migration table template is provided in the Program Files\\GPMC\\Scripts folder on computers on which the Group Policy Management Console (GPMC) is installed. For more information about the syntax that is used by migration tables, see this sample migration table. An administrator can create a simple migration table by saving a copy of the sample migration table and then modifying the copy as needed. The GPMC also provides interfaces so you can automate the creation and editing of migration tables.

You can load an existing migration table at a specified path by using the [**IGPM::GetMigrationTable**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpm-getmigrationtable?branch=master) method, or you can create an empty migration table by using the [**IGPM::CreateMigrationTable**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpm-createmigrationtable?branch=master) method. The [**IGPMMigrationTable**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmmigrationtable?branch=master) interface enables you to manage a migration table. You can use the [**IGPMMigrationTable::Add**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmmigrationtable-add?branch=master) method to extract the security principals and the UNC paths from a live or backed-up GPO. Then, you can use them to automatically populate the source entries in a migration table. To specify the migration table to use during an import or copy operation, specify the relevant **IGPMMigrationTable** interface as a parameter of the [**IGPMGPO::Import**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmgpo-import?branch=master) or [**IGPMGPO::CopyTo**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmgpo-copyto?branch=master) method.

You can use the sample CreateMigrationTable.wsf file in the [Group Policy Management Console Scripting Samples](group-policy-management-console-scripting-samples.md) to create a migration table by automatically populating references to the security principals and to the UNC paths. You automatically populate the references from one or more GPOs or from backed-up GPOs.

 

 




