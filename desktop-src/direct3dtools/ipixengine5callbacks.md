---
description: Callbacks used for viewing textures.
MS-HAID: vspixengine.IPixEngine5Callbacks
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine5Callbacks interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: F87F00ED-C816-49A3-926B-28E3C8330EA2
api_name: 
 - IPixEngine5Callbacks
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine5callbacks"></span>IPixEngine5Callbacks interface

Callbacks used for viewing textures.

## Members

The **IPixEngine5Callbacks** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPixEngine5Callbacks** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine5Callbacks** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-freetexturecomplete"><strong>FreeTextureComplete</strong></a></td><td ><p>A callback function used to notify the host when a texture has been freed.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-loadhistogramcomplete-pixenginehistogram-ptr"><strong>LoadHistogramComplete</strong></a></td><td ><p>A callback function used to notify the host when a histogram load has been completed.</p></td></tr><tr class="odd"><td ><a href="/previous-versions/windows/desktop/legacy/mt432759(v=vs.85)"><strong>LoadTextureFromFileComplete</strong></a></td><td ><p>A callback function used to notify the host when a texture load has been completed.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-loadtextureslicecomplete-pixenginetextureslicedescriptor-pixenginehistogram-ptr"><strong>LoadTextureSliceComplete</strong></a></td><td ><p>A callback function used to notify the host when a texture slice load has been completed.</p></td></tr><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-readtexelvaluecomplete-uint-bstr-arr-double-arr"><strong>ReadTexelValueComplete</strong></a></td><td ><p>A callback function used to notify the host when a texel value read has been completed.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-rendertexturecomplete"><strong>RenderTextureComplete</strong></a></td><td ><p>A callback function used to notify the host when a texture render has been completed.</p></td></tr><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/ipixengine5callbacks-savetexturecomplete"><strong>SaveTextureComplete</strong></a></td><td ><p>A callback function used to notify the host when saving a texture has been completed.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
