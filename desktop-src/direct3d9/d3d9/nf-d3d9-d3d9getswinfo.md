---
title: D3D9GetSWInfo
description: Retrieves info about the software Direct3D device.
ms.topic: reference
ms.date: 08/08/2024
req.lib: 
req.dll: rgb9rast.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- rgb9rast.dll
api_name:
- D3D9GetSWInfo
targetos: Windows
ms.localizationpriority: low
---

# D3D9GetSWInfo function

Retrieves info about the software Direct3D device.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
HRESULT APIENTRY
D3D9GetSWInfo(
  D3DCAPS9           *pCaps,
  PD3D8_SWCALLBACKS   pCallbacks,
  DWORD              *pNumTextures,
  DDSURFACEDESC     **ppTexList,
  DWORD              *pNumQueries,
  D3DQUERYTYPE      **ppQueries
);
```

## Parameters

`pCaps`

**D3DCAPS9** is a standard Direct3D 9 API structure. The software driver fills this out to indicate what capabilities are supported.

`pCallbacks`

**PD3D8_SWCALLBACKS** is a pointer to a struct that represents the set of functions that the software driver implements that are called by Direct3D.

`pNumTextures`

Used to retrieve the number of textures that the software driver supports.

`ppTexList`

**DDSURFACEDESC** is a structure that defines what operations you can perform for a given texture format. *ppTexList* is an array of those that's allocated and filled out by **D3D9GetSWInfo**.

`pNumQueries`

Used to retrieve the number of queries that the software driver supports.

`ppQueries`

**D3DQUERYTYPE** is an enumerated type. *ppQueries* is an array that's allocated and filled out by **D3D9GetSWInfo**.

## Return value

An **HRESULT** value indicating success or failure.

## Remarks

This function doesn't have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`rgb9rast.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

Also, on GitHub, see the sample apps [DirectX Video Acceleration (DXVA) 2 sample](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/multimedia/mediafoundation/dxva2_videoproc) and [DXVA-HD sample](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/multimedia/mediafoundation/DXVA_HD). Those sample apps make calls to **D3D9GetSWInfo**.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10 [desktop apps only] |
| **Minimum supported server** | Windows Server 2016 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | rgb9rast.dll |
