---
title: Dynamically Linked Auxiliary Classes
description: A dynamically linked auxiliary class is a class that is attached to an individual object, rather than to an object class.
ms.assetid: 10530a3c-89fc-4ff0-a0b7-1c9a27659003
ms.tgt_platform: multiple
keywords:
- Dynamically Linked Auxiliary Classes AD
ms.topic: article
ms.date: 05/31/2018
---

# Dynamically Linked Auxiliary Classes

A dynamically linked auxiliary class is a class that is attached to an individual object, rather than to an object class. Dynamic linking enables you to store additional attributes with an individual object without the forest-wide impact of extending the schema definition for an entire class. For example, an enterprise could use dynamic linking to attach a sales-specific auxiliary class to the user objects of its sales people, and other department-specific auxiliary classes to the user objects of employees in other departments.

Dynamic linking is not complex: add the name of the auxiliary class to the values of an object's **objectClass** attribute. If the auxiliary class has any mandatory attributes (**mustHave** or **systemMustHave**), you must set them at the same time. For more information and a code example, see [Adding an Auxiliary Class to an Object Instance](adding-an-auxiliary-class-to-an-object-instance.md).

To remove a dynamically linked auxiliary class, clear the values of all attributes from the auxiliary class, and then remove the name of the auxiliary class from the **objectClass** attribute of the object.

If you dynamically add an auxiliary class that is a subclass of another auxiliary class, both auxiliary classes are added to the target object. However, removing the child auxiliary class does not remove its parent; each class must be explicitly removed.

 

 




