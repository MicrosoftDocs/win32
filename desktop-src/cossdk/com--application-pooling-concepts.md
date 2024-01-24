---
description: COM+ application pooling allows single-threaded processes to scale, similar to the way that thread pooling allows single-threaded objects to scale.
ms.assetid: 28bd13d9-ff5c-456e-ab98-d2ff3a499f1c
title: COM+ Application Pooling Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Application Pooling Concepts

COM+ application pooling allows single-threaded processes to scale, similar to the way that thread pooling allows single-threaded objects to scale. Application pooling can also help recover from failures in single processes by providing other running processes able to handle activations.

> [!Note]  
> Library applications have the recycling and pooling properties of their host process.

 

All methods of the [**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2) interface support application pooling.

COM+ application pooling is configurable per application by using the ConcurrentApps property of the [**COMAdminCatalogObject**](comadmincatalogobject.md) object in the [**Applications**](applications.md) collection. ConcurrentApps is an integer value that specifies the maximum number of simultaneous Dllhost processes that should be started to service activations for an application. This property can be set by using the Component Services administration tool or programmatically.

If the ConcurrentApps property is set to 1, which is the default value, the COM+ Application Pooling service is disabled.

## Related topics

<dl> <dt>

[COM+ Application Pooling Tasks](com--application-pooling-tasks.md)
</dt> <dt>

[COM+ Application Recycling Concepts](com--application-recycling-concepts.md)
</dt> </dl>

 

 



