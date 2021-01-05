---
description: The COMAdmin objects offer a simple object model that provides you with access to the COM+ catalog.
ms.assetid: 84cee7a7-f7a6-41a0-afd5-fae56365612e
title: Overview of the COMAdmin Objects
ms.topic: article
ms.date: 05/31/2018
---

# Overview of the COMAdmin Objects

The COMAdmin objects offer a simple object model that provides you with access to the COM+ catalog. In doing so, they serve to model all the functionality provided by the Component Services administrative tool. Whenever you do any kind of COM+ administration, you are interacting with the COM+ catalog. For a description of the catalog, see [Accessing the COM+ Catalog](accessing-the-com--catalog.md).

The information you obtain either from the Component Services administrative tool or by using the COMAdmin objects is structured similarly, and the actions you perform in either context are analogous. The basic correlation between using the Component Services snap-in and programmatic administration is that folders in the console tree of the snap-in correspond to collections in the COM+ catalog. That is, just as each folder in the snap-in contains items all of a kind; for example, **COM+ Applications** holds installed COM+ applications—each collection in the COM+ catalog holds items of a uniform kind. Further, just as each item in a folder has properties that you can set on a property sheet, each item in a collection exposes properties that you can set.

To enable you to configure objects within this structure, the COMAdmin objects provide you with the means to do the following:

-   Access the COM+ catalog
-   Access collections in the catalog
-   Access items in collections
-   Access properties on the items in the collections

To support these actions, the COMAdmin Library provides the following three classes:

-   [**COMAdminCatalog**](comadmincatalog.md), which represents the catalog itself.
-   [**COMAdminCatalogCollection**](comadmincatalogcollection.md), which represents any collection.
-   [**COMAdminCatalogObject**](comadmincatalogobject.md), which represents any item in a collection.

For fuller descriptions of these classes, see [Summary Description of the COMAdmin Classes](summary-description-of-the-comadmin-classes.md) in this section.

To get a quick idea of typical actions you perform in programmatic administration, see [Introductory Example Using the COM+ Administration Catalog](introductory-example-using-the-com--administration-catalog.md).

## Related topics

<dl> <dt>

[COM+ Administration Operations Within Transactions](com--administration-operations-within-transactions.md)
</dt> <dt>

[Handling COM+ Administration Errors](handling-com--administration-errors.md)
</dt> <dt>

[Introductory Example Using the COM+ Administration Catalog](introductory-example-using-the-com--administration-catalog.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> <dt>

[Setting Properties and Saving Changes to the COM+ Catalog](setting-properties-and-saving-changes-to-the-com--catalog.md)
</dt> </dl>

 

 



