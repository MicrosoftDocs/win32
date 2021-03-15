---
description: ID3DXInclude is a user-implemented interface to provide callbacks for \#include directives during shader compilation.
ms.assetid: 8e0bfff1-8d6d-4381-b9fd-f5f64f854712
title: ID3DXInclude interface (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXInclude
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXInclude interface

ID3DXInclude is a user-implemented interface to provide callbacks for \#include directives during shader compilation. Each of the methods in this interface must be implemented by the user which will then be used as callbacks to the application when one of the following occurs:

-   An HLSL shader that contains a \#include is compiled by calling one of the D3DXCompileShader\*\*\* functions.
-   An assembly shader \#include is assembled by calling any of the D3DXAssembleShader\*\*\* functions.
-   An effect that contains a \#include is compiled by by calling any of the D3DXCreateEffect\*\*\* or D3DXCreateEffectCompiler\*\*\* functions.

## Members

The **ID3DXInclude** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXInclude** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXInclude** interface has these methods.



| Method                               | Description                                                                                           |
|:-------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**Close**](id3dxinclude--close.md) | A user-implemented method for closing a shader \#include file.<br/>                             |
| [**Open**](id3dxinclude--open.md)   | A user-implemented method for opening and reading the contents of a shader \#include file.<br/> |



 

## Remarks

A user creates an ID3DXInclude interface by implementing a class that derives from this interface, and implementing all the interface methods.

The LPD3DXINCLUDE type is defined as a pointer to this interface.


```
typedef interface ID3DXInclude ID3DXInclude;
typedef interface ID3DXInclude *LPD3DXINCLUDE;
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Interfaces](dx9-graphics-reference-effects-interfaces.md)
</dt> </dl>

 

 
