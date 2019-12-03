---
title: GetRenderTargetSampleCount
description: Gets the number of samples for a render target.
ms.assetid: e813134e-c58c-4845-b519-c1074993801e
keywords:
- GetRenderTargetSampleCount HLSL
topic_type:
- apiref
api_name:
- GetRenderTargetSampleCount
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetRenderTargetSampleCount

Gets the number of samples for a render target.



| *UINT* GetRenderTargetSampleCount() |
|-------------------------------------|



 

## Parameters



| Item                                                                                 | Description |
|--------------------------------------------------------------------------------------|-------------|
| <span id="None"></span><span id="none"></span><span id="NONE"></span>None<br/> |             |



 

## Return Value

The number of samples.

## Remarks

Use this function and [**GetRenderTargetSamplePosition**](dx-graphics-hlsl-getrendertargetsampleposition.md) to find out the number and position of the sampling locations for a render target.

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md) and higher shader models | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md)           | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md)           | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)           | no        |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





