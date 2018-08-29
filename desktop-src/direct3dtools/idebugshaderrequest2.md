---
Description: 'Request to start debugging a shader. This request contains two parts: generate a trace, and debug a trace.'
MS-HAID: vspixengine.IDebugShaderRequest2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderRequest2 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.idebugshaderrequest2"></span>IDebugShaderRequest2 interface

Request to start debugging a shader. This request contains two parts: generate a trace, and debug a trace.

## Members

The **IDebugShaderRequest2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDebugShaderRequest2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IDebugShaderRequest2** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422662"><strong>BeginDebugShader</strong></a></td><td style="text-align: left;"><p>Requests to start debugging the specified list of instructions.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422663"><strong>GenerateInstructions</strong></a></td><td style="text-align: left;"><p>Requests to generate shader trace instructions in a debug request. Trace-based debugging occurs on the CPU (warp) instead of the GPU.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



