---
title: When to Extend the Schema
description: Extend the schema only if no existing object class fulfills the requirements of your application. Extending the schema is a complex operation; schema changes are replicated to every domain controller in the enterprise forest. Consider this carefully.
ms.assetid: 92231f31-d2af-4c3b-981e-e55cc478899d
ms.tgt_platform: multiple
keywords:
- When to Extend the Schema AD
- schema AD , when to extend
ms.topic: article
ms.date: 05/31/2018
---

# When to Extend the Schema

Extend the schema only if no existing object class fulfills the requirements of your application. Extending the schema is a complex operation; schema changes are replicated to every domain controller in the enterprise forest. Consider this carefully.

The schema can be extended in three ways:

-   Derive a new subclass from an existing class - the subclass has all of the attributes of the superclass and any attributes you specify. Derive from an existing class:
    -   When the existing class requires additional attributes, but otherwise is acceptable.
    -   When the ability to transform existing objects of the class into a new class is not required. It is not possible to add a subclass to an existing object.
    -   To use the existing Directory Manager snap-in to manage the extended attributes of the objects.
-   Add attributes to an existing class and/or add parent objects for the class. When adding multiple attributes, perform this operation in a structured manner by defining an auxiliary class and adding that auxiliary class to the existing class.
-   Modification of an existing class is required when an application requires the ability to extend existing objects of the class. For example, to add application-specific data to the User object, extend the class User normally, because you must handle existing Users and not just special Users created by your application.
-   Create a new class with the required attributes. Create a new class; that is, a class derived from "Top" when no existing class fulfills the operational requirements.

When you subclass an existing class, any user interface items associated to the original class will not be inherited by the subclass. For example, if you subclass a user object, the property pages and menu items associated to user are not inherited. For this reason, it is preferable to extend an existing object or create an auxiliary class rather than create a subclass.

Whether you subclass an existing class or modify an existing class, you will want to extend tools such as the Active Directory Users and Computers snap-in to manage the extended attributes of the objects. For more information, see [Extending the User Interface for Directory Objects](extending-the-user-interface-for-directory-objects.md).

 

 




