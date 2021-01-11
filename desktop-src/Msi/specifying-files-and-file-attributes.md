---
description: The installation and removal of each file is determined by the Windows Installer Component that controls the file.
ms.assetid: 6f84bf57-2c68-4f37-b9cd-eee3a657e7cd
title: Specifying Files and File Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Files and File Attributes

The installation and removal of each file is determined by the [Windows Installer Component](windows-installer-components.md) that controls the file. Once the grouping of resources into components has been specified, file attribute information can be added to the installation database. In this section, you add file information to the installation database for the Notepad sample. See the [File Tables Group](file-tables-group.md).

The files in the Notepad sample are uncompressed. See [Compressed and Uncompressed Sources](compressed-and-uncompressed-sources.md) for information on how to add cabinet files to packages. This sample does not contain file versioning information. For more information about file versioning, see [File Versioning Rules](file-versioning-rules.md) and [Default File Versioning](default-file-versioning.md).

Use your database editor to open MNP2000.msi and enter the following data into the empty File table.

[File Table](file-table.md)



| File         | Component\_ | FileName     | FileSize | Version | Language | Attributes | Sequence |
|--------------|-------------|--------------|----------|---------|----------|------------|----------|
| Baseball.txt | Baseball    | Baseball.txt | 1000     |         |          | 0          | 1        |
| Concert.txt  | Concert     | Concert.txt  | 1000     |         |          | 0          | 1        |
| Dance.txt    | Dance       | Dance.txt    | 1000     |         |          | 0          | 1        |
| Football.txt | Football    | Football.txt | 1000     |         |          | 0          | 1        |
| Help.txt     | Help        | Help.txt     | 1000     |         |          | 0          | 1        |
| January.txt  | January     | January.txt  | 1000     |         |          | 0          | 1        |
| NewYears.txt | NewYears    | NewYears.txt | 1000     |         |          | 0          | 1        |
| Redpark.exe  | Notepad     | Redpark.exe  | 45328    |         |          | 0          | 1        |
| Readme.txt   | Notepad     | Readme.txt   | 1000     |         |          | 0          | 1        |



 

[Continue](specifying-source-media.md)

 

 



