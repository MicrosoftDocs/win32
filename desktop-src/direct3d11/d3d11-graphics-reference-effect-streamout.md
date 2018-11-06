---
title: Stream Out Syntax
description: A geometry shader with stream out is declared with a particular syntax.
ms.assetid: 58cf6503-0dde-4c88-837d-ae0e0eda17d5
ms.topic: article
ms.date: 05/31/2018
---

# Stream Out Syntax

A geometry shader with stream out is declared with a particular syntax. This topic describes the syntax. In the effect runtime, this syntax will be converted to a call to [**ID3D11Device::CreateGeometryShaderWithStreamOutput**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput).

## Construct Syntax


```
[ StreamingShaderVar = ] ConstructGSWithSO( ShaderVar, "OutputDecl0" )
```





| Name                   | Description                                                                                                                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **StreamingShaderVar** | Optional. An ASCI string that uniquely identifies the name of a geometry shader variable with stream out. This is optional because ConstructGSWithSO can be placed directly in a SetGeometryShader or BindInterfaces call. |
| **ShaderVar**          | A geometry shader or vertex shader variable.                                                                                                                                                                               |
| **OutputDecl0**        | A string defining which shader outputs in stream 0 are streamed out. See below for syntax.                                                                                                                                 |



 

This is the syntax was defined in fx\_4\_0 files. Note that in gs\_4\_0 and vs\_x shaders, there is only one stream of data. The resulting shader will output one stream to both the stream out unit and the rasterizer unit.


```
[ StreamingShaderVar = ] ConstructGSWithSO( ShaderVar, "OutputDecl0", "OutputDecl1", "OutputDecl2", 
"OutputDecl3", RasterizedStream )
```





| Name                   | Description                                                                                                                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **StreamingShaderVar** | Optional. An ASCI string that uniquely identifies the name of a geometry shader variable with stream out. This is optional because ConstructGSWithSO can be placed directly in a SetGeometryShader or BindInterfaces call. |
| **ShaderVar**          | A geometry shader or vertex shader variable.                                                                                                                                                                               |
| **OutputDecl0**        | A string defining which shader outputs in stream 0 are streamed out. See below for syntax.                                                                                                                                 |
| **OutputDecl1**        | A string defining which shader outputs in stream 1 are streamed out. See below for syntax.                                                                                                                                 |
| **OutputDecl2**        | A string defining which shader outputs in stream 2 are streamed out. See below for syntax.                                                                                                                                 |
| **OutputDecl3**        | A string defining which shader outputs in stream 3 are streamed out. See below for syntax.                                                                                                                                 |
| **RasterizedStream**   | An integer specifying which stream will be sent to the rasterizer.                                                                                                                                                         |



 

Note that gs\_5\_0 shaders can define up to four streams of data. The resulting shader will output one stream to the stream out unit for each non-**NULL** output declaration and one stream the rasterizer unit.

## Stream Out Declaration Syntax


```
" [ Buffer: ] Semantic[ SemanticIndex ] [ .Mask ]; [ ... ; ] ... [ ... ;]"
```





| Name              | Description                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------|
| **Buffer**        | Optional. An integer, 0 <= Buffer < 4, specifying which stream out buffer the value will go to. |
| **Semantic**      | A string, along with SemanticIndex, specifying which value to output.                                 |
| **SemanticIndex** | Optional. The index associated with Semantic.                                                         |
| **Mask**          | Optional. A component mask, indicating which components of the value to output.                       |



 

There is one special Semantic, labeled "$SKIP" which indicates an empty semantic, leaving the corresponding memory in the stream out buffer untouched. The $SKIP semantic cannot have a SemanticIndex, but can have a Mask.

The entire stream out declaration can be **NULL**.

## Example


```
struct GSOutput
{
int4 Pos : Position;
int4 Color : Color;
int4 Texcoord : Texcoord;
};

[maxvertexcount(1)]
void gsBase (inout PointStream<GSOutput> OutputStream, inout PointStream<GSOutput> OutputStream1)
{
GSOutput output;
output.Pos = int4(1,2,3,4);
output.Color = int4(5,6,7,8);
output.Texcoord = int4(9,10,11,12);
OutputStream.Append(output);

output.Pos = int4(1,2,3,4);
    output.Color = int4(5,6,7,8);
output.Texcoord = int4(9,10,11,12);
OutputStream1.Append(output);
};


GeometryShader pGSComp = CompileShader(gs_5_0, gsBase());
GeometryShader pGSwSO = ConstructGSWithSO(pGSComp, "0:Position.xy; 1:Position.zw; 2:Color.xy", 
                                                   "3:Texcoord.xyzw; 3:$SKIP.x;", NULL, NULL, 1);

// The following two passes perform the same operation
technique11 SOPoints
{
    pass 
    {
        SetGeometryShader(ConstructGSWithSO(pGSComp, "0:Position.xy; 1:Position.zw; 2:Color.xy", 
                                                     "3:Texcoord.xyzw; 3:$SKIP.x;", NULL, NULL, 1));
    }
    pass 
    {
        SetGeometryShader(pGSwSO);
    }
}
```



## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 




