---
description: Windows Installer installs and removes an application or product in parts referred to as components.
ms.assetid: 949d8b8c-8f1a-4fde-9a7d-824d33436e62
title: Organizing Applications into Components
ms.topic: article
ms.date: 05/31/2018
---

# Organizing Applications into Components

Windows Installer installs and removes an application or product in parts referred to as [components](windows-installer-components.md). Components are collections of resources that are always installed or removed as a unit from a user's system. A resource can be a file, registry key, shortcut, or anything else that may be installed. Every component is assigned a unique component code [GUID](guid.md).

Authors of installation packages should only create components, and versions of components, that can be installed and removed without damaging other components. Also, the removal of a component should not leave behind any orphaned resources on the user's computer, such as unused files, registry keys, or shortcuts. To ensure this, authors should adhere to the following general rules when organizing resources into components:

-   Never create two components that install a resource under the same name and target location. If a resource must be duplicated in multiple components, change its name or target location in each component. This rule should be applied across applications, products, product versions, and companies.
-   Note that the previous rule means that two components must not have the same key path file. The key path value points to a particular file or folder belonging to the component that the installer uses to detect the component. If two components had the same key path file, the installer would be unable to distinguish which component is installed. Two components however may share a key path folder.
-   Do not create a version of a component that is incompatible with all previous versions of the component. The component may be shared by other applications, products, product versions, and companies. Instead create a new component.
-   Do not create components containing resources that will need to be installed into more than one directory on the user's system. The installer installs all of the resources in a component into the same directory. It is not possible to install some resources into subdirectories.
-   Do not include more than one COM server per component. If a component contains a COM server, this must be the key path for the component.
-   Do not specify more than one file per component as a target for the **Start** menu or a Desktop shortcut.

When organizing an application into components, package authors may need to add, remove, or modify the resources in an existing installation. In this case, the author must decide whether to provide the resources by introducing a new component or by modifying existing components and changing them into a new version of the component. Because a unique component code must be assigned when a new component is introduced, authors must determine whether their changes require changing the component code. For more information, see [Changing the Component Code](changing-the-component-code.md), [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md), and [Defining Installer Components](defining-installer-components.md).

 

 



