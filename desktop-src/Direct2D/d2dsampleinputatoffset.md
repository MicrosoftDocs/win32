---
title: D2DSampleInputAtOffset function (D2d1effecthelpers.h)
description: Samples input N at an offset of offset from the input coordinate. Only available for complex inputs.
ms.assetid: 4A01264E-04E3-49BD-9EF8-7834D9B8B0B8
keywords:
- D2DSampleInputAtOffset function Direct2D
topic_type:
- apiref
api_name:
- D2DSampleInputAtOffset
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2DSampleInputAtOffset function

Samples input N at an offset of offset from the input coordinate. Only available for complex inputs.

## Syntax

``` syntax
float4 WINAPI D2DSampleInputAtOffset(
  in uint N,
  in float2 offset
);
```

## Parameters

<dl> <dt>

*N* \[in\]
</dt> <dd>

The input number.

</dd> <dt>

*offset* \[in\]
</dt> <dd>

The uv offset.

</dd> </dl>

## Return value

The function returns a **float4**, in the format TEXCOORDN.

## Remarks

The following example shows the function being used as part of a highlighting and shadows gradient mask.

``` syntax
  
D2D_PS_ENTRY(HighlightsAndShadowsGradientMask)  
{  
    MIN_TYPE(float4) blurred = D2DGetInput(0);  
  
    // Compute X and Y gradients 
    MIN_TYPE(float) dX1 = D2DSampleInputAtOffset(0, float2(1, 0));
    MIN_TYPE(float) dX2 = D2DSampleInputAtOffset(0, float2(-1, 0));
    MIN_TYPE(float) dY1 = D2DSampleInputAtOffset(0, float2(0, 1));
    MIN_TYPE(float) dY2 = D2DSampleInputAtOffset(0, float2(0, -1));
    
    // TODO: math to calculate shadow gradients

    // Return the value in the alpha channel.  
    blurred.a = // TODO: math to calculate blurred value
  
    return blurred;  
}  
```

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.hlsli</dt> </dl> |
| DLL<br/>    | <dl> <dt>D2d1.dll</dt> </dl>                |



## See also

<dl> <dt>

[Effect Shader Linking](effect-shader-linking.md)
</dt> <dt>

[HLSL Helpers](hlsl-helpers.md)
</dt> </dl>

 

 





