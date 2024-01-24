---
description: Merge Modules provide a standard method for you to deliver shared Windows Installer components, and setup logic to applications.
ms.assetid: 63ced106-12e3-4483-8bfe-22c54fe7a204
title: Using Automation to Merge a Merge Module into a Database
ms.topic: article
ms.date: 05/31/2018
---

# Using Automation to Merge a Merge Module into a Database

[Merge Modules](merge-modules.md) provide a standard method for you to deliver shared Windows Installer [*components*](c-gly.md), and setup logic to applications.

Merge modules must be merged into an installation package by using a merge tool. The best practice is to obtain a freely distributed merge tool, or purchase one of the merge tools that are available from independent software vendors, for example, you can use [Mergemod.dll](merge-module-automation.md).

The following procedure shows you how to merge a merge module into a Windows Installer database by using [Merge Module Automation](merge-module-automation.md).

**To merge a module into a database**

1.  Open a log file by using the [**OpenLog**](merge-openlog.md) method.

    This step is required only if you need to create a log file, or append an existing log file for the merge process.

2.  Open the [.msi](windows-installer-file-extensions.md) installation database by using the [**OpenDatabase**](merge-opendatabase.md) method of the [**Merge Object**](merge-object.md).

    This step is required.

    The database that you open is the one that you want to receive the merge module.

3.  Open the [.msm](windows-installer-file-extensions.md) merge module by using the [**OpenModule**](merge-openmodule.md) method.

    This step is required.

    This is the merge module that is being merged into the database. A module must be opened before it can be merged with an installation database.

4.  Merge the module into the installation database by calling the [**Merge**](merge-object.md) method or [**MergeEx**](merge-mergeex.md) method.

    This step is required.

    The [**Merge**](merge-object.md) method or [**MergeEx**](merge-mergeex.md) method can only be called one time to merge a specific combination of [.msi](windows-installer-file-extensions.md) and .msm files.

    > [!Note]  
    > The [**MergeEx**](merge-mergeex.md) method is only available in [Mergemod.dll version 2.0](merge-module-automation.md) or later, and only when using the [**IMsmMerge2**](/windows/desktop/api/Mergemod/nn-mergemod-imsmmerge2) interface.

     

5.  Retrieve the [**Errors**](merge-errors.md) property and examine the collection of [**Error**](error-object.md) objects it returns for merge conflicts or other errors.

    You must resolve any errors.

    The retrieval is nondestructive, and multiple instances of the error collection can be retrieved by repeatedly reading the [**Errors**](merge-errors.md) property.

6.  Associate the components of the merge module with the features by using the [**Connect**](merge-connect.md) method.

    This step is only required if you have existing features and you want to add features to merge into the installation database.

    A feature must exist before you call this method. For more information, see [Connecting a Merge Module to Multiple Features](connecting-a-merge-module-to-multiple-features.md).

7.  If necessary, extract source files from the module by doing one or more of the following:
    -   Use [**ExtractFiles**](merge-extractfiles.md) or [**ExtractFilesEx**](merge-extractfilesex.md) to extract files from an embedded .cab file and then copy into a specified directory.
        > [!Note]  
        > [**ExtractFilesEx**](merge-extractfilesex.md) requires [Mergemod.dll version 2.0](merge-module-automation.md) or later.

         

    -   Use [**ExtractCAB**](merge-extractcab.md) to extract files from an embedded .cab file, and then save in a specified file.
    -   Use [**CreateSourceImage**](merge-createsourceimage.md) to extract files from a module, and then after the merge, copy to a source image on disk.
        > [!Note]  
        > [**CreateSourceImage**](merge-createsourceimage.md) is only available in [Mergemod.dll version 2.0](merge-module-automation.md) or later.

         
8.  Close the current open merge module by using the [**CloseModule**](merge-closemodule.md) method.

    This step is required.

9.  Close the open installation database by using the [**CloseDatabase**](merge-closedatabase.md) method.

    This step is required.

    Closing a database clears all dependency information, but does not affect any errors that are not retrieved.

10. Close the current log file by using the [**CloseLog**](merge-closelog.md) method.

    This step is required if you have an open log file.

After the module has been merged into the database using [Mergemod.dll](merge-module-automation.md), the [Media Table](media-table.md) must be updated to describe the desired source image layout. The merge process provided by Mergemod.dll does not update the Media Table because the consumer of the merge module can select various ways to layout the source image.

## Related topics

<dl> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



