---
Description: Contains the top-level collections in the catalog.
ms.assetid: 6cd23e6a-53b8-42ec-97df-59281f019252
title: Root collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Root collection

Contains the top-level collections in the catalog. It does not contain any [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) objects or support any properties.

The **Root** collection does not support the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

You cannot navigate to the **Root** collection from any collection.

## Members

The **Root** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

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

 

 



