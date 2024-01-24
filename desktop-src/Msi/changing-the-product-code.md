---
description: The product code is a GUID that is the principal identification of an application or product. See Product Codes.
ms.assetid: 4de84885-587d-405f-ba85-d62e09e8ba92
title: Changing the Product Code
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Product Code

The product code is a GUID that is the principal identification of an application or product. See [Product Codes](product-codes.md).

An update that meets the following guidelines generally does not require a change of the product code and can be handled as a [small update](small-updates.md), or if the version is to change, as a [minor upgrade](minor-upgrades.md):

-   The update can enlarge or reduce the feature-component tree but it must not reorganize the existing hierarchy of features and components described by the [Feature](feature-table.md) and [FeatureComponents](featurecomponents-table.md) tables. It can add a new feature to the existing feature-component tree. If it removes a parent feature, it must also remove all the child features of the removed feature.
-   The update can add a new component to a new or an existing feature.
-   The update must not change the component code of any component. Consequently, a small update or minor upgrade must never change the name of a component's key file because this would require changing the component code.
-   The update must not change the name of the .msi file of the installation package. Instead, because it modifies the package, it should change the package code. Note that this means that the update can change the tables, custom actions, and dialogs in the .msi file without changing the file's name.
-   The update can add, remove, or modify the files, registry keys, or shortcuts of components that are not shared by two or more features. If the update modifies a versioned file, that file's version must be incremented in the [File table](file-table.md). If the update removes resources, it should also update the [RemoveFile](removefile-table.md) and [RemoveRegistry](removeregistry-table.md) tables to remove any unused files, registry keys, or shortcuts that have already been installed.
-   The update of a component that is shared by two or more features must be backward compatible with all applications and features that use the component. The update can modify the resource of a shared component, such as files, registry entries, and shortcuts, as long as the changes are backward compatible. It is not recommended that the update add or remove files, registry entries, or shortcuts from a shared component.
-   A small update is shipped as a Windows Installer [patch package](patch-packages.md). (A full product CD-ROM is usually not provided with a small update.)

The product code must be changed if any of the following are true for the update:

-   Coexisting installations of both original and updated products on the same system must be possible.
-   The name of the .msi file has been changed.
-   The component code of an existing component has changed.
-   A component is removed from an existing feature.
-   An existing feature has been made into a child of an existing feature.
-   An existing child feature has been removed from its parent feature.

Note that adding a new child feature, consisting entirely of new components, to an existing feature does not require changing the product code.

New child features can be authored by including msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent in the Attributes field of the [Feature table](feature-table.md). If the minor upgrade only adds new child features, then REINSTALL=ALL is sufficient to force the installation of the new child features. For more information, see [Controlling Feature Selection States](controlling-feature-selection-states.md).

A new child feature may be hidden from the user. To synchronize the installation state of a new child feature with its parent feature, set the msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent bits for the child feature.

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Property Reference](property-reference.md)
</dt> </dl>

 

 



