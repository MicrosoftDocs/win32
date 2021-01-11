---
description: Windows Installer upgrade packages can be authored to have major upgrades not install if a user already has a newer version installed.
ms.assetid: f46e82bd-70b3-46a2-8246-a1eadfdc589d
title: Prevent an Old Package from Installing Over a Newer Version
ms.topic: article
ms.date: 05/31/2018
---

# Preventing an Old Package from Installing Over a Newer Version

Windows Installer upgrade packages can be authored to have major upgrades not install if a user already has a newer version installed. The procedure in this topic can only prevent downgrades that might be caused by running a major upgrade package. This procedure relies on the [FindRelatedProducts Action](findrelatedproducts-action.md), which only runs during a first-time installation and does not run in maintenance mode (reinstallation). Because minor upgrades are performed using reinstallation, this procedure cannot be used to determine whether a minor upgrade package is attempting to downgrade an application. For more information, see [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md).

**To prevent an old package from installing over a newer version**

1.  Enter the [**UpgradeCode**](upgradecode.md) Property for the group of related products that may be eligible to receive this upgrade into the UpgradeCode column of the [Upgrade Table](upgrade-table.md).
2.  Enter the **msidbUpgradeAttributesOnlyDetect** bit flag in the Attributes column of the [Upgrade Table](upgrade-table.md).
3.  Enter the version of the upgrade provided by this package into the VersionMin column of the [Upgrade Table](upgrade-table.md). Leave the VersionMax column blank.
4.  Enter the name of the property that is to be set by the [FindRelatedProducts Action](findrelatedproducts-action.md) into the ActionProperty column of the [Upgrade Table](upgrade-table.md).
5.  Add the [**SecureCustomProperties**](securecustomproperties.md) property and the property named in the ActionProperty column of the [Upgrade Table](upgrade-table.md) to the [Property Table](property-table.md).
6.  Add a [Custom Action Type 19](custom-action-type-19.md) after the FindRelatedProducts action in the [InstallExecuteSequence Table](installexecutesequence-table.md). Include a record in the [CustomAction Table](customaction-table.md) for this action and enter the text to be displayed in the Target column. The type 19 custom action is built into the installer, so there is no code to write.
7.  Enter the name of the ActionProperty into the Condition column of the record in [InstallExecuteSequence Table](installexecutesequence-table.md) that contains the [Custom Action Type 19](custom-action-type-19.md). This conditions the custom action to only be executed when the [Upgrade Table](upgrade-table.md) detects that a newer version is already installed.

    For example, a Windows Installer package that upgrades a group of related products to version 3.0 may include the following records in its [Upgrade](upgrade-table.md), [CustomAction](customaction-table.md), [InstallExecuteSequence](installexecutesequence-table.md), and [Property](property-table.md) tables. All the related products in the group have the same UpgradeCode, but the installer does not install this upgrade package if a version later than 3.0 is already installed on the computer. In this case, the Installer presents an error message and the installation fails. The version 3.0 upgrade package installs over versions 1.0 and 2.0.

    [Upgrade Table](upgrade-table.md)

    

    | UpgradeCode                            | VersionMin | VersionMax | Language | Attributes                                | Remove | ActionProperty  |
    |----------------------------------------|------------|------------|----------|-------------------------------------------|--------|-----------------|
    | {E7BE6D45-49FF-4701-A17E-BDCC98CE180D} | 3.0        |            |          | msidbUpgradeAttributesOnlyDetect          |        | NEWPRODUCTFOUND |
    | {E7BE6D45-49FF-4701-A17E-BDCC98CE180D} | 1.0        | 3.0        |          | msidbUpgradeAttributesVersionMinInclusive |        | UPGRADEFOUND    |

    

     

    [CustomAction Table](customaction-table.md)

    

    | Action | Type | Source | Target                                 |
    |--------|------|--------|----------------------------------------|
    | CA1    | 19   |        | A higher upgrade is already installed. |

    

     

    [InstallExecuteSequence Table](installexecutesequence-table.md)

    

    | Action              | Condition       | Sequence |
    |---------------------|-----------------|----------|
    | FindRelatedProducts |                 | 200      |
    | CA1                 | NEWPRODUCTFOUND | 201      |

    

     

    [Property Table](property-table.md)

    

    | Property                                                 | Value                        |
    |----------------------------------------------------------|------------------------------|
    | [**SecureCustomProperties**](securecustomproperties.md) | NEWPRODUCTFOUND;UPGRADEFOUND |

    

     

 

 



