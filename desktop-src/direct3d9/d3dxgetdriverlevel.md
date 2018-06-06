---
Description: Returns the driver level.
ms.assetid: e8c85201-7850-4c8d-a124-ceb76d4e24d5
title: D3DXGetDriverLevel function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**LPDIRECT3DDEVICE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9) interface representing the device.

</dd> </dl>

## Return value

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

 

 




