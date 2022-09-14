---
description: Each item in a collection exposes properties.
ms.assetid: d9af57ea-c5b3-4017-bdc2-e43b86b3ddcd
title: Editing Properties in the COM+ Catalog
ms.topic: article
ms.date: 05/31/2018
---

# Editing Properties in the COM+ Catalog

Each item in a collection exposes properties. These properties serve to hold configuration data for whatever element the item represents. In the Component Services administrative tool, these properties appear on a property page that you access by right-clicking an item in a folder.

Because the items in a given collection all represent the same kind of thing, those items expose a set of properties that is consistent across the collection. For example, the [**Applications**](applications.md) collection exposes a Name property, an AppID property, and so forth. This is analogous to how each application in the Component Services administrative tool has a consistently structured property page available for it. For a list of properties available to the **Applications** collection, see **Applications**. For a list of properties available to the [**Components**](components.md) collection, see **Components**.

For a complete list of properties exposed by items in each collection, see [COM+ Administration Collections](com--administration-collections.md).

You represent an item in a collection by using an object created from the [**COMAdminCatalogObject**](comadmincatalogobject.md) class. This object enables you to set and get any of the properties exposed by the item. When setting properties, it is also possible that you might be contending with another writer to the COM+ catalog. For more information, see [Getting and Setting Properties](getting-and-setting-properties.md).

After you have set properties, no changes are actually committed until you explicitly save changes. For more information, see [Saving or Discarding Changes](saving-or-discarding-changes.md).

When you save changes, the COM+ catalog enforces some configuration logic to ensure that you don't set things to incompatible configurations. It also changes some properties for you when you explicitly change certain other properties. For more information, see [Interdependencies Between Properties](interdependencies-between-properties.md).

Additionally, COM+ has a facility that enables you to dynamically query to see what properties are available for the items in a given collection. For details, see [Querying for Available Properties](querying-for-available-properties.md).

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

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> </dl>

 

 



