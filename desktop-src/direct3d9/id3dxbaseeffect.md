---
description: Provides methods for getting and setting effect parameters such as constants, functions, shaders, and techniques.
ms.assetid: dd5e107d-2f09-4f6c-ad6c-52cbcbe0cbd1
title: ID3DXBaseEffect interface (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseEffect interface

Provides methods for getting and setting effect parameters such as constants, functions, shaders, and techniques.

## Members

The **ID3DXBaseEffect** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXBaseEffect** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXBaseEffect** interface has these methods.



| Method                                                                                    | Description                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAnnotation**](id3dxbaseeffect--getannotation.md)                                   | Gets the handle of an annotation. <br/>                                                                                                                                                                                     |
| [**GetAnnotationByName**](id3dxbaseeffect--getannotationbyname.md)                       | Gets the handle of an annotation by looking up its name.<br/>                                                                                                                                                               |
| [**GetBool**](id3dxbaseeffect--getbool.md)                                               | Gets a BOOL value.<br/>                                                                                                                                                                                                     |
| [**GetBoolArray**](id3dxbaseeffect--getboolarray.md)                                     | Gets an array of BOOL values.<br/>                                                                                                                                                                                          |
| [**GetDesc**](id3dxbaseeffect--getdesc.md)                                               | Gets the effect description.<br/>                                                                                                                                                                                           |
| [**GetFloat**](id3dxbaseeffect--getfloat.md)                                             | Gets a floating point value.<br/>                                                                                                                                                                                           |
| [**GetFloatArray**](id3dxbaseeffect--getfloatarray.md)                                   | Gets an array of floating point values.<br/>                                                                                                                                                                                |
| [**GetFunction**](id3dxbaseeffect--getfunction.md)                                       | Gets the handle of a function.<br/>                                                                                                                                                                                         |
| [**GetFunctionByName**](id3dxbaseeffect--getfunctionbyname.md)                           | Gets the handle of a function by looking up its name.<br/>                                                                                                                                                                  |
| [**GetFunctionDesc**](id3dxbaseeffect--getfunctiondesc.md)                               | Gets a function description.<br/>                                                                                                                                                                                           |
| [**GetInt**](id3dxbaseeffect--getint.md)                                                 | Gets an integer.<br/>                                                                                                                                                                                                       |
| [**GetIntArray**](id3dxbaseeffect--getintarray.md)                                       | Gets an array of integers.<br/>                                                                                                                                                                                             |
| [**GetMatrix**](id3dxbaseeffect--getmatrix.md)                                           | Gets a nontransposed matrix.<br/>                                                                                                                                                                                           |
| [**GetMatrixArray**](id3dxbaseeffect--getmatrixarray.md)                                 | Gets an array of nontransposed matrices.<br/>                                                                                                                                                                               |
| [**GetMatrixPointerArray**](id3dxbaseeffect--getmatrixpointerarray.md)                   | Gets an array of pointers to nontransposed matrices.<br/>                                                                                                                                                                   |
| [**GetMatrixTranspose**](id3dxbaseeffect--getmatrixtranspose.md)                         | Gets a transposed matrix.<br/>                                                                                                                                                                                              |
| [**GetMatrixTransposeArray**](id3dxbaseeffect--getmatrixtransposearray.md)               | Gets an array of transposed matrices.<br/>                                                                                                                                                                                  |
| [**GetMatrixTransposePointerArray**](id3dxbaseeffect--getmatrixtransposepointerarray.md) | Gets an array of pointers to transposed matrices.<br/>                                                                                                                                                                      |
| [**GetParameter**](id3dxbaseeffect--getparameter.md)                                     | Gets the handle of a top-level parameter or a structure member parameter.<br/>                                                                                                                                              |
| [**GetParameterByName**](id3dxbaseeffect--getparameterbyname.md)                         | Gets the handle of a top-level parameter or a structure member parameter by looking up its name.<br/>                                                                                                                       |
| [**GetParameterBySemantic**](id3dxbaseeffect--getparameterbysemantic.md)                 | Gets the handle of a top-level parameter or a structure member parameter by looking up its semantic with a case-insensitive search.<br/>                                                                                    |
| [**GetParameterDesc**](id3dxbaseeffect--getparameterdesc.md)                             | Gets a parameter or annotation description.<br/>                                                                                                                                                                            |
| [**GetParameterElement**](id3dxbaseeffect--getparameterelement.md)                       | Get the handle of an array element parameter.<br/>                                                                                                                                                                          |
| [**GetPass**](id3dxbaseeffect--getpass.md)                                               | Gets the handle of a pass.<br/>                                                                                                                                                                                             |
| [**GetPassByName**](id3dxbaseeffect--getpassbyname.md)                                   | Gets the handle of a pass by looking up its name.<br/>                                                                                                                                                                      |
| [**GetPassDesc**](id3dxbaseeffect--getpassdesc.md)                                       | Gets a pass description.<br/>                                                                                                                                                                                               |
| [**GetPixelShader**](id3dxbaseeffect--getpixelshader.md)                                 | Gets a pixel shader.<br/>                                                                                                                                                                                                   |
| [**GetString**](id3dxbaseeffect--getstring.md)                                           | Gets a string.<br/>                                                                                                                                                                                                         |
| [**GetTechnique**](id3dxbaseeffect--gettechnique.md)                                     | Gets the handle of a technique.<br/>                                                                                                                                                                                        |
| [**GetTechniqueByName**](id3dxbaseeffect--gettechniquebyname.md)                         | Gets the handle of a technique by looking up its name.<br/>                                                                                                                                                                 |
| [**GetTechniqueDesc**](id3dxbaseeffect--gettechniquedesc.md)                             | Gets a technique description.<br/>                                                                                                                                                                                          |
| [**GetTexture**](id3dxbaseeffect--gettexture.md)                                         | Gets a texture.<br/>                                                                                                                                                                                                        |
| [**GetValue**](id3dxbaseeffect--getvalue.md)                                             | Get the value of an arbitrary parameter or annotation, including simple types, structs, arrays, strings, shaders and textures. This method can be used in place of nearly all the Getxxx calls in **ID3DXBaseEffect**.<br/> |
| [**GetVector**](id3dxbaseeffect--getvector.md)                                           | Gets a vector.<br/>                                                                                                                                                                                                         |
| [**GetVectorArray**](id3dxbaseeffect--getvectorarray.md)                                 | Gets an array of vectors.<br/>                                                                                                                                                                                              |
| [**GetVertexShader**](id3dxbaseeffect--getvertexshader.md)                               | Gets a vertex shader.<br/>                                                                                                                                                                                                  |
| [**SetArrayRange**](id3dxbaseeffect--setarrayrange.md)                                   | Set the range of an array to pass to the device.<br/>                                                                                                                                                                       |
| [**SetBool**](id3dxbaseeffect--setbool.md)                                               | Sets a BOOL value.<br/>                                                                                                                                                                                                     |
| [**SetBoolArray**](id3dxbaseeffect--setboolarray.md)                                     | Sets an array of Boolean values.<br/>                                                                                                                                                                                       |
| [**SetFloat**](id3dxbaseeffect--setfloat.md)                                             | Sets a floating point value.<br/>                                                                                                                                                                                           |
| [**SetFloatArray**](id3dxbaseeffect--setfloatarray.md)                                   | Sets an array of floating point values.<br/>                                                                                                                                                                                |
| [**SetInt**](id3dxbaseeffect--setint.md)                                                 | Sets an integer.<br/>                                                                                                                                                                                                       |
| [**SetIntArray**](id3dxbaseeffect--setintarray.md)                                       | Sets an array of integers.<br/>                                                                                                                                                                                             |
| [**SetMatrix**](id3dxbaseeffect--setmatrix.md)                                           | Sets a non-transposed matrix.<br/>                                                                                                                                                                                          |
| [**SetMatrixArray**](id3dxbaseeffect--setmatrixarray.md)                                 | Sets an array of nontransposed matrices.<br/>                                                                                                                                                                               |
| [**SetMatrixPointerArray**](id3dxbaseeffect--setmatrixpointerarray.md)                   | Sets an array of pointers to nontransposed matrices.<br/>                                                                                                                                                                   |
| [**SetMatrixTranspose**](id3dxbaseeffect--setmatrixtranspose.md)                         | Sets a transposed matrix.<br/>                                                                                                                                                                                              |
| [**SetMatrixTransposeArray**](id3dxbaseeffect--setmatrixtransposearray.md)               | Sets an array of transposed matrices.<br/>                                                                                                                                                                                  |
| [**SetMatrixTransposePointerArray**](id3dxbaseeffect--setmatrixtransposepointerarray.md) | Sets an array of pointers to transposed matrices.<br/>                                                                                                                                                                      |
| [**SetString**](id3dxbaseeffect--setstring.md)                                           | Sets a string.<br/>                                                                                                                                                                                                         |
| [**SetTexture**](id3dxbaseeffect--settexture.md)                                         | Sets a texture.<br/>                                                                                                                                                                                                        |
| [**SetValue**](id3dxbaseeffect--setvalue.md)                                             | Set the value of an arbitrary parameter or annotation, including simple types, structs, arrays, strings, shaders and textures. <br/>                                                                                        |
| [**SetVector**](id3dxbaseeffect--setvector.md)                                           | Sets a vector.<br/>                                                                                                                                                                                                         |
| [**SetVectorArray**](id3dxbaseeffect--setvectorarray.md)                                 | Sets an array of vectors.<br/>                                                                                                                                                                                              |



 

## Remarks

The LPD3DXBASEEFFECT type is defined as a pointer to this interface.


```
typedef interface ID3DXBaseEffect ID3DXBaseEffect;
typedef interface ID3DXBaseEffect *LPD3DXBASEEFFECT;
        
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Interfaces](dx9-graphics-reference-effects-interfaces.md)
</dt> <dt>

[**D3DXCreateEffect**](d3dxcreateeffect.md)
</dt> </dl>

 

 
