---
description: There are three classes provided by the COMAdmin library (comadmin.dll), each of which implements a COM dual interface.
ms.assetid: 5a20199f-9d46-4dbe-8e30-2c7ddbde8795
title: Summary Description of the COMAdmin Classes
ms.topic: article
ms.date: 05/31/2018
---

# Summary Description of the COMAdmin Classes

There are three classes provided by the COMAdmin library (comadmin.dll), each of which implements a COM dual interface. You use objects created from these classes to gain access to the catalog, to represent collections in the catalog, and to represent the items contained within collections.

## COMAdminCatalog

The [**COMAdminCatalog**](comadmincatalog.md) class represents the catalog itself. An object created from **COMAdminCatalog** is the fundamental object that you use in programmatic administration. Besides establishing the basic connection with the catalog server when you instantiate it, **COMAdminCatalog** provides methods that enable you to do the following:

-   Get collections on the catalog.
-   Connect to the catalog server on a remote machine.
-   Install, export, start, shut down, and obtain information regarding COM+ applications.
-   Install components into COM+ applications and obtain information regarding components.
-   Start, stop, or refresh services running on the machine.
-   Refresh, restore, or back up catalog information.

In COM+ 1.0, the [**COMAdminCatalog**](comadmincatalog.md) class implements the [**ICOMAdminCatalog**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog) interface. In COM+ 1.5, the **COMAdminCatalog** class implements [**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2) as its default interface.

## COMAdminCatalogCollection

The [**COMAdminCatalogCollection**](comadmincatalogcollection.md) class represents any collection in the catalog, by supplying a string naming the particular collection at object instantiation time. (Available catalog collections are named in the table at [COM+ Administration Collections](com--administration-collections.md).) Objects are created from this class when retrieving a top-level collection by calling the [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) method of the [**COMAdminCatalog**](comadmincatalog.md) object. These objects are also created when retrieving a child collection by calling the **GetCollection** method of its parent collection object. **COMAdminCatalogCollection** objects enable you to do the following:

-   Enumerate through the items contained within the collection.
-   Retrieve an item from the collection.
-   Add or remove items to or from the collection.
-   Save or discard any pending changes made to the collection or to the items it contains.
-   Get a different collection in the catalog.

The [**COMAdminCatalogObject**](comadmincatalogobject.md) class implements the [**ICatalogCollection**](/windows/desktop/api/ComAdmin/nn-comadmin-icatalogcollection) interface.

## COMAdminCatalogObject

The [**COMAdminCatalogObject**](comadmincatalogobject.md) class represents any item that is contained within a collection. Objects are created from this class when getting an item through the [**Item**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-get_item) property of a catalog collection object. Objects created from the **COMAdminCatalogObject** class enable you to do the following:

-   Get or set properties supported by the item that the object is being used to represent.
-   Obtain information about the item and its properties.

The [**COMAdminCatalogObject**](comadmincatalogobject.md) class implements the [**ICatalogObject**](/windows/desktop/api/ComAdmin/nn-comadmin-icatalogobject) interface.

## Related topics

<dl> <dt>

[Accessing the COM+ Catalog](accessing-the-com--catalog.md)
</dt> <dt>

[Overview of the COMAdmin Objects](overview-of-the-comadmin-objects.md)
</dt> </dl>

 

 



