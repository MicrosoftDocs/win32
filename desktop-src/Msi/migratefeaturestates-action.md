---
description: The MigrateFeatureStates action is used during upgrading and when installing a new application over a related application.
ms.assetid: 3f53c555-02a9-4249-9f1a-98cd655fc79f
title: MigrateFeatureStates Action
ms.topic: article
ms.date: 05/31/2018
---

# MigrateFeatureStates Action

The MigrateFeatureStates action is used during upgrading and when installing a new application over a related application. MigrateFeatureStates reads the feature states in the existing application and then sets these feature states in the pending installation. The method is only useful when the new feature tree has not greatly changed from the original.

The MigrateFeatureStates action only runs the first time the product is installed. The MigrateFeatureStates action does not run during maintenance mode or uninstallation.

MigrateFeatureStates action runs through each record of the [Upgrade table](upgrade-table.md) in sequence and compares the upgrade code, product version, and language in each row to all products installed on the system. If MigrateFeatureStates action detects a correspondence, and if the msidbUpgradeAttributesMigrateFeatures bit flag is set in the Attributes column of the Upgrade table, the installer queries the existing feature states for the product and sets these states for the same features in the new application. The action only migrates the feature states if the [**Preselected**](preselected.md) property is not set.

## Sequence Restrictions

The MigrateFeatureStates action should come immediately after the [CostFinalize action](costfinalize-action.md). MigrateFeatureStates must be sequenced in both the [InstallUISequence table](installuisequence-table.md) and the [InstallExecuteSequence table](installexecutesequence-table.md). The installer prevents MigrateFeatureStates from running in InstallExecuteSequence if the action has already run in InstallUISequence.

## ActionData Messages

MigrateFeatureSettings sends an action data message for each product.

## Remarks

If more than one installed product shares a feature, the installation state for that feature may differ between products. MigrateFeatureState action uses the following order of precedence when migrating feature installation states: run local, run from source, advertised, and uninstalled. For example, installed product A may have feature Y as INSTALLSTATE\_LOCAL and installed product B may have feature Y as INSTALLSTATE\_ABSENT. If an upgrade installs product C and migrates the installation state of feature Y, MigrateFeatureState sets the installation state of feature Y in product C to INSTALLSTATE\_LOCAL.

For more information about how to use the MigrateFeatureStates action for product upgrades, see [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md).

 

 



