---
Description: 'Extracts the mean and principal component analysis (PCA) basis vectors for a given cluster from an ID3DXPRTCompBuffer compressed data buffer.'
ms.assetid: 'dcb1372f-2c8f-4d18-9840-5982b2ed0d6e'
title: 'ID3DXPRTCompBuffer::ExtractBasis method'
---

# ID3DXPRTCompBuffer::ExtractBasis method

Extracts the mean and principal component analysis (PCA) basis vectors for a given cluster from an [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) compressed data buffer.

## Syntax


```C++
HRESULT ExtractBasis(
  [in]      UINT  Cluster,
  [in, out] FLOAT *pClusterBasis
);
```



## Parameters

<dl> <dt>

*Cluster* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Cluster for which the basis will be extracted.

</dd> <dt>

*pClusterBasis* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to an array of basis vector data for Cluster. The size of the FLOAT data stored will be: (1 + Number of PCA vectors per cluster) \* (Number of coefficients) \* (Number of color channels)

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTCompBuffer](id3dxprtcompbuffer.md)
</dt> </dl>

 

 




