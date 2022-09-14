---
title: Simple Elements
description: A simple element is a UI element that shares an IAccessible object with other elements and relies on that IAccessible object (typically its parent) to expose its properties.
ms.assetid: 3f6bd992-4e0a-4dba-b6e9-e70dca77c880
ms.topic: article
ms.date: 05/31/2018
---

# Simple Elements

A *simple element* is a UI element that shares an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object with other elements and relies on that **IAccessible** object (typically its parent) to expose its properties. To differentiate between the elements sharing an **IAccessible** object, the server assigns a unique, positive child identifier to each simple element. This assignment is done on a per-instance-of-interface basis, so the IDs must be unique within that context. Many implementations assign these IDs sequentially, beginning with 1. This scheme does not allow simple elements to have children of their own. Simple elements are also known as *children*.

To be uniquely identified and exposed, a simple element requires an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object and child ID. Therefore, when communicating with an **IAccessible** object, the clients must supply the appropriate child ID. A special identifier, **CHILDID\_SELF**, can be used to refer to the accessible object itself, instead of one of its children.

The [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object shared among simple elements often corresponds to a common parent object in the user interface. For example, system list boxes expose an accessible object for the overall list box and simple elements for each list box item. In this case, the **IAccessible** object for the list box is also the parent or container of the list items.

For more information about accessible objects, see [Accessible Objects](accessible-objects.md).

 

 




