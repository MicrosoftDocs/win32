---
description: Applications use the ID3DXEffectPool interface to identify parameters that are going to be shared across effects. See parameter sharing in Cloning and Sharing (Direct3D 9). This interface has no methods.
ms.assetid: dd5e55eb-9436-422d-9743-38be44d05962
title: ID3DXEffectPool interface (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectPool
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXEffectPool interface

Applications use the **ID3DXEffectPool** interface to identify parameters that are going to be shared across effects. See parameter sharing in [Cloning and Sharing (Direct3D 9)](cloning-and-sharing.md). This interface has no methods.

## Members

The **ID3DXEffectPool** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Remarks

The ID3DXEffectPool interface is obtained by calling [**D3DXCreateEffectPool**](d3dxcreateeffectpool.md).

The LPD3DXEFFECTPOOL type is defined as a pointer to this interface.


```
typedef interface ID3DXEffectPool ID3DXEffectPool;
typedef interface ID3DXEffectPool *LPD3DXEFFECTPOOL;
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

 

 
