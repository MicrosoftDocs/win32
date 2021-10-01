---
title: Helper structures and functions for Direct3D 12
description: These helper structures and helper functions are declared in `d3dx12.h`.
ms.assetid: 095958A9-345B-45AE-8363-B353534044B2
keywords:
- Helper functions
- Helper structures
- d3dx12.h
ms.localizationpriority: low
ms.topic: article
ms.date: 05/31/2018
---

# Helper structures and functions for Direct3D 12

These helper structures and helper functions are declared in `d3dx12.h`.

`d3dx12.h` is available separately from the Direct3D 12 headers. You can download `d3dx12.h` from [The D3D12 Helper Library](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h).

You can use these helper structures to create and initialize Direct3D structures. These helper structures behave like C++ classes. Each helper structure typically has a default constructor, an explicit constructor, a destructor, and a cast operator for the associated D3D12 structure. Each helper structure has a 'C' prefix and is associated with a D3D12 structure which lacks the 'C' prefix. Most helper structures contain initialization member methods, some contain comparison functions.

## In this section

| Topic | Description |
|-|-|
| [Helper Interfaces for D3D12](helper-interfaces-for-d3d12.md) | These helper interfaces help particularly in handling subresources, and are declared in `d3dx12.h`.  |
| [Helper Structures for D3D12](helper-structures-for-d3d12.md) | These helper structures help initialize many of the Direct3D 12 structures, and are declared in `d3dx12.h`. |
| [Helper Functions for D3D12](helper-functions-for-d3d12.md) | These helper functions help particularly in handling subresources, and are declared in `d3dx12.h`.  |

## Related topics

* [Direct3D 12 Reference](direct3d-12-reference.md)
