---
title: D2DSampleInputAtPosition function (D2d1effecthelpers.h)
description: Samples input N at an absolute scene position, rather than an input-relative position. Only available for complex inputs.
ms.assetid: E839287F-91D1-4591-8DE7-1DFC3001A23D
keywords:
- D2DSampleInputAtPosition function Direct2D
topic_type:
- apiref
api_name:
- D2DSampleInputAtPosition
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2DSampleInputAtPosition function

Samples input N at an absolute scene position, rather than an input-relative position. Only available for complex inputs.

## Syntax

``` syntax
float4 WINAPI D2DSampleInputAtPosition(
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

The following example shows the function used in a circular wrap.

``` syntax
  
D2D_PS_ENTRY(CircularWrapPS)  
{  
    // TODO: perform math to calculate a circular wrap
  
    // Find the input scene position.  
    float2 inputScenePosition = float2( TODO: add math parameters );  
  
    return D2DSampleInputAtPosition(0, inputScenePosition);  
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

 

 





