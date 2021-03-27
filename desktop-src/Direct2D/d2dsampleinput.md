---
title: D2DSampleInput function (D2d1effecthelpers.h)
description: Samples input N at position uv. Only available for complex inputs.
ms.assetid: 8C1E3B23-D05B-4FCC-B32F-A5870A7C3FEF
keywords:
- D2DSampleInput function Direct2D
topic_type:
- apiref
api_name:
- D2DSampleInput
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2DSampleInput function

Samples input N at position uv. Only available for complex inputs.

## Syntax

``` syntax
float4 WINAPI D2DSampleInput(
  in uint N,
  in float2 uv
);
```

## Parameters

<dl> <dt>

*N* \[in\]
</dt> <dd>

The input number.

</dd> <dt>

*uv* \[in\]
</dt> <dd>

The uv position.

</dd> </dl>

## Return value

The function returns a **float4**, in the format TEXCOORDN.

## Remarks

The following example shows the function being used to calculate surface normals.

``` syntax
   
float3 CalculateSurfaceNormal(TAPARGS)  
{  
    float3 normal = float3(0, 0, 1.0);  
  
    // unrolled loop  
    normal.xy += tap1.zw * D2DSampleInput(0, tap1.xy).a;  
    normal.xy += tap2.zw * D2DSampleInput(0, tap2.xy).a;  
    normal.xy += tap3.zw * D2DSampleInput(0, tap3.xy).a;  
    normal.xy += tap4.zw * D2DSampleInput(0, tap4.xy).a;  
    normal.xy += tap5.zw * D2DSampleInput(0, tap5.xy).a;  
    normal.xy += tap6.zw * D2DSampleInput(0, tap6.xy).a;  
  
    normal = normalize(normal);  
      
    return normal;  
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

 

 





