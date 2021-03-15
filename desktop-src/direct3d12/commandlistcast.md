---
title: CommandListCast function (D3dx12.h)
description: This function template casts a constant pointer to any command list into a const pointer to an ID3D12CommandList.
ms.assetid: 63719AA1-2119-456C-9D23-13933D38AFA9
keywords:
- CommandListCast function
topic_type:
- apiref
api_name:
- CommandListCast
api_location:
- D3D12.dll
api_type:
- DllExport
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CommandListCast function

This function template casts a constant pointer to any command list into a const pointer to an ID3D12CommandList.

This cast is useful for passing strongly-typed command list pointers into [**ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists).

## Syntax


```C++
ID3D12CommandList * const * inline CommandListCast(
   t_CommandListType * const * pp
);
```



## Parameters

<dl> <dt>

*pp* 
</dt> <dd>

Type: **t\_CommandListType \* const \***

The strongly-typed command list to cast.

The template argument **t\_CommandListType** specifies any strongly-typed command list object.

</dd> </dl>

## Return value

Type: **ID3D12CommandList \* const \***

The strongly-typed command list, reinterpreted as an [**ID3D12CommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandlist).

## Remarks

CommandListCast performs a **reinterpret\_cast**. The cast is valid as long as the const-ness of the command list is respected.

The CommandListCast function is defined as the following:


```C++
template <typename t_CommandListType>
inline ID3D12CommandList * const * CommandListCast(t_CommandListType * const * pp)
{
    return reinterpret_cast<ID3D12CommandList * const *>(pp);
}
          
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> </dl>

 

 





