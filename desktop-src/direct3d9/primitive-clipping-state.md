---
description: Primitives that lie partially inside (or completely outside) the view frustum can be clipped so that only the visible portion of the primitive will be rendered.
ms.assetid: 096683a4-2d8f-49d3-b1a0-832150907f11
title: Primitive Clipping State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Primitive Clipping State (Direct3D 9)

Primitives that lie partially inside (or completely outside) the [view frustum](viewports-and-clipping.md) can be clipped so that only the visible portion of the primitive will be rendered. Clipping reduces the amount of work that is done to only those primitives or portions of a primitive that will be visible.

To use the pipeline for clipping, set the D3DRS\_CLIPPING render state to **TRUE** (the default value) to enable clipping, or to **FALSE** to disable Direct3D clipping.

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 



