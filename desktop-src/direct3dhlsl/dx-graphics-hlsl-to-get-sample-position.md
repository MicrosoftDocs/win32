---
title: GetSamplePosition (DirectX HLSL Texture Object)
description: Gets the position of the specified sample.
ms.assetid: 4e622b85-82d6-4339-b03a-becbe5f9aa57
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# GetSamplePosition (DirectX HLSL Texture Object)

Gets the position of the specified sample.

ret Object.GetSamplePosition( int s );



 

## Parameters



| Item                                                                                           | Description                                                                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <span id="Object"></span><span id="object"></span><span id="OBJECT"></span>*Object*<br/> | A Texture2DMS or a Texture2DMSArray [texture-object](dx-graphics-hlsl-to-type.md) type.<br/> |
| <span id="s"></span><span id="S"></span>*s*<br/>                                         | \[in\] The zero-based sample index.<br/>                                                      |



 

## Return Value

Returns the (x,y) sample position, a two-component floating-point vector.

## Minimum Shader Model

This function is supported in the following shader models.



| vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|----------|-----------|----------|-----------|----------|-----------|
|          | x         |          | x         |          | x         |



 

-   Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Remarks

A pixel shader can be evaluated at sample frequency (run a pixel shader once per sample) or at pixel frequency (run a pixel shader once per pixel). Attach the SV\_SampleIndex semantic to a pixel shader input to invoke a pixel shader at sample frequency, the input value is then used as a sample index when sampling the render target.

You can interpolate a pixel shader input in several ways. To interpolate at:

-   A pixel center, don't use any semantic.
-   A sample, use the SV\_SampleIndex semantic.
-   A centroid location, use the [\_centroid](dx-graphics-hlsl-struct.md) modifier.

## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

 





