---
description: The following Database Functions must never be called from a custom action.
ms.assetid: 55fdd82b-9f34-4c2c-a837-8a09f21f568a
title: Functions Not for Use in Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Functions Not for Use in Custom Actions

The following [Database Functions](database-functions.md) must never be called from a custom action.

-   [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta)
-   [**MsiConfigureProductEx**](/windows/desktop/api/Msi/nf-msi-msiconfigureproductexa)
-   [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa)
-   [**MsiDatabaseApplyTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseapplytransforma)
-   [**MsiDatabaseCommit**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasecommit)
-   [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta)
-   [**MsiDatabaseGenerateTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasegeneratetransforma)
-   [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta)
-   [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea)
-   [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga)
-   [**MsiEnableUIPreview**](/windows/desktop/api/Msiquery/nf-msiquery-msienableuipreview)
-   [**MsiGetDatabaseState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetdatabasestate)
-   [**MsiOpenDatabase**](/windows/desktop/api/Msiquery/nf-msiquery-msiopendatabasea)
-   [**MsiPreviewBillboard**](/windows/desktop/api/Msiquery/nf-msiquery-msipreviewbillboarda)
-   [**MsiPreviewDialog**](/windows/desktop/api/Msiquery/nf-msiquery-msipreviewdialoga)
-   [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta)
-   [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)
-   [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord)
-   [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action.

-   [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha)
-   [**MsiCollectUserInfo**](/windows/desktop/api/Msi/nf-msi-msicollectuserinfoa)
-   [**MsiConfigureFeature**](/windows/desktop/api/Msi/nf-msi-msiconfigurefeaturea)
-   [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta)
-   [**MsiConfigureProductEx**](/windows/desktop/api/Msi/nf-msi-msiconfigureproductexa)
-   [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga)
-   [**MsiGetFeatureInfo**](/windows/desktop/api/Msi/nf-msi-msigetfeatureinfoa)
-   [**MsiGetProductCode**](/windows/desktop/api/Msi/nf-msi-msigetproductcodea)
-   [**MsiGetProductProperty**](/windows/desktop/api/Msi/nf-msi-msigetproductpropertya)
-   [**MsiInstallMissingComponent**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingcomponenta)
-   [**MsiInstallMissingFile**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingfilea)
-   [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta)
-   [**MsiOpenPackage**](/windows/desktop/api/Msi/nf-msi-msiopenpackagea)
-   [**MsiOpenProduct**](/windows/desktop/api/Msi/nf-msi-msiopenproducta)
-   [**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea)
-   [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta)
-   [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)
-   [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)
-   [**MsiUseFeature**](/windows/desktop/api/Msi/nf-msi-msiusefeaturea)
-   [**MsiUseFeatureEx**](/windows/desktop/api/Msi/nf-msi-msiusefeatureexa)
-   [**MsiVerifyPackage**](/windows/desktop/api/Msi/nf-msi-msiverifypackagea)

The following [Installer Functions](installer-function-reference.md) must never be called from a custom action if doing so starts another installation. They may be called from a custom action that does not start another installation.

-   [**MsiProvideComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidecomponenta)
-   [**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta)
-   [**MsiProvideQualifiedComponentEx**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponentexa)

A custom action should never spawn a new thread that uses Windows Installer functions to change the feature state, component state, or to send messages from a Control Event. Attempting to do this causes the installation to fail.

 

 



