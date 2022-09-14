---
description: Querying for Available Related Collections
ms.assetid: 9c7d2a01-5dc3-4d35-b938-f1d0525a8286
title: Querying for Available Related Collections
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Available Related Collections

If you are writing a general-purpose administration tool, it is likely that you will need to write routines for navigating the entire collection hierarchy. To support this, COM+ has a facility that enables you to dynamically query for the related collections that are available from any given collection.

The [**RelatedCollectionInfo**](relatedcollectioninfo.md) collection is available from any collection that you might be holding and contains an item for each available related collection. You can enumerate through these items to determine whether a given collection is available.

You can get the [**RelatedCollectionInfo**](relatedcollectioninfo.md) collection from any collection you are holding by using the [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) method on the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, leaving the second parameter blank where you would normally specify a parent item's Key property.

## Related topics

<dl> <dt>

[Navigating the COM+ Collection Hierarchy](navigating-the-com--collection-hierarchy.md)
</dt> <dt>

[Populating COM+ Collections](populating-com--collections.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> </dl>

 

 



