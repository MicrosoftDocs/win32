---
Description: Identifies compressed key frame animation data.
ms.assetid: 2aab46db-e0ad-4bbb-b1c5-a254ec6cb984
title: XFILECOMPRESSEDANIMATIONSET structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- XFILECOMPRESSEDANIMATIONSET
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# XFILECOMPRESSEDANIMATIONSET structure

Identifies compressed key frame animation data.

## Syntax


```C++
typedef struct XFILECOMPRESSEDANIMATIONSET {
  DWORD CompressedBlockSize;
  FLOAT TicksPerSec;
  DWORD PlaybackType;
  DWORD BufferLength;
} XFILECOMPRESSEDANIMATIONSET, *LPXFILECOMPRESSEDANIMATIONSET;
```



## Members

<dl> <dt>

**CompressedBlockSize**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Total size, in bytes, of the compressed data in the compressed key frame animation data buffer.

</dd> <dt>

**TicksPerSec**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of animation key frame ticks that occur per second.

</dd> <dt>

**PlaybackType**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Type of the animation set playback loop. See [**D3DXPLAYBACK\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb205397(v=VS.85).aspx).

</dd> <dt>

**BufferLength**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Minimum buffer size, in bytes, required to hold compressed key frame animation data. Value is equal to ( ( CompressedBlockSize + 3 ) / 4 ).

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX X File Structures](dx9-graphics-reference-d3dx-x-file-structures.md)
</dt> <dt>

[**ID3DXCompressedAnimationSet**](id3dxcompressedanimationset.md)
</dt> </dl>

 

 




