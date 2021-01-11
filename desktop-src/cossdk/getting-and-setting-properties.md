---
description: Getting and Setting Properties
ms.assetid: 259612e7-70df-4f0f-90bc-766008dfdce7
title: Getting and Setting Properties (Component Services)
ms.topic: article
ms.date: 05/31/2018
---

# Getting and Setting Properties (Component Services)

Before you can read or write particular properties exposed by an item in a collection, you must take the following steps:

1.  Retrieve the collection.
2.  Populate the collection to read in data for it from the COM+ catalog.
3.  Retrieve the specific item in the collection, representing it with an object from the [**COMAdminCatalogObject**](comadmincatalogobject.md) class.

For an example that illustrates these steps, see [Navigating the COM+ Collection Hierarchy](navigating-the-com--collection-hierarchy.md).

Because the particular properties exposed can vary depending on what the item represents; that is, an item representing a component has different properties than one representing a COM+ application. Set any of these properties using a single generic property, the Value property, on [**COMAdminCatalogObject**](comadmincatalogobject.md).

The Value property enables you to get or set any specific named property exposed by an item, returning a value for a named property when getting, and taking a name and value when setting.

No changes are actually recorded to the COM+ catalog until you explicitly save changes using the [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) method on the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object. Pending changes for all properties on all items in a given collection are saved all at once. For details, see [Saving or Discarding Changes](saving-or-discarding-changes.md).

Not all changes that you make will be accepted. The COM+ catalog enforces some coherency logic to ensure that you configure things in a reasonable way. Additionally, when you change some properties, others might change automatically by the same coherency logic. These effects show up when you attempt to save changes.

> [!Note]  
> It is possible for you to be in contention with another writer to the COM+ catalog. Between calls to [**Populate**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-populate) and [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) for a given collection, you do not have a lock on any of that data in the catalog. Multiple parties may simultaneously be configuring items in a given collection and could be contending when they save changes. This means that someone else might change settings on an object before or after you do, either running some kind of program using the COMAdmin objects or using the Component Services administrative tool, either locally or remotely. The general rule with writing objects on the catalog is that all properties on an object are written at once. That is, the last writer wins—the object is saved in the catalog precisely as the last writer configured it.

 

## Related topics

<dl> <dt>

[Interdependencies Between Properties](interdependencies-between-properties.md)
</dt> <dt>

[Querying for Available Properties](querying-for-available-properties.md)
</dt> <dt>

[Saving or Discarding Changes](saving-or-discarding-changes.md)
</dt> </dl>

 

 



