---
Description: Callback to return pixel history intersections (draw call level) and primitives (triangle level) in two different results.
MS-HAID: vspixengine.IPixelHistoryCallback2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixelHistoryCallback2 interface
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixelhistorycallback2"></span>IPixelHistoryCallback2 interface

Callback to return pixel history intersections (draw call level) and primitives (triangle level) in two different results.

## Members

The **IPixelHistoryCallback2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixelHistoryCallback2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixelHistoryCallback2** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432737"><strong>IntersectionsCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of pixel history intersection information returned by the assocaited request.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432738"><strong>PrimitivesCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of pixel history primitive operation information returned by the associated request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



