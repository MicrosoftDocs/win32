---
title: D3DX Interfaces (Direct3D 11 Graphics)
description: This section contains reference information for the component object model (COM) interfaces provided by the D3DX utility library.
ms.assetid: 0d3be1e6-b558-4586-9440-251a5611d7cd
keywords:
- D3DX interfaces, Direct3D 11
- interfaces, Direct3D 11 D3DX
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX Interfaces (Direct3D 11 Graphics)

This section contains reference information for the component object model (COM) interfaces provided by the D3DX utility library.

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 


## In this section




| Topic | Description | 
|-------|-------------|
| [**ID3DX11DataLoader**](id3dx11dataloader.md)<br> |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> Data loading object used by [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md) for loading data asynchronously.<br> | 
| [**ID3DX11DataProcessor**](id3dx11dataprocessor.md)<br> |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> Data processing object used by [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md) for loading data asynchronously.<br> | 
| [**ID3DX11ThreadPump**](id3dx11threadpump.md)<br> |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> A thread pump executes tasks asynchronously. It is created by calling [**D3DX11CreateThreadPump**](d3dx11createthreadpump.md). There are several APIs that take an optional thread pump as a parameter, such as [**D3DX11CreateTextureFromFile**](d3dx11createtexturefromfile.md) and [**D3DX11CompileFromFile**](d3dx11compilefromfile.md); if you pass a thread pump interface into these APIs, the functions will execute asynchronously on a separate thread. Particularly on multiprocessor machines, a thread pump can load resources and process data without a noticeable decrease in performance.<br> | 




 

## Related topics

<dl> <dt>

[D3DX 11 Reference](d3d11-graphics-reference-d3dx11.md)
</dt> </dl>

 

 





