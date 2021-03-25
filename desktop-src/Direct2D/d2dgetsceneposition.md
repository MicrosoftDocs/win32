---
title: D2DGetScenePosition function (D2d1effecthelpers.h)
description: Returns the value of the input SCENE\_POSITION. Only available when D2D\_REQUIRES\_SCENE\_POSITION is declared in the source file.
ms.assetid: 451E4C31-D93D-44B6-81D1-AC5FD986ACBD
keywords:
- D2DGetScenePosition function Direct2D
topic_type:
- apiref
api_name:
- D2DGetScenePosition
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2DGetScenePosition function

Returns the value of the input SCENE\_POSITION. Only available when D2D\_REQUIRES\_SCENE\_POSITION is declared in the source file.

## Syntax

``` syntax
float4 WINAPI D2DGetScenePosition(void);
```

## Parameters

This function has no parameters.

## Return value

The function returns a **float4** in the format SCENE\_POSITION.

## Remarks

The following example shows the use of the function in generating a dissolve pattern.

``` syntax
D2D_PS_ENTRY(BlendDissolve)  
{  
    min16float4 dest   = D2DGetInput(0);  
    min16float4 source = D2DGetInput(1);  
  
    min16float4 color = dest;  
  
    if ((source.a > 0.0) && (source.a >= Rand((min16float2)D2DGetScenePosition().xy)))  
    {  
        // TODO: perform  dissovlve math
    }  
  
    return color;  
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

 

 





