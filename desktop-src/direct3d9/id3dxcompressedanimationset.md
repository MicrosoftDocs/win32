---
description: An application uses the methods of this interface to implement a key frame animation set stored in a compressed data format.
ms.assetid: 858f09b7-c3b6-4e22-8017-ce2d6188ba80
title: ID3DXCompressedAnimationSet interface (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXCompressedAnimationSet
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXCompressedAnimationSet interface

An application uses the methods of this interface to implement a key frame animation set stored in a compressed data format.

## Members

The **ID3DXCompressedAnimationSet** interface inherits from [**ID3DXAnimationSet**](id3dxanimationset.md). **ID3DXCompressedAnimationSet** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXCompressedAnimationSet** interface has these methods.



| Method                                                                                  | Description                                                                      |
|:----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**GetCallbackKeys**](id3dxcompressedanimationset--getcallbackkeys.md)                 | Fills an array with callback key data used for key frame animation.<br/>   |
| [**GetCompressedData**](id3dxcompressedanimationset--getcompresseddata.md)             | Gets the data buffer that stores compressed key frame animation data.<br/> |
| [**GetNumCallbackKeys**](id3dxcompressedanimationset--getnumcallbackkeys.md)           | Gets the number of callback keys in the animation set.<br/>                |
| [**GetPlaybackType**](id3dxcompressedanimationset--getplaybacktype.md)                 | Gets the type of the animation set playback loop.<br/>                     |
| [**GetSourceTicksPerSecond**](id3dxcompressedanimationset--getsourcetickspersecond.md) | Gets the number of animation key frame ticks that occur per second.<br/>   |



 

## Remarks

Create a compressed-format key frame animation set with [**D3DXCreateCompressedAnimationSet**](d3dxcreatecompressedanimationset.md).

The LPD3DXCOMPRESSEDANIMATIONSET type is defined as a pointer to this interface.


```
typedef interface ID3DXCompressedAnimationSet ID3DXCompressedAnimationSet;
typedef interface ID3DXCompressedAnimationSet *LPD3DXCOMPRESSEDANIMATIONSET;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[**ID3DXAnimationSet**](id3dxanimationset.md)
</dt> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 




