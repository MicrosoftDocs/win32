---
description: Callback function for UVAtlas.
ms.assetid: a605ae27-10c9-49b4-98fe-8c788c2c0752
title: LPD3DXUVATLASCB
ms.topic: reference
ms.date: 05/31/2018
---

# LPD3DXUVATLASCB

Callback function for UVAtlas.

## Syntax


```
typedef HRESULT (*LPD3DXUVATLASCB ( 
    FLOAT fPercentDone,
    LPVOID lpUserContext
);
```



## Parameters

\[out\] fPercentDone - Floating point number between 0 and 1.0 that represents the percentage of calculations completed (between 0 and 100 percent).

\[in\] lpUserContext - Pointer to a user-defined value which is passed to the callback function; typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

## Return Value

This function must be implemented to return S\_OK to keep running the simulator. Any other value will halt the simulator.

## Remarks

Be sure to specify the [**Windows Data Types**](../winprog/windows-data-types.md) calling convention when declaring the callback function. Otherwise, stack overflows can occur.



| Requirement                         | Value            |
|--------------------------|-------------|
| Header                   | d3dx9mesh.h |
| Import Library           | d3dx9.lib   |
| Minimum Operating System | Windows 98  |



 

## Related topics

<dl> <dt>

[Callback Functions](dx9-graphics-reference-d3dx-callback-functions.md)
</dt> </dl>

 

 
