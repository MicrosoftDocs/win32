---
Description: Access to DirectDraw Surfaces
ms.assetid: '21002c9f-8b8b-49f3-9ea3-3703780e3412'
title: Access to DirectDraw Surfaces
---

# Access to DirectDraw Surfaces

The Media Sample objects provided by the VMR to upstream filters support the [**IVMRSurface**](ivmrsurface.md) interface. To obtain the interface, call QueryInterface on the [**IMediaSample**](imediasample.md) interface and specify IID\_IVMRSurface. Upstream filters can then use the IVMRSurface methods to access and manipulate the surface that has been created by the VMR.

## Related topics

<dl> <dt>

[Using the VMR for DirectShow Filter Developers](using-the-vmr-for-directshow-filter-developers.md)
</dt> </dl>

 

 



