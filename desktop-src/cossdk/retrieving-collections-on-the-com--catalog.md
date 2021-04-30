---
description: Retrieving Collections on the COM+ Catalog
ms.assetid: 7cd5c491-6c85-410f-845b-c2f7b4f2a560
title: Retrieving Collections on the COM+ Catalog
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Collections on the COM+ Catalog

Data on the COM+ catalog is stored within a hierarchy of collections. In the Component Services administrative tool, many of these collections appear as folders in the console tree. Collections that don't appear as folders can be accessed only programmatically. Collections serve as containers for items. The items in a given collection are all of a consistent type; that is, they all represent the same kind of element, and there can be an arbitrary number of items in a collection. For example, the [**Applications**](applications.md) collection contains an item for each COM+ application that is installed on the machine. This collection appears in the administrative tool as the **COM+ Applications** folder.

The collections occur in a hierarchical structure because the elements they contain follow an innate order of inclusion. For example, because components are installed into a COM+ application, the [**Components**](components.md) collection is logically subsumed under the [**Applications**](applications.md) collection. More particularly, to hold the components installed into that particular application, there is a distinct **Components** collection for each item in the **Applications** collection.

You must get a collection on the catalog whenever you want to retrieve an item and set properties on it. In the general case, you need to step through several collections to get to the element you want. For the procedure for doing this, see [Navigating the COM+ Collection Hierarchy](navigating-the-com--collection-hierarchy.md).

After you have retrieved a collection and before you can work directly with the items it contains, you must populate the collection, which fetches data for the collection's contents from the COM+ catalog. For details, see [Populating COM+ Collections](populating-com--collections.md).

Additionally, there is a facility you can use that enables you to dynamically query to see what related collections are available from a given collection you are holding. For details, see [Querying for Available Related Collections](querying-for-available-related-collections.md).

## Related topics

<dl> <dt>

[COM+ Administration Operations Within Transactions](com--administration-operations-within-transactions.md)
</dt> <dt>

[Handling COM+ Administration Errors](handling-com--administration-errors.md)
</dt> <dt>

[Introductory Example Using the COM+ Administration Catalog](introductory-example-using-the-com--administration-catalog.md)
</dt> <dt>

[Overview of the COMAdmin Objects](overview-of-the-comadmin-objects.md)
</dt> <dt>

[Setting Properties and Saving Changes to the COM+ Catalog](setting-properties-and-saving-changes-to-the-com--catalog.md)
</dt> </dl>

 

 



