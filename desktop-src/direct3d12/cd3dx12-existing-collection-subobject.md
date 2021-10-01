---
title: CD3DX12_EXISTING_COLLECTION_SUBOBJECT class (D3dx12.h)
description: A helper class for creating an existing collection state subobject.
keywords:
- CD3DX12_EXISTING_COLLECTION_SUBOBJECT class
topic_type:
- apiref
api_name:
- CD3DX12_EXISTING_COLLECTION_SUBOBJECT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/04/2021
---

# CD3DX12_EXISTING_COLLECTION_SUBOBJECT class

A helper class for creating an existing collection state subobject.

For more info about the D3DX12 State Object Creation Helpers, see [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md).

## Syntax

```cpp
class CD3DX12_EXISTING_COLLECTION_SUBOBJECT
{
    CD3DX12_EXISTING_COLLECTION_SUBOBJECT() noexcept;
    CD3DX12_EXISTING_COLLECTION_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC&);
    SetExistingCollection(ID3D12StateObject* pExistingCollection) noexcept;
    void DefineExport(
        LPCWSTR Name,
        LPCWSTR ExportToRename = nullptr,
        D3D12_EXPORT_FLAGS Flags = D3D12_EXPORT_FLAG_NONE);
    template<size_t N> void DefineExports(LPCWSTR(&Exports)[N]);
    void DefineExports(const LPCWSTR* Exports, UINT N);
    D3D12_STATE_SUBOBJECT_TYPE Type() const noexcept override;
    operator const D3D12_STATE_SUBOBJECT& () const noexcept;
    operator const D3D12_EXISTING_COLLECTION_DESC& () const noexcept;
};
```

## Members

`CD3DX12_EXISTING_COLLECTION_SUBOBJECT`

Default constructor. Creates a new, default-initialized, instance of a **CD3DX12_EXISTING_COLLECTION_SUBOBJECT**.

`CD3DX12_EXISTING_COLLECTION_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC&)`

Constructor that creates a new instance of a **CD3DX12_EXISTING_COLLECTION_SUBOBJECT** initialized with the contents of a [**CD3DX12_STATE_OBJECT_DESC**](cd3dx12-state-object-desc.md) object.

`SetExistingCollection(ID3D12StateObject*)`

Function for setting the existing collection in the form of the pointer to an [ID3D12StateObject](/windows/win32/api/d3d12/nn-d3d12-id3d12stateobject) passed as the parameter.

`DefineExport(LPCWSTR, LPCWSTR = nullptr, D3D12_EXPORT_FLAGS)`

Defines a symbol exported from the subobject. Takes a [D3D12_EXPORT_FLAGS](/windows/win32/api/d3d12/ne-d3d12-d3d12_export_flags) as an optional parameter.

`DefineExports(LPCWSTR(&)[N]);`

Defines an array of symbols exported from the subobject. Template parameter *N* specifies the number of elements in the array.

`DefineExports(const LPCWSTR*, UINT)`

Defines an array of *N* symbols exported from the subobject.

`Type`

Retrieves the type of the subobject, represented by the [D3D12_STATE_SUBOBJECT_TYPE_EXISTING_COLLECTION](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_subobject_type) constant.

`operator const D3D12_STATE_SUBOBJECT&`

Conversion operator that returns a reference to a constant [**D3D12_STATE_SUBOBJECT**](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_subobject) object describing the state object.

`operator const D3D12_EXISTING_COLLECTION_DESC&`

Conversion operator that returns a reference to a constant [**D3D12_EXISTING_COLLECTION_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_existing_collection_desc) object describing the state object.

## Remarks

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md)
