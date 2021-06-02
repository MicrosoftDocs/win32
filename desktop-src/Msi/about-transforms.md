---
description: A transform is a collection of changes applied to an installation. By applying a transform to a base installation package, the installer can add or replace data in the installation database. The installer can only apply transforms during an installation.
ms.assetid: 1edc5227-70ac-4769-ab7f-67d01031dc33
title: About Transforms
ms.topic: article
ms.date: 05/31/2018
---

# About Transforms

A transform is a collection of changes applied to an installation. By applying a transform to a base installation package, the installer can add or replace data in the installation database. The installer can only apply transforms during an installation.

The installer registers a list of transforms required by the product during the installation. The installer must apply these transforms to the product's installation package when configuring or installing the product. If a listed transform is unavailable, and if the transform source resiliency cannot restore it, the installation fails.

A transform can modify information that is in any persistent table in the [installer database](installer-database.md). A transform can also add or remove persistent tables in the installer database. Transforms cannot modify any part of an installation package that is not in a database table, such as information in the [summary information stream](summary-information-stream.md), information in substorages, or files in embedded cabinets.

Transforms have a summary information stream that can contain validation conditions and error conditions. The transform validation and error conditions can be added to the summary information using the [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa) function. The validation conditions control whether the installer can apply the transform to a given installation database. Validation of the transform can be conditioned upon the values of the [**UpgradeCode**](upgradecode.md), [**ProductCode**](productcode.md), [**ProductVersion**](productversion.md) and [**ProductLanguage**](productlanguage.md) properties specified in the transform and those in the installation database. The transform error conditions control which errors get suppressed when the transform is applied. The error conditions included within the transform are overridden by the error conditions specified using the [**MsiDatabaseApplyTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseapplytransforma) and [**ApplyTransform**](database-applytransform.md) methods.

> [!Note]  
> Typical customization transforms have no validation conditions or validate against the [**ProductCode**](productcode.md). The transforms stored within [patch packages](patch-packages.md) generally have strict validation conditions to ensure that the correct transform is applied to the patch target.

 

There are three types of Windows Installer transforms:

-   [Embedded Transforms](embedded-transforms.md)
-   [Secured Transforms](secured-transforms.md)
-   [Unsecured Transforms](unsecured-transforms.md)

 

 



