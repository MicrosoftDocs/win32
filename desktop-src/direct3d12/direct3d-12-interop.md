---
title: Working with Direct3D 11, Direct3D 10 and Direct2D
description: This section covers interop techniques with earlier versions of Direct3D and Direct2D, the Direct3D 11on12 API, and porting guidelines from Direct3D 11 to Direct3D 12.
ms.assetid: 1AB98335-30B1-4244-B244-F8573524B38C
ms.topic: article
ms.date: 05/31/2018
---

# Working with Direct3D 11, Direct3D 10 and Direct2D

This section covers interop techniques with earlier versions of Direct3D and Direct2D, the Direct3D 11on12 API, and porting guidelines from Direct3D 11 to Direct3D 12.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Direct3D 12 Interop](direct3d-12-with-direct3d-11--direct-2d-and-gdi.md)<br/>             | D3D12 can be used to write componentized applications. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Direct3D 11 on 12](direct3d-11-on-12.md)<br/>                                             | D3D11On12 is a mechanism by which developers can use D3D11 interfaces and objects to drive the D3D12 API. D3D11on12 enables components written using D3D11 (for example, D2D text and UI) to work together with components written targeting the D3D12 API. D3D11on12 also enables incremental porting of an application from D3D11 to D3D12, by enabling portions of the app to continue targeting D3D11 for simplicity while others target D3D12 for performance, while always having complete and correct rendering. D3D11On12 makes it simpler than using interop techniques to share resources and synchronize work between the two APIs. <br/> |
| [Porting from Direct3D 11 to Direct3D 12](porting-from-direct3d-11-to-direct3d-12.md)<br/> | This section provides some guidance on porting from a custom Direct3D 11 graphics engine to Direct3D 12.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> </dl>

 

 





