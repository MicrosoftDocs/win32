---
description: Extensions to the IPixEngine6 interface containing additions around versioning.
MS-HAID: vspixengine.IPixEngine7
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine7 interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: D30020DF-B998-413F-B09B-179A31B0AED2
api_name: 
 - IPixEngine7
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine7"></span>IPixEngine7 interface

Extensions to the IPixEngine6 interface containing additions around versioning.

## Members

The **IPixEngine7** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPixEngine7** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine7** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine7-initengineasync-resourcepair-arr-uint-iversioncallback-ptr-dword-dword"><strong>InitEngineAsync</strong></a></td><td ><p>Asynchronously passes resources to the engine, such as strings for error messages.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine7-setplaybackendpointasync-bool-bstr-bstr-remotingversion-iversioncallback-ptr-dword-dword"><strong>SetPlaybackEndpointAsync</strong></a></td><td ><p>Asynchronously sets the endpoint address used to connect to a remote engine.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
