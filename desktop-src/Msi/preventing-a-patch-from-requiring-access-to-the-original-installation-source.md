---
description: It is not possible to eliminate all circumstances under which the application of a patch may require access to the original installation source.
ms.assetid: f7028c55-e4a5-4596-af7a-728c9f4f367e
title: Preventing a Patch from Requiring Access to the Original Installation Source
ms.topic: article
ms.date: 05/31/2018
---

# Preventing a Patch from Requiring Access to the Original Installation Source

It is not possible to eliminate all circumstances under which the application of a patch may require access to the original installation source.

Adhere to following points to minimize the possibility that your patch will require access to the original source:

-   Use whole-file only patches. This eliminates the need to create binary patches for all previously released versions of the file. Note that whole file patches are generally larger in size than binary patches. You can easily set a patch to be a whole file patch by authoring the IncludeWholeFilesOnly property with a value of 1 (one) in the Patch Creation Properties (PCP) file.
-   Ensure that none of your custom actions access the original source location.
-   Ensure that the ResolveSource action is conditionalized so that it only runs when needed, or alternatively is not present at all.
-   Populate the [MsiFileHash Table](msifilehash-table.md) for all unversioned files. The Windows Installer SDK tool, Msifiler.exe, can easily do this for you.
-   Ensure that all files have the correct version and language information. The Windows Installer SDK tool, Msifiler.exe, can easily do this for you.

## Source Requirements When Patching

Access to the original installation sources may be required to apply the patch in the following cases:

-   The patch applies to a feature that is currently run from source. In this case, the feature is transitioned from the run-from-source state to the local state.
-   The patch applies to a component that has a missing or corrupted file.
-   The patch applies to a file in a component that also contains unversioned files with no MsiFileHash entries. A populated [MsiFileHash Table](msifilehash-table.md) is required to prevent unnecessary recopying of unversioned files from the source location.
-   The patch was applied with a REINSTALLMODE of amus or emus. This option is dangerous in that it performs file copy operations regardless of file version. This can lead to down-reving of files and almost always requires the source. The recommended REINSTALLMODE value is omus.
-   The cached package for the product is missing. The cached package is needed for application of a patch. The cached package is stored in the %windir%\\Installer folder.
-   The package is authored to make a call to the [ResolveSource Action](resolvesource-action.md). This action should generally be avoided or conditionalized appropriately, because its execution always results in an access to the source.
-   The package has a custom action that attempts to access the source in some manner. The most common example is a type 23 concurrent installation custom action.
    > [!Note]  
    > Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see [Concurrent Installations](concurrent-installations.md).

     

-   The patch package consists of binary patches that do not apply to the current version of the file on the computer.

Consider the following example where Windows Installer requires access to the original source when applying a patch:

1.  Install RTM version of the product Example.
2.  Apply patch Qfe1.msp to the computer. This patches version 1.0 of Example.dll to version 1.1.
3.  A new patch, Qfe2.msp is provided, which updates Example.dll to version 1.2 and obsoletes Qfe1.msp. However, the patch was only created to target version 1.0 of Example.dll because it was generated using the RTM version of the product. Example.dll version 1.2 includes the fix contained in Example.dll version 1.1, but the .msp file was generated between the RTM and QFE2 images. So, when Qfe2.msp is applied to the computer, Windows Installer needs to access the original source. The binary patch for Example.dll cannot apply to version 1.1; it can only apply to version 1.0. This results in the Installer recopying version 1.0 of Example.dll from the original source location so that the patch can be applied successfully.

## Source Requirements When Removing a Patch

Access to the original installation sources may be required to remove a patch if the Windows Installer has not stored baseline information about the patch. Beginning with Windows Installer 3.0, the installer selectively saves baseline information about files when they are updated. For more information about the baseline cache, see [Reducing Patch Size](reducing-patch-size.md) .

 

 



