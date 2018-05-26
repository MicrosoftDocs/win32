---
Description: The following Database Functions must never be called from a custom action.
ms.assetid: 55fdd82b-9f34-4c2c-a837-8a09f21f568a
title: Functions Not for Use in Custom Actions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions Not for Use in Custom Actions

The following [Database Functions](database-functions.md) must never be called from a custom action.

-   [**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master)
-   [**MsiConfigureProductEx**](/windows/win32/Msi/nf-msi-msiconfigureproductexa?branch=master)
-   [**MsiCreateTransformSummaryInfo**](/windows/win32/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa?branch=master)
-   [**MsiDatabaseApplyTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabaseapplytransforma?branch=master)
-   [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master)
-   [**MsiDatabaseExport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseexporta?branch=master)
-   [**MsiDatabaseGenerateTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabasegeneratetransforma?branch=master)
-   [**MsiDatabaseImport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseimporta?branch=master)
-   [**MsiDatabaseMerge**](/windows/win32/Msiquery/nf-msiquery-msidatabasemergea?branch=master)
-   [**MsiEnableLog**](/windows/win32/Msi/nf-msi-msienableloga?branch=master)
-   [**MsiEnableUIPreview**](/windows/win32/Msiquery/nf-msiquery-msienableuipreview?branch=master)
-   [**MsiGetDatabaseState**](/windows/win32/Msiquery/nf-msiquery-msigetdatabasestate?branch=master)
-   [**MsiOpenDatabase**](/windows/win32/Msiquery/nf-msiquery-msiopendatabasea?branch=master)
-   [**MsiPreviewBillboard**](/windows/win32/Msiquery/nf-msiquery-msipreviewbillboarda?branch=master)
-   [**MsiPreviewDialog**](/windows/win32/Msiquery/nf-msiquery-msipreviewdialoga?branch=master)
-   [**MsiReinstallProduct**](/windows/win32/Msi/nf-msi-msireinstallproducta?branch=master)
-   [**MsiSetExternalUI**](/windows/win32/Msi/nf-msi-msisetexternaluia?branch=master)
-   [**MsiSetExternalUIRecord**](/windows/win32/Msi/nf-msi-msisetexternaluirecord?branch=master)
-   [**MsiSetInternalUI**](/windows/win32/Msi/nf-msi-msisetinternalui?branch=master)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action.

-   [**MsiApplyPatch**](/windows/win32/Msi/nf-msi-msiapplypatcha?branch=master)
-   [**MsiCollectUserInfo**](/windows/win32/Msi/nf-msi-msicollectuserinfoa?branch=master)
-   [**MsiConfigureFeature**](/windows/win32/Msi/nf-msi-msiconfigurefeaturea?branch=master)
-   [**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master)
-   [**MsiConfigureProductEx**](/windows/win32/Msi/nf-msi-msiconfigureproductexa?branch=master)
-   [**MsiEnableLog**](/windows/win32/Msi/nf-msi-msienableloga?branch=master)
-   [**MsiGetFeatureInfo**](/windows/win32/Msi/nf-msi-msigetfeatureinfoa?branch=master)
-   [**MsiGetProductCode**](/windows/win32/Msi/nf-msi-msigetproductcodea?branch=master)
-   [**MsiGetProductProperty**](/windows/win32/Msi/nf-msi-msigetproductpropertya?branch=master)
-   [**MsiInstallMissingComponent**](/windows/win32/Msi/nf-msi-msiinstallmissingcomponenta?branch=master)
-   [**MsiInstallMissingFile**](/windows/win32/Msi/nf-msi-msiinstallmissingfilea?branch=master)
-   [**MsiInstallProduct**](/windows/win32/Msi/nf-msi-msiinstallproducta?branch=master)
-   [**MsiOpenPackage**](/windows/win32/Msi/nf-msi-msiopenpackagea?branch=master)
-   [**MsiOpenProduct**](/windows/win32/Msi/nf-msi-msiopenproducta?branch=master)
-   [**MsiReinstallFeature**](/windows/win32/Msi/nf-msi-msireinstallfeaturea?branch=master)
-   [**MsiReinstallProduct**](/windows/win32/Msi/nf-msi-msireinstallproducta?branch=master)
-   [**MsiSetExternalUI**](/windows/win32/Msi/nf-msi-msisetexternaluia?branch=master)
-   [**MsiSetInternalUI**](/windows/win32/Msi/nf-msi-msisetinternalui?branch=master)
-   [**MsiUseFeature**](/windows/win32/Msi/nf-msi-msiusefeaturea?branch=master)
-   [**MsiUseFeatureEx**](/windows/win32/Msi/nf-msi-msiusefeatureexa?branch=master)
-   [**MsiVerifyPackage**](/windows/win32/Msi/nf-msi-msiverifypackagea?branch=master)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action if doing so starts another installation. They may be called from a custom action that does not start another installation.

-   [**MsiProvideComponent**](/windows/win32/Msi/nf-msi-msiprovidecomponenta?branch=master)
-   [**MsiProvideQualifiedComponent**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponenta?branch=master)
-   [**MsiProvideQualifiedComponentEx**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponentexa?branch=master)

A custom action should never spawn a new thread that uses Windows Installer functions to change the feature state, component state, or to send messages from a Control Event. Attempting to do this causes the installation to fail.

 

 



