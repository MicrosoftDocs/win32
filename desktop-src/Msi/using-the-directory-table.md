---
description: The Directory table specifies the layout of an installation.
ms.assetid: 3f2e1cc2-6b36-4615-86e6-e78485edd2f7
title: Using the Directory Table
ms.topic: article
ms.date: 05/31/2018
---

# Using the Directory Table

The [Directory table](directory-table.md) specifies the layout of an installation. When the directories are resolved during the [CostFinalize action](costfinalize-action.md), the keys in the Directory table become [properties](properties.md) set to directory paths. Note that the installer sets a number of standard [properties](properties.md) to system folder paths. See the [Property Reference](property-reference.md) for a list of the properties that are set to system folders.

The best way to specify the target location for a directory is by authoring the [Directory table](directory-table.md) in your installation package to provide the correct location as discussed in this section. If it is necessary to change the directory location at the time of the installation see also the section: [Changing the Target Location for a Directory](changing-the-target-location-for-a-directory.md)

The following is an example of a Directory table.



| Directory     | Directory\_Parent | DefaultDir |
|---------------|-------------------|------------|
| TARGETDIR     |                   | SourceDir  |
| EXEDIR        | TARGETDIR         | App        |
| DLLDIR        | EXEDIR            | Bin        |
| DesktopFolder | TARGETDIR         | Desktop    |



 

Each row of the Directory table indicates a directory both at the source and the target. For example, assume the installation package resides at \\\\applications\\source\\. Because the Directory\_Parent field of the first row is Null, this record indicates the root directories for both the source and the target. For the source, the value of this directory is given by the DefaultDir field. The [**SourceDir**](sourcedir.md) property defaults to the location of the installation package. Thus, unless the **SourceDir** property is overridden, the root source directory is \\\\applications\\source\\.

The Directory field of the first record indicates the location of the root target directory. In this case, the value of the [**TARGETDIR**](targetdir.md) property indicates this directory. Typically, the value of the **TARGETDIR** property is set at the command line or through a user interface. In this case, assume the **TARGETDIR** property is set to C:\\Program Files\\Target\\.

For the second record, the Directory\_Parent field is not Null. Therefore, this record indicates a non-root directory for both the source and the target. For a non-root source directory, the source directory indicated by the record described in the Directory\_Parent field is the parent directory. For the second record, the Directory\_Parent field is TARGETDIR. As shown earlier, the source directory indicated by the TARGETDIR record resolved to \\\\applications\\source\\. Thus, the source directory indicated by the second record is \\\\applications\\source\\App\\.

A similar process works for the target directory. The value of the parent directory for the target directory described in the second record is the target directory resolved by the Directory\_Parent field. Again, the Directory\_Parent field contains the value TARGETDIR. This indicates the first record that resolves to a target directory of C:\\Program Files\\Target\\. The Directory field contains an author-defined property called EXEDIR. If this property is set, then its value gives the full path of the directory. Thus, if this property is set to C:\\Data\\Common\\, the value of the target directory indicated by the second record is C:\\Data\\Common\\. If it is not set, the target directory takes the name given by the DefaultDir field. In this case, the target directory is C:\\Program Files\\Target\\App\\.

The same process works for the third record. If EXEDIR and DLLDIR are not set, the target directory is C:\\Program Files\\Target\\App\\Bin, and the source directory is \\\\applications\\source\\App\\Bin\\.

The fourth record uses the [**DesktopFolder**](desktopfolder.md) property. If the location of the user's desktop is C:\\Winnt\\Profiles\\User\\Desktop\\, the target directory resolves to C:\\Winnt\\Profiles\\User\\Desktop\\. The source directory resolves to \\\\applications\\source\\Desktop\\.

There are two additional syntax features that can be used in the DefaultDir column of the Directory table. For a non-root source directory, a period (.) entered in the DefaultDir column indicates that the directory should be located in its parent directory without a subdirectory. To specify different source and target directory paths, separate the target and source paths in the DefaultDir column with a colon as follows: \[targetpath\]:\[sourcepath\]. These features can be used together to add levels to either the source or target paths for a single directory. See the following example of a Directory table.



| Directory   | Directory\_Parent | DefaultDir |
|-------------|-------------------|------------|
| TARGETDIR   |                   | SourceDir  |
| MyAppDir    | TARGETDIR         | MyApp      |
| BinDir      | MyAppDir          | Bin        |
| Binx86Dir   | BinDir            | .:x86      |
| BinAlphaDir | BinDir            | .:Alpha    |



 

The source and target paths resolve for the MyAppDir, BinDir, Binx86Dir, and BinAlphaDir rows as follows.



| Record       | Target paths            | Source paths                   |
|--------------|-------------------------|--------------------------------|
| MyAppDir:    | \[TARGETDIR\]MyApp      | \[SourceDir\]MyApp             |
| BinDir:      | \[TARGETDIR\]MyApp\\Bin | \[SourceDir\]MyApp\\Bin        |
| Binx86Dir:   | \[TARGETDIR\]MyApp\\Bin | \[SourceDir\]MyApp\\Bin\\x86   |
| BinAlphaDir: | \[TARGETDIR\]MyApp\\Bin | \[SourceDir\]MyApp\\Bin\\Alpha |



 

> [!Note]  
> The Alpha platform is not supported by the Windows Installer.

 

 

 



