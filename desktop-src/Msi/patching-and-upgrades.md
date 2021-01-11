---
description: Because an installation package can contain the files that make up an application as well the information needed for their installation, Windows Installer can be used to update the application.
ms.assetid: da946739-9efc-4bf0-8a9a-6f6ead3c4a34
title: Patching and Upgrades
ms.topic: article
ms.date: 05/31/2018
---

# Patching and Upgrades

Because an installation package can contain the files that make up an application as well the information needed for their installation, Windows Installer can be used to update the application. The installer can update information in the following parts of the installation package:

-   The .msi file.
-   The files of the application.
-   The Windows Installer registration information.

The type of update can be characterized by the changes the update makes to the application's product code, product version, and package code. The application's product version is stored in the [**ProductVersion**](productversion.md) property. The application's product code is stored in the [**ProductCode**](productcode.md) property. The application's [package code](package-codes.md) is stored in the [**Revision Number Summary**](revision-number-summary.md) Property.

An update that changes the application into another product is required to change the [**ProductCode**](productcode.md) of the application. For more information about which updates require changing the **ProductCode** see [Changing the Product Code](changing-the-product-code.md). The update can change the [**ProductVersion**](productversion.md) and leave the **ProductCode** unchanged if future versions of the application will need to differentiate between the updated and nonupdated versions of the current product. The [Package Code](package-codes.md) uniquely identifies the installation package and should always be changed whenever update or upgrade changes any information in the installation package.

When deciding whether to change the product version, you should consider If future versions of the application will need to differentiate between the updated and nonupdated versions of the current product. To ensure differentiation in the future, a [minor upgrade](minor-upgrades.md) should be used instead of a [small update](small-updates.md).

-   If an update changes the .msi file and application files, but does not change the [**ProductCode**](productcode.md) property or [**ProductVersion**](productversion.md) property, it is termed a [small update](small-updates.md).
-   If the update changes the [**ProductVersion**](productversion.md), but does not change the [**ProductCode**](productcode.md), it is termed a [minor upgrade](minor-upgrades.md).
-   If the update changes the installation into an entirely different product, the [**ProductCode**](productcode.md) must change and the update is termed a [major upgrade](major-upgrades.md).

> [!Note]  
> To ensure differentiation of versions of the current product in the future, a [minor upgrade](minor-upgrades.md) should be used instead of a [small update](small-updates.md).

 

The following table summarizes the different types of updates.



| Type of update                       | Productcode | ProductVersion | Description                                                                                                                                                                                                                                                                                                           |
|--------------------------------------|-------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Small Update](small-updates.md)    | No change   | No change      | An update to one or two files that is too small to warrant changing the [**ProductVersion**](productversion.md). The package code in the [**Revision Number Summary**](revision-number-summary.md) Property does change. Can be shipped as a full installation package or as a [patch package](patch-packages.md). |
| [Minor Upgrade](minor-upgrades.md)  | No change   | Changed        | A small update making changes significant enough to warrant changing the [**ProductVersion**](productversion.md) property. Can be shipped as a full installation package or as a [patch package](patch-packages.md).                                                                                                |
| [Major Upgrades](major-upgrades.md) | Changed     | Changed        | A comprehensive update of the product warranting a change in the [**ProductCode**](productcode.md) property. Shipped as a [patch package](patch-packages.md) or as a full product installation package.                                                                                                             |



 

> [!Note]  
> The Windows Installer can install an application, or an update, for all users of a computer (per-machine context) or for a particular user (per-user context) depending on the access privileges of the user, the value of the [**ALLUSERS**](allusers.md) property, and the version of the operating system. Application developers should consider in which context updates will be installed. If the contexts of the application and update are different, the application may not be updated as expected.

 

Users can update to an application by reinstalling a Windows Installer package for the application. Note that [Minor Upgrades](minor-upgrades.md) can be applied in the same way as [Small Updates](small-updates.md). For more information about updating an application by reinstalling the application, see these sections:

-   [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md)
-   [Applying Major Upgrades by Installing the Product](applying-major-upgrades-by-installing-the-product.md)

An update to an application can be provided to users as a Windows Installer patch package. A patch can contain an entire file or only the file bits necessary to update part of a file. This means that the user can download an upgrade patch that is much smaller than the entire product and that preserves user customizations through the upgrade. Note that [Minor Upgrades](minor-upgrades.md) can be applied in the same way as [Small Updates](small-updates.md). For more information about updating an application using a patch, see these sections:

-   [Patching](patching.md)
-   [Creating a Small Update Patch](creating-a-small-update-patch.md)
-   [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md)
-   [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md)
-   [Applying Major Upgrades by Patching the Local Installation of the Product](applying-major-upgrades-by-patching-the-local-installation-of-the-product.md)

 

 



