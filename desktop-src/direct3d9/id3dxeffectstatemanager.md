---
description: This is a user-implemented interface that allows a user to set the device state from an effect.
ms.assetid: ccd3e456-e27b-4128-b20b-99ff8dafcbe1
title: ID3DXEffectStateManager interface (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectStateManager
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectStateManager interface

This is a user-implemented interface that allows a user to set the device state from an effect. Each of the methods in this interface must be implemented by the user and will then be used as callbacks to the application when either of the following occur:

-   An effect calls [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   Effect state is dynamically updated by calling the appropriate state change API. See individual method pages for details.

When an application uses the state manager to implement custom callbacks, an effect no longer automatically saves and restores state when calling [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md) and [**ID3DXEffect::EndPass**](id3dxeffect--endpass.md). Because the application has implemented a custom save and restore behavior in the callbacks, this automatic behavior is bypassed.

## Members

The **ID3DXEffectStateManager** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXEffectStateManager** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXEffectStateManager** interface has these methods.



| Method                                                                                | Description                                                                                                                  |
|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**LightEnable**](id3dxeffectstatemanager--lightenable.md)                           | A callback function that must be implemented by a user to enable/disable a light.<br/>                                 |
| [**SetFVF**](id3dxeffectstatemanager--setfvf.md)                                     | A callback function that must be implemented by a user to set a FVF code.<br/>                                         |
| [**SetLight**](id3dxeffectstatemanager--setlight.md)                                 | A callback function that must be implemented by a user to set a light.<br/>                                            |
| [**SetMaterial**](id3dxeffectstatemanager--setmaterial.md)                           | A callback function that must be implemented by a user to set material state.<br/>                                     |
| [**SetNPatchMode**](id3dxeffectstatemanager--setnpatchmode.md)                       | A callback function that must be implemented by a user to set the number of subdivision segments for N-patches.<br/>   |
| [**SetPixelShader**](id3dxeffectstatemanager--setpixelshader.md)                     | A callback function that must be implemented by a user to set a pixel shader.<br/>                                     |
| [**SetPixelShaderConstantB**](id3dxeffectstatemanager--setpixelshaderconstantb.md)   | A callback function that must be implemented by a user to set an array of vertex shader Boolean constants.<br/>        |
| [**SetPixelShaderConstantF**](id3dxeffectstatemanager--setpixelshaderconstantf.md)   | A callback function that must be implemented by a user to set an array of vertex shader floating-point constants.<br/> |
| [**SetPixelShaderConstantI**](id3dxeffectstatemanager--setpixelshaderconstanti.md)   | A callback function that must be implemented by a user to set an array of vertex shader integer constants.<br/>        |
| [**SetRenderState**](id3dxeffectstatemanager--setrenderstate.md)                     | A callback function that must be implemented by a user to set render state.<br/>                                       |
| [**SetSamplerState**](id3dxeffectstatemanager--setsamplerstate.md)                   | A callback function that must be implemented by a user to set a sampler.<br/>                                          |
| [**SetTexture**](id3dxeffectstatemanager--settexture.md)                             | A callback function that must be implemented by a user to set a texture.<br/>                                          |
| [**SetTextureStageState**](id3dxeffectstatemanager--settexturestagestate.md)         | A callback function that must be implemented by a user to set the texture stage state.<br/>                            |
| [**SetTransform**](id3dxeffectstatemanager--settransform.md)                         | A callback function that must be implemented by a user to set a transform.<br/>                                        |
| [**SetVertexShader**](id3dxeffectstatemanager--setvertexshader.md)                   | A callback function that must be implemented by a user to set a vertex shader.<br/>                                    |
| [**SetVertexShaderConstantB**](id3dxeffectstatemanager--setvertexshaderconstantb.md) | A callback function that must be implemented by a user to set an array of vertex shader Boolean constants.<br/>        |
| [**SetVertexShaderConstantF**](id3dxeffectstatemanager--setvertexshaderconstantf.md) | A callback function that must be implemented by a user to set an array of vertex shader floating-point constants.<br/> |
| [**SetVertexShaderConstantI**](id3dxeffectstatemanager--setvertexshaderconstanti.md) | A callback function that must be implemented by a user to set an array of vertex shader integer constants.<br/>        |



 

## Remarks

A user creates an ID3DXEffectStateManager interface by implementing a class that derives from this interface, and implementing all the interface methods. Once the interface is created, you can get or set the state manager within an effect using [**ID3DXEffect::GetStateManager**](id3dxeffect--getstatemanager.md) and [**ID3DXEffect::SetStateManager**](id3dxeffect--setstatemanager.md).

The LPD3DXEFFECTSTATEMANAGER type is defined as a pointer to this interface.


```
typedef interface ID3DXEffectStateManager ID3DXEffectStateManager;
typedef interface ID3DXEffectStateManager *LPD3DXEFFECTSTATEMANAGER;
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Interfaces](dx9-graphics-reference-effects-interfaces.md)
</dt> </dl>

 

 
