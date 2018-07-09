---
title: Shader Type
description: The syntax for declaring a shader variable in an effect changed from Direct3D 9 to Direct3D 10.
ms.assetid: d24ae9ad-1b3a-4a05-b28b-b6a0583c3da8
keywords:
- Shader Type HLSL
topic_type:
- apiref
api_name:
- Shader Type
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# Shader Type

The syntax for declaring a shader variable in an effect changed from Direct3D 9 to Direct3D 10.

## Shader Type for Direct3D 10

Declare a shader variable within an effect pass (in Direct3D 10) using the shader type syntax:



|                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SetPixelShader** Compile( **ShaderTarget, ShaderFunction** ); **SetGeometryShader** Compile( **ShaderTarget, ShaderFunction** ); **SetVertexShader** Compile( **ShaderTarget, ShaderFunction** ); |



 

### Parameters



| Item                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SetXXXShader"></span><span id="setxxxshader"></span><span id="SETXXXSHADER"></span>**SetXXXShader**<br/>         | The Direct3D API call that creates the shader object. Can be either: **SetPixelShader** or **SetGeometryShader** or **SetVertexShader**.<br/>                                                                                                                                                                                                                                                                                                   |
| <span id="ShaderTarget"></span><span id="shadertarget"></span><span id="SHADERTARGET"></span>**ShaderTarget**<br/>         | The shader model to compile against. This is valid for any target including all Direct3D 9 targets plus the [shader model 4](dx-graphics-hlsl-sm4.md) targets: vs\_4\_0, gs\_4\_0, and ps\_4\_0.<br/>                                                                                                                                                                                                                                          |
| <span id="ShaderFunction"></span><span id="shaderfunction"></span><span id="SHADERFUNCTION"></span>**ShaderFunction**<br/> | An ASCII string that contains the name of the shader entry point function; this is the function that begins execution when the shader is invoked. The (...) represents the shader arguments; these are the same arguments passed to the shader creation API's: [**VSSetShader**](https://msdn.microsoft.com/library/windows/desktop/bb173628) or [**GSSetShader**](https://msdn.microsoft.com/library/windows/desktop/bb173582) or [**PSSetShader**](https://msdn.microsoft.com/library/windows/desktop/bb173605).<br/> |



 

### Example

Here is an example that creates a vertex shader and pixel shader object, compiled for a particular shader model. In the Direct3D 10 example, there is no geometry shader, so the pointer is set to **NULL**.


```
// Direct3D 10
technique10 Render
{
    pass P0
    {
        SetVertexShader( CompileShader( vs_4_0, VS() ) );
        SetGeometryShader( NULL );
        SetPixelShader( CompileShader( ps_4_0, PS() ) );
    }
}
```



## Shader Type for Direct3D 9

Declare a shader variable within an effect pass (for Direct3D 9) using the shader type syntax:



|                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------|
| **PixelShader** = compile **ShaderTarget ShaderFunction(...);VertexShader** = compile **ShaderTarget ShaderFunction(...);** |



 

### Parameters



| Item                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="XXXShader"></span><span id="xxxshader"></span><span id="XXXSHADER"></span>**XXXShader**<br/>                                         | A shader variable, which represents the compiled shader. Can be either: **PixelShader** or **VertexShader**.<br/>                                                                                                                                                                                                                                                                                           |
| <span id="ShaderTarget"></span><span id="shadertarget"></span><span id="SHADERTARGET"></span>**ShaderTarget**<br/>                             | The [shader model](dx-graphics-hlsl-models.md) to compile against; depends on the type of shader variable.<br/>                                                                                                                                                                                                                                                                                            |
| <span id="ShaderFunction_..._"></span><span id="shaderfunction_..._"></span><span id="SHADERFUNCTION_..._"></span>**ShaderFunction(...)**<br/> | An ASCII string that contains the name of the shader entry point function; this is the function that begins execution when the shader is invoked. The (...) represents the shader arguments; these are the same arguments passed to the shader creation API's: [**SetVertexShader**](https://msdn.microsoft.com/library/windows/desktop/bb174465) or [**SetPixelShader**](https://msdn.microsoft.com/library/windows/desktop/bb174450).<br/> |



 

### Example

Here is an example of a vertex shader and pixel shader object, compiled for a particular shader model.


```
// Direct3D 9
technique RenderSceneWithTexture1Light
{
    pass P0
    {          
        VertexShader = compile vs_2_0 RenderSceneVS( 1, true, true );
        PixelShader  = compile ps_2_0 RenderScenePS( true );
    }
}
```



## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





