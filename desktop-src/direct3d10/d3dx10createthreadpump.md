---
Description: Create a thread pump.
ms.assetid: a7a016e2-784d-4d7a-8058-88895bf3c4e2
title: D3DX10CreateThreadPump function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CreateThreadPump function

Create a thread pump.

## Syntax


```C++
HRESULT D3DX10CreateThreadPump(
  _In_  UINT              cIoThreads,
  _In_  UINT              cProcThreads,
  _Out_ ID3DX10ThreadPump **ppThreadPump
);
```



## Parameters

<dl> <dt>

*cIoThreads* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of I/O threads to create. If 0 is specified, Direct3D will attempt to calculate the optimal number of threads based on the hardware configuration.

</dd> <dt>

*cProcThreads* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of process threads to create. If 0 is specified, Direct3D will attempt to calculate the optimal number of threads based on the hardware configuration.

</dd> <dt>

*ppThreadPump* \[out\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\*\***

The created thread pump. See [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

A thread pump is a very resource-intensive object. Only one thread pump should be created per application.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




