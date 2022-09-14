---
title: Annotation Syntax (Direct3D 11)
description: An annotation is a user-defined piece of information, declared with the syntax described in this section.
ms.assetid: a81198d2-c4d7-47b5-b3b8-2de11a9ee9a3
ms.topic: reference
ms.date: 05/31/2018
---

# Annotation Syntax (Direct3D 11)

An annotation is a user-defined piece of information, declared with the syntax described in this section.



| <*DataType* *Name* = *Value*; *...* ;> |
|----------------------------------------------|



 

## Parameters



| Item                                                                                                   | Description                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DataType"></span><span id="datatype"></span><span id="DATATYPE"></span>*DataType*<br/> | \[in\] The data type, which includes any [scalar HLSL](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-scalar) type as well as the [string type](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-scalar).<br/> |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*<br/>                 | \[in\] An ASCII string, that represents the annotation name.<br/>                                                                                                          |
| <span id="Value"></span><span id="value"></span><span id="VALUE"></span>*Value*<br/>             | \[in\] The initial value of the annotation.<br/>                                                                                                                           |
| <span id="..."></span>*...*<br/>                                                                 | \[in\] Additional annotations (name-value pairs).<br/>                                                                                                                     |



 

## Remarks

You may add more than one annotation within the angle brackets, each one separated by a semicolon. The effect framework APIs recognize annotations on global variables; all other annotations are ignored.

## Example

Here are some examples.


```
       
int i <int blabla=27; string blacksheep="Hello There";>;

int j <int bambam=30; string blacksheep="Goodbye There";> = 5 ;

float y <float y=2.3;> = 2.3, z <float y=1.3;> = 1.3 ;

half w <half GlobalW = 3.62;>;

float4 main(float4 pos : SV_POSITION ) : SV_POSITION
{
    pos.y = pos.x > 0 ? pos.w * 1.3 : pos.z * .032;
    for (int x = i; x < j ; x++) 
    {
        pos.w = pos.w * pos.y + x + j - y * w;
    } 

return pos;
}
```



## Related topics

<dl> <dt>

[Effect Format](d3d11-effect-format.md)
</dt> <dt>

[Effect Variable Syntax](d3d11-effect-variable-syntax.md)
</dt> </dl>

 

