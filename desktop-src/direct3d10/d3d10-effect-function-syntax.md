---
Description: An effect function is written in HLSL and is declared with the following syntax.
ms.assetid: 5ac85f09-50ac-4e8f-b4d2-ae8306b59348
title: Effect Function Syntax (Direct3D 10)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Effect Function Syntax (Direct3D 10)

An effect function is written in HLSL and is declared with the following syntax.

## Syntax

*ReturnType* *FunctionName* ( \[ *ArgumentList* \] )

{

<dl> \[ *Statements* \]  
</dl>

};



| Name         | Description                                                                                                                                                                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReturnType   | Any [HLSL type](https://msdn.microsoft.com/windows/desktop/684c42d1-2dd4-42e1-9cff-580edb5c6bcd)                                                                                                                                                                                                       |
| FunctionName | An ASCII string that uniquely identifies the name of the shader function.                                                                                                                                                                                            |
| ArgumentList | One or more arguments, separated by commas (see [Function Arguments (DirectX HLSL)](https://msdn.microsoft.com/windows/desktop/80e0dbc8-26b7-4250-bb01-6856fc70f6b8)).                                                                                                                             |
| Statements   | One or more statements (see [Statements (DirectX HLSL)](https://msdn.microsoft.com/windows/desktop/a7bb89c8-07e6-4853-9aad-12a4d4271e43)) that make up the body of the function. If a function is defined without a body, it is considered to be a prototype; and must be redefined with a body before use. |



 

An effect function may be a shader or it may simply be a function called by a shader. A function is uniquely identified by its name, the types of its parameters, and the target platform; therefore, functions can be overloaded. Any valid HLSL function should fit this format; for a more detailed list of syntax for HLSL functions, see [Functions (DirectX HLSL)](https://msdn.microsoft.com/windows/desktop/b6f934e5-eac7-4859-b1d0-698632011e1d).

## Example

The [BasicHLSL10 sample](https://msdn.microsoft.com/windows/desktop/e749975d-211e-f7ed-5dd1-b9c29681c71b) uses both a pixel shader and a vertex shader. The pixel shader function is called RenderScenePS and is shown below.


```
       
PS_OUTPUT RenderScenePS( VS_OUTPUT In,
                         uniform bool bTexture ) 
{ 
    PS_OUTPUT Output;

    // Lookup mesh texture and modulate it with diffuse
    if( bTexture )
        Output.RGBColor = g_MeshTexture.Sample(MeshTextureSampler, In.TextureUV) *  
                              In.Diffuse;
    else
        Output.RGBColor = In.Diffuse;

    return Output;
}
```



## Related topics

<dl> <dt>

[Effect Format](d3d10-effect-format.md)
</dt> </dl>

 

 



