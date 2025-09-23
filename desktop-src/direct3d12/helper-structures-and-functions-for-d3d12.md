---
title: Helper structures and functions for Direct3D 12
description: These helper structures and helper functions are declared in `d3dx12.h`.
ms.assetid: 095958A9-345B-45AE-8363-B353534044B2
keywords:
- Helper functions
- Helper structures
- d3dx12.h
ms.topic: concept-article
ms.date: 11/07/2024
---

# Helper structures and functions for Direct3D 12

These helper structures and helper functions are declared in `d3dx12.h`. `d3dx12.h` is available separately from the Direct3D 12 headers, and is not included in the Windows SDK.

You can use these helper structures to create and initialize Direct3D structures. These helper structures behave like C++ classes. Each helper structure typically has a default constructor, an explicit constructor, a destructor, and a cast operator for the associated D3D12 structure. Each helper structure has a 'C' prefix and is associated with a D3D12 structure which lacks the 'C' prefix. Most helper structures contain initialization member methods, some contain comparison functions.

## Integration

The original D3DX12 library was a single C++ header file (`d3dx12.h`), which you copied into your project. There are a number of DirectX-related project templates that make use of that form of integration.

The library has since been refactored into multiple files in order to make it more modular and easier to maintain, and some functionality was added (for example, property tables) that requires a small static library. There are a number of choices for integrating this new library into your project:

* Download the files from [GitHub](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/) and copy the `d3dx12*.*` files into your project. The files are available under the [MIT License](https://github.com/microsoft/DirectX-Headers/blob/main/LICENSE).

* Use the [DirectX-Headers](https://github.com/microsoft/DirectX-Headers) repository as a 'git submodule' for your project. There is a `CMakeList.txt` included for building the auxiliary static library needed for property table data.

* Make use of the NuGet package [Microsoft.Direct3D.D3D12](https://www.nuget.org/packages/Microsoft.Direct3D.D3D12/) in your project, which includes the D3DX12 library along with the [DirectX 12 Agility SDK](https://aka.ms/directx12agility). For more info, see [Install and use a NuGet package in Visual Studio](/nuget/quickstart/install-and-use-a-package-in-visual-studio).

* Make use of the **directx-headers** port in VCPKG. For more info, see [vcpkg overview](/vcpkg/get_started/overview).

## In this section

| Topic | Description |
|-|-|
| [Helper Interfaces for D3D12](helper-interfaces-for-d3d12.md) | These helper interfaces help particularly in handling subresources, and are declared in `d3dx12.h`.  |
| [Helper Structures for D3D12](helper-structures-for-d3d12.md) | These helper structures help initialize many of the Direct3D 12 structures, and are declared in `d3dx12.h`. |
| [Helper Functions for D3D12](helper-functions-for-d3d12.md) | These helper functions help particularly in handling subresources, and are declared in `d3dx12.h`.  |

## Related topics

* [Direct3D 12 Reference](direct3d-12-reference.md)
