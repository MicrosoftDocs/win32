---
description: 'Request to start debugging a shader. This request contains two parts: generate a trace, and debug a trace.'
MS-HAID: vspixengine.IDebugShaderRequest2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderRequest2 interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 80F95900-F2E6-4B5C-B902-573280956E94
api_name: 
 - IDebugShaderRequest2
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.idebugshaderrequest2"></span>IDebugShaderRequest2 interface

Request to start debugging a shader. This request contains two parts: generate a trace, and debug a trace.

## Members

The **IDebugShaderRequest2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDebugShaderRequest2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IDebugShaderRequest2** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/idebugshaderrequest2-begindebugshader-ipixerrorcallback-ptr-dword-byte-arr-dword-ptr"><strong>BeginDebugShader</strong></a></td><td ><p>Requests to start debugging the specified list of instructions.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/idebugshaderrequest2-generateinstructions-ipixerrorcallback-ptr-debugshaderrequestinfo-ptr-pixelhistoryoperation-ptr-idebugshadercallback-ptr"><strong>GenerateInstructions</strong></a></td><td ><p>Requests to generate shader trace instructions in a debug request. Trace-based debugging occurs on the CPU (warp) instead of the GPU.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
