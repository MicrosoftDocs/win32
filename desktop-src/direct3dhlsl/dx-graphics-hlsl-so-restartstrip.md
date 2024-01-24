---
title: RestartStrip (DirectX HLSL Stream-Output Object)
description: Ends the current primitive strip and starts a new strip. If the current strip does not have enough vertices emitted to fill the primitive topology, the incomplete primitive at the end will be discarded.
ms.assetid: ca8eb7cf-1b4a-4082-b768-01390c5f8b47
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# RestartStrip (DirectX HLSL Stream-Output Object)

Ends the current primitive strip and starts a new strip. If the current strip does not have enough vertices emitted to fill the primitive topology, the incomplete primitive at the end will be discarded.

RestartStrip();



 

## Parameters



| Item                                                                                     | Description |
|------------------------------------------------------------------------------------------|-------------|
| <span id="None"></span><span id="none"></span><span id="NONE"></span>**None**<br/> |             |



 

## Return Value

None

## Remarks

A strip cut causes the current strip to end, and a new strip to start. A strip cut can be done by explicitly calling this method, or just by rendering up to the maximum index value ( 1, which is 0xffffffff for 32-bit indices or 0xffff for 16-bit indices). Each instance of an indexed-instanced draw generates a strip cut automatically. This is true even if the topology is not a triangle strip.

> [!Note]  
> Support for restart and the  1 'magic value' for a cut is only available on [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 10.0 or higher devices.

 

The output is always assumed to be a triangle strip. To make the output a triangle list, you must call RestartStrip between each triangle. Triangle fans are unsupported.

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Stream-Output Object](dx-graphics-hlsl-so-type.md)
</dt> </dl>

 

