---
title: Containers and Leaves
description: Active Directory Domain Services contain a hierarchy of objects in which every object instance, except the root of the directory hierarchy, is contained by some other object.
ms.assetid: ef17e84c-6c7f-4ebe-a904-fead6c27518d
ms.tgt_platform: multiple
keywords:
- containers and leaves Active Directory
- leaf Active Directory
- container Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Containers and Leaves

Active Directory Domain Services contain a hierarchy of objects in which every object instance, except the root of the directory hierarchy, is contained by some other object. The structure of this hierarchy is more flexible than a file system of directories and files. Instead, rules, in the [Active Directory Schema](active-directory-schema.md), determine which object classes can contain instances of which other object classes. For example, the default schema definition of the [**User**](/windows/desktop/ADSchema/c-user) object class includes the [**Organizational-Unit**](/windows/desktop/ADSchema/c-organizationalunit) and [**Container**](/windows/desktop/ADSchema/c-container) object classes as possible superiors; that is, possible parent-objects or containers of a **User** object instance. This means that an **Organizational-Unit** object can contain a **User** object, but a **User** object cannot contain another **User** object, unless the schema definition of the **User** class is changed.

Except for schema objects, that is, the [**classSchema**](/windows/desktop/ADSchema/c-classschema) or [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) objects that define the classes and attributes that can exist in a server forest, any object in Active Directory Domain Services may be a container. Specifically, any object class that appears in the [**possSuperiors**](/windows/desktop/ADSchema/a-posssuperiors) or [**systemPossSuperiors**](/windows/desktop/ADSchema/a-systemposssuperiors) attribute of an object class definition is potentially a container. For more information about containers of a predefined object class, see [Active Directory Domain Services Reference](active-directory-domain-services-reference.md). You can bind programmatically to the abstract schema and use the [**IADsClass::get\_Containment**](/windows/desktop/api/iads/nn-iads-iadsclass) or [**IADsClass::get\_PossibleSuperiors**](/windows/desktop/api/iads/nn-iads-iadsclass) methods to get the classes that a given class can contain or be contained by. For more information, see [Reading the Abstract Schema](reading-the-abstract-schema.md). You can also read the [**possibleInferiors**](/windows/desktop/ADSchema/a-possibleinferiors) attribute of any object instance to determine the object classes that the object can contain. Be aware that **possibleInferiors** is a constructed attribute, which means it is calculated from the **possSuperiors**/**systemPossSuperiors** values of the other class definitions and is not actually stored in the directory.

Be aware that the Active Directory Schema defines a [**Container**](/windows/desktop/ADSchema/c-container) class. As discussed previously, an object is not required to be an instance of the **Container** class to be a container. There is also a [**Leaf**](/windows/desktop/ADSchema/c-leaf) class, and although subclasses of this class are typically not containers, there is no reason why they cannot be.

Finally, you can set a flag on the display specifier associated with an object class to indicate that user interfaces should always display instances of the class as leaves rather than containers. This helps prevent the user interface from being cluttered by too many containers. For more information, see [Viewing Containers as Leaf Nodes](viewing-containers-as-leaf-nodes.md).

 

 