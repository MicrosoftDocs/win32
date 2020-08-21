---
title: About the User Interfaces of Active Directory Domain Services
description: Administrators and users must be able to view and modify directory service objects in Microsoft Active Directory Domain Services from a user interface.
ms.assetid: b6eec599-ebb3-40af-a4a2-059755285854
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# About the User Interfaces of Active Directory Domain Services

Administrators and users must be able to view and modify directory service objects in Microsoft Active Directory Domain Services from a user interface. Administrators manage the Active Directory server using different Microsoft Management Console (MMC) snap-ins, specifically, the Active Directory Domain Services Users and Computers, Active Directory Domain Services Sites and Services, Active Directory Domain Services Domains and Trusts, and Active Directory Domain Services Schema Manager snap-ins. The end user, if granted appropriate permissions, can also use the Active Directory MMC snap-ins to view directory objects. The Windows shell can also be used to view directory objects. The Windows shell enables users to browse objects stored in the directory from either the directory item in My Network Places on the desktop or through the search dialogs available in the Start menu.

Active Directory Domain Services support a user interface that adapts to meet the needs of administrators and end users. Active Directory Domain Services enable you to extend the user interface that represents existing object classes as well as new classes added to the schema. The following elements can be used to control or extend the UI for each class defined in the schema:

-   [Property Pages for Use with Display Specifiers](property-pages-for-use-with-display-specifiers.md)
-   [Context Menus for Use with Display Specifiers](context-menus-for-use-with-display-specifiers.md)
-   [Class and Attribute Display Names](class-and-attribute-display-names.md)
-   [Object Creation Wizards](object-creation-wizards.md)
-   [Class Icons](class-icons.md)
-   [Viewing Containers as Leaf Nodes](viewing-containers-as-leaf-nodes.md)

Beginning with Windows 2000, the system provides COM objects that implement common dialog boxes for working with directory objects. These dialog boxes provide a common UI without having to reimplement these dialog boxes.

-   [Directory Object Picker](directory-object-picker.md)
-   [Domain Browser](domain-browser.md)
-   [Container Browser](container-browser.md)

Active Directory administrative snap-ins, context menus, and property pages can be extended using MMC extension snap-ins. Other MMC extensions, such as taskpads, namespace items, control bars, and toolbars can also be implemented. For more information, see [Extending the Active Directory Administrative Snap-ins](/previous-versions/windows/desktop/mmc/extending-the-active-directory-administrative-snap-ins).

 

 