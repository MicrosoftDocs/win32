---
description: You can use the Custom Action Patch Uninstall option to specify that the installer run the custom action only when a patch is uninstalled.
ms.assetid: c741aa40-ba4c-459e-936a-19c002620c30
title: Patch Uninstall Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Patch Uninstall Custom Actions

You can use the [Custom Action Patch Uninstall option](custom-action-patch-uninstall-option.md) to specify that the installer run the custom action only when a patch is uninstalled.

**Windows Installer 4.5 and later:** You can use the [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md) to specify that the installer only run the custom action when a patch is uninstalled.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):  **

The [Custom Action Patch Uninstall option](custom-action-patch-uninstall-option.md) is not available. There is no method for marking a [custom action](custom-actions.md) within a patch package to be run when the patch is uninstalled because the installer does not apply the patch packages being uninstalled.

To have a [custom action](custom-actions.md) run when a particular patch is uninstalled, the custom action must either be present in the original application or be in a patch for the product that is always applied.

Developers can use the [**MsiPatchRemovalList**](msipatchremovallist.md) property to author a Windows Installer package or patch that performs [custom actions](custom-actions.md) on the removal of a patch. The custom action can be authored into the original installation package, a patch that has already been applied to the package, or a patch that is not an [uninstallable patch](uninstallable-patches.md). The custom action can be conditionalized on the **MsiPatchRemovalList** property in the sequence tables. See [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md) for more information about conditionalizing actions.

The custom action can obtain the GUIDs of patches being removed from the value of the [**MsiPatchRemovalList**](msipatchremovallist.md) property. The custom action can determine whether the installation state of the patch is applied, obsolete, or superseded by calling the [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa) or the [**PatchProperty**](patch-patchproperty.md) property of the [Patch object](patch-object.md).

If the custom action requires special metadata from the patch, the patch should contain a custom action that writes the metadata to a registry or file location when the patch is applied. The custom action in the original application or a patch that is always applied can obtain the information needed to remove the patch's changes.

Patches making changes that are difficult to undo correctly should not be marked as [uninstallable patches](uninstallable-patches.md).

## Related topics

<dl> <dt>

[Patch Sequencing](sequencing-patches.md)
</dt> <dt>

[Removing Patches](removing-patches.md)
</dt> <dt>

[Uninstallable Patches](uninstallable-patches.md)
</dt> <dt>

[Uninstalling Patches](uninstalling-patches.md)
</dt> <dt>

[**MSIPATCHREMOVE**](msipatchremove.md)
</dt> <dt>

[**MsiEnumapplicationsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
</dt> <dt>

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
</dt> </dl>

 

 



