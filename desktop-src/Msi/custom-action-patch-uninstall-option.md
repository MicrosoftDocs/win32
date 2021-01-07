---
description: Use the following option flag to specify that the installer run the custom action only when a patch is being uninstalled. To set the option, add the value in this table to the value in the ExtendedType field of the CustomAction table.
ms.assetid: aa4d9e21-5316-42b5-a22e-c7a5becd3cae
title: Custom Action Patch Uninstall Option
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Patch Uninstall Option

Use the following option flag to specify that the installer run the custom action only when a patch is being uninstalled. To set the option, add the value in this table to the value in the ExtendedType field of the [CustomAction table](customaction-table.md).

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This option is available beginning with Windows Installer 4.5.



| Constant                                | Hexadecimal | Decimal | Description                                                    |
|-----------------------------------------|-------------|---------|----------------------------------------------------------------|
| **msidbCustomActionTypePatchUninstall** | 0x8000      | 32768   | The custom action runs only when a patch is being uninstalled. |



 

## Remarks

This attribute can be added to a custom action by authoring it in the Windows Installer package (.msi file). A new custom action with this attribute can be added by a patch. A custom action having this attribute can be updated by a patch. This attribute cannot be added or removed by a patch to an existing custom action.

If a patch adds or updates a custom action with this attribute, Windows Installer runs the new or updated custom action when the patch is uninstalled. Windows Installer makes the updates within the patch being uninstalled available to the patch uninstall custom action. The patch must include a [MsiTransformView*<PatchGUID>*](msitransformview.md) table to provide this information to Windows Installer.

When a package that contains a custom action with the **msidbCustomActionTypePatchUninstall** attribute is installed using an installer version earlier than Windows Installer 4.0, the installer does not call the custom action when the patch is uninstalled. The install can run the custom action during the installation, repair, or update of the package.

Custom actions with the **msidbCustomActionTypePatchUninstall** attribute should be conditioned using the [**MSIPATCHREMOVE**](msipatchremove.md) property to prevent the custom action from running when installing, repairing, or updating using a system with Windows Installer 4.0 or earlier. When Windows Installer 4.5 and later is installed, all the patches on the system having custom actions marked with the **msidbCustomActionTypePatchUninstall** attribute run the custom action during patch uninstallation. If Windows Installer 4.5 or later is removed from the system, patches lose the custom action patch uninstall functionality.

For information about running a custom action during the uninstallation of a patch using a version earlier than Windows Installer 4.5, see [Patch Uninstall Custom Actions](patch-uninstall-custom-actions.md).

## Related topics

<dl> <dt>

[Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md)
</dt> <dt>

[Custom Action Reference](custom-action-reference.md)
</dt> <dt>

[About Custom Actions](about-custom-actions.md)
</dt> <dt>

[Using Custom Actions](using-custom-actions.md)
</dt> <dt>

[MsiTransformView*<PatchGUID>*](msitransformview.md)
</dt> </dl>

 

 



