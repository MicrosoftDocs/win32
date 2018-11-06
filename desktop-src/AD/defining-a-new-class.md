---
title: Defining a New Class
description: When you define a new class, specify the legal parent classes of the new class, that is, the classes that can contain instances of your new class.
ms.assetid: 24e346b3-2de2-41f9-a0a2-7b7d8ab5668b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Defining a New Class

When you define a new class, specify the legal parent classes of the new class, that is, the classes that can contain instances of your new class. The legal parent classes are specified in the **possSuperiors** and **systemPossSuperiors** attributes of the new class, as well as in the possible superiors inherited from its superclasses, but not from auxiliary classes.

Be specific when defining the legal parent classes for the new class. Decide where you want users to create instances of your class. For example, specifying "container" as a legal parent will enable the user create instances under any of the standard containers (**container**, **organizationalUnit**, and so on), while specifying "computer" would enable instances to be created only under instances of the **computer** object.

**To Create a Class**

1.  Choose a name for the class. For more information about composing a common-name and an LDAP display name for a new class, see [Naming Attributes and Classes](naming-attributes-and-classes.md).
2.  Obtain an object identifier (OID) for the class. For more information, see [Obtaining an Object Identifier](obtaining-an-object-identifier.md).
3.  Choose a "default object category" for the class. For more information, see [Object Class and Object Category](object-class-and-object-category.md).
4.  Choose an "object class category" for the class. This indicates whether the class is abstract, structural, or auxiliary. For more information, see [Structural, Abstract, and Auxiliary Classes](structural-abstract-and-auxiliary-classes.md).
5.  Create a new **classSchema** object. Many attributes can be set for an **classSchema** object. The following attributes are critical to the definition of a new class:

    -   Classes from which the new class inherits: **subClassOf**, **auxiliaryClass**, and **systemAuxiliaryClass**
    -   Names and identifiers for the new class: **cn**, **lDAPDisplayName**, **adminDisplayName**, **schemaIDGUID**, **governsID**
    -   Possible attributes of the new class: **mustContain**, **systemMustContain**, **mayContain**, **systemMayContain**
    -   Possible parents of the new class: **possSuperiors**, **systemPossSuperiors**
    -   **objectClassCategory**
    -   **defaultObjectCategory**
    -   **defaultHidingValue**
    -   **rDnAttId**
    -   **defaultSecurityDescriptor**
    -   **description** (optional)

    For more information, and descriptions of these attributes, see [Characteristics of Object Classes](characteristics-of-object-classes.md).

    Be aware that the classes specified in **subClassOf**, **possSuperiors**, **systemPossSuperiors**, **auxiliaryClass**, and **systemAuxiliaryClass**, must exist when the new class is written to the directory; otherwise, the **classSchema** object will fail to be added to the directory. Similarly, the attributes specified in **mustContain**, **systemMustContain**, **mayContain**, and **systemMayContain**, must exist or the class creation operation will fail.

6.  Write the new **classSchema** object to the directory.

**To add an attribute to the mayContain property**

1.  Obtain the **classSchema** object for the class to modify.
2.  Add the new attribute to the **mayContain** multi-valued property.
3.  Write the changed **classSchema** object back to the directory.

New attributes can be created at the same time as new classes; the order of creating the new attributes and classes is important. For more information, see [What the Installation Must Do](what-the-installation-must-do.md).

**To add new attributes and new classes at the same time**

1.  Define all of the new attributes first. For more information, see [Defining a New Attribute](defining-a-new-attribute.md).
2.  Update the Schema Cache before defining any new classes. For more information, see [Updating the Schema Cache](updating-the-schema-cache.md).
3.  Create the new classes.
4.  Add the desired attributes to the new classes.
5.  Update the Schema Cache again.

 

 




