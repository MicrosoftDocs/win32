---
title: D3DX11CreateAsyncMemoryLoader function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks. Create an asynchronous-memory loader.
ms.assetid: '0bf1e6a2-a968-4644-a7b4-e847ed4f7450'
keywords: ["D3DX11CreateAsyncMemoryLoader function Direct3D 11"]
topic_type:
- apiref
api_name:
- D3DX11CreateAsyncMemoryLoader
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
---

# D3DX11CreateAsyncMemoryLoader function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.

 

Create an asynchronous-memory loader.

## Syntax


```C++
HRESULT D3DX11CreateAsyncMemoryLoader(
  _In_  LPCVOID           pData,
  _In_  SIZE_T            cbData,
  _Out_ ID3DX11DataLoader **ppDataLoader
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Pointer to the data.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Size of the data.

</dd> <dt>

*ppDataLoader* \[out\]
</dt> <dd>

Type: **[**ID3DX11DataLoader**](id3dx11dataloader.md)\*\***

The address of a pointer to the asynchronous-data loader (see [**ID3DX11DataLoader Interface**](id3dx11dataloader.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

There’s no implementation of the ‘async loader’ outside of D3DX 10, and D3DX 11.

For Windows Store apps, the DirectX samples (for example, the [Direct3D tutorial sample](http://go.microsoft.com/fwlink/p/?linkid=255263)) include the **BasicLoader** module that uses the Windows Runtime asynchronous programming model ([**AsyncBase**](64259b9b-f427-4ffd-a611-e7a2f82362b2)).

For Win32 desktop apps, you can use the [Concurrency Runtime](56237d96-10b0-494a-9cb4-f5c5090436c5) to implement something similar to the Windows Runtime asynchronous programming model.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11async.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>    |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





