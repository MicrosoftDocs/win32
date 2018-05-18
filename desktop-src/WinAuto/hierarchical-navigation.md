---
title: Hierarchical Navigation
description: Often clients must move between objects based on their parent-child relationships. For example, a client might already have information about a toolbar control, but not have information about the buttons contained within it.
ms.assetid: '7adf803c-140a-4f7d-8dc5-71abca706800'
---

# Hierarchical Navigation

Often clients must move between objects based on their parent-child relationships. For example, a client might already have information about a toolbar control, but not have information about the buttons contained within it.

The [**IAccessible**](iaccessible.md) interface exposes the hierarchical relationships between objects. Clients can navigate from a parent object to its children or from a child object to its parent by calling [**IAccessible::get\_accParent**](iaccessible-iaccessible--get-accparent.md) or [**IAccessible::get\_accChild**](iaccessible-iaccessible--get-accchild.md).

 

 




