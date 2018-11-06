---
title: Accessible Objects
description: With Microsoft Active Accessibility, UI elements are exposed to clients as Component Object Model (COM) objects.
ms.assetid: ab5669c3-33ce-4d56-a028-e36db25c0b28
ms.topic: article
ms.date: 05/31/2018
---

# Accessible Objects

With Microsoft Active Accessibility, UI elements are exposed to clients as Component Object Model (COM) objects. These *accessible objects* maintain pieces of information, called *properties*, which describe the object's name, screen location, and other information needed by accessibility aids. Accessible objects also provide *methods* that clients call to cause the object to perform some action. Accessible objects that have simple elements associated with them are also called *parents*, or *containers*.

Accessible objects are implemented using Microsoft Active Accessibility's COM-based [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. The **IAccessible** methods and properties enable client applications to get information about UI elements needed by users. For example, [**IAccessible::get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent) returns an interface pointer to an accessible object's parent, and [**IAccessible::accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate) provides a means for clients to get information about other objects within a container.

For more information about how accessible objects and simple elements are related, see [Simple Elements](simple-elements.md).

 

 




