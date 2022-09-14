---
title: return Statement
description: A return statement signals the end of a function.
ms.assetid: e6c097af-ba0b-4abc-8099-69882ced1e18
keywords:
- return Statement HLSL
topic_type:
- apiref
api_name:
- return Statement
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# return Statement

A return statement signals the end of a function.

return \[value\];



 

The simplest return statement returns control from the function to the calling program; it returns no value.


```
void main()
{
    return ;
}
```



However, a return statement can return one or more values. This example returns a literal value:


```
float main( float input : COLOR0) : COLOR0
{
    return 0;
}
```



This example returns the scalar result of an expression.


```
return  light.enabled = true ;
```



This example returns a four-component vector that is constructed from a local variable and a literal.


```
return  float4(color.rgb, 1) ;
```



This example returns a four-component vector that is constructed from the result that is returned from an intrinsic function, together with literal values.


```
float4 func(float2 a: POSITION): COLOR
{
    return float4(sin(length(a) * 100.0) * 0.5 + 0.5, sin(a.y * 50.0), 0, 1);
}
```



This example returns a structure that contains one or more members.


```
float4x4 WorldViewProj;

struct VS_OUTPUT
{
    float4 Pos  : POSITION;
};

VS_OUTPUT VertexShader_Tutorial_1(float4 inPos : POSITION )
{
    VS_OUTPUT out;
    out.Pos = mul(inPos, WorldViewProj );
    return out;
};
```



## See also

<dl> <dt>

[Functions (DirectX HLSL)](dx-graphics-hlsl-functions.md)
</dt> </dl>

 

 




