---
title: Windows numerics and DirectXMath interop APIs (Windowsnumerics.h)
description: These functions convert Windows.Foundation.Numerics types to and from the DirectXMath SIMD types XMVECTOR and XMMATRIX.
ms.assetid: 05851054-196E-4955-B9C5-85C2E33EF488
keywords:
- Windows numerics and DirectXMath interop APIs
topic_type:
- apiref
api_name:
- WWindows numerics and DirectXMath interop APIs
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Windows numerics and DirectXMath interop APIs

These functions convert [**Windows.Foundation.Numerics**](/uwp/api/Windows.Foundation.Numerics) types to and from the DirectXMath SIMD types [XMVECTOR](../dxmath/xmvector-data-type.md) and [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix).

## Functions

| Name | Description |
|-|-|
| `XMVECTOR XMLoadFloat2(_In_ float2 const* pSource)` | Loads a float2 into a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md). |
| `XMVECTOR XMLoadFloat3(_In_ float3 const* pSource)` | Loads a float3 into a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md). |
| `XMVECTOR XMLoadFloat4(_In_ float4 const* pSource)` | Loads a float4 into a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md). |
| `XMMATRIX XMLoadFloat3x2(_In_ float3x2 const* pSource)` | Loads a float3x2 into a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix). |
| `XMMATRIX XMLoadFloat4x4(_In_ float4x4 const* pSource)` | Loads a float4x4 into a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix). |
| `XMVECTOR XMLoadPlane(_In_ plane const* pSource)` | Loads a plane into a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix). |
| `XMVECTOR XMLoadQuaternion(_In_ quaternion const* pSource)` | Loads a quaternion into a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix). |
| `void XMStoreFloat2(_Out_ float2* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md) into a float2. |
| `void XMStoreFloat3(_Out_ float3* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md) into a float3. |
| `void XMStoreFloat4(_Out_ float4* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md) into a float4. |
| `void XMStoreFloat3x2(_Out_ float3x2* pDestination, _In_ FXMMATRIX value)` | Stores a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) into a float3x2. |
| `void XMStoreFloat4x4(_Out_ float4x4* pDestination, _In_ FXMMATRIX value)` | Stores a DirectXMath [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) into a float4x4. |
| `void XMStorePlane(_Out_ plane* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md) into a plane. |
| `void XMStoreQuaternion(_Out_ quaternion* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](../dxmath/xmvector-data-type.md) into a quaternion. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | DirectX |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
