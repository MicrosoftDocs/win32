---
Description: Saves a compressed precomputed radiance transfer (PRT) buffer to disk.
ms.assetid: cc94a83e-f755-411d-a993-4529c5d53cd5
title: D3DXSavePRTCompBufferToFile function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSavePRTCompBufferToFile
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSavePRTCompBufferToFile function

Saves a compressed precomputed radiance transfer (PRT) buffer to disk.

## Syntax


```C++
HRESULT D3DXSavePRTCompBufferToFile(
  _In_ LPCSTR              pFileName,
  _In_ LPD3DXPRTCOMPBUFFER pBuffer
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Name of the file to which the compressed buffer is to be saved.

</dd> <dt>

*pBuffer* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTCOMPBUFFER**](id3dxprtcompbuffer.md)**

Address of a pointer to the input [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSavePRTCompBufferToFileW. Otherwise, the function call resolves to D3DXSavePRTCompBufferToFileA.

The PCA file format is a binary file in the form of a header and then two or three data blocks.

```C++
struct PRTCompressHeader
{
    UINT NumSamples;
    UINT NumCoeffs;
    UINT NumChannels;
    UINT TexWidth;
    UINT TexHeight;
    UINT bIsTex;
    UINT NumClusters;
    UINT NumPCA;
};
```

For the case of ``bIsTex`` being non-zero, ``NumSamples`` should equal ``TexWidth * TexHeight``.

The basis data block that follows the header is ``NumCoeffs * NumChannels * (NumPCA+1) * NumClusters * sizeof(float)`` bytes.

Following that is the PCA weights data block which is ``NumPCA * NumSamples * sizeof(float)`` bytes

If ``NumClusters`` is greater than 1, then the file ends with the cluster IDs data block of ``NumSamples * sizeof(UINT)`` bytes.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 
