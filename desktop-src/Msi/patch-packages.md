---
description: A Windows Installer patch (.msp file) is a file used to deliver updates to Windows Installer applications.
ms.assetid: f59736d7-0b5a-466c-ab60-f210ccccb07f
title: Patch Packages
ms.topic: article
ms.date: 05/31/2018
---

# Patch Packages

A Windows Installer patch (.msp file) is a file used to deliver updates to Windows Installer applications. The patch is a self-contained package that contains all the information required to update the application. A patch package (.msp file) can be much smaller than the Windows Installer package (.msi file) for the entire updated application. For more information about delivering smaller updates to applications, see [Reducing Patch Size](reducing-patch-size.md).

A patch package contains the actual updates to the application and describes which versions of the application can receive the patch. Patches contain at minimum two database transforms. One transform updates the information in the installation database of the application. The other transform adds information that the installer uses for patching files. The installer uses the information provided by the transforms to apply patch files that are stored in the cabinet file stream of the patch package. A patch package does not have a database like an installation package (.msi file.)

Beginning with Windows Installer version 3.0, patch packages can contain information that describe the patching sequence for the patch relative to other updates in the [MsiPatchSequence](msipatchsequence-table.md) table and additional descriptive information in the [MsiPatchMetadata](msipatchmetadata-table.md) table.

Users can install applications and updates from a network administrative image. Although patch packages can be applied to administrative installations, the recommended method to deliver updates is to have users install the original application and then apply the patches to the local instance of the application on to their computer. This keeps users in synchronization with the administrative image. If a patch is applied to the administrative installation, all clients of that administrative installation must recache and reinstall the application to receive the update. Until a user recaches and reinstalls, the user is unable to install-on-demand and repair installations from the patched administrative installation.

Beginning with Windows Installer 3.0, non-administrators can apply patches to per-user-managed applications after the patch has been approved as trusted by an administrator. For more information on how to do this, see [Patching Per-User Managed Applications](patching-per-user-managed-applications.md). Another method is to use least privileged user account patching.

> [!Note]  
> If the [AllowLockdownPatch](allowlockdownpatch.md) policy has been set, non-administrator users can apply a patch to an existing application while running an installation at elevated privileges. This method is not recommended because it enables untrusted patches to be applied to an application that can run with elevated privileges.

 

Patch packages are comprised of the following parts. For more information about the construction of patch packages, see [Creating a Patch Package](creating-a-patch-package.md).

## Summary Information Stream

The summary information stream of the patch package provides information about the identity and purpose of the patch.

The summary information stream holds a minimum of the following:

-   A GUID that uniquely identifies the patch. The GUID for this patch is appended with a list of GUIDs for earlier patches that are replaced by this patch.
-   A semicolon-delimited list of product codes for valid targets for this patch.
-   A semicolon-delimited list of transform substorage names in the order they are to be processed.
-   A semicolon-delimited list of sources for this patch.

## Transform Substorage

A patch package contains transforms that can add or remove files, registry entries, user interfaces, and customizations. Transforms are included as substorages in the package. A patch package contains two transforms for each target database. One transform is the actual updates to the installation database and is generated from the differences between the original and updated images of the installation package. The other transform adds entries to the [Patch](patch-table.md), [PatchPackage](patchpackage-table.md), [Media](media-table.md), [InstallExecuteSequence](installexecutesequence-table.md), and [AdminExecuteSequence](adminexecutesequence-table.md) tables. Information in the substorage ties it to a specific [**UpgradeCode**](upgradecode.md), [**ProductCode**](productcode.md), [**ProductVersion**](productversion.md), and [**ProductLanguage**](productlanguage.md). A patch package that can be applied to multiple targets contains more than one pair of these transforms.

## Cabinet File Stream

The cabinet file stream included in a patch can contain these types of files:

-   Patch files containing the information required to change the old version of the file into the new version. A single patch file can be used to update one or more old versions of a file.
-   Additional files being added to the application that are not present in the old version.
-   An entire replacement file. In the rare case where the new version of a file is smaller than the patch required to update the old version of that file, the new file can be included in its entirety. These are new files that are installed over their old versions.

## Related topics

<dl> <dt>

[Creating a Patch Package](creating-a-patch-package.md)
</dt> </dl>

 

 



