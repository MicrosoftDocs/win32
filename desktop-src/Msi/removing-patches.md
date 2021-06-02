---
description: Beginning with Windows Installer&\#160;version&\#160;3.0, it is possible to create and install patches that can be uninstalled singly, and in any order, without having to uninstall and reinstall the entire application and other patches.
ms.assetid: 2ad30ac9-eac9-49cf-98ae-5c053a0b500a
title: Removing Patches
ms.topic: article
ms.date: 05/31/2018
---

# Removing Patches

Beginning with Windows Installer version 3.0, it is possible to create and install patches that can be uninstalled singly, and in any order, without having to uninstall and reinstall the entire application and other patches. Windows Installer 3.0 also enables [Patch Packages](patch-packages.md) to be authored with a [MsiPatchSequence Table](msipatchsequence-table.md) that contains patch sequencing information. With versions of Windows Installer earlier than Windows Installer 3.0, the only method to remove particular patches from an application is to uninstall the entire patched application and then reinstall without reapplying any patches being removed.

Whether a patch can be uninstalled depends upon how the patch was authored, the version of Windows Installer used to install the patch, and the changes made by the patch to the application. If a patch is not uninstallable, then the only way to remove the patch is to uninstall the entire application and reinstall without applying the patch being removed.

You can uninstall one or more patches using a command line option, the scripting interface, or by calling [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa) from another application. See [Uninstalling Patches](uninstalling-patches.md) for more information about how to uninstall patches.

The value of the [**MSIPATCHREMOVE**](msipatchremove.md) property lists the patches to be uninstalled. For each patch in the list, the installer verifies that the patch is uninstallable. If the user does not have privileges to remove the patch, the patch is unknown for the product, patch policy prevents removal, or the patch was marked as not uninstallable, the installer returns an error that indicates a failed installation transaction. See [Uninstallable Patches](uninstallable-patches.md) for more information about what determines whether a patch is not uninstallable.

Once the patch is verified as removable, the installer removes the patch from the patch application sequence. For more information about how Windows Installer 3.0 determines what sequence to use when applying patches see [Sequencing Patches](sequencing-patches.md). Note that removing patches from the sequence can cause patches marked obsolete or superseded to become active.

All patches selected for removal are listed in the [**MsiPatchRemovalList**](msipatchremovallist.md) property. This property is a private property that is set by the installer and can be used in conditional expressions or queried by [custom actions](custom-actions.md). The property contains the list of patch code GUIDs of patches to be removed. A custom action can determine whether the installation state of the patch is applied, obsolete or superseded by calling the [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa) or the [**PatchProperty**](patch-patchproperty.md) property of the [Patch Object](patch-object.md).

After a patch is removed the state of the application is the same as if the patch was never installed. If possible, the installer restricts the process to the subset of features affected by the patch being removed. The installer automatically sets the [**REINSTALL**](reinstall.md) property to the list of affected features. Files that were added by the patch are removed and files that were modified by the patch are overwritten. Files and registry entries are restored to the version expected by the product minus the patch. Features and components that were added by the patch are unregistered from the application. Note that additional content added by the patch can remain on the user's computer if the content is used by another patch that is still applicable.

If a file of a shared component is updated by a patch, the change affects all applications that share the component. When the patch is removed, again, the change affects all applications that share the component. This means that removal of a patch by one application can restore the file of the shared component to a lower version than required by another application. This could fix the first application, but cause the second application to stop working. In this case, the second application can be repaired by reinstalling the second application using the methods describe in [Reinstalling a Feature or Application](reinstalling-a-feature-or-application.md). This will restore the patched version of the file.

## Related topics

<dl> <dt>

[**MsiEnumapplicationsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
</dt> <dt>

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[**MSIPATCHREMOVE**](msipatchremove.md)
</dt> <dt>

[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
</dt> <dt>

[Patch Sequencing](sequencing-patches.md)
</dt> <dt>

[Patch Uninstall Custom Actions](patch-uninstall-custom-actions.md)
</dt> <dt>

[Uninstallable Patches](uninstallable-patches.md)
</dt> <dt>

[Uninstalling Patches](uninstalling-patches.md)
</dt> </dl>

 

 



