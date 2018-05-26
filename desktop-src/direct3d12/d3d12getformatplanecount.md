---
title: D3D12GetFormatPlaneCount function
description: Gets the number of planes for the specified DXGI format for the specified virtual adapter (an ID3D12Device).
ms.assetid: CD21F6F9-A9AA-4CE8-A430-57C70326CB4B
keywords:
- D3D12GetFormatPlaneCount function
topic_type:
- apiref
api_name:
- D3D12GetFormatPlaneCount
api_location:
- D3D12.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3D12GetFormatPlaneCount function

Gets the number of planes for the specified DXGI format for the specified virtual adapter (an **ID3D12Device**).

## Syntax


```C++
UINT8 inline D3D12GetFormatPlaneCount(
  _In_ ID3D12Device *pDevice,
       DXGI_FORMAT  Format
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D12Device**](/windows/win32/D3D12/nn-d3d12-id3d12device?branch=master)\***

The virtual adapter (an [**ID3D12Device**](/windows/win32/D3D12/nn-d3d12-id3d12device?branch=master)) for which to get the plane count.

</dd> <dt>

*Format* 
</dt> <dd>

Type: **[**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)**

The [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) for which to get the plane count.

</dd> </dl>

## Return value

Type: **UINT8**

The plane count for the specified format on the specified virtual adapter.

## Requirements



|                    |                                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_FEATURE\_DATA\_FORMAT\_INFO**](/windows/win32/d3d12/ns-d3d12-d3d12_feature_data_format_info?branch=master)
</dt> <dt>

[**CheckFeatureSupport**](/windows/win32/D3D12/nf-d3d12-id3d12device-checkfeaturesupport?branch=master)
</dt> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> </dl>

 

 





