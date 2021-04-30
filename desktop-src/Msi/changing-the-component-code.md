---
description: When specifying the components for an installation, package authors should follow the general rules for component organization described in Organizing Applications into Components.
ms.assetid: 7cf322e9-c49a-40a8-be4e-ab03ecba1c1f
title: Changing the Component Code
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Component Code

When specifying the [components](windows-installer-components.md) for an installation, package authors should follow the general rules for component organization described in [Organizing Applications into Components](organizing-applications-into-components.md). Authors may need to introduce new components or modify existing components. If the addition, removal, or modification of resources effectively creates a new component, then the component code must also be changed.

## Creating a New Component

Introduce a new component and assign it a unique component code when making any of the following changes:

-   Any change that has not been shown by testing to be compatible with previous versions of the component. In this case, you must also change the name or target location of every resource in the component.
-   A change in the name or target location of any file, registry key, shortcut, or other resource in the component. In this case, you must also change the name or target location of every resource in the component.
-   The addition or removal of any file, registry key, shortcut, or other resource from the component. In this case, you must also change the name or target location of every resource in the component.
-   Recompiling a 32-bit component into a 64-bit component.

When introducing a new component, authors need to do one of the following to ensure that the component does not conflict with any existing components:

-   Change the name or target location of any resource that may be installed under the same name and target location by another component.
-   Otherwise guarantee that the new component is never installed into the same folder as another component which has a resource under a common name and location. This includes localized versions of files with the same file name. For more information, see [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md).
-   When changing the component code of an existing component, also change the name or target location of every file, registry key, shortcut, and other resource in the component.

### Creating a New Version of a Component

A new version of a component is assigned the same component code as another existing component. Modifying a component without changing the component code is only optional in the following cases:

-   The changes to the component have been proven by testing to be backward compatible with all previous versions of the component.
-   The author can guarantee that the new version of the component will never be installed on a system where it would conflict with previous versions of the component or applications requiring a previous version. For more information, see [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md).

The component code of a new version of a component must not be changed when it would result in two components sharing resources, such as registry values, files, or shortcuts.

 

 



