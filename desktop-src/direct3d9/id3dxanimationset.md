---
description: This interface encapsulates the minimum functionality required of an animation set by an animation controller.
ms.assetid: 'vs|directx_sdk|~\id3dxanimationset.htm'
title: ID3DXAnimationSet interface (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationSet
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationSet interface

This interface encapsulates the minimum functionality required of an animation set by an animation controller. Advanced users might want to implement this interface themselves to suit their specialized needs; for most users, however, the derived [**ID3DXCompressedAnimationSet**](id3dxcompressedanimationset.md) and [**ID3DXKeyframedAnimationSet**](id3dxkeyframedanimationset.md) interfaces should suffice.

## Members

The **ID3DXAnimationSet** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXAnimationSet** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXAnimationSet** interface has these methods.



| Method                                                                        | Description                                                                       |
|:------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**GetAnimationIndexByName**](id3dxanimationset--getanimationindexbyname.md) | Gets the index of an animation, given its name.<br/>                        |
| [**GetAnimationNameByIndex**](id3dxanimationset--getanimationnamebyindex.md) | Gets the name of an animation, given its index.<br/>                        |
| [**GetCallback**](id3dxanimationset--getcallback.md)                         | Gets information about a specific callback in the animation set.<br/>       |
| [**GetName**](id3dxanimationset--getname.md)                                 | Gets the animation set name.<br/>                                           |
| [**GetNumAnimations**](id3dxanimationset--getnumanimations.md)               | Gets the number of animations in the animation set.<br/>                    |
| [**GetPeriod**](id3dxanimationset--getperiod.md)                             | Gets the period of the animation set.<br/>                                  |
| [**GetPeriodicPosition**](id3dxanimationset--getperiodicposition.md)         | Returns time position in the local timeframe of an animation set.<br/>      |
| [**GetSRT**](id3dxanimationset--getsrt.md)                                   | Gets the scale, rotation, and translation values of the animation set.<br/> |



 

## Remarks

An animation set consists of animations for many nodes for the same animation.

The LPD3DXANIMATIONSET type is defined as a pointer to this interface.


```
typedef interface ID3DXAnimationSet ID3DXAnimationSet;
typedef interface ID3DXAnimationSet *LPD3DXANIMATIONSET;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
