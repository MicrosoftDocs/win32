---
description: The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer&\#160;2.0 and earlier versions.
ms.assetid: 850b598a-338e-4f84-8336-01e962256a08
title: Not Supported in Windows Installer 2.0
ms.topic: article
ms.date: 05/31/2018
---

# Not Supported in Windows Installer 2.0

The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer 2.0 and earlier versions. The absence of a feature from this list does not guarantee that the feature is supported. See the main documentation to determine which Windows Installer version is required for a particular feature. For information about other Windows Installer versions see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

Windows Installer 2.0 can run on Microsoft Windows 2000, Microsoft Windows XP, or Windows Server 2003. For a list of all Windows Installer versions, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

The following features are not supported in Windows Installer 2.0 and earlier versions.

[Installer Functions](installer-functions.md)

-   [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
-   [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea)
-   [**MsiApplyMultiplePatches**](/windows/desktop/api/Msi/nf-msi-msiapplymultiplepatchesa)
-   [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa)
-   [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
-   [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
-   [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa)
-   [**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa)
-   [**MsiQueryComponentState**](/windows/desktop/api/Msi/nf-msi-msiquerycomponentstatea)
-   [**MsiExtractPatchXMLData**](/windows/desktop/api/Msi/nf-msi-msiextractpatchxmldataa)
-   [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa)
-   [**MsiSourceListEnumSources**](/windows/desktop/api/Msi/nf-msi-msisourcelistenumsourcesa)
-   [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa)
-   [**MsiSourceListClearSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearsourcea)
-   [**MsiSourceListClearAllEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearallexa)
-   [**MsiSourceListForceResolutionEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistforceresolutionexa)
-   [**MsiSourceListGetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistgetinfoa)
-   [**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa)
-   [**MsiSourceListEnumMediaDisks**](/windows/desktop/api/Msi/nf-msi-msisourcelistenummediadisksa)
-   [**MsiSourceListAddMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska)
-   [**MsiSourceListClearMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearmediadiska)

[Windows Installer Structures](installer-structures.md)

-   [**MSIPATCHSEQUENCEINFO**](/windows/win32/api/msi/ns-msi-msipatchsequenceinfoa)

[Database Tables](database-tables.md)

-   [MsiPatchCertificate](msipatchcertificate-table.md)
-   [MsiPatchSequence](msipatchsequence-table.md)
-   [MsiPatchMetadata](msipatchmetadata-table.md)

[Properties](properties.md)

-   [**MSIDISABLELUAPATCHING**](msidisableluapatching.md)
-   [**MSIENFORCEUPGRADECOMPONENTRULES**](msienforceupgradecomponentrules.md)
-   [**MSIPATCHREMOVE**](msipatchremove.md)
-   [**MsiPatchRemovalList**](msipatchremovallist.md)
-   [**MsiUISourceResOnly**](msiuisourceresonly.md)
-   [**MsiUIHideCancel**](msiuihidecancel.md)
-   [**MsiUIProgressOnly**](msiuiprogressonly.md)

[System Policy](system-policy.md)

-   [DisableLUAPatching](disableluapatching.md)
-   [DisablePatchUninstall](disablepatchuninstall.md)
-   [DisableFlyWeightPatching](disableflyweightpatching.md)
-   [EnforceUpgradeComponentRules](enforceupgradecomponentrules.md)
-   [MaxPatchCacheSize](maxpatchcachesize.md)

[Error Codes](error-codes.md)

-   ERROR\_PATCH\_REMOVAL\_UNSUPPORTED
-   ERROR\_UNKNOWN\_PATCH
-   ERROR\_PATCH\_NO\_SEQUENCE
-   ERROR\_PATCH\_REMOVAL\_DISALLOWED
-   ERROR\_INVALID\_PATCH\_XML
-   ERROR\_PATCH\_MANAGED\_ADVERTISED\_PRODUCT

Logging Modes

-   [**INSTALLLOGMODE\_LOGONLYONERROR**](/windows/desktop/api/Msi/nf-msi-msienableloga)

[Automation Interface](automation-interface.md)

-   Properties of [**Product Object**](product-object.md)

    -   [**Product.UserSid**](product-usersid.md)
    -   [**Product.Sources**](product-sources.md)
    -   [**Product.MediaDisks**](product-mediadisks.md)
    -   [**Product.FeatureState**](product-featurestate.md)
    -   [**Product.Context**](product-context.md)
    -   [**Product.InstallProperty**](product-installproperty.md)
    -   [**Product.ProductCode**](product-productcode.md)
    -   [**Product.ComponentState**](product-componentstate.md)
    -   [**Product.State**](product-state.md)
    -   [**Product.SourceListInfo**](product-sourcelistinfo.md)

-   Methods of [**Product Object**](product-object.md)

    -   [**Product.SourceListForceResolution**](product-sourcelistforceresolution.md)
    -   [**Product.SourceListClearMediaDisk**](product-sourcelistclearmediadisk.md)
    -   [**Product.SourceListClearAll**](product-sourcelistclearall.md)
    -   [**Product.SourceListClearSource**](product-sourcelistclearsource.md)
    -   [**Product.SourceListAddSource**](product-sourcelistaddsource.md)
    -   [**Product.SourceListAddMediaDisk**](product-sourcelistaddmediadisk.md)

-   Properties of [**Patch Object**](patch-object.md)

    -   [**Patch.UserSid**](patch-usersid.md)
    -   [**Patch.State**](patch-state.md)
    -   [**Patch.Sources**](patch-sources.md)
    -   [**Patch.SourceListInfo**](patch-sourcelistinfo.md)
    -   [**Patch.ProductCode**](patch-productcode.md)
    -   [**Patch.PatchProperty**](patch-patchproperty.md)
    -   [**Patch.PatchCode**](patch-patchcode.md)
    -   [**Patch.MediaDisks**](patch-mediadisks.md)
    -   [**Patch.Context**](patch-context.md)

-   Methods of the [**Patch Object**](patch-object.md)

    -   [**Patch.SourceListForceResolution**](patch-sourcelistforceresolution.md)
    -   [**Patch.SourceListClearAll**](patch-sourcelistclearall.md)
    -   [**Patch.SourceListClearSource**](patch-sourcelistclearsource.md)
    -   [**Patch.SourceListClearMediaDisk**](patch-sourcelistclearmediadisk.md)
    -   [**Patch.SourceListAddSource**](patch-sourcelistaddsource.md)
    -   [**Patch.SourceListAddMediaDisk**](patch-sourcelistaddmediadisk.md)

-   Properties of the [**Installer Object**](installer-object.md)

    -   [**Installer.ProductsEx**](installer-productsex.md)
    -   [**Installer.ProductInfo**](installer-productinfo.md)
    -   [**Installer.PatchesEx**](installer-patchesex.md)

-   Methods of the [**Installer Object**](installer-object.md)

    -   [**Installer.ApplyMultiplePatches**](installer-applymultiplepatches.md)
    -   [**Installer.ApplyPatch**](installer-applypatch.md)
    -   [**Installer.RemovePatches**](installer-removepatches.md)
    -   [**Installer.ExtractPatchXMLData**](installer-extractpatchxmldata.md)

The following features are also not supported in Windows Installer version 2.0.2600. Windows Installer version 2.0.2600 was released with Windows XP and Windows 2000 Server. The features are available beginning with Windows Installer version 2.0.3790 released with Windows Server 2003. For a list of all Windows Installer versions, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

[Installer Functions](installer-functions.md)

-   [**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa)
    -   MSIADVERTISEOPTIONS\_INSTANCE
-   [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha)
-   [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa)

[Automation Interface](automation-interface.md)

-   Methods of the [**Installer Object**](installer-object.md)

    -   [**Installer.ApplyPatch**](installer-applypatch.md)
    -   [**Installer.ProductInfo**](installer-productinfo.md)

[Properties](properties.md)

-   [**MSINEWINSTANCE**](msinewinstance.md)
-   [**MSIINSTANCEGUID**](msiinstanceguid.md)
-   [**MsiNTSuiteWebServer**](msintsuitewebserver.md)

[Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md)

-   [**msidbCustomActionTypeTSAware**](custom-action-in-script-execution-options.md)

[Error Codes](error-codes.md)

-   [ERROR\_INSTALL\_REMOTE\_PROHIBITED](error-codes.md)

[Machine Policies](machine-policies.md)

-   [DisableMSI](disablemsi.md)
-   [TransformsSecure policy](transformssecure-policy.md)

[Command Line Options](command-line-options.md)

-   [/c](command-line-options.md)
-   [/n](command-line-options.md)
-   [/Lx](command-line-options.md)

[Control Attributes](control-attributes.md)

-   **ImageHandle** was removed

## Notes

The [Standard Installer Command-Line Options](standard-installer-command-line-options.md) are not supported by Windows Installer 2.0. Instead use the Windows Installer [Command-Line Options](command-line-options.md).

When Windows Installer 2.0 installs a patch package, it ignores information in the [MsiPatchSequence](msipatchsequence-table.md) or [MsiPatchMetadata](msipatchmetadata-table.md) tables. Later versions of the Windows Installer can use the information in these tables to improve patch sequencing, removal, and optimization. For information about improved patching functionality in Windows Installer, see [Patching](patching.md).

Windows Installer 2.0 does not support [Uninstallable Patches](uninstallable-patches.md) and the only method to remove particular patches from an application is to uninstall the entire patched application and then reinstall without reapplying any patches being removed.

Windows Installer 2.0 does not support patch sequencing and installs patches in the order that they are provided to the system when [installing multiple patches](installing-multiple-patches.md).

Windows Installer 2.0 does not support the use of [User Account Control (UAC) Patching](user-account-control--uac--patching.md) to enable digitally-signed patches that can be applied by non-administrator users.

Windows Installer 2.0 does not support [Patch Optimization](patch-optimization.md). Patching can take significantly more time than with later Windows Installer versions that only updates files affected by the patch.

Windows Installer 2.0 does not support [Using Windows Installer to Inventory Products and Patches](inventory-products-and-patches-.md).

Windows Installer 2.0 does not support the retrieval and modification of source list information for Windows Installer applications and patches installed on the system for all users. Later versions of Windows Installer enable administrators to manage source lists and source list properties for network, URL and media sources. Later versions enable administrators to manage source lists from an external process. For more information see [Managing Installation Sources](managing-installation-sources.md).

Windows Installer 2.0 does not support installing multiple instances of products or patches without a separate installation package for each instance. Later Windows Installer versions can install multiple instances of a product by using product code transforms and one .msi package or one patch. For information see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md).

Starting with Windows XP with Service Pack 2 (SP2), Windows Installer can use the HTTP, HTTPS, and FILE protocols. The installer does not support the FTP and GOPHER protocols.

 

 



