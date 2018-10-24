---
Description: Request for pixel history intersections and primitives separately.
MS-HAID: vspixengine.IPixelHistoryRequest2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixelHistoryRequest2 interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixelhistoryrequest2"></span>IPixelHistoryRequest2 interface

Request for pixel history intersections and primitives separately.

## Members

The **IPixelHistoryRequest2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixelHistoryRequest2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixelHistoryRequest2** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432742"><strong>RequestIntersections</strong></a></td><td style="text-align: left;"><p>Requests a list of events that cause a change in the specified pixel, render target / UAV, and frame.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432743"><strong>RequestPrimitives</strong></a></td><td style="text-align: left;"><p>Requests a list of primitives from a particular intersection. For more information, see the RequestIntersections member function.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



