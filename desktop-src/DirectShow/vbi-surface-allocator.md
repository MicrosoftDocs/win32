---
description: VBI Surface Allocator
ms.assetid: 51c73a25-1112-4fb4-a45f-967c6a1b5c55
title: VBI Surface Allocator
ms.topic: article
ms.date: 05/31/2018
---

# VBI Surface Allocator

The VBI Surface Allocator controls the allocation of VBI buffers in analog television graphs with hardware video port capture scenarios. With devices such as the Bt829 decoder, the frame buffer may contain multiple VBI capture buffers that are accessed via a proprietary hardware-based mechanism known generically as a Video Port. The VBI Surface Allocator filter connects downstream from the capture filter and has no output pin. The filter works closely with the [Overlay Mixer](overlay-mixer-filter.md) (via DirectDraw) to perform coordinated operations on the hardware video port, utilizing the same limited SVGA frame buffer memory.



| Label | Value |
|------------------------------------------|-------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                                                  |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_VPVBI                                               |
| Input Pin Interfaces                     | [**IKsPropertySet**](ikspropertyset.md)                                            |
| Output Pin Media Types                   | MEDIATYPE\_NULL, MEDIASUBTYPE\_NULL. (Nothing is ever connected to the output pin.) |
| Output Pin Interfaces                    | Not applicable.                                                                     |
| Filter CLSID                             | CLSID\_VBISurfaces                                                                  |
| Property Page CLSID                      | No property page.                                                                   |
| Executable                               | vbisurf.ax                                                                          |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                       |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                       |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



