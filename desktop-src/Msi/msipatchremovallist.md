---
description: The installer sets the value of the MsiPatchRemovalList property to a list of patches that are being removed during the installation.
ms.assetid: 6e0b391a-d840-4f01-af12-4708ce6c9ce8
title: MsiPatchRemovalList property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiPatchRemovalList property

The installer sets the value of the **MsiPatchRemovalList** property to a list of patches that are being removed during the installation. The patches are represented in the list by their patch code GUIDs separated by semicolons.

Developers can use the **MsiPatchRemovalList** property to author a Windows Installer package or patch that performs [custom actions](custom-actions.md) on the removal of a patch. The custom action can be authored into the original installation package, a patch that has already been applied to the package, or a patch that is not an [uninstallable patch](uninstallable-patches.md). The custom action can be conditionalized on the **MsiPatchRemovalList** property in the sequence tables. See [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md) for more information about conditionalizing actions.

The custom action can obtain the GUIDs of patches being removed from the value of the **MsiPatchRemovalList** property. The custom action can determine whether the installation state of the patch is applied, obsolete, or superseded by calling the [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa) function or the [**PatchProperty**](patch-patchproperty.md) property of the [Patch object](patch-object.md).

## Remarks

For more information about removing patches, see [Removing Patches](removing-patches.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




