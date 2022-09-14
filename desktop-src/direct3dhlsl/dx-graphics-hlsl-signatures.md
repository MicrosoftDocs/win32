---
title: Signatures
description: A shader signature is a list of the parameters that are either input to or output from a shader function.
ms.assetid: c73a4f3e-e6fa-4e49-9ee8-4e200269dba7
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Signatures

A shader signature is a list of the parameters that are either input to or output from a shader function. In Direct3D 10, adjacent stages effectively share a register array, where the output shader (or pipeline stage) writes data to specific locations in the register array and the input shader must read from the same locations. The API uses shader signatures to bind shader outputs with inputs without the overhead of semantic resolution.

In Direct3D 10, input signatures are generated from a shader-input declaration and the output signature is generated from a shader-output declaration. An input signature is said to be compatible with an output signature when the output signature is a strict subset (argument type and order match) of the input signature. The most straightforward way to achieve this is to link corresponding shader inputs and outputs by the same structure type.

Here is an example of compatible signatures.


```
// Vertex Shader Output Signature
Struct VSOut
{
  float4 Pos: SV_Position;
  float3 MyNormal: Normal;
  float2 MyTex : Texcoord0;
}

// Pixel Shader Input Signature
Struct PSInWorks
{
  float4 Pos: SV_Position;
  float3 MyNormal: Normal;
}
```



Here is an example of incompatible signatures; the order of parameters in the input signature does not match the order in the output signature.


```
// Vertex Shader Output Signature
Struct VSOut
{
  float4 Pos: SV_Position;
  float3 MyNormal: Normal;
  float2 MyTex : Texcoord0;
}

// Pixel Shader Input Signature
Struct PSInFails
{
  float3 MyNormal: Normal;
  float4 Pos: SV_Position;
}
```



PSInWorks is a compatible subset of VSOut (the first two entries match both type and order with the first two entries in VSOut). However, PSInFails is incompatible because the ordering does not match with VSOut.

## Related topics

<dl> <dt>

[Functions](dx-graphics-hlsl-functions.md)
</dt> </dl>

 

 




