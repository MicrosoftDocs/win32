---
title: Effect Function Syntax (Direct3D 11)
description: An effect function is written in HLSL and is declared with the syntax described in this section.
ms.assetid: '5e12ba65-98bf-4f21-be75-602687157eb1'
---

# Effect Function Syntax (Direct3D 11)

An effect function is written in HLSL and is declared with the syntax described in this section.

## Syntax

*ReturnType* *FunctionName* ( \[ *ArgumentList* \] )

{

<dl> \[ *Statements* \]  
</dl>

};



| Name         | Description                                                                                                                                                                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReturnType   | Any [HLSL type](https://msdn.microsoft.com/library/windows/desktop/bb509706)                                                                                                                                                                                                       |
| FunctionName | An ASCII string that uniquely identifies the name of the shader function.                                                                                                                                                                                            |
| ArgumentList | One or more arguments, separated by commas (see [Function Arguments (DirectX HLSL)](https://msdn.microsoft.com/library/windows/desktop/bb509606)).                                                                                                                             |
| Statements   | One or more statements (see [Statements (DirectX HLSL)](https://msdn.microsoft.com/library/windows/desktop/bb509663)) that make up the body of the function. If a function is defined without a body, it is considered to be a prototype; and must be redefined with a body before use. |



 

An effect function may be a shader or it may simply be a function called by a shader. A function is uniquely identified by its name, the types of its parameters, and the target platform; therefore, functions can be overloaded. Any valid HLSL function should fit this format; for a more detailed list of syntax for HLSL functions, see [Functions (DirectX HLSL)](https://msdn.microsoft.com/library/windows/desktop/bb509605).

## Example

The following is an example of a pixel shader function.


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

[Effect Format](d3d11-effect-format.md)
</dt> </dl>

 

 




