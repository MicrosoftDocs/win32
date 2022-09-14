---
description: Request for pixel history intersections and primitives separately.
MS-HAID: vspixengine.IPixelHistoryRequest2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixelHistoryRequest2 interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: B62A9EBA-4497-4825-A2F1-285A4AD45012
api_name: 
 - IPixelHistoryRequest2
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixelhistoryrequest2"></span>IPixelHistoryRequest2 interface

Request for pixel history intersections and primitives separately.

## Members

The **IPixelHistoryRequest2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPixelHistoryRequest2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixelHistoryRequest2** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixelhistoryrequest2-requestintersections-dword-point2d-dword-ipixelhistorycallback2-ptr-dword-dword"><strong>RequestIntersections</strong></a></td><td ><p>Requests a list of events that cause a change in the specified pixel, render target / UAV, and frame.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixelhistoryrequest2-requestprimitives-pixelhistoryintersection-ptr-ipixelhistorycallback2-ptr-dword-dword"><strong>RequestPrimitives</strong></a></td><td ><p>Requests a list of primitives from a particular intersection. For more information, see the RequestIntersections member function.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
