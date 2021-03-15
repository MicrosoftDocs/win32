---
description: Get the number of items in each of the three queues inside the thread pump.
ms.assetid: b5b829a5-5ef7-4ef5-afb4-efe1bb22ae70
title: ID3DX10ThreadPump::GetQueueStatus method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10ThreadPump.GetQueueStatus
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10ThreadPump::GetQueueStatus method

Get the number of items in each of the three queues inside the thread pump.

## Syntax


```C++
HRESULT GetQueueStatus(
  [in] UINT *pIoQueue,
  [in] UINT *pProcessQueue,
  [in] UINT *pDeviceQueue
);
```



## Parameters

<dl> <dt>

*pIoQueue* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Number of items in the I/O queue.

</dd> <dt>

*pProcessQueue* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Number of items in the process queue.

</dd> <dt>

*pDeviceQueue* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Number of items in the device queue.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10ThreadPump](id3dx10threadpump.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
