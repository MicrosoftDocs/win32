---
description: The Concert feature file of the original product, MNP2000, contains an error in the Concert.txt file.
ms.assetid: 4289bd0c-bdf3-4747-9287-94f737ce4f5c
title: Planning a Small Update Patch
ms.topic: article
ms.date: 05/31/2018
---

# Planning a Small Update Patch

The Concert feature file of the original product, MNP2000, contains an error in the Concert.txt file. Because Windows Installer was used for the installation and setup of the application, minor fixes to the application may be handled by installing a small update patch package. A [small update](small-updates.md) makes changes to one or more application files that are too minor to change the product code. The following example shows you how to create a Windows Installer patch package that can apply the small update and provide a quick fix to the MNP2000 product.

To create the small update first obtain a fully uncompressed image of the MNP2000 product that includes the error in Concert.txt. The image must include MNP2000.msi and all the source files described in [Planning the Installation](planning-the-installation.md). In the following discussion this is called the Target image. The Target image must be fully uncompressed because the patch creation process is unable to generate binary patches for files compressed in cabinets. Put the .msi file and all the source files of the Target image into a folder named Target.

Next, obtain a fully uncompressed image of the MNP2000 product with a Concert.txt file that is fixed. This is called the Upgraded image in the following discussion. Use an installation database editing tool, such as Orca, to update the .msi file. For example, if the size of the corrected Concert.txt is smaller than the original, be sure to enter the new size in the FileSize field of the File table of the upgraded image. Note that because the package has changed you must assign a new package code in the [**Revision Number Summary**](revision-number-summary.md) Property. Put the .msi file and all the source files of the Upgraded image into a folder named Upgraded.

For the purposes of this example, assume that the size of the Concert.txt file changes. This means that FileSize fields in the File tables of the Target and Upgraded database contain different data.

The following [File Table](file-table.md) identifies the record from the Target Image.



| File        | Component\_ | FileName    | FileSize | Version | Language | Attributes | Sequence |
|-------------|-------------|-------------|----------|---------|----------|------------|----------|
| Concert.txt | Concert     | Concert.txt | 1000     |         |          | 0          | 1        |



 

The following File Table identifies the record from the Upgraded Image.



| File        | Component\_ | FileName    | FileSize | Version | Language | Attributes | Sequence |
|-------------|-------------|-------------|----------|---------|----------|------------|----------|
| Concert.txt | Concert     | Concert.txt | 900      |         |          | 0          | 1        |



 

> [!Note]
> The file must have the same key in the [File Tables](file-table.md) of both the target image and the updated image. The string values in the File column of both tables must be identical. Uppercase and lowercase must be identical also.
> 
> Follow the guidelines described in [Creating a Patch Package](creating-a-patch-package.md). Do not author a package with [File Table](file-table.md) keys that differ only by case, because [Msimsp.exe](msimsp-exe.md) and [Patchwiz.dll](patchwiz-dll.md) call Makecab.exe, which is case-insensitive and patch generation fails.

[Continue](creating-a-patch-creation-properties-file.md)

 

 



