---
description: A typical use for transitive components is to prepare a product to reinstall during a system upgrade.
ms.assetid: 73677573-945f-4646-89d8-93e28f7856fe
title: Using Transitive Components
ms.topic: article
ms.date: 05/31/2018
---

# Using Transitive Components

A typical use for transitive components is to prepare a product to reinstall during a system upgrade. The author of the installation package specifies those components that need to be swapped out during a system upgrade as having the transitive attribute. When the user later upgrades the system, the product must be reinstalled. Upon this reinstall, the installer removes the earlier components and installs the later components, without having to install the entire product.

**To include two transitive components in the installation package**

1.  Include both transitive components in the installation package.
2.  Author both transitive components into the [Component table](component-table.md) the same as regular components. Each transitive component must have its own unique GUID specified in the ComponentId column.
3.  Include the **msidbComponentAttributesTransitive** bit in the Attributes column of the Component table for each transitive component. If this bit is set, the installer reevaluates the value of the statement in the Condition column upon a reinstall.

    If the value was previously False and has changed to True, the installer installs the component.

    If the value was previously True and has changed to False the installer removes the component even if the component has other products as clients.

    > [!Note]  
    > Unless the transitive bit is set, the component remains enabled once installed even if the conditional statement evaluates to False on a subsequent maintenance installation of the product. The conditions must be based only on computer states. Do not use with conditions based on user states or properties set on the command line because this can cause the installer to require a reinstallation of the product on each use by a different user.

     

4.  Enter complementary conditional expressions into the Condition fields of the Control table such that when the condition on the first transitive component changes to False the condition on the second transitive component changes to True. This results in the removal of the first component and installation of the second component upon reinstallation of the application.

A reinstallation of the product is necessary to switch the transitive components. Package authors therefore need to provide users with a method for reinstalling the product and for setting the modes of the [**REINSTALLMODE**](reinstallmode.md) property. There are basically three ways to trigger the reinstallation:

-   Run and configure the reinstallation through the user interface by authoring a package that uses the [*full UI*](f-gly.md).
-   Run the reinstallation from the command line by using **msiexec /f** and select the modes from the list for the **/f** [command line option](command-line-options.md).
-   Have the application call [**MsiReInstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta) or [**MsiReInstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea).

The bit should only be used with conditions based on computer states. Do not use with conditions based on user states or properties set on the command line because this can cause the installer to require a reinstallation of the product on each use by a different user.

> [!Note]
> Unless the Transitive bit in the Attributes column is set for a component, the component remains enabled once installed even if the conditional statement in the Condition column evaluates to False on a subsequent maintenance installation of the product.
> 
> In most cases, if an application includes transitive components, Windows Installer requires the application's source to repair or upgrade the application. In these cases, the system restoration CD-ROM shipped by an original equipment manufacturer does not work and an actual installation source for the application needs to be provided.

 

 

 



