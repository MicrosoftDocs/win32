---
description: Sets a pointer to an optional callback function that computes the percentage of spherical harmonic (SH) computations completed and gives the caller the option of aborting the simulator.
ms.assetid: 0a47610d-fa4e-4094-9adb-4fd9306b8a12
title: ID3DXPRTEngine::SetCallBack method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.SetCallBack
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::SetCallBack method

Sets a pointer to an optional callback function that computes the percentage of spherical harmonic (SH) computations completed and gives the caller the option of aborting the simulator.

## Syntax


```C++
HRESULT SetCallBack(
  [in] LPD3DXSHPRTSIMCB pCB,
  [in] FLOAT            Frequency,
  [in] LPVOID           lpUserContext
);
```



## Parameters

<dl> <dt>

*pCB* \[in\]
</dt> <dd>

Type: **[LPD3DXSHPRTSIMCB](lpd3dxshprtsimcb.md)**

Pointer to the [LPD3DXSHPRTSIMCB](lpd3dxshprtsimcb.md) callback function that computes the percentage of SH computations completed. The callback function must be implemented to return S\_OK to keep running the simulator. Any other value will abort the simulator.

</dd> <dt>

*Frequency* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Frequency of callback calls. The inverse of Frequency is approximately the number of times the callback function will be called.

</dd> <dt>

*lpUserContext* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Pointer to a user-defined value which is passed to the callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is S\_OK.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
