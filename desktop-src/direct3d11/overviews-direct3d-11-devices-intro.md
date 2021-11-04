---
title: Introduction to a Device in Direct3D 11
description: The Direct3D 11 object model separates resource creation and rendering functionality into a device and one or more contexts; this separation is designed to facilitate multithreading.
ms.assetid: b9b45d18-f7b7-40f9-ae4e-576ca7a6eba7
ms.topic: article
ms.date: 05/31/2018
---

# Introduction to a Device in Direct3D 11

The Direct3D 11 object model separates resource creation and rendering functionality into a device and one or more contexts; this separation is designed to facilitate multithreading.

-   [Device](#introduction-to-a-device-in-direct3d-11)
-   [Device Context](#device-context)
    -   [Immediate Context](#immediate-context)
    -   [Deferred Context](#deferred-context)
-   [Threading Considerations](#threading-considerations)
-   [Related topics](#related-topics)

## Device

A device is used to create resources and to enumerate the capabilities of a display adapter. In Direct3D 11, a device is represented with an [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) interface.

Each application must have at least one device, most applications only create one device. Create a device for one of the hardware drivers installed on your machine by calling [**D3D11CreateDevice**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdevice) or [**D3D11CreateDeviceAndSwapChain**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdeviceandswapchain) and specify the driver type with the [**D3D\_DRIVER\_TYPE**](/windows/desktop/api/D3DCommon/ne-d3dcommon-d3d_driver_type) flag. Each device can use one or more device contexts, depending on the functionality desired.

## Device Context

A device context contains the circumstance or setting in which a device is used. More specifically, a device context is used to set pipeline state and generate rendering commands using the resources owned by a device. Direct3D 11 implements two types of device contexts, one for immediate rendering and the other for deferred rendering; both contexts are represented with an [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) interface.

### Immediate Context

An immediate context renders directly to the driver. Each device has one and only one immediate context which can retrieve data from the GPU. An immediate context can be used to immediately render (or play back) a [command list](overviews-direct3d-11-render-multi-thread-command-list.md).

There are two ways to get an immediate context:

-   By calling either [**D3D11CreateDevice**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdevice) or [**D3D11CreateDeviceAndSwapChain**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdeviceandswapchain).
-   By calling [**ID3D11Device::GetImmediateContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-getimmediatecontext).

### Deferred Context

A deferred context records GPU commands into a [command list](overviews-direct3d-11-render-multi-thread-command-list.md). A deferred context is primarily used for multithreading and is not necessary for a single-threaded application. A deferred context is generally used by a worker thread instead of the main rendering thread. When you create a deferred context, it does not inherit any state from the immediate context.

To get a deferred context, call [**ID3D11Device::CreateDeferredContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createdeferredcontext).

Any context -- immediate or deferred -- can be used on any thread as long as the context is only used in one thread at a time.

## Threading Considerations

This table highlights the differences in the threading model in Direct3D 11 from prior versions of Direct3D.




| 
|
| Differences between Direct3D 11 and previous versions of Direct3D:<br /> All <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11device"><strong>ID3D11Device</strong></a> interface methods are free-threaded, which means it is safe to have multiple threads call the functions at the same time.<br /><ul><li>All <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11devicechild"><strong>ID3D11DeviceChild</strong></a>-derived interfaces (<a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11buffer"><strong>ID3D11Buffer</strong></a>, <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11query"><strong>ID3D11Query</strong></a>, etc.) are free-threaded.</li><li>Direct3D 11 splits resource creating and rendering into two interfaces. Map, Unmap, Begin, End, and GetData are implemented on <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext"><strong>ID3D11DeviceContext</strong></a> because <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11device"><strong>ID3D11Device</strong></a> strongly defines the order of operations. <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11resource"><strong>ID3D11Resource</strong></a> and <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11asynchronous"><strong>ID3D11Asynchronous</strong></a> interfaces also implement methods for free-threaded operations.</li><li>The <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext"><strong>ID3D11DeviceContext</strong></a> methods (except for those that exist on <a href="/windows/desktop/api/D3D11/nn-d3d11-id3d11devicechild"><strong>ID3D11DeviceChild</strong></a>) are not free-threaded, that is, they require single threading. Only one thread may safely be calling any of its methods (Draw, Copy, Map, etc.) at a time.</li><li>In general, free-threading minimizes the number of synchronization primitives used as well as their duration. However, an application that uses synchronization held for a long time can directly impact how much concurrency an application can expect to achieve.</li></ul>ID3D10Device interface methods are not designed to be free-threaded. ID3D10Device implements all create and rendering functionality (as does ID3D9Device in Direct3D 9). Map and Unmap are implemented on ID3D10Resource-derived interfaces, Begin, End, and GetData are implemented on ID3D10Asynchronous-derived interfaces.<br /> | 




 

## Related topics

<dl> <dt>

[Devices](overviews-direct3d-11-devices.md)
</dt> </dl>

 

 





