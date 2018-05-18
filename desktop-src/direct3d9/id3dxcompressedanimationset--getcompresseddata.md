---
Description: 'Gets the data buffer that stores compressed key frame animation data.'
ms.assetid: 'cb42a4c8-6420-4694-9921-0d36cfe960e5'
title: 'ID3DXCompressedAnimationSet::GetCompressedData method'
---

# ID3DXCompressedAnimationSet::GetCompressedData method

Gets the data buffer that stores compressed key frame animation data.

## Syntax


```C++
HRESULT GetCompressedData(
  [out] LPD3DXBUFFER *ppCompressedData
);
```



## Parameters

<dl> <dt>

*ppCompressedData* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to the [**ID3DXBuffer**](id3dxbuffer.md) data buffer that receives compressed key frame animation data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXCompressedAnimationSet](id3dxcompressedanimationset.md)
</dt> </dl>

 

 




