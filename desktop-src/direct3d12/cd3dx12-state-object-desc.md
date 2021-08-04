---
title: CD3DX12_STATE_OBJECT_DESC class (D3dx12.h)
description: The central class of the D3DX12 State Object Creation Helpers, which are helper classes for creating state objects out of an arbitrary set of subobjects.
keywords:
- CD3DX12_STATE_OBJECT_DESC class
topic_type:
- apiref
api_name:
- CD3DX12_STATE_OBJECT_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/03/2021
---

# CD3DX12_STATE_OBJECT_DESC class

The central class of the D3DX12 State Object Creation Helpers, which are helper classes for creating state objects out of an arbitrary set of subobjects.

## Syntax

```cpp
class CD3DX12_STATE_OBJECT_DESC
{
    CD3DX12_STATE_OBJECT_DESC() noexcept;
    CD3DX12_STATE_OBJECT_DESC(D3D12_STATE_OBJECT_TYPE) noexcept;
    void SetStateObjectType(D3D12_STATE_OBJECT_TYPE) noexcept;
    operator const D3D12_STATE_OBJECT_DESC& ();
    operator const D3D12_STATE_OBJECT_DESC* ();
    template<typename T> T* CreateSubobject();
};
```

## Members

### CD3DX12_STATE_OBJECT_DESC

Default constructor. Creates a new, default-initialized, instance of a **CD3DX12_STATE_OBJECT_DESC**.

### CD3DX12_STATE_OBJECT_DESC(D3D12_STATE_OBJECT_TYPE)

Constructor that creates a new instance of a **CD3DX12_STATE_OBJECT_DESC** initialized with a subjobject type corresponding to the value of the [**D3D12_STATE_OBJECT_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_object_type) passed to it.

### SetStateObjectType(D3D12_STATE_OBJECT_TYPE)

Method that sets the subjobject type to the value of the [**D3D12_STATE_OBJECT_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_object_type) passed to it.

### operator const D3D12_STATE_OBJECT_DESC&

Conversion operator that returns a reference to a constant [**D3D12_STATE_OBJECT_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_object_desc) object describing the state object.

### operator const D3D12_STATE_OBJECT_DESC*

Conversion operator that returns a pointer to a constant [**D3D12_STATE_OBJECT_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_object_desc) object describing the state object.

### CreateSubobject

A function template that creates a sububject helper whose lifetime is owned by this class.

Template parameter *T* specifies the a subjobject helper type, for example, [CD3DX12_HIT_GROUP_SUBOBJECT](cd3dx12-hit-group-subobject.md).

## Remarks

To use the D3DX12 State Object Creation Helpers, begin by instantiating a **CD3DX12_STATE_OBJECT_DESC** object, and call its **CreateSubobject** function to create subobjects. The subobject helpers each have methods specific to that subobject for configuring its contents.

```cpp
CD3DX12_STATE_OBJECT_DESC Collection1(D3D12_STATE_OBJECT_TYPE_COLLECTION);
auto Lib0 = Collection1.CreateSubobject<CD3DX12_DXIL_LIBRARY_SUBOBJECT>();
Lib0->SetDXILLibrary(&pMyAppDxilLibs[0]);
Lib0->DefineExport(L"rayGenShader0");
// In practice, these export listings might be data/engine-driven.
...
```

Alternatively, you can instantiate subobject helpers explicitly, such as via local variables instead, passing the state object desc (which should point to it) into the helper constructor (or call `mySubobjectHelper.AddToStateObject(Collection1)`).

In this alternative scenario, you need to keep the subobject alive as long as the state object it's associated with is alive, otherwise its pointer references will be stale.

```cpp
CD3DX12_STATE_OBJECT_DESC RaytracingState2(D3D12_STATE_OBJECT_TYPE_RAYTRACING_PIPELINE);
CD3DX12_DXIL_LIBRARY_SUBOBJECT LibA(RaytracingState2);
LibA.SetDXILLibrary(&pMyAppDxilLibs[4]);
// Not manually specifying exports; meaning that all exports in the libraries are exported.
...
```

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
