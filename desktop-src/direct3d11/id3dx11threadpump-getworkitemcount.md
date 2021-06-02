---
title: ID3DX11ThreadPump GetWorkItemCount method (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Gets the number of work items in the thread pump.
ms.assetid: 04883b25-64dc-41a3-849f-710a59e9d3da
keywords:
- GetWorkItemCount method Direct3D 11
- GetWorkItemCount method Direct3D 11 , ID3DX11ThreadPump interface
- ID3DX11ThreadPump interface Direct3D 11 , GetWorkItemCount method
topic_type:
- apiref
api_name:
- ID3DX11ThreadPump.GetWorkItemCount
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11ThreadPump::GetWorkItemCount method

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Gets the number of work items in the thread pump.

## Syntax


```C++
UINT GetWorkItemCount();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of work items queued in the thread pump.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DX11ThreadPump](id3dx11threadpump.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

