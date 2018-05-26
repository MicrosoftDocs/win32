---
title: Implementing Extension DLLs
description: If you are creating a resource type and want to allow administrators to manage your resource type through Failover Cluster Administrator, use the code from the ClipBookServer and FileShareSample samples from the Windows SDK as a template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd65361f-034f-4b28-8532-ab427fff5dfe
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Administrator Failover Cluster ,extension DLLs,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Extension DLLs

\[Support for the Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

If you are creating a [resource type](resource-types.md) and want to allow administrators to manage your resource type through [Failover Cluster Administrator](cluster-administrator.md), use the code from the ClipBookServer and FileShareSample samples from the Windows SDK as a template.

Change the sample code provided only under the following circumstances:

-   You want to add functionality to the default extension DLL generated for a resource type.
-   You are extending an object other than a resource type.

In both cases, you will be modifying the generated code to add context menus, property sheet pages, and wizard pages to the Failover Cluster Administrator user interface. The following sections describe how to use the Failover Cluster Administrator extension functions to perform these tasks:

-   [Adding Context Menu Items](adding-context-menu-items.md)
-   [Adding Property Sheet Pages](adding-property-sheet-pages.md)
-   [Adding Wizard and Wizard97 Pages](adding-wizard-and-wizard97-pages.md)
-   [Using the Information Interfaces](using-the-information-interfaces.md)

## Implementing and using extension DLLs on 64-bit operating systems

Cluster-aware applications designed and built for 32-bit operating systems will run on a 64-bit operating system, subject to some constraints on any 32-bit cluster administrator extension DLLs that may exist for the application.

Failover Cluster Administrator extension DLLs built for 32-bit operating systems will not work on a 64-bit operating system because they are registered to be loaded in process to the native cluster administrator, which will be a 64-bit application running on a 64-bit operating system.

The following list provides some ways to remedy this situation:

-   Recompile the cluster administrator extension DLL as 64-bit. This will enable the DLL to be loaded in process into the native 64-bit cluster administrator and managed from the native 64-bit cluster administrator.
-   Manage the 32-bit cluster-aware application remotely from a 32-bit client.

 

 




