---
description: An annotation is a user-defined piece of information, declared with the following syntax.
ms.assetid: 9178e61e-05a4-441c-a9f1-e05e23ab48a5
title: Annotation Syntax (Direct3D 10)
ms.topic: reference
ms.date: 05/31/2018
---

# Annotation Syntax (Direct3D 10)

An annotation is a user-defined piece of information, declared with the following syntax.



| <*DataType* *Name* = *Value*; ... ;> |
|--------------------------------------------|



 

## Parameters



| Item                                                                                                   | Description                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DataType"></span><span id="datatype"></span><span id="DATATYPE"></span>*DataType*<br/> | \[in\] The data type, which includes any [scalar HLSL](../direct3dhlsl/dx-graphics-hlsl-scalar.md) type as well as the [string type](../direct3dhlsl/dx-graphics-hlsl-scalar.md).<br/> |
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

[Effect Variable Syntax](d3d10-effect-variable-syntax.md)
</dt> </dl>

 

 
