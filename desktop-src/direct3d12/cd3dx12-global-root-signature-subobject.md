---
title: CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT class (D3dx12.h)
description: A helper class for creating a global root signature state suboject.
keywords:
- CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT class
topic_type:
- apiref
api_name:
- CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 08/04/2021
---

# CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT class

A helper class for creating a global root signature state suboject.

For more info about the D3DX12 State Object Creation Helpers, see [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md).

## Syntax

```cpp
class CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT
{
    CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT() noexcept;
    CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC& ContainingStateObject);
    void SetRootSignature(ID3D12RootSignature* pRootSig) noexcept;
    D3D12_STATE_SUBOBJECT_TYPE Type() const noexcept override;
    operator const D3D12_STATE_SUBOBJECT& () const noexcept { return *m_pSubobject; }
    operator ID3D12RootSignature* () const noexcept { return D3DX12_COM_PTR_GET(m_pRootSig); }
};
```

## Members

`CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT`

Default constructor. Creates a new, default-initialized, instance of a **CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT**.

`CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC&)`

Constructor that creates a new instance of a **CD3DX12_GLOBAL_ROOT_SIGNATURE_SUBOBJECT** initialized with the contents of a [**CD3DX12_STATE_OBJECT_DESC**](cd3dx12-state-object-desc.md) object.

`SetRootSignature(ID3D12RootSignature*)`

Function for setting the root signature in the form of the pointer to an [ID3D12RootSignature](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignature) passed as the parameter.

`Type`

Retrieves the type of the subobject, represented by the [D3D12_STATE_SUBOBJECT_TYPE_GLOBAL_ROOT_SIGNATURE](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_subobject_type) constant.

`operator const D3D12_STATE_SUBOBJECT&`

Conversion operator that returns a reference to a constant [D3D12_STATE_SUBOBJECT](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_subobject) object describing the state object.

`operator ID3D12RootSignature*`

Conversion operator that returns the root signature in the form of a pointer to an [ID3D12RootSignature](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignature).

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md)
