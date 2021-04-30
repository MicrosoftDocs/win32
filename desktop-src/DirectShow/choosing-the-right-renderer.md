---
description: Choosing the Right Video Renderer
ms.assetid: c57c4c68-ea1c-4198-94b4-e9b6e53bb625
title: Choosing the Right Video Renderer
ms.topic: article
ms.date: 05/31/2018
---

# Choosing the Right Video Renderer

DirectShow provides several video renderer filters, summarized in the following table.



| Filter                                                                  | Remarks                                           |
|-------------------------------------------------------------------------|---------------------------------------------------|
| [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) | Uses Direct3D 9. Requires Windows Vista or later. |
| [Video Mixing Renderer 9](video-mixing-renderer-filter-9.md) (VMR-9)   | Uses Direct3D 9. Requires Windows XP or later.    |
| [Video Mixing Filter 7](video-mixing-renderer-filter-7.md) (VMR-7)     | Uses DirectDraw. Requires Windows XP or later.    |
| [Overlay Mixer](using-the-overlay-mixer-in-video-capture.md)           | Supports hardware overlays through DirectDraw.    |
| Legacy [Video Renderer](video-renderer-filter.md) filter.              | Uses DirectDraw or (rarely) GDI                   |



 

Which renderer to use depends largely on which versions of Windows you need to support.

-   In Windows Vista and later, applications should use the EVR if the hardware supports it. Otherwise, fall back to the VMR-9 or VMR-7. The EVR offers better performance and better video quality than previous renderers. Also, it is designed to work with the Desktop Window Manager (DWM).
-   Prior to Windows Vista, use the VMR-9 if the hardware supports it and video port functionality is not required. Otherwise, use the VMR-7.
-   On older systems, you might need to use the Overlay Mixer (for video port or hardware overlay support) or the legacy Video Renderer filter.

The [**IGraphBuilder::Render**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-render) and [**RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) methods use the VMR-7 by default. If the hardware does not support the VMR-7, these methods fall back to the legacy Video Renderer filter. The EVR and VMR-9 are never the default renderers.

## Related topics

<dl> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 



