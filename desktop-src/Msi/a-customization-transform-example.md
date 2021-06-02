---
description: This example illustrates how a customization transform may be used to disable features and add new resources.
ms.assetid: 028b1d01-3b66-4640-98f9-ca33f90ca516
title: A Customization Transform Example
ms.topic: article
ms.date: 05/31/2018
---

# A Customization Transform Example

This example illustrates how a customization transform may be used to disable features and add new resources.

An administrator can permanently disable a feature by using a customization transform to enter a 0 into the Level column of the [Feature table](feature-table.md). The application of the customization transform then prevents the installation and display of that feature even if the user selects a complete installation using the UI or by setting the [**ADDLOCAL**](addlocal.md) property to ALL on the command line. For a discussion of installation level, see [Feature table](feature-table.md) and [**INSTALLLEVEL**](installlevel.md) property.

The resources needed to customize an application can be deployed by using a customization transform to add one or more new components. The transform must add one or more new features to contain these new components. For the rules that should be followed when deploying resources, such as files, registry keys, or shortcuts, see [Using Transforms to Add Resources](using-transforms-to-add-resources.md).

This example illustrates how to create a [transform](transforms.md) to customize the installation of the application described in [An Installation Example](an-installation-example.md). The original installation package installs all the features of the sample application, including the feature Gate, which enables users to view admissions information for the Red Park Arena. Some groups of users only need the application features that give event scheduling information, and do not need the Gate feature. These groups also need to get a special phone list. The transform must therefore do two things: 1) customize the installation so that this group only receives the application features they need and 2) provide the resources needed for the new phone list.

An example of a minimal user interface for this sample is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) as the file Uisample.msi. If you have the SDK, you have access to all the tools and data necessary to reproduce the sample installation package, user interface, and customization transform.

The customization transform has the following specifications:

-   The customization transform is embedded inside the MNP2000.msi file to guarantee that it is always available with the installation database.
-   Installing MNP2000.msi with the customization transform does not install the Gate feature, child features of the Gate feature, or any of the components of the Gate feature, even if the user selects the Complete type of installation.
-   Other applications may share some or all of the components of the Gate feature. The installation packages of these applications may install all their components on the user's computer.
-   Removing MNP2000.msi with the customization transform does not remove any of the Gate components that have been installed by other applications.
-   Installing MNP2000.msi with the customization transform also installs a new top level feature, Phone\_List, and a new component, phone, which requires the installation of the resource, Phone.txt. The user accesses the Phone\_List feature using a shortcut in the Menu directory.

[Continue](customizing-an-original-database.md)

 

 



