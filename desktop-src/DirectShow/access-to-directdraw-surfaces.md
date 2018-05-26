---
Description: Access to DirectDraw Surfaces
ms.assetid: 21002c9f-8b8b-49f3-9ea3-3703780e3412
title: Access to DirectDraw Surfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Access to DirectDraw Surfaces

The Media Sample objects provided by the VMR to upstream filters support the [**IVMRSurface**](/windows/win32/Strmif/nn-strmif-ivmrsurface?branch=master) interface. To obtain the interface, call QueryInterface on the [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface and specify IID\_IVMRSurface. Upstream filters can then use the IVMRSurface methods to access and manipulate the surface that has been created by the VMR.

## Related topics

<dl> <dt>

[Using the VMR for DirectShow Filter Developers](using-the-vmr-for-directshow-filter-developers.md)
</dt> </dl>

 

 



