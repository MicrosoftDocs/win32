---
description: Requests to start debugging the specified list of instructions.
MS-HAID: vspixengine.IDebugShaderRequest2\_BeginDebugShader\_IPixErrorCallback\_ptr\_DWORD\_BYTE\_arr\_DWORD\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderRequest2::BeginDebugShader method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: B454D673-C14F-4A8F-9DA7-2C47510BE5DA
api_name: 
 - IDebugShaderRequest2.BeginDebugShader
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.idebugshaderrequest2_begindebugshader_ipixerrorcallback_ptr_dword_byte_arr_dword_ptr"></span>IDebugShaderRequest2::BeginDebugShader method

Requests to start debugging the specified list of instructions.

## Syntax


```C++
HRESULT BeginDebugShader(
   IPixErrorCallback * errorCallback,
   DWORD               instructionStreamSize,
   BYTE []             count1_instructionStream,
   DWORD *             pDevice
);
```

## Parameters

*errorCallback*   
The address of a callback for errors that might occur during debugging.

*instructionStreamSize*   
The number of instructions in the instruction stream.

*count1\_instructionStream*   
The specified instruction stream.

*pDevice*   
The address to pass to the debug engine for communicating with this debug session (debug engine readprocessmemory on this address).

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IDebugShaderRequest2**](/windows/desktop/direct3dtools/idebugshaderrequest2)

 

 
