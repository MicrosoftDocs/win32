---
Description: Returns the driver level.
ms.assetid: e8c85201-7850-4c8d-a124-ceb76d4e24d5
title: D3DXGetDriverLevel function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXGetDriverLevel function

Returns the driver level.

## Syntax


```C++
UINT D3DXGetDriverLevel(
  _In_ LPDIRECT3DDEVICE9 pDevice
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface representing the device.

</dd> </dl>

## Return value

Type: **[**UINT**](winprog.windows_data_types)**

The driver level. See remarks.

## Remarks

This method returns the driver version, which is one of the following:

-   700 - Direct3D 7 level driver
-   800 - Direct3D 8 level driver
-   900 - Direct3D 9 level driver

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](dx9-graphics-reference-d3dx-functions-general-purpose.md)
</dt> </dl>

 

 




