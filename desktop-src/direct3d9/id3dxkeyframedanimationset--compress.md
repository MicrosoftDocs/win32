---
Description: Transforms animations in an animation set into a compressed format and returns a pointer to the buffer that stores the compressed data.
ms.assetid: b70b6dfb-545f-4309-ab72-9543c3c48fc4
title: ID3DXKeyframedAnimationSet::Compress method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXKeyframedAnimationSet::Compress method

Transforms animations in an animation set into a compressed format and returns a pointer to the buffer that stores the compressed data.

## Syntax


```C++
HRESULT Compress(
  [in]  DWORD        Flags,
  [in]  FLOAT        Lossiness,
  [in]  LPD3DXFRAME  pHierarchy,
  [out] LPD3DXBUFFER *ppCompressedData
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

One of the [**D3DXCOMPRESSION\_FLAGS**](https://msdn.microsoft.com/windows/desktop/41592b71-52ba-4727-a885-fb10fc23c5f8) values that define the compression mode used for storing compressed animation set data. D3DXCOMPRESS\_DEFAULT is the only value currently supported.

</dd> <dt>

*Lossiness* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Desired compression loss ratio, in the range from 0 to 1.

</dd> <dt>

*pHierarchy* \[in\]
</dt> <dd>

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

Pointer to a [**D3DXFRAME**](d3dxframe.md) transformation frame hierarchy. Can be **NULL**.

</dd> <dt>

*ppCompressedData* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to the [**ID3DXBuffer**](id3dxbuffer.md) compressed animation set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXKeyframedAnimationSet](id3dxkeyframedanimationset.md)
</dt> </dl>

 

 




