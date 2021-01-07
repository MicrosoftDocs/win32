---
description: A merge module can be applied to an .msi file to add directories to the installation but it cannot replace or remove any existing directories.
ms.assetid: 5b808aa2-b2b2-4703-bd57-0b5e1e73b306
title: Authoring Merge Module Directory Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module Directory Tables

A merge module can be applied to an .msi file to add directories to the installation but it cannot replace or remove any existing directories. The [Directory table](directory-table.md) specifies the layout of the directories the merge module provides to the target installation. A Directory table is required in every merge module.

Use the following guidelines when authoring the Directory Table in a merge module. For more information, see [Directory Table](directory-table.md) and [Using The Directory Table](using-the-directory-table.md).

-   The directory structure added by the merge module must have a single root directory. The root must be named TARGETDIR. The user may change the value of TARGETDIR during the merge to specify where to attach the module's directory structure onto the target's directory tree.
-   Merge module tables other than the Directory table must not directly reference directory locations to TARGETDIR. The location of such a reference changes if the value of TARGETDIR is changed by the user.
-   The tables in the merge module must reference the location of a child directory of TARGETDIR, or another directory in the merge module's tree. Do the following to specify TARGETDIR as the parent of a directory in the merge module. Enter the directory into the Directory column and enter TARGETDIR into the Directory\_Parent column. Use the "." notation in the DefaultDir column to indicate that this directory is located in TARGETDIR without a subdirectory. For more information, see [Using the Directory Table](using-the-directory-table.md).
-   The names of directories added by the merge module must use the naming conventions described in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md). This includes directories predefined by properties such as the [**SystemFolder**](systemfolder.md) property and [**ProgramFilesFolder**](programfilesfolder.md) property.
-   Append a [*GUID*](g-gly.md) to every entry in the Directory table (except TARGETDIR.) This includes Directory table entries that specify Windows Installer [**SystemFolder**](systemfolder.md) properties, for example, SystemFolder.00000000\_0000\_0000\_0000\_000000000000. The library Mergemod.dll adds custom actions to set the **SystemFolder** property.
-   When a predefined directory is included in a merge module, the merge tool automatically adds a [Custom Action Type 51](custom-action-type-51.md) to the target database. The merge module author must ensure that a [CustomAction table](customaction-table.md) is also included. The CustomAction table may be empty, but this table is required to exist in the target database and ensures that the modified predefined directories are written to the correct locations. For example, when a system directory is included in a merge module, the merge module author must ensure that a Custom Action table exists.

    Note that the matching algorithm for the generation of these type 51 custom actions only checks that the directory name begins with one of the predefined [**SystemFolder**](systemfolder.md) properties. It does not verify that the directory name exactly equals the directory property. Any directory beginning with one of these standard folder names gets a type 51 custom action, even if the rest of the name is not a GUID. Authors need to take care that this does not generate false positive matches, and unintended custom action generation, on derivative primary keys that begin with one of the **SystemFolder** properties.

The following is an example of a Directory table in a merge module and the expected resolved directories.



| Directory                                              | Directory\_Parent                                | DefaultDir  |
|--------------------------------------------------------|--------------------------------------------------|-------------|
| TARGETDIR                                              |                                                  | SourceDir   |
| Dir00.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17        | TARGETDIR                                        | .:MMM\_Prog |
| SystemFolder.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17 | TARGETDIR                                        | MMM\_Sys    |
| Dir02.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17        | Dir00.BC82E350\_ C7FC\_11d1\_ A848\_006097ABDE17 | MFC\_OCX    |



 

A merge module with the above Directory table is expected to result in the following directory structure.



| Directory                                              | Target                                     | Source                                               |
|--------------------------------------------------------|--------------------------------------------|------------------------------------------------------|
| Dir00.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17        | \[Merge Module's Install Point\]\\         | \[Merge Module's Source Point\]\\MMM\_Prog           |
| SystemFolder.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17 | \[SystemFolder\]\\                         | \[Merge Module's Source Point\]\\MMM\_Sys            |
| Dir02.BC82E350\_ C7FC\_11d1\_ A848-006097ABDE17        | \[Merge Module's Install Point\]\\MFC\_OCX | \[Merge Module's Source Point\]\\MMM\_Prog\\MFC\_OCX |



 

 

 



