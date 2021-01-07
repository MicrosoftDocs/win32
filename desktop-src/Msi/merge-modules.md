---
description: Merge modules provide a standard method by which developers deliver shared Windows Installer components and setup logic to their applications.
ms.assetid: '673de3ff-e58c-4153-9c8d-c3baebba5eb1'
title: Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Merge Modules

Merge modules provide a standard method by which developers deliver shared Windows Installer [*components*](c-gly.md) and setup logic to their applications. Merge modules are used to deliver shared code, files, resources, registry entries, and setup logic to applications as a single compound file. Developers authoring new merge modules or using existing merge modules should follow the standard outlined in this section.

A merge module is similar in structure to a simplified Windows Installer [*.msi file*](m-gly.md). However, a merge module cannot be installed alone, it must be merged into an installation package using a merge tool. Developers wanting to use merge modules must obtain one of the freely distributed merge tools, such as Mergemod.dll, or purchase a merge tool from an independent software vendor. Developers can create new merge modules by using many of the same software tools used to create a Windows Installer installation package, such as the database table editor Orca provided with the Windows Installer SDK.

When a merge module is merged into the .msi file of an application, all the information and resources required to install the components delivered by the merge module are incorporated into the application's .msi file. The merge module is then no longer required to install these components and the merge module does not need to be accessible to a user. Because all the information needed to install the components is delivered as a single file, the use of merge modules can eliminate many instances of version conflicts, missing registry entries, and improperly installed files.

For more information about merge modules, see:

-   [About Merge Modules](about-merge-modules.md)
-   [Using Merge Modules](using-merge-modules.md)
-   [Merge Module Reference](merge-module-reference.md)

 

 



