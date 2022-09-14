---
title: Linked Attributes (AD DS)
description: Linked attributes are pairs of attributes in which the system calculates the values of one attribute (the back link) based on the values set on the other attribute (the forward link) throughout the forest.
ms.assetid: 31b7e8f5-e46d-4aff-9b17-c8dec7f19bae
ms.tgt_platform: multiple
keywords:
- Linked Attributes AD
- Attributes AD ,linked
ms.topic: article
ms.date: 05/31/2018
---

# Linked Attributes (AD DS)

Linked attributes are pairs of attributes in which the system calculates the values of one attribute (the back link) based on the values set on the other attribute (the forward link) throughout the forest. A back-link value on any object instance consists of the DNs of all the objects that have the object's DN set in the corresponding forward link. For example, "Manager" and "Reports" are a pair of linked attributes, where Manager is the forward link and Reports is the back link. Now suppose Bill is Joe's manager. If you store the DN of Bill's user object in the "Manager" attribute of Joe's user object, then the DN of Joe's user object will show up in the "Reports" attribute of Bill's user object.

A forward link/back link pair is identified by the [**linkID**](/windows/desktop/ADSchema/a-linkid) values of two [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) definitions. The **linkID** of the forward link is an even, positive, nonzero value, and the **linkID** of the associated back link is the forward **linkID** plus one. For example, the **linkID** for "Manager" is 42 and the **linkID** for "Reports" is 43.

The following is a list of guidelines for defining a new pair of linked attributes:

-   The [**linkID**](/windows/desktop/ADSchema/a-linkid) values must be unique among all [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) objects. To avoid conflicts, you should auto-generate the **linkID** by following the instructions in the topic [Obtaining a Link ID](obtaining-a-link-id.md).
-   A back link must have a corresponding forward link, that is, the forward link must exist before a corresponding back link attribute can be created.
-   A back link is always a multi-valued attribute. A forward link can be single-valued or multi-valued. Use a multi-valued forward link when there is a many-to-many relationship.
-   The [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) value of a forward link must be 2.5.5.1, 2.5.5.7, or 2.5.5.14. These values correspond to syntaxes that contain a distinguished name, such as the [**Object(DS-DN)**](/windows/desktop/ADSchema/s-object-ds-dn) syntax.
-   The [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) value of a back link must be 2.5.5.1, which is the [**Object(DS-DN)**](/windows/desktop/ADSchema/s-object-ds-dn) syntax.
-   By convention, back link attributes are added to the [**mayContain**](/windows/desktop/ADSchema/a-maycontain) value of the [**top**](/windows/desktop/ADSchema/c-top) abstract class. This enables the back link attribute to be read from objects of any class because they are not actually stored with the object, but are calculated based on the forward link values.

 

 