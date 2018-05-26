---
title: Windows Numerics and DirectXMath Interop APIs
description: These functions convert Windows.Foundation.Numerics types to and from the DirectXMath SIMD types XMVECTOR and XMMATRIX.
ms.assetid: 05851054-196E-4955-B9C5-85C2E33EF488
keywords:
- Windows Numerics and DirectXMath Interop APIs
topic_type:
- apiref
api_name:
- Windows Numerics and DirectXMath Interop APIs
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Numerics and DirectXMath Interop APIs

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

These functions convert [**Windows.Foundation.Numerics**](https://msdn.microsoft.com/library/windows/apps/dn895051) types to and from the DirectXMath SIMD types [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) and [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959).

## Functions



| Name                                                                           | Description                                                                   |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `XMVECTOR XMLoadFloat2(_In_ float2 const* pSource)`                            | Loads a float2 into a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742).      |
| `XMVECTOR XMLoadFloat3(_In_ float3 const* pSource)`                            | Loads a float3 into a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742).      |
| `XMVECTOR XMLoadFloat4(_In_ float4 const* pSource)`                            | Loads a float4 into a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742).      |
| `XMMATRIX XMLoadFloat3x2(_In_ float3x2 const* pSource)`                        | Loads a float3x2 into a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959).              |
| `XMMATRIX XMLoadFloat4x4(_In_ float4x4 const* pSource)`                        | Loads a float4x4 into a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959).              |
| `XMVECTOR XMLoadPlane(_In_ plane const* pSource)`                              | Loads a plane into a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959).                 |
| `XMVECTOR XMLoadQuaternion(_In_ quaternion const* pSource)`                    | Loads a quaternion into a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959).            |
| `void XMStoreFloat2(_Out_ float2* pDestination, _In_ FXMVECTOR value)`         | Stores a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) into a float2.     |
| `void XMStoreFloat3(_Out_ float3* pDestination, _In_ FXMVECTOR value)`         | Stores a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) into a float3.     |
| `void XMStoreFloat4(_Out_ float4* pDestination, _In_ FXMVECTOR value)`         | Stores a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) into a float4.     |
| `void XMStoreFloat3x2(_Out_ float3x2* pDestination, _In_ FXMMATRIX value)`     | Stores a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959) into a float3x2.             |
| `void XMStoreFloat4x4(_Out_ float4x4* pDestination, _In_ FXMMATRIX value)`     | Stores a DirectXMath [XMMATRIX](https://msdn.microsoft.com/library/windows/desktop/ee419959) into a float4x4.             |
| `void XMStorePlane(_Out_ plane* pDestination, _In_ FXMVECTOR value)`           | Stores a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) into a plane.      |
| `void XMStoreQuaternion(_Out_ quaternion* pDestination, _In_ FXMVECTOR value)` | Stores a DirectXMath [XMVECTOR](https://msdn.microsoft.com/library/windows/desktop/ee420742) into a quaternion. |



 

## Requirements



|                      |                                                                                              |
|----------------------|----------------------------------------------------------------------------------------------|
| Namespace<br/> | DirectX<br/>                                                                           |
| Header<br/>    | <dl> <dt>Windowsnumerics.h</dt> </dl> |



## See also

<dl> <dt>

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
</dt> </dl>

 

 





