---
description: These flags provide additional information about effect parameters.
ms.assetid: 7e1e4c64-56b8-4fdb-8178-50f7d61b917b
title: D3DX_PARAMETER (D3dx9effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX_PARAMETER_ANNOTATION
- D3DX_PARAMETER_LITERAL
- D3DX_PARAMETER_SHARED
api_type: 
- HeaderDef
api_location: 
- d3dx9effect.h
---

# D3DX\_PARAMETER

These flags provide additional information about effect parameters.

Effect parameter constants are used by [**D3DXPARAMETER\_DESC**](d3dxparameter-desc.md).



| Constant                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="D3DX_PARAMETER_ANNOTATION"></span><span id="d3dx_parameter_annotation"></span><dl> <dt>**D3DX\_PARAMETER\_ANNOTATION**</dt> </dl> | This parameter is marked as an annotation. See [Add Information to Effect Parameters with Annotations](using-an-effect.md).<br/>                                                                                                                                                                                                 |
| <span id="D3DX_PARAMETER_LITERAL"></span><span id="d3dx_parameter_literal"></span><dl> <dt>**D3DX\_PARAMETER\_LITERAL**</dt> </dl>          | This parameter is marked as a literal value. Literal parameters cannot change after compile, allowing the compiler to optimize their usage. Shared parameters cannot be marked as a literal. See [Usages and Literals (Direct3D 9)](usages-and-literals.md). <br/>                                                               |
| <span id="D3DX_PARAMETER_SHARED"></span><span id="d3dx_parameter_shared"></span><dl> <dt>**D3DX\_PARAMETER\_SHARED**</dt> </dl>             | The value of a parameter will be shared by all effects in the same namespace. Changing the value in one effect will change it in all shared effects. See [Sharing Parameters](cloning-and-sharing.md). **D3DX\_PARAMETER\_SHARED** cannot be combined with **D3DX\_PARAMETER\_LITERAL** or **D3DX\_PARAMETER\_ANNOTATION**.<br/> |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Constants](dx9-graphics-reference-effects-constants.md)
</dt> </dl>

 

 




