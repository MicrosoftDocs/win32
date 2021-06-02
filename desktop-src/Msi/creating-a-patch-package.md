---
description: Developers create a patch package by generating a patch creation file and using Msimsp.exe to call the UiCreatePatchPackageEx function in Patchwiz.dll.
ms.assetid: 8a163653-6ba1-46ea-9832-f998749d29ae
title: Creating a Patch Package
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Patch Package

Developers create a patch package by generating a patch creation file and using [Msimsp.exe](msimsp-exe.md) to call the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function in [Patchwiz.dll](patchwiz-dll.md). Msimsp.exe and Patchwiz.dll are provided in the Windows Installer SDK. For more information, see [A Small Update Patching Example](a-small-update-patching-example.md).

Because the application of a patch to a Windows Installer package results in the installation of the original sources using a new .msi file, the new .msi file must remain compatible with the layout of the original source.

When you author a patch package you must use an uncompressed setup image to create a patch, for example, an administrative image or an uncompressed setup image from a CD-ROM. You must also adhere to the following restrictions:

-   Do not move files from one folder to another.
-   Do not move files from one cabinet to another.
-   Do not change the order of files in a cabinet.
-   Do not change the sequence number of existing files. The sequence number is the value specified in the Sequence column of the [File Table](file-table.md).
-   Any new files that are added by the patch must be placed at the end of the existing file sequence. The sequence number of any new file in the upgraded image must be greater than the largest sequence number of existing files in the target image.
-   Do not change the primary keys in the [File Table](file-table.md) between the original and new .msi file versions.
    > [!Note]  
    > The file must have the same key in the [File Table](file-table.md) of both the target image and the updated image. The string values in the File column of both tables must be identical, including the case.

     

-   Do not author a package with [File Table](file-table.md) keys that differ only in case, for example, avoid the following table example.

    

    | File       | Component\_ | FileName   |
    |------------|-------------|------------|
    | readme.txt | Comp1       | readme.txt |
    | ReadMe.txt | Comp2       | readme.txt |

    

     

    The Windows Installer can allow the previous table example when Comp1 and Comp2 are installed on different directories, but then you cannot use [Msimsp.exe](msimsp-exe.md) or [Patchwiz.dll](patchwiz-dll.md) to generate a patch for the package. Msimsp.exe and Patchwiz.dll call Makecab.exe, which is case-insensitive and fails.

    When using merge modules in the setup, ensure that file sequence numbers and layout adhere to the above guidelines.

 

 



