---
description: Locks a range of vertex or texel sample data and obtains a pointer to the location in buffer memory.
ms.assetid: 8de2725f-507e-41ee-828d-2fb19cc2252c
title: ID3DXPRTBuffer::LockBuffer method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTBuffer.LockBuffer
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::LockBuffer method

Locks a range of vertex or texel sample data and obtains a pointer to the location in buffer memory.

## Syntax


```C++
HRESULT LockBuffer(
  [in]  UINT  Start,
  [in]  UINT  NumSamples,
  [out] FLOAT **ppData
);
```



## Parameters

<dl> <dt>

*Start* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Index of the sample of vertex or texel data.

</dd> <dt>

*NumSamples* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vertices (or texels) sampled.

</dd> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\*\***

Pointer to the location in memory where the Start sample begins. The memory layout of the buffer data is:


```
float fData[NumberSamples][NumberChannels][NumberCoefficients]      
```



</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned:

## Remarks

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> <dt>

[**ID3DXPRTBuffer::GetNumChannels**](id3dxprtbuffer--getnumchannels.md)
</dt> <dt>

[**ID3DXPRTBuffer::GetNumCoeffs**](id3dxprtbuffer--getnumcoeffs.md)
</dt> <dt>

[**ID3DXPRTBuffer::GetNumSamples**](id3dxprtbuffer--getnumsamples.md)
</dt> </dl>

 

 
