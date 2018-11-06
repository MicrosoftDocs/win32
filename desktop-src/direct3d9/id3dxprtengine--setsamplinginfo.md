---
Description: Sets sampling properties used by the precomputed radiance transfer (PRT) simulator.
ms.assetid: a33963a7-fbcb-4e1c-a4f3-fb20a99fcf9f
title: ID3DXPRTEngine::SetSamplingInfo method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.SetSamplingInfo
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::SetSamplingInfo method

Sets sampling properties used by the precomputed radiance transfer (PRT) simulator.

## Syntax


```C++
HRESULT SetSamplingInfo(
  [in] UINT  NumRays,
  [in] BOOL  UseSphere,
  [in] BOOL  UseCosine,
  [in] BOOL  Adaptive,
  [in] FLOAT AdaptiveThresh
);
```



## Parameters

<dl> <dt>

*NumRays* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Number of light rays to direct at each sample. Must be greater than zero.

</dd> <dt>

*UseSphere* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

If **TRUE**, samples will be computed over a full sphere. If **FALSE**, samples will be computed over a hemisphere.

</dd> <dt>

*UseCosine* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

If **TRUE**, use a cosine weighting of samples. If both UseCosine and UseSphere are **TRUE**, the method will fail and an error will be returned.

</dd> <dt>

*Adaptive* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Must be **FALSE**. Adaptive sampling is currently not implemented.

</dd> <dt>

*AdaptiveThresh* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Ignored.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_NOTIMPL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




