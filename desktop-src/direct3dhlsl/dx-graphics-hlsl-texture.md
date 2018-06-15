---
title: Texture Type
description: Use the following syntax to declare a texture variable.
ms.assetid: 54db5432-dab8-4a4d-a4de-93c6fa640535
keywords:
- Texture Type HLSL
topic_type:
- apiref
api_name:
- Texture Type
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Texture Type

Use the following syntax to declare a texture variable.



|                |
|----------------|
| **Type Name;** |



 

## Parameters



| Item                                                                                     | Description                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**<br/> | One of the following types: texture (untyped, for backwards compatibility), Texture1D, Texture1DArray, Texture2D, Texture2DArray, Texture3D, TextureCube. The element size must fit into 4 32-bit quantities.<br/> |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/> | An ASCII string that uniquely identifies the variable name.<br/>                                                                                                                                                   |



 

## Remarks

There are three parts to using a texture.

1.  Declaring a texture variable. This is done with the syntax shown above. For example, these are valid declarations.

    ```
    texture g_MeshTexture;
    ```

    

    \- or -

    ```
    Texture2D g_MeshTexture;
    ```

    

2.  Declaring and initializing a sampler object. This is done with slightly different syntax in Direct3D 9 and Direct3D 10. For details about sampler object syntax, see [Sampler Type (DirectX HLSL)](dx-graphics-hlsl-sampler.md).
3.  Invoking a texture function in a shader.



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Differences between Direct3D 9 and Direct3D 10:<br/> Direct3D 9 uses [<strong>intrinsic texture functions</strong>](dx-graphics-hlsl-intrinsic-functions.md) to perform texture operations. This example is from the [BasicHLSL Sample](https://msdn.microsoft.com/en-us/library/Ee416223(v=VS.85).aspx) and uses [<strong>tex2D(s, t) (DirectX HLSL)</strong>](dx-graphics-hlsl-tex2d.md) to perform texture sampling.<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>Output.RGBColor = tex2D(MeshTextureSampler, In.TextureUV) * In.Diffuse;</code></pre></td>
</tr>
</tbody>
</table>

<p>Direct3D 10 uses [templated texture objects](dx-graphics-hlsl-to-type.md) instead. Here is an example of the equivalent texture operation. This example is from the [BasicHLSL10 Sample](https://msdn.microsoft.com/en-us/library/Ee416395(v=VS.85).aspx) and uses the [sample](dx-graphics-hlsl-to-sample.md) texture-object function.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>Output.RGBColor = g_MeshTexture.Sample(MeshTextureSampler, In.TextureUV) * In.Diffuse;</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





