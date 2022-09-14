---
description: Concurrent Installations, also called Nested Installations, is a deprecated feature of the Windows Installer.
ms.assetid: 579ae4ee-47a0-440e-81ca-ea8bf60c5349
title: Concurrent Installations
ms.topic: article
ms.date: 05/31/2018
---

# Concurrent Installations

Concurrent Installations, also called Nested Installations, is a deprecated feature of the Windows Installer. Applications installed with concurrent installations can eventually fail because they are difficult for customers to service correctly. Do not use concurrent installations to install products that are intended to be released to the public. Concurrent installations can have limited applicability in controlled corporate environments when used to install applications that are not intended for public release. The concurrent installations documentation is provided for package authors that wish to use concurrent installations with applications that are not for public distribution.

A concurrent installation action installs another Windows Installer package during a currently running installation. A concurrent installation is added to a package by authoring a concurrent installation action into the [CustomAction table](customaction-table.md) and scheduling this custom action into the sequence tables. The Target field of the CustomAction table contains a string of public property settings used by the concurrent installation. The Source field of the CustomAction table identifies the concurrent package. A concurrent installation action can only reinstall or remove an application that has been installed by the current application's installation package.

The type of concurrent installation action is specified in the Type field of the CustomAction table. Depending upon the custom action type, the package for the concurrent application can reside in a substorage of the main package, as a file at a location specified by a property, or as an advertised application on the user's machine. The following types of custom actions perform a concurrent installation.



| Custom action type                                 | Description                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------|
| [Custom Action Type 7](custom-action-type-7.md)   | Concurrent installation of a product residing in the installation package.      |
| [Custom Action Type 23](custom-action-type-23.md) | Concurrent installation of an installer package within the current source tree. |
| [Custom Action Type 39](custom-action-type-39.md) | Concurrent installation of an advertised installer package.                     |



 

A concurrent installation shares the same user interface and logging settings as the main installation.

Concurrent installation actions should be placed between the [InstallInitialize action](installinitialize-action.md) and [InstallFinalize action](installfinalize-action.md) of the main installation's action sequence. Upon rollback of the main installation, the installer will then rollback the concurrent installation as well. The use of [deferred execution](deferred-execution-custom-actions.md) with concurrent installation actions is unnecessary because the installer combines rollback information from the concurrent and main installations. All changes are reversed upon a rollback installation.

The return values for concurrent installation actions are the same as for other custom actions. See [Custom Action Return Values](custom-action-return-values.md).

Standard or custom actions that specify an automatic restart of the system, or request the user to restart, can also perform restart or request from within a concurrent installation.

Once the installer begins a concurrent installation, it locks out all other installations until the concurrent installation is complete and before continuing the main installation. The installer can only execute concurrent installations as synchronous custom actions. See [Synchronous and Asynchronous Custom Actions](synchronous-and-asynchronous-custom-actions.md). The option flags described in [Custom Action Return Processing Options](custom-action-return-processing-options.md) must be set to none (+0) or **msidbCustomActionTypeContinue** (+64).

A concurrent installation action can install an application to be run locally, to run from source, to be reinstalled, or to be removed in the same manner as when using [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) for a regular installation. To specify the type of installation, pass either the [**ADDLOCAL**](addlocal.md), [**ADDSOURCE**](addsource.md), [**REINSTALL**](reinstall.md), or [**REMOVE**](remove.md) property to the concurrent installation action.

Concurrent installation actions can be authored in pairs, one action used for installing and the other action used for removing the concurrent installation. A [Custom Action Type 7](custom-action-type-7.md) or [Custom Action Type 23](custom-action-type-23.md) is typically used to install. A [Custom Action Type 39](custom-action-type-39.md) is typically used to remove the concurrent installation when the parent product is uninstalled. The record for the removal custom action in the [CustomAction table](customaction-table.md) can have the product code GUID in the Source field and "REMOVE=ALL" in the Target field. The two custom actions need to be authored in the action sequence table with mutually exclusive conditions. For example, the custom action that installs the product can have "NOT Installed" in its Condition field and the custom action removes the concurrent installation can have REMOVE="ALL" in its Condition field.

There is no method for querying a package for its cost. This makes the costing of a concurrent installations difficult. Rows must be added to the [ReserveCost table](reservecost-table.md) to indicate the folders and worst-case costs of the component associated with the concurrent install.

The only [Custom Action Return Processing Options](custom-action-return-processing-options.md) available with concurrent installation actions are none (+0) or **msidbCustomActionTypeContinue** (+64).

Note that a parent installation cannot call its own package as a concurrent installation action.

Note that if a per-machine installation attempts to run a per-user concurrent installation, the installer registers the parent installation as per-user by default. This can cause the installer to incorrectly remove the application because the installer attempts to uninstall the application per-machine when it is actually registered as per-user. To force the state of a concurrent installation to track the state of its parent installation, enter ALLUSERS="\[ALLUSERS\]" in the Target column of the [CustomAction table](customaction-table.md). In this case, the concurrent installation is per-machine if the parent is per-machine, and the concurrent installation is per-user if the parent is per-user.

Developers should note the following warnings when authoring concurrent installations.

-   Concurrent installations cannot share components.
-   An administrative installation cannot also contain a concurrent installation.
-   Patching and upgrading may not work with concurrent installations.
-   The installer may not properly cost a concurrent installation.
-   Integrated ProgressBars cannot be used with concurrent installations.
-   Resources that are to be advertised cannot be installed by the concurrent installation.
-   A package that performs a concurrent installation of an application should also uninstall the concurrent application when the parent product is uninstalled.

To prevent a package from ever being installed as a concurrent installation, add either of the following conditional statements to the [LaunchCondition](launchcondition-table.md) table. This prevents the package from ever being installed by a concurrent installation action run by another installation. This does not prevent the package from being removed by the [RemoveExistingProducts](removeexistingproducts-action.md) action. See also the [**ParentOriginalDatabase**](parentoriginaldatabase.md) property and [**ParentProductCode**](parentproductcode.md) property.

``` syntax
"Not ParentProductCode"
```

``` syntax
"Not ParentOriginalDatabase"
```

 

 



