---
description: In certain cases, authors may decide they need to break the rules for creating components as discussed in Organizing Applications into Components and Changing the Component Code.
ms.assetid: 487b6a00-77eb-4c51-8e32-46bcd4493df8
title: What happens if the component rules are broken?
ms.topic: article
ms.date: 05/31/2018
---

# What happens if the component rules are broken?

In certain cases, authors may decide they need to break the rules for creating components as discussed in [Organizing Applications into Components](organizing-applications-into-components.md) and [Changing the Component Code](changing-the-component-code.md). Authors need to be aware of the possible consequences of doing this and must otherwise guarantee that their components are never installed where they can damage other applications or components on the user's system.

The following list describes ways that authors sometimes break the recommended component rules and the possible consequences.

An author adds resources to a component without the changing the component code.

-   Products installed with the old component have no information about the added resources in their installation database.
-   If both a new product that has the added resources and an old product are installed on the same computer, the resources can be left behind if the new product is uninstalled first.
-   An old product without the added resources cannot repair the newer version of the component. Reinstalling the old product does not restore the added resources.

An author removes resources from a component without changing the component code.

-   Products installed with the new component have no information about the removed resources in their installation database.
-   If both an old product, having the resource information, and a new product are installed on the same computer, the resources can be left behind if the old product is uninstalled first.
-   A new product with the removed resources cannot repair the older version of the product. Reinstalling the new product does not restore the removed resources.

An author includes a file that is incompatible with previous versions without changing the component code.

If an incompatible file is included in a component without changing the component code, [default file versioning](default-file-versioning.md) causes the installer to overwrite the original file with the more recent incompatible file. This can damage old products needing the original file. It may also prevent the installer from repairing the old product because the version of a component's key path file determines the version of the component. If a newer version of the key path file is already installed, the installer does not install an older version of the component. For more information, see [File Versioning Rules](file-versioning-rules.md). In this case, the new product must be removed before the old product can be reinstalled.

-   [Default file versioning](default-file-versioning.md) causes the installer to overwrite the original file with the more recent incompatible file.
-   Old products that need the original file are damaged.
-   It may also prevent the installer from repairing the old product because the version of a component's key path file determines the version of the component. If a newer version of the key path file is already installed, the installer does not install the older version of the component. For more information, see [File Versioning Rules](file-versioning-rules.md). In this case, the new product must be removed before the old product can be reinstalled.

An author includes the same resource in two different components.

If two components have a resource under the same name and location and both components are installed into the same folder, then the removal of either component removes the common resource, which damages the remaining component.

-   Uninstalling either component removes the resource and breaks the other component.
-   The component reference-counting mechanism is damaged.

 

 



