---
Description: Extracts the per-sample cluster IDs from an ID3DXPRTCompBuffer compressed data buffer.
ms.assetid: d78d82ab-58bc-4b73-9ca0-8b7f06867618
title: ID3DXPRTCompBufferExtractClusterIDs method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTCompBuffer::ExtractClusterIDs method

Extracts the per-sample cluster IDs from an [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) compressed data buffer.

## Syntax


```C++
HRESULT ExtractClusterIDs(
  [in, out] UINT *pClusterIDs
);
```



## Parameters

<dl> <dt>

*pClusterIDs* \[in, out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Pointer to the location in memory where IDs are written. The length of memory required is the value returned by [**ID3DXPRTCompBuffer::GetNumSamples**](id3dxprtcompbuffer--getnumsamples.md).

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

 

 




