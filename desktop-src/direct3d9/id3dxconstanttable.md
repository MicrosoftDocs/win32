---
description: The ID3DXConstantTable interface is used to access the constant table. This table contains the variables that are used by high-level language shaders and effects.
ms.assetid: 5d412c77-3d35-4913-86e5-8efa0549a2bb
title: ID3DXConstantTable interface (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXConstantTable
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXConstantTable interface

The ID3DXConstantTable interface is used to access the constant table. This table contains the variables that are used by high-level language shaders and effects.

## Members

The **ID3DXConstantTable** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXConstantTable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXConstantTable** interface has these methods.



| Method                                                                                       | Description                                                                                                                        |
|:---------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**GetBufferPointer**](id3dxconstanttable--getbufferpointer.md)                             | Gets a pointer to the buffer that contains the constant table.<br/>                                                          |
| [**GetBufferSize**](id3dxconstanttable--getbuffersize.md)                                   | Gets the buffer size of the constant table.<br/>                                                                             |
| [**GetConstant**](id3dxconstanttable--getconstant.md)                                       | Gets a constant by looking up its index.<br/>                                                                                |
| [**GetConstantByName**](id3dxconstanttable--getconstantbyname.md)                           | Gets a constant by looking up its name.<br/>                                                                                 |
| [**GetConstantDesc**](id3dxconstanttable--getconstantdesc.md)                               | Gets a pointer to an array of constant descriptions in the constant table.<br/>                                              |
| [**GetConstantElement**](id3dxconstanttable--getconstantelement.md)                         | Gets a constant from an array of constants. An array is made up of elements.<br/>                                            |
| [**GetDesc**](id3dxconstanttable--getdesc.md)                                               | Gets a description of the constant table.<br/>                                                                               |
| [**GetSamplerIndex**](id3dxconstanttable--getsamplerindex.md)                               | Returns the sampler index.<br/>                                                                                              |
| [**SetBool**](id3dxconstanttable--setbool.md)                                               | Sets a Boolean value.<br/>                                                                                                   |
| [**SetBoolArray**](id3dxconstanttable--setboolarray.md)                                     | Sets an array of Boolean values.<br/>                                                                                        |
| [**SetDefaults**](id3dxconstanttable--setdefaults.md)                                       | Sets the constants to their default values. The default values are declared in the variable declarations in the shader.<br/> |
| [**SetFloat**](id3dxconstanttable--setfloat.md)                                             | Sets a floating-point number.<br/>                                                                                           |
| [**SetFloatArray**](id3dxconstanttable--setfloatarray.md)                                   | Sets an array of floating-point numbers.<br/>                                                                                |
| [**SetInt**](id3dxconstanttable--setint.md)                                                 | Sets an integer value.<br/>                                                                                                  |
| [**SetIntArray**](id3dxconstanttable--setintarray.md)                                       | Sets an array of integers.<br/>                                                                                              |
| [**SetMatrix**](id3dxconstanttable--setmatrix.md)                                           | Sets a nontransposed matrix.<br/>                                                                                            |
| [**SetMatrixArray**](id3dxconstanttable--setmatrixarray.md)                                 | Sets an array of nontransposed matrices.<br/>                                                                                |
| [**SetMatrixPointerArray**](id3dxconstanttable--setmatrixpointerarray.md)                   | Sets an array of pointers to nontransposed matrices.<br/>                                                                    |
| [**SetMatrixTranspose**](id3dxconstanttable--setmatrixtranspose.md)                         | Sets a transposed matrix.<br/>                                                                                               |
| [**SetMatrixTransposeArray**](id3dxconstanttable--setmatrixtransposearray.md)               | Sets an array of transposed matrices.<br/>                                                                                   |
| [**SetMatrixTransposePointerArray**](id3dxconstanttable--setmatrixtransposepointerarray.md) | Sets an array of pointers to transposed matrices.<br/>                                                                       |
| [**SetValue**](id3dxconstanttable--setvalue.md)                                             | Sets the contents of the buffer to the constant table.<br/>                                                                  |
| [**SetVector**](id3dxconstanttable--setvector.md)                                           | Sets a 4D vector.<br/>                                                                                                       |
| [**SetVectorArray**](id3dxconstanttable--setvectorarray.md)                                 | Sets an array of 4D vectors.<br/>                                                                                            |



 

## Remarks

The LPD3DXCONSTANTTABLE type is defined as a pointer to the **ID3DXConstantTable** interface.


```
typedef interface ID3DXConstantTable ID3DXConstantTable;
typedef interface ID3DXConstantTable *LPD3DXCONSTANTTABLE;
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

 

 
