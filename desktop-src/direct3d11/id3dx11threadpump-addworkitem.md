---
title: ID3DX11ThreadPump AddWorkItem method (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Adds a work item to the thread pump.
ms.assetid: 2578506c-6175-457a-bf10-94929bb3c0c4
keywords:
- AddWorkItem method Direct3D 11
- AddWorkItem method Direct3D 11 , ID3DX11ThreadPump interface
- ID3DX11ThreadPump interface Direct3D 11 , AddWorkItem method
topic_type:
- apiref
api_name:
- ID3DX11ThreadPump.AddWorkItem
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11ThreadPump::AddWorkItem method

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Adds a work item to the thread pump.

## Syntax


```C++
HRESULT AddWorkItem(
  [in]  ID3DX11DataLoader    *pDataLoader,
  [in]  ID3DX11DataProcessor *pDataProcessor,
  [in]  HRESULT              *pHResult,
  [out] void                 **ppDeviceObject
);
```



## Parameters

<dl> <dt>

*pDataLoader* \[in\]
</dt> <dd>

Type: **[**ID3DX11DataLoader**](id3dx11dataloader.md)\***

The loader that the thread pump will use when a work item requires data to be loaded.

</dd> <dt>

*pDataProcessor* \[in\]
</dt> <dd>

Type: **[**ID3DX11DataProcessor**](id3dx11dataprocessor.md)\***

The processor that the thread pump will use when a work item requires data to be processed.

</dd> <dt>

*pHResult* \[in\]
</dt> <dd>

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)\***

A pointer to the return value. May be **NULL**.

</dd> <dt>

*ppDeviceObject* \[out\]
</dt> <dd>

Type: **void\*\***

The device that uses the object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

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

 

 





