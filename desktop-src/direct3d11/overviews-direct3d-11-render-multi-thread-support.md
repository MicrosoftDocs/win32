---
title: How To Check for Driver Support
description: This topic shows how to determine whether multithreading features (including resource creation and command lists) are supported for hardware acceleration.
ms.assetid: f577357c-c2e5-4e58-9870-2e995bdc6782
ms.topic: article
ms.date: 05/31/2018
---

# How To: Check for Driver Support

This topic shows how to determine whether multithreading features (including [resource creation](overviews-direct3d-11-render-multi-thread-intro.md) and [command lists](overviews-direct3d-11-render-multi-thread-command-list.md)) are supported for hardware acceleration.

We recommend for applications to check for graphics hardware support of multithreading. If the driver and graphics hardware do not support multithreaded object creation, performance can be limited in the following ways:

-   Creating multiple objects (even of different types) at the same time might be limited.
-   Creating an object while rendering graphics commands by using an [immediate context](overviews-direct3d-11-render-multi-thread-render.md) might be limited. For example, if hardware does not support multithreading, an application should avoid creating on a background thread an object that requires a very long time to create. A create operation that takes very long can block immediate context rendering and increase the risk of a visual frame rate stutter.

The runtime supports multithreading and command lists regardless of driver and hardware support; if there is no driver and hardware support for either multithreads or command lists, the runtime will emulate the functionality. For more information about multithreading, see [Introduction to Multithreading in Direct3D 11](overviews-direct3d-11-render-multi-thread-intro.md).

**To check for driver support for multithreading:**

1.  Initialize an [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) interface object. By default, multithreading is enabled.
2.  Call [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport). Pass the **D3D11\_FEATURE\_THREADING** value to the *Feature* parameter, pass the [**D3D11\_FEATURE\_DATA\_THREADING**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_threading) structure to the *pFeatureSupportData* parameter, and pass the size of the **D3D11\_FEATURE\_DATA\_THREADING** structure to the *FeatureSupportDataSize* parameter.
3.  If the [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport) method succeeds, the [**D3D11\_FEATURE\_DATA\_THREADING**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_threading) structure that you passed in the previous step will be initialized with information about multithreading support.
    -   If **DriverConcurrentCreates** is **TRUE**, a driver can create more than one resource at the same time (concurrently) on different threads.

        If **DriverCommandLists** is **TRUE**, the driver supports command lists. That is, rendering commands issued by an immediate context can be concurrent with object creation on separate threads with low risk of a frame rate stutter.

    -   If **DriverConcurrentCreates** is **FALSE**, a driver does not support concurrent creation, which means the amount of concurrency possible is extremely limited. The graphics hardware cannot create objects of different types on different threads simultanueously. Additionally, the graphics hardware cannot use an immediate context to issue render commands while the graphics hardware attempts to create a resource on another thread.

## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Multithreading](overviews-direct3d-11-render-multi-thread.md)
</dt> </dl>

 

 




