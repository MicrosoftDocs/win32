---
description: There are two ways to author the Windows Installer installation database such that an action is only called when the package is uninstalled.
ms.assetid: 67b205bb-11d8-454f-b5d5-93330219f6cc
title: Conditioning Actions to Run During Removal
ms.topic: article
ms.date: 05/31/2018
---

# Conditioning Actions to Run During Removal

There are two ways to author the installation database such that an action is only called when the package is uninstalled:

-   If the action is sequenced after the [InstallValidate action](installvalidate-action.md) in the [InstallExecuteSequence table](installexecutesequence-table.md), the package author may specify a condition of REMOVE="ALL" for the action in the Condition column. Note that the [**REMOVE**](remove.md) property is not guaranteed to be set to ALL during an uninstall before the installer executes the InstallValidate action. Note that the quote marks around the value ALL are required in this case.
-   If the action is sequenced after the [CostFinalize action](costfinalize-action.md) and any actions that could change the feature state, such as [MigrateFeatureStates action](migratefeaturestates-action.md), the action can be conditioned on the state of a particular feature or component. See [Conditional Statement Syntax](conditional-statement-syntax.md). Use this option to call an action during the removal of a particular feature or component, which may occur outside of the complete removal of the application.

Note that the [**Installed**](installed.md) property can be used in conditional expressions to determine whether a product is installed per-computer or for the current user. To determine whether the product is installed for a different user, check the [**ProductState**](productstate.md) property.

Note that older versions of a product may be removed during an upgrade by the [RemoveExistingProducts action](removeexistingproducts-action.md). The [Upgrade table](upgrade-table.md) may also set the [**REMOVE**](remove.md) property to ALL in this case. To determine whether a product is being removed by an upgrade, check the [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md) property. The installer only sets this property when RemoveExistingProducts removes the product. The installer does not set the property during a normal uninstall, such as removal with Add/Remove programs.

 

 



