---
title: Stream-Output Object
description: A stream-output object is a templated object that streams data out of the geometry-shader stage. Use the following syntax to declare a stream-output object.
ms.assetid: 07a5489c-c238-4466-9282-5b168448aff7
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Stream-Output Object

A stream-output object is a templated object that streams data out of the [geometry-shader stage](/previous-versions//bb205146(v=vs.85)). Use the following syntax to declare a stream-output object.



| inout *StreamOutputObject*<*DataType*> *Name;* |
|------------------------------------------------------|



 

## Parameters

<dl> <dt>

<span id="StreamOutputObject___________________________DataType_________________________________________Name"></span><span id="streamoutputobject___________________________datatype_________________________________________name"></span><span id="STREAMOUTPUTOBJECT___________________________DATATYPE_________________________________________NAME"></span>*StreamOutputObject* < *DataType* >   *Name*
</dt> <dd>

The stream-output object (SO) declaration.



| Stream-Output Object Types | Description                       |
|----------------------------|-----------------------------------|
| *PointStream*              | A sequence of point primitives    |
| *LineStream*               | A sequence of line primitives     |
| *TriangleStream*           | A sequence of triangle primitives |



 

*DataType* - Output data type; can be any [HLSL data type](dx-graphics-hlsl-data-types.md). Must be surrounded by the angle brackets.

*Name* - Variable name; an ASCII string that uniquely identifies the object.

</dd> </dl>

## Example

This is an example of a stream-output object declaration that streams out triangle primitives whose data is defined by the PS\_CUBEMAP\_IN structure. The geometry-shader is limited to generating 18 vertices.


```
struct PS_CUBEMAP_IN
{
    float4 Pos : SV_POSITION;     // Projection coord
    float2 Tex : TEXCOORD0;       // Texture coord
    uint RTIndex : SV_RenderTargetArrayIndex;
};

[maxvertexcount(18)]
void main( inout TriangleStream<PS_CUBEMAP_IN> CubeMapStream, triangle PS_CUBEMAP_INT[3] )
{
    ...
}
```



This is a code snippet from the [CubeMapGS Sample](https://msdn.microsoft.com/library/Ee416398(v=VS.85).aspx).

## Stream-Output Object Methods

Use the following syntax to call stream-output-object methods.


```
Object.Method
```



The following methods are implemented.



| Methods                                              | Description                                                      |
|------------------------------------------------------|------------------------------------------------------------------|
| [Append](dx-graphics-hlsl-so-append.md)             | Append output data to an existing stream.                        |
| [RestartStrip](dx-graphics-hlsl-so-restartstrip.md) | End the current primitive strip and start a new primitive strip. |



 

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md) and higher shader models | yes       |



 

## Related topics

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 