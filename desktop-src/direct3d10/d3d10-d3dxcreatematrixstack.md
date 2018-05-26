---
Description: Create a matrix stack.
ms.assetid: df0f3564-0226-44b8-b22b-4dd27905c44c
title: D3DXCreateMatrixStack function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreateMatrixStack function

Create a matrix stack.

## Syntax


```C++
HRESULT D3DXCreateMatrixStack(
  _In_  UINT              Flags,
  _Out_ LPD3DXMATRIXSTACK *ppStack
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Not implemented. Specify zero.

</dd> <dt>

*ppStack* \[out\]
</dt> <dd>

Type: **LPD3DXMATRIXSTACK\***

The address of a pointer to a matrix stack (see [**ID3DXMatrixStack Interface**](d3d10-id3dxmatrixstack.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




