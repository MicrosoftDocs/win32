---
title: ID3D12Resource GetDesc method
description: Gets the resource description.
ms.assetid: B8D84D69-6B13-4E86-8EF6-A841354B1E5C
keywords:
- GetDesc method
- GetDesc method, ID3D12Resource interface
- ID3D12Resource interface, GetDesc method
topic_type:
- apiref
api_name:
- ID3D12Resource.GetDesc
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
- d3d12.h
---

# ID3D12Resource::GetDesc method

Gets the resource description.

## Syntax


```C++
D3D12_RESOURCE_DESC GetDesc();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**D3D12\_RESOURCE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_desc)**

A Direct3D 12 resource description structure.

## Examples

Returns required size of a buffer to be used for data upload.


```C++
// Returns required size of a buffer to be used for data upload
inline UINT64 GetRequiredIntermediateSize(
    _In_ ID3D12Resource* pDestinationResource,
    _In_range_(0,D3D12_REQ_SUBRESOURCES) UINT FirstSubresource,
    _In_range_(0,D3D12_REQ_SUBRESOURCES-FirstSubresource) UINT NumSubresources)
{
    D3D12_RESOURCE_DESC Desc = pDestinationResource->GetDesc();
    UINT64 RequiredSize = 0;
    
    ID3D12Device* pDevice;
    pDestinationResource->GetDevice(__uuidof(*pDevice), reinterpret_cast<void**>(&pDevice));
    pDevice->GetCopyableFootprints(&Desc, FirstSubresource, NumSubresources, 0, nullptr, nullptr, nullptr, &RequiredSize);
    pDevice->Release();
    
    return RequiredSize;
}
```



Refer to the [Example Code in the D3D12 Reference](notes-on-example-code.md).

## See also

<dl> <dt>

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)
</dt> </dl>

 

 




