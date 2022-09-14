---
title: GetRenderTargetSamplePosition
description: Gets the sampling position (x,y) for a given sample index.
ms.assetid: 07f14d1c-4fe5-4838-acce-d664cdc641e6
keywords:
- GetRenderTargetSamplePosition HLSL
topic_type:
- apiref
api_name:
- GetRenderTargetSamplePosition
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetRenderTargetSamplePosition

Gets the sampling position (x,y) for a given sample index.

float<2> GetRenderTargetSamplePosition( in int<1> Index<br/>);



 

## Parameters



| Item                                                                                       | Description                                  |
|--------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="Index"></span><span id="index"></span><span id="INDEX"></span>*Index*<br/> | \[in\] A zero-based sample index.<br/> |



 

## Return Value

The (x,y) position of the given sample.

## Remarks

Use this function and [**GetRenderTargetSampleCount**](dx-graphics-hlsl-getrendertargetsamplecount.md) to find out the number and position of the sampling locations for a render target.

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

 

 





