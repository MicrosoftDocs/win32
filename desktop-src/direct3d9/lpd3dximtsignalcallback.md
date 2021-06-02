---
description: Function prototype used by D3DXComputeIMTFromSignal to describe a user-defined signal in an input mesh's u,v space. The function evaluates a procedural signal of dimension uSignalDimension at the provided u,v coordinate.
ms.assetid: 97b07dbc-6b84-46d2-acc7-db81d94538f7
title: LPD3DXIMTSIGNALCALLBACK
ms.topic: reference
ms.date: 05/31/2018
---

# LPD3DXIMTSIGNALCALLBACK

Function prototype used by [**D3DXComputeIMTFromSignal**](d3dxcomputeimtfromsignal.md) to describe a user-defined signal in an input mesh's u,v space. The function evaluates a procedural signal of dimension uSignalDimension at the provided u,v coordinate.

## Syntax


```
typedef HRESULT (WINAPI* LPD3DXIMTSIGNALCALLBACK)
     (CONST D3DXVECTOR2 *uv,
      UINT uPrimitiveID,
      UINT uSignalDimension,
      VOID *pUserData,
      FLOAT *pfSignalOut);
```



## Parameters

\[in\] uv - A pointer to a vector that contains the vertex texture coordinate.

\[in\] uPrimitiveId - The index of the input triangle on the mesh for which the signal should be calculated.

\[in\] uSignalDimension - The number of floats to store in the array of signal data (pfSignalOut).

\[in\] pUserData - The pUserData pointer passed in to [**D3DXComputeIMTFromSignal**](d3dxcomputeimtfromsignal.md).

\[out\] pfSignalOut - An array of floats, that contains the signal data.

## Return Value

This function must be implemented to return S\_OK.

## Remarks

Be sure to specify the [**Windows Data Types**](../winprog/windows-data-types.md) calling convention when declaring the callback function. Otherwise, stack overflows can occur.



| Requirement               | Value            |
|----------------|-------------|
| Header         | d3dx9mesh.h |
| Import Library | d3dx9.lib   |



 

## Related topics

<dl> <dt>

[Callback Functions](dx9-graphics-reference-d3dx-callback-functions.md)
</dt> </dl>

 

 
