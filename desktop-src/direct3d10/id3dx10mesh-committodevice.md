---
Description: Commit any changes made to a mesh to the device so that the changes can be rendered. This should be called after a mesh's data is altered and before it is rendered. A mesh cannot be rendered unless it is committed to the device. See remarks.
ms.assetid: 26927553-d1d8-4745-85ad-a8a6fe949306
title: ID3DX10Mesh::CommitToDevice method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Mesh::CommitToDevice method

Commit any changes made to a mesh to the device so that the changes can be rendered. This should be called after a mesh's data is altered and before it is rendered. A mesh cannot be rendered unless it is committed to the device. See remarks.

## Syntax


```C++
HRESULT CommitToDevice();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

When a mesh is loaded, it's data is loaded into staging resources, meaning the data can be altered but not rendered. When CommitToDevice is called, the data from the staging resources are copied into device resources so that they can be rendered. Although the data is committed to the device, the staging resources remain and can be modified. If any modifications are made to the staging resources, the staging resources must be committed to the device again in order for those changes to be rendered on screen.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




