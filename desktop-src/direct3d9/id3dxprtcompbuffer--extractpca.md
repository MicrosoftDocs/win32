---
description: Extracts the per-sample principal component analysis (PCA) projection coefficients from an ID3DXPRTCompBuffer compressed data buffer.
ms.assetid: 149098c2-35ca-46e9-a13a-94906c95cfd9
title: ID3DXPRTCompBuffer::ExtractPCA method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTCompBuffer.ExtractPCA
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTCompBuffer::ExtractPCA method

Extracts the per-sample principal component analysis (PCA) projection coefficients from an [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) compressed data buffer.

## Syntax


```C++
HRESULT ExtractPCA(
  [in] UINT  StartPCA,
  [in] UINT  NumExtract,
  [in] FLOAT *pPCACoefficients
);
```



## Parameters

<dl> <dt>

*StartPCA* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Starting index for PCA projection coefficients to extract from the buffer.

</dd> <dt>

*NumExtract* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of PCA projection coefficients to extract from the buffer.

</dd> <dt>

*pPCACoefficients* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to the location where clustered principal component analysis (CPCA) coefficients are written. The size of the data written is (Number of Samples) \* (Number of PCA Coefficients).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTCompBuffer](id3dxprtcompbuffer.md)
</dt> </dl>

 

 
