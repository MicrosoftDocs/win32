---
description: Merge modules provide a standard method for developers to deliver shared Windows Installer components and setup logic to their applications.
ms.assetid: 3eb087b1-0f44-40d8-a950-67d489f09408
title: Using the API to Merge a Merge Module into a Database
ms.topic: article
ms.date: 05/31/2018
---

# Using the API to Merge a Merge Module into a Database

[Merge modules](merge-modules.md) provide a standard method for developers to deliver shared Windows Installer [*components*](c-gly.md) and setup logic to their applications. Merge modules must be merged into an installation package using a merge tool. The best alternative is to obtain a freely distributed merge tool or purchase one of the merging tools available from independent software vendors. For example you can use the functionality provided by [Mergemod.dll](merge-module-automation.md).

Use the following steps in sequence to merge a merge module into a Windows Installer installation database by the API of [Mergemod.dll](merge-module-automation.md).

**To merge a merge module into a Windows Installer installation database**

1.  Open a log file using [**OpenLog**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-openlog). This step is required only if you need to create a log file, or append an existing log file, for the merge process.
2.  Open the installation database, an [.msi file](windows-installer-file-extensions.md), that will receive the merge module using [**OpenDatabase**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-opendatabase). This step is required.
3.  Open the merge module, an [.msm file](windows-installer-file-extensions.md), that is being merged into the database using [**OpenModule**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-openmodule). A module must be opened before it can be merged with an installation database. This step is required.
4.  Merge the module into the installation database by using [**Merge**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-merge) or [**MergeEx**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-mergeex). Note that **Merge** or **MergeEx** can only be called once to merge a particular combination of .msi and .msm files. **MergeEx** is only available when using [Mergemod.dll version 2.0](merge-module-automation.md) or later and only when using the [IMsmMerge2](/windows/desktop/api/Mergemod/nn-mergemod-imsmmerge2) interface. This step is required.
5.  Call [**get\_Errors**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-get_errors) and examine the retrieved collection of errors for merge conflicts or other errors. The retrieval is non-destructive. Multiple instances of the error collection may be retrieved by repeatedly reading calling **get\_Errors**. You will need to resolve any errors as appropriate for your case.
6.  Associate the components of the merge module with any additional features that have been, or will be, merged into the installation database using [**Connect**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-connect). The feature must already exist before calling this method. This step is only required if you have additional features, for more information see [Connecting a Merge Module to Multiple Features](connecting-a-merge-module-to-multiple-features.md)
7.  If necessary, extract source files from the module by doing one or more of the following.

    To extract files from an embedded .cab file and then copy into a specified directory, use [**ExtractFiles**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-extractfiles) or [**ExtractFilesEx**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-extractfilesex). Note that **ExtractFilesEx** requires [Mergemod.dll version 2.0](merge-module-automation.md) or later.

    To extract files from an embedded .cab file and then save in a specified file, use [**ExtractCAB**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-extractcab).

    To extract files from a module and then copy to a source image on disk after the merge, use [**CreateSourceImage**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-createsourceimage). Note that **CreateSourceImage** is only available with [Mergemod.dll version 2.0](merge-module-automation.md) or later.

8.  Close the current open merge module using [**CloseModule**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closemodule). This step is required.
9.  Close the current open installation database using [**CloseDatabase**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closedatabase). This step is required. Closing a database clears all dependency information but does not affect any errors that have not been retrieved.
10. Close the current log file using [**CloseLog**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closelog). This step is required if you have opened a log file.

After the module has been merged into the database using [Mergemod.dll](merge-module-automation.md), the [Media Table](media-table.md) must be updated to describe the desired source image layout. The merge process provided by Mergemod.dll does not update the Media Table because the consumer of the merge module can select various ways to layout the source image.

 

 
