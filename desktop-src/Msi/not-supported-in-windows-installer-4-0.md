---
description: The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer&\#160;4.0 and earlier versions.
ms.assetid: 7256b759-3fb5-4195-b0e4-a1631327ebb7
title: Not Supported in Windows Installer 4.0
ms.topic: article
ms.date: 05/31/2018
---

# Not Supported in Windows Installer 4.0

The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer 4.0 and earlier versions. The absence of a feature from this list does not guarantee that the feature is supported. See the main documentation to determine which Windows Installer version is required for a particular feature. For information about other Windows Installer versions see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

Windows Installer 4.0 is available for Microsoft Windows Server 2008 and Windows Vista. For a complete list of all Windows Installer versions and redistributables, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

The following features are not supported in Windows Installer 4.0 and earlier versions.

[Installer Functions](installer-functions.md)

-   [**MsiBeginTransaction**](/windows/desktop/api/Msi/nf-msi-msibegintransactiona)
-   [**MsiEndTransaction**](/windows/desktop/api/Msi/nf-msi-msiendtransaction)
-   [**MsiJoinTransaction**](/windows/desktop/api/Msi/nf-msi-msijointransaction)

[Properties](properties.md)

-   [**MSIDISABLEEEUI**](msidisableeeui.md)
-   [**MSIUNINSTALLSUPERSEDEDCOMPONENTS**](msiuninstallsupersededcomponents.md)

[Database Tables](database-tables.md)

-   [MsiEmbeddedChainer table](msiembeddedchainer-table.md)
-   [MsiEmbeddedUI table](msiembeddedui-table.md)
-   [MsiPackageCertificate Table](msipackagecertificate-table.md)
-   [Component table](component-table.md)
- **msidbComponentAttributesUninstallOnSupersedence**  
    **msidbComponentAttributesShared**  
    
-   [CustomAction](customaction-table.md) ExtendedType Column  
    

[Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md)



[MsiTransformView\<PatchGUID\>](msitransformview.md)  

**msidbCustomActionTypePatchUninstall**  


[System Policy](system-policy.md)

-   [DisableSharedComponent](disablesharedcomponent.md)
-   [MsiDisableEmbeddedUI](msidisableembeddedui.md)

Callback Function Prototypes

-   *EmbeddedUIHandler*
-   *InitializeEmbeddedUI*
-   *ShutdownEmbeddedUI*

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)

-   [ICE92](ice92.md) verifies no component has both the **msidbComponentAttributesPermanent** and **msidbComponentAttributesUninstallOnSupersedence** attributes.

## Notes

Windows Installer 4.0 cannot perform [Multiple Package Installations](multiple-package-installations.md) using [*transaction processing*](t-gly.md).

Using Windows Installer 4.0 or earlier versions of the installer, small updates and minor upgrades can fail when using the [EnforceUpgradeComponentRules](enforceupgradecomponentrules.md) policy or [**MSIENFORCEUPGRADECOMPONENTRULES**](msienforceupgradecomponentrules.md) property because the update removes a component.

A custom user interface cannot be embedded within the Windows Installer package by using the method described in [Using an Embedded UI](using-an-embedded-ui.md).

 

 



