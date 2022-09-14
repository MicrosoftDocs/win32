---
description: Querying for Available Properties
ms.assetid: 9acf10cd-19a8-4542-8078-3e4ee275d4d5
title: Querying for Available Properties
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Available Properties

If you are writing a general-purpose administration tool, you most likely will need to write routines for setting properties in full generality. To support this, there is a facility that enables you to dynamically query for the properties that are available for the items in any given collection.

The [**PropertyInfo**](propertyinfo.md) collection is available from any collection that you might be holding. The **PropertyInfo** collection contains an item for each available property. You can enumerate through these items to determine whether a given property is available.

You can get the [**PropertyInfo**](propertyinfo.md) collection from any collection you are holding by using the [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) method on the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, leaving the second parameter blank where you would normally specify a parent item's Key property.

## Related topics

<dl> <dt>

[Getting and Setting Properties](getting-and-setting-properties.md)
</dt> <dt>

[Interdependencies Between Properties](interdependencies-between-properties.md)
</dt> <dt>

[Saving or Discarding Changes](saving-or-discarding-changes.md)
</dt> </dl>

 

 



