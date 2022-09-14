---
title: Recommendations for Schema Extension Applications
description: This topic includes recommendations for schema extension applications.
ms.assetid: 615e927e-a113-4557-b354-55a208a649eb
ms.tgt_platform: multiple
keywords:
- Recommendations for Schema Extension Applications AD
ms.topic: article
ms.date: 05/31/2018
---

# Recommendations for Schema Extension Applications

In addition to the prerequisites, the following best practices are recommended for schema extension applications:

-   Find the schema master. Bind to the schema on the DC that is the schema master. Avoid unnecessarily changing the schema master role between DCs. To bind to the schema container on the schema master. For more information, see [Prerequisites for Installing a Schema Extension](prerequisites-for-installing-a-schema-extension.md).
-   Before performing any action, check the **allowedChildClassesEffective** property of the schema container to verify that you can create attributes and/or classes. If **attributeSchema** and **classSchema** are not values in that property, you do not have sufficient rights to add attributes or classes to the schema. For more information, see [Example Code for Checking for Rights to Create Schema Objects](example-code-for-checking-for-rights-to-create-schema-objects.md).
-   Ensure that the Schema Update Allowed is set appropriately in the registry of the schema master. To create or set this value, restore it to its original state as part of your application clean-up routine. For more information about checking and setting this value, see [Enabling Schema Changes at the Schema Master](enabling-schema-changes-at-the-schema-master.md).
-   Before adding attributes or classes, be sure that they do not already exist. If they do exist, verify that they are the same attributes or classes you are adding and not an attribute or class created by someone with different syntax and properties that are incompatible with your attributes or classes.

    For attributes, query for **cn**, **attributeID**, **governsID**, **lDAPDisplayName**, and **schemaIDGUID** to ensure they are not already used. If you add a set of linked attributes (one forward link, one back link), ensure that the **linkID**s are not already used. Query for **governsID** because the object identifier (OID) must be unique among attributes and classes.

    For classes, query for **cn**, **governsID**, **attributeID**, **lDAPDisplayName**, and **schemaIDGUID** to ensure they are not already used. Query for **attributeID** because the OID must be unique among classes and attributes.

    For more information about checking for naming collisions, see [Example Code for Detecting Schema Naming Collisions](example-code-for-detecting-schema-naming-collisions.md).

    If attributes or classes exist that conflict with your new attributes or classes, your application should not apply your schema changes.

-   If such a collision exists, your application should not apply your schema changes. The schema administrator may need to resolve the collision and then run your application again. Alternatively, a different **lDAPDisplayName** could be used; however, any applications using the attribute or object must be aware of that change. To help avoid OID collisions, obtain an OID from an ISO name registration authority.
-   If your application is dependent on attributes or classes that it has added, update the schema cache before adding the new attributes or classes that are dependent on those attributes or classes. Be aware that the **schemaUpdateNow** operational attribute is synchronous. That is, the [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put) method call will block until the schema cache is updated. When the call returns, the schema cache has been updated and the new attributes and/or classes are accessible.

    For more information about how to update the schema cache, see [Example Code for Updating the Schema Cache](example-code-for-updating-the-schema-cache.md).

 

 