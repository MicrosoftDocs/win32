---
Description: 'Get the number of items in each of the three queues inside the thread pump.'
ms.assetid: 'b5b829a5-5ef7-4ef5-afb4-efe1bb22ae70'
title: 'ID3DX10ThreadPump::GetQueueStatus method'
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

Type: **[**UINT**](winprog.windows_data_types)\***

Number of items in the I/O queue.

</dd> <dt>

*pProcessQueue* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Number of items in the process queue.

</dd> <dt>

*pDeviceQueue* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Number of items in the device queue.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10ThreadPump](id3dx10threadpump.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




