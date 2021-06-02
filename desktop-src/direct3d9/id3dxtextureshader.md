---
description: The ID3DXTextureShader interface.
ms.assetid: 48ea307d-857f-4b73-9e13-de391fbce07b
title: ID3DXTextureShader interface (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureShader
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureShader interface

The ID3DXTextureShader interface.

## Members

The **ID3DXTextureShader** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXTextureShader** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXTextureShader** interface has these methods.



| Method                                                                                       | Description                                                                 |
|:---------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**GetConstant**](id3dxtextureshader--getconstant.md)                                       | Gets a constant by looking up its index.<br/>                         |
| [**GetConstantBuffer**](id3dxtextureshader--getconstantbuffer.md)                           | Get a pointer to the constant table.<br/>                             |
| [**GetConstantByName**](id3dxtextureshader--getconstantbyname.md)                           | Gets a constant by looking up its name.<br/>                          |
| [**GetConstantDesc**](id3dxtextureshader--getconstantdesc.md)                               | Gets a pointer to the array of constants in the constant table.<br/>  |
| [**GetConstantElement**](id3dxtextureshader--getconstantelement.md)                         | Get a constant from the constant table.<br/>                          |
| [**GetDesc**](id3dxtextureshader--getdesc.md)                                               | Gets a description of the constant table.<br/>                        |
| [**GetFunction**](id3dxtextureshader--getfunction.md)                                       | Gets a pointer to the function DWORD stream.<br/>                     |
| [**SetBool**](id3dxtextureshader--setbool.md)                                               | Sets a BOOL value.<br/>                                               |
| [**SetBoolArray**](id3dxtextureshader--setboolarray.md)                                     | Sets an array of BOOL values.<br/>                                    |
| [**SetDefaults**](id3dxtextureshader--setdefaults.md)                                       | Sets the constants to the default values declared in the shader.<br/> |
| [**SetFloat**](id3dxtextureshader--setfloat.md)                                             | Sets a floating-point number.<br/>                                    |
| [**SetFloatArray**](id3dxtextureshader--setfloatarray.md)                                   | Sets an array of floating-point numbers.<br/>                         |
| [**SetInt**](id3dxtextureshader--setint.md)                                                 | Sets an integer value.<br/>                                           |
| [**SetIntArray**](id3dxtextureshader--setintarray.md)                                       | Sets an array of integers.<br/>                                       |
| [**SetMatrix**](id3dxtextureshader--setmatrix.md)                                           | Sets a non-transposed matrix.<br/>                                    |
| [**SetMatrixArray**](id3dxtextureshader--setmatrixarray.md)                                 | Sets an array of non-transposed matrices.<br/>                        |
| [**SetMatrixPointerArray**](id3dxtextureshader--setmatrixpointerarray.md)                   | Sets an array of pointers to non-transposed matrices.<br/>            |
| [**SetMatrixTranspose**](id3dxtextureshader--setmatrixtranspose.md)                         | Sets a transposed matrix.<br/>                                        |
| [**SetMatrixTransposeArray**](id3dxtextureshader--setmatrixtransposearray.md)               | Sets an array of transposed matrices.<br/>                            |
| [**SetMatrixTransposePointerArray**](id3dxtextureshader--setmatrixtransposepointerarray.md) | Sets an array of pointers to transposed matrices.<br/>                |
| [**SetValue**](id3dxtextureshader--setvalue.md)                                             | Sets the constant table with the data in the buffer.<br/>             |
| [**SetVector**](id3dxtextureshader--setvector.md)                                           | Sets a 4D vector.<br/>                                                |
| [**SetVectorArray**](id3dxtextureshader--setvectorarray.md)                                 | Sets an array of 4D vectors.<br/>                                     |



 

## Remarks

The **ID3DXTextureShader** interface is obtained by calling the [**D3DXCreateTextureShader**](d3dxcreatetextureshader.md) function.

The **ID3DXTextureShader** interface, like all COM interfaces, inherits the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface.

The LPD3DXTEXTURESHADER type is defined as a pointer to the **ID3DXTextureShader** interface.


```
typedef interface ID3DXTextureShader *LPD3DXTEXTURESHADER;
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
