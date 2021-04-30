---
description: Add a work item to the thread pump.
ms.assetid: f07789dc-a3d5-4bad-9768-527e701271b8
title: ID3DX10ThreadPump::AddWorkItem method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10ThreadPump.AddWorkItem
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10ThreadPump::AddWorkItem method

Add a work item to the thread pump.

## Syntax


```C++
HRESULT AddWorkItem(
  [in]  ID3DX10DataLoader    *pDataLoader,
  [in]  ID3DX10DataProcessor *pDataProcessor,
  [in]  HRESULT              *pHResult,
  [out] void                 **ppDeviceObject
);
```



## Parameters

<dl> <dt>

*pDataLoader* \[in\]
</dt> <dd>

Type: **[**ID3DX10DataLoader**](id3dx10dataloader.md)\***

The loader that the thread pump will use when a work item requires data to be loaded.

</dd> <dt>

*pDataProcessor* \[in\]
</dt> <dd>

Type: **[**ID3DX10DataProcessor**](id3dx10dataprocessor.md)\***

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

 

 




