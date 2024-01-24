---
description: Extensions to the original IPixEngine interface.
MS-HAID: vspixengine.IPixEngine2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2 interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: D650FB4C-C332-4E2E-85EB-DDCE3DA87B0C
api_name: 
 - IPixEngine2
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine2"></span>IPixEngine2 interface

Extensions to the original IPixEngine interface.

## Members

The **IPixEngine2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPixEngine2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine2** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine2-endexperiment-bstr-ifileiocallback-ptr"><strong>EndExperiment</strong></a></td><td ><p>Ends the experiement and completes the graphics log.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine2-getplaybackmachine-bstr-bool-ptr-bstr-ptr"><strong>GetPlaybackMachine</strong></a></td><td ><p>Gets information about the current playback machine.</p></td></tr><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine2-onnewdataavailable-bool-bool-int64-int64-int32-byte-arr"><strong>OnNewDataAvailable</strong></a></td><td ><p>Requests to indicate that the graphics log has new data inside of it.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine2-setplaybackmachine-bstr-bool-bstr"><strong>SetPlaybackMachine</strong></a></td><td ><p>Sets the current playback machine for the specified graphics log.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
