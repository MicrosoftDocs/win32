---
title: CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION class (D3dx12.h)
description: A helper class for creating a DXIL-subobject-to-exports association state subobject.
keywords:
- CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION class
topic_type:
- apiref
api_name:
- CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 08/04/2021
---

# CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION class

A helper class for creating a DXIL-subobject-to-exports association state subobject.

For more info about the D3DX12 State Object Creation Helpers, see [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md).

## Syntax

```cpp
class CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION
{
    CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION() noexcept;
    CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION(CD3DX12_STATE_OBJECT_DESC& ContainingStateObject);
    void SetSubobjectNameToAssociate(LPCWSTR SubobjectToAssociate);
    void AddExport(LPCWSTR Export);
    template<size_t N> void AddExports(LPCWSTR(&Exports)[N]);
    void AddExports(const LPCWSTR* Exports, UINT N);
    D3D12_STATE_SUBOBJECT_TYPE Type() const noexcept override;
    operator const D3D12_STATE_SUBOBJECT& () const noexcept;
    operator const D3D12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION& () const noexcept;
};
```

## Members

`CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION`

Default constructor. Creates a new, default-initialized, instance of a **CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION**.

`CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION(CD3DX12_STATE_OBJECT_DESC&)`

Constructor that creates a new instance of a **CD3DX12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION** initialized with the contents of a [**CD3DX12_STATE_OBJECT_DESC**](cd3dx12-state-object-desc.md) object.

`SetSubobjectNameToAssociate(LPCWSTR)`

Function for setting the name of the subobject to associate.

`AddExport(LPCWSTR)`

Adds an export to associate.

`AddExports(LPCWSTR(&)[N]);`

Adds an array of exports to associate. Template parameter *N* specifies the number of elements in the array.

`AddExports(const LPCWSTR*, UINT)`

Defines an array of *N* exports to associate.

`Type`

Retrieves the type of the subobject, represented by the [D3D12_STATE_SUBOBJECT_TYPE_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_subobject_type) constant.

`operator const D3D12_STATE_SUBOBJECT&`

Conversion operator that returns a reference to a constant [D3D12_STATE_SUBOBJECT](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_subobject) object describing the state object.

`operator const D3D12_SUBOBJECT_TO_EXPORTS_ASSOCIATION&`

Conversion operator that returns a reference to a constant [D3D12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION](/windows/win32/api/d3d12/ns-d3d12-d3d12_dxil_subobject_to_exports_association) object describing the state object.

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md)
