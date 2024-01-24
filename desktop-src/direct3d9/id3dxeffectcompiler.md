---
description: The ID3DXEffectCompiler interface compiles an effect from a function or from a vertex shader.
ms.assetid: 2d1dbc63-1eb9-4736-a0b5-7f899c0638be
title: ID3DXEffectCompiler interface (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectCompiler
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXEffectCompiler interface

The **ID3DXEffectCompiler** interface compiles an effect from a function or from a vertex shader.

## Members

The **ID3DXEffectCompiler** interface inherits from [**ID3DXBaseEffect**](id3dxbaseeffect.md). **ID3DXEffectCompiler** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXEffectCompiler** interface has these methods.



| Method                                                      | Description                                                                                                                                 |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**CompileEffect**](id3dxeffectcompiler--compileeffect.md) | Compile an effect.<br/>                                                                                                               |
| [**CompileShader**](id3dxeffectcompiler--compileshader.md) | Compiles a shader from an effect that contains one or more functions.<br/>                                                            |
| [**GetLiteral**](id3dxeffectcompiler--getliteral.md)       | Gets a literal status of a parameter. A literal parameter has a value that doesn't change during the lifetime of an effect.<br/>      |
| [**SetLiteral**](id3dxeffectcompiler--setliteral.md)       | Toggles the literal status of a parameter. A literal parameter has a value that doesn't change during the lifetime of an effect.<br/> |



 

## Remarks

The ID3DXEffectCompiler interface is obtained by calling [**D3DXCreateEffectCompiler**](d3dxcreateeffectcompiler.md), [**D3DXCreateEffectCompilerFromFile**](d3dxcreateeffectcompilerfromfile.md), or [**D3DXCreateEffectCompilerFromResource**](d3dxcreateeffectcompilerfromresource.md).

The LPD3DXEFFECTCOMPILER type is defined as a pointer to this interface.


```
typedef interface ID3DXEffectCompiler ID3DXEffectCompiler;
typedef interface ID3DXEffectCompiler *LPD3DXEFFECTCOMPILER;
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[**ID3DXBaseEffect**](id3dxbaseeffect.md)
</dt> <dt>

[Effect Interfaces](dx9-graphics-reference-effects-interfaces.md)
</dt> <dt>

[**D3DXCreateEffectCompiler**](d3dxcreateeffectcompiler.md)
</dt> <dt>

[**D3DXCreateEffectCompilerFromFile**](d3dxcreateeffectcompilerfromfile.md)
</dt> <dt>

[**D3DXCreateEffectCompilerFromResource**](d3dxcreateeffectcompilerfromresource.md)
</dt> </dl>

 

 




