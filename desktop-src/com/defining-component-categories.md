---
title: Defining Component Categories
description: Defining Component Categories
ms.assetid: 2d67a998-5200-4285-bd99-48cf59683569
ms.topic: article
ms.date: 05/31/2018
---

# Defining Component Categories

The author of a component category definition creates a unique GUID (the CATID) that is published along with the definition. Other parties know the definition of this type and can make use of its supported classes accordingly. Like the method signature of an interface, a category's semantics should not be modified after being installed. It is better to maintain backward compatibility of the category by introducing a new category identifier with revised semantics.

Because interface identifiers (IID) and component category identifiers (CATID) exist in different namespaces, it seems as if it would be possible to use the same GUID for both an IID and a CATID. However, since IIDs are often used for the CLSID of the interface's proxy/stub server, there is the potential for conflict. Therefore, do not use the same GUID for an IID and CATID.

## Related topics

<dl> <dt>

[Associating Icons with a Category](associating-icons-with-a-category.md)
</dt> <dt>

[Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
</dt> <dt>

[Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
</dt> <dt>

[Default Classes and Associations](default-classes-and-associations.md)
</dt> <dt>

[The Component Categories Manager](the-component-categories-manager.md)
</dt> </dl>

 

 




