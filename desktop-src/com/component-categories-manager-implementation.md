---
title: Component Categories Manager Implementation
description: As the number of available components grows, it becomes increasingly difficult to manage these components. In terms of the interfaces they expose as well as the tasks they perform, many components offer similar functionality.
ms.assetid: c2c67129-bf19-465b-8354-193922aeafaa
ms.topic: article
ms.date: 05/31/2018
---

# Component Categories Manager Implementation

As the number of available components grows, it becomes increasingly difficult to manage these components. In terms of the interfaces they expose as well as the tasks they perform, many components offer similar functionality.

It is often necessary to enumerate the components that can be used in a certain context. Examples of this are the **Insert Object** dialog box used in OLE compound documents and the **Insert Control** dialog box used in OLE controls. These dialog boxes list all components that fulfill (or claim to fulfill) the interface contracts for compound documents or controls. These existing categories (OLE document, OLE control) do not imply an exact interface signature. OLE documents have to expose a certain set of core interfaces (for example, [**IOleObject**](/windows/desktop/api/OleIdl/nn-oleidl-ioleobject) or [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage)) but can also expose additional interfaces such as [**IOleLink**](/windows/desktop/api/OleIdl/nn-oleidl-iolelink).

In the past, components have been tagged by adding a human-readable name ("Insertable", "Control", and so on) as a subkey to the **HKEY\_CLASSES\_ROOT\\CLSID\\{...}** registry key corresponding to the component. This works well for a central definition of categories but risks name collisions when many independent parties define new categories. As in other areas of COM, the solution to providing an extensible namespace lies in the use of globally unique identifiers (GUIDs). Instead of using a human-readable name, a unique number (CATID) is assigned to each category.

Another limitation with the existing categorization is that it is limited to expressing the capabilities of the component itself. Many components require certain capabilities from the containers. When such a component is inserted into a container, the insertion can fail or behave unexpectedly, even though the component fulfills the contracts implied by one of its categories. To enumerate the components that can be used successfully in certain situations, the capabilities of both the component and the container must be considered.

Because of these considerations, the following changes were made to the existing categorization:

-   Categories are indicated by using CATIDs that are globally unique identifiers.
-   Under the **Components** subkey of the **HKEY\_CLASSES\_ROOT\\CLSID** registry key, two separate subkeys, "Implemented Categories" and "Required Categories", were developed. These subkeys contain the lists of CATIDs that are provided by the component or that the container of the component must provide.

To ease managing the component categories, categories are listed in a central place in the registry: **HKEY\_CLASSES\_ROOT\\Component Categories**. This key lists the installed categories both with their CATID and with localized, human-readable names.

For more information, see the following topics:

-   [Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
-   [Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
-   [The Component Categories Manager](the-component-categories-manager.md)
-   [Default Classes and Associations](default-classes-and-associations.md)
-   [Defining Component Categories](defining-component-categories.md)
-   [Associating Icons with a Category](associating-icons-with-a-category.md)

 

 




