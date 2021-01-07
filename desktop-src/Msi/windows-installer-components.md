---
description: A component is a piece of the application or product to be installed.
ms.assetid: f1c9696d-3267-44be-a904-ab26250fae2e
title: Windows Installer Components
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer Components

A component is a piece of the application or product to be installed. Examples of components include single files, a group of related files, COM objects, registration, registry keys, shortcuts, resources, libraries grouped into a directory, or shared pieces of code such as MFC or DAO.

The installer service installs or removes a component as a single coherent piece. It tracks every component by the respective component ID GUID specified in the ComponentId column of the [Component table](component-table.md).

> [!Note]  
> Two components that share the same component ID are treated as multiple instances of the same component regardless of their actual content. Only a single instance of any component is installed on a user's computer. Several features or applications may therefore share some components.

 

Because components are commonly shared, the author of an installation package must follow strict rules when specifying the components of a feature or application. This is essential for the correct operation of the Windows Installer reference-counting mechanism. For more information, see [Organizing Applications into Components](organizing-applications-into-components.md).

In brief, these rules are:

-   Each component must be stored in a single folder.
-   No file, registry entry, shortcut, or other resources should ever be shipped as a member of more than one component. This applies across products, product versions, and companies.

For more information about using components, see

-   [Installing a Missing Component](installing-a-missing-component.md)
-   [Installing Permanent Components, Files, Fonts, Registry Keys](installing-permanent-components-files-fonts-registry-keys.md)
-   [Using Qualified Components](using-qualified-components.md)
-   [Using Transitive Components](using-transitive-components.md)
-   [Working with Features and Components](working-with-features-and-components.md)
-   [Authoring a Large Package](authoring-a-large-package.md)
-   [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md)
-   [Searching for a Broken Feature or Component](searching-for-a-broken-feature-or-component.md)
-   [Publishing Products, Features, and Components](publishing-products-features-and-components.md)

 

 



