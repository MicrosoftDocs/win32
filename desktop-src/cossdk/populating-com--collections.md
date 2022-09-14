---
description: Populating COM+ Collections
ms.assetid: df86cbab-dcb8-46ac-aebf-8516276b6e81
title: Populating COM+ Collections
ms.topic: article
ms.date: 05/31/2018
---

# Populating COM+ Collections

After you have retrieved a collection and before you can work directly with the items it contains, you must populate the collection by using the [**Populate**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-populate) method. This fetches data for the collection's contents from the COM+ catalog.

It is important to understand that whenever you use the COMAdmin objects to manipulate items or data in collections, you are really working on transiently cached data; you are not working directly with the persisted catalog. Nothing that you do with a collection or any of its items is reflected on the catalog until you call [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) on the collection. For more detail, see [Saving or Discarding Changes](saving-or-discarding-changes.md).

Any subsequent calls to [**Populate**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-populate), prior to calling [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), has the effect of discarding pending changes to all items in the collection. **Populate** always populates the cache you're working in with whatever data is persisted on the underlying catalog data store.

## Related topics

<dl> <dt>

[Navigating the COM+ Collection Hierarchy](navigating-the-com--collection-hierarchy.md)
</dt> <dt>

[Querying for Available Related Collections](querying-for-available-related-collections.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> </dl>

 

 



