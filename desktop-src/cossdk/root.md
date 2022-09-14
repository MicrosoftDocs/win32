---
description: Contains the top-level collections in the catalog.
ms.assetid: 6cd23e6a-53b8-42ec-97df-59281f019252
title: Root collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Root
api_type: 
- COM
api_location: 
---

# Root collection

Contains the top-level collections in the catalog. It does not contain any [**COMAdminCatalogObject**](comadmincatalogobject.md) objects or support any properties.

The **Root** collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

You cannot navigate to the **Root** collection from any collection.

## Members

The **Root** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

The following are the top-level collections in the catalog:

-   [**ApplicationCluster**](applicationcluster.md)
-   [**ApplicationInstances**](applicationinstances.md)
-   [**Applications**](applications.md)
-   [**ComputerList**](computerlist.md)
-   [**DCOMProtocols**](dcomprotocols.md)
-   [**EventClassesForIID**](eventclassesforiid.md)
-   [**FilesForImport**](filesforimport.md)
-   [**InprocServers**](inprocservers.md)
-   [**LegacyServers**](legacyservers.md)
-   [**LocalComputer**](localcomputer.md)
-   [**Partitions**](partitions.md)
-   [**PartitionUsers**](partitionusers.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**TransientSubscriptions**](transientsubscriptions.md)
-   [**WOWInprocServers**](wowinprocservers.md)
-   [**WOWLegacyServers**](wowlegacyservers.md)

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
