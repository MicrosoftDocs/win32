---
description: A Direct3D device can be in either an operational state or a lost state.
ms.assetid: dc4326ba-2ebc-4bca-8fba-02d8db739b8f
title: Lost Devices (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Lost Devices (Direct3D 9)

A Direct3D device can be in either an operational state or a lost state. The operational state is the normal state of the device in which the device runs and presents all rendering as expected. The device makes a transition to the lost state when an event, such as the loss of keyboard focus in a full-screen application, causes rendering to become impossible. The lost state is characterized by the silent failure of all rendering operations, which means that the rendering methods can return success codes even though the rendering operations fail. In this situation, the error code D3DERR\_DEVICELOST is returned by [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present).

By design, the full set of scenarios that can cause a device to become lost is not specified. Some typical examples include loss of focus, such as when the user presses ALT+TAB or when a system dialog is initialized. Devices can also be lost due to a power management event, or when another application assumes full-screen operation. In addition, any failure from [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) puts the device into a lost state.

All methods that derive from [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) are guaranteed to work after a device is lost. After device loss, each function generally has the following three options:

-   Fail with D3DERR\_DEVICELOST - This means that the application needs to recognize that the device was lost, so that the application identifies that something isn't happening as expected.
-   Silently fail, returning S\_OK or any other return codes - If a function silently fails, the application generally can't distinguish between the result of "success" and a "silent failure."
-   The function returns a return code.



|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 9Ex:<br/> A Direct3D 9 device returns D3DERR\_DEVICELOST. Once it has been returned from [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present), the emulation behavior no longer operates and all future calls will fail until the device is successfully reset.<br/> A Direct3D 9Ex device never returns D3DERR\_DEVICELOST, but can return new status messages (see [device behavior changes](dx9lh.md)).<br/> |



 

## Responding to a Lost Device

A lost device must re-create resources (including video memory resources) after it has been reset. If a device is lost, the application queries the device to see if it can be restored to the operational state. If not, the application waits until the device can be restored.

If the device can be restored, the application prepares the device by destroying all video-memory resources and any swap chains. Then, the application calls the [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) method. Reset is the only method that has an effect when a device is lost, and is the only method by which an application can change the device from a lost to an operational state. Reset will fail unless the application releases all resources that are allocated in D3DPOOL\_DEFAULT, including those created by the [**IDirect3DDevice9::CreateRenderTarget**](/windows/desktop/api) and [**IDirect3DDevice9::CreateDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createdepthstencilsurface) methods.

For the most part, the high-frequency calls of Direct3D do not return any information about whether the device has been lost. The application can continue to call rendering methods, such as [**IDirect3DDevice9::DrawPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawprimitive), without receiving notification of a lost device. Internally, these operations are discarded until the device is reset to the operational state.

The application can determine what to do on encountering a lost device by querying the return value of the [**IDirect3DDevice9::TestCooperativeLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-testcooperativelevel) method.

## Locking Operations

Internally, Direct3D does enough work to ensure that a lock operation will succeed after a device is lost. However, it is not guaranteed that the video-memory resource's data will be accurate during the lock operation. It is guaranteed that no error code will be returned. This allows applications to be written without concern for device loss during a lock operation.

## Resources

Resources can consume video memory. Because a lost device is disconnected from the video memory owned by the adapter, it is not possible to guarantee allocation of video memory when the device is lost. As a result, all resource creation methods are implemented to succeed by returning D3D\_OK, but do in fact allocate only dummy system memory. Because any video-memory resource must be destroyed before the device is resized, there is no issue of over-allocating video memory. These dummy surfaces allow lock and copy operations to appear to function normally until the application calls [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present) and discovers that the device has been lost.

All video memory must be released before a device can be reset from a lost state to an operational state. This means that the application should release any swap chains created with [**IDirect3DDevice9::CreateAdditionalSwapChain**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createadditionalswapchain) and any resources placed in the D3DPOOL\_DEFAULT memory class. The application need not release resources in the D3DPOOL\_MANAGED or D3DPOOL\_SYSTEMMEM memory classes. Other state data is automatically destroyed by the transition to an operational state.

You are encouraged to develop applications with a single code path to respond to device loss. This code path is likely to be similar, if not identical, to the code path taken to initialize the device at startup.

## Retrieved Data

Direct3D allows applications to validate texture and render states against single pass rendering by the hardware using [**IDirect3DDevice9::ValidateDevice**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-validatedevice). This method, which is typically invoked during initialization of the application, will return D3DERR\_DEVICELOST if the device has been lost.

Direct3D also allows applications to copy generated or previously written images from video-memory resources to nonvolatile system-memory resources. Because the source images of such transfers might be lost at any time, Direct3D allows such copy operations to fail when the device is lost.

Regarding asynchronous queries, [**IDirect3DQuery9::GetData**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-getdata) returns D3DERR\_DEVICELOST if the FLUSH flag is specified, in order to indicate to the application that **IDirect3DQuery9::GetData** will never return S\_OK.

The copy operation, [**IDirect3DDevice9::GetFrontBufferData**](/windows/desktop/api), can fail with D3DERR\_DEVICELOST since there is no primary surface when the device is lost. [**IDirect3DDevice9::CreateAdditionalSwapChain**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createadditionalswapchain) can also fail with D3DERR\_DEVICELOST because a back buffer can't be created when the device is lost. Note that these cases are the only instance of D3DERR\_DEVICELOST outside of the [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present), [**IDirect3DDevice9::TestCooperativeLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-testcooperativelevel), and [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) methods.

## Programmable Shaders

In Direct3D 9, vertex shaders and pixel shaders don't need to be re-created after reset. They will be remembered. In previous versions of DirectX, a lost device required shaders to be re-created.

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 
