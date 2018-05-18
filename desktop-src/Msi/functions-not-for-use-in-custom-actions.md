---
Description: 'The following Database Functions must never be called from a custom action.'
ms.assetid: '55fdd82b-9f34-4c2c-a837-8a09f21f568a'
title: Functions Not for Use in Custom Actions
---

# Functions Not for Use in Custom Actions

The following [Database Functions](database-functions.md) must never be called from a custom action.

-   [**MsiConfigureProduct**](msiconfigureproduct.md)
-   [**MsiConfigureProductEx**](msiconfigureproductex.md)
-   [**MsiCreateTransformSummaryInfo**](msicreatetransformsummaryinfo.md)
-   [**MsiDatabaseApplyTransform**](msidatabaseapplytransform.md)
-   [**MsiDatabaseCommit**](msidatabasecommit.md)
-   [**MsiDatabaseExport**](msidatabaseexport.md)
-   [**MsiDatabaseGenerateTransform**](msidatabasegeneratetransform.md)
-   [**MsiDatabaseImport**](msidatabaseimport.md)
-   [**MsiDatabaseMerge**](msidatabasemerge.md)
-   [**MsiEnableLog**](msienablelog.md)
-   [**MsiEnableUIPreview**](msienableuipreview.md)
-   [**MsiGetDatabaseState**](msigetdatabasestate.md)
-   [**MsiOpenDatabase**](msiopendatabase.md)
-   [**MsiPreviewBillboard**](msipreviewbillboard.md)
-   [**MsiPreviewDialog**](msipreviewdialog.md)
-   [**MsiReinstallProduct**](msireinstallproduct.md)
-   [**MsiSetExternalUI**](msisetexternalui.md)
-   [**MsiSetExternalUIRecord**](msisetexternaluirecord.md)
-   [**MsiSetInternalUI**](msisetinternalui.md)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action.

-   [**MsiApplyPatch**](msiapplypatch.md)
-   [**MsiCollectUserInfo**](msicollectuserinfo.md)
-   [**MsiConfigureFeature**](msiconfigurefeature.md)
-   [**MsiConfigureProduct**](msiconfigureproduct.md)
-   [**MsiConfigureProductEx**](msiconfigureproductex.md)
-   [**MsiEnableLog**](msienablelog.md)
-   [**MsiGetFeatureInfo**](msigetfeatureinfo.md)
-   [**MsiGetProductCode**](msigetproductcode.md)
-   [**MsiGetProductProperty**](msigetproductproperty.md)
-   [**MsiInstallMissingComponent**](msiinstallmissingcomponent.md)
-   [**MsiInstallMissingFile**](msiinstallmissingfile.md)
-   [**MsiInstallProduct**](msiinstallproduct.md)
-   [**MsiOpenPackage**](msiopenpackage.md)
-   [**MsiOpenProduct**](msiopenproduct.md)
-   [**MsiReinstallFeature**](msireinstallfeature.md)
-   [**MsiReinstallProduct**](msireinstallproduct.md)
-   [**MsiSetExternalUI**](msisetexternalui.md)
-   [**MsiSetInternalUI**](msisetinternalui.md)
-   [**MsiUseFeature**](msiusefeature.md)
-   [**MsiUseFeatureEx**](msiusefeatureex.md)
-   [**MsiVerifyPackage**](msiverifypackage.md)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action if doing so starts another installation. They may be called from a custom action that does not start another installation.

-   [**MsiProvideComponent**](msiprovidecomponent.md)
-   [**MsiProvideQualifiedComponent**](msiprovidequalifiedcomponent.md)
-   [**MsiProvideQualifiedComponentEx**](msiprovidequalifiedcomponentex.md)

A custom action should never spawn a new thread that uses Windows Installer functions to change the feature state, component state, or to send messages from a Control Event. Attempting to do this causes the installation to fail.

 

 



