---
description: Applications can query hardware to detect the supported Direct3D device types. This section contains information about the primary tasks involved in enumerating display adapters and selecting Direct3D devices.
ms.assetid: d140b90c-3a20-49f4-883b-662b6c05dcea
title: Selecting a Device (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a Device (Direct3D 9)

Applications can query hardware to detect the supported Direct3D device types. This section contains information about the primary tasks involved in enumerating display adapters and selecting Direct3D devices.

An application must perform a series of tasks to select an appropriate Direct3D device. Note that the following steps are intended for a full-screen application and that, in most cases, a windowed application can skip most of these steps.

1.  Initially, the application must enumerate the display adapters on the system. An adapter is a physical piece of hardware. Note that the graphics card might contain more than a single adapter, as is the case with a dual-headed display. Applications that are not concerned with multi-monitor support can disregard this step, and pass D3DADAPTER\_DEFAULT to the [**IDirect3D9::EnumAdapterModes**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-enumadaptermodes) method in step 2.
2.  For each adapter, the application enumerates the supported display modes by calling [**IDirect3D9::EnumAdapterModes**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-enumadaptermodes).
3.  If required, the application checks for the presence of hardware acceleration in each enumerated display mode by calling [**IDirect3D9::CheckDeviceType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicetype), as shown in the following code example. Note that this is only one of the possible uses for **IDirect3D9::CheckDeviceType**; for details, see [Determining Hardware Support (Direct3D 9)](determining-hardware-support.md).
    ```
    D3DPRESENT_PARAMETERS Params;
    // Initialize values for D3DPRESENT_PARAMETERS members. 

    Params.BackBufferFormat = D3DFMT_X1R5G5B5; 

    if(FAILED(m_pD3D->CheckDeviceType(Device.m_uAdapter, 
                      Device.m_DevType, 
                      Params.BackBufferFormat, Params.BackBufferFormat, 
                      FALSE))) 
        return E_FAIL;
    ```

    

4.  The application checks for the desired level of functionality for the device on this adapter by calling the [**IDirect3D9::GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3d9-getdevicecaps) method. The capability returned by this method is guaranteed to be constant for a device across all display modes, verified by [**IDirect3D9::CheckDeviceType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicetype).
5.  Devices can always render to surfaces of the format of an enumerated display mode that is supported by the device. If the application is required to render to a surface of a different format, it can call [**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat). If the device can render to the format, then it is guaranteed that all capabilities returned by [**IDirect3D9::GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3d9-getdevicecaps) are applicable.
6.  Lastly, the application can determine if multisampling techniques, such as full-scene antialiasing, are supported for a render format by using the [**IDirect3D9::CheckDeviceMultiSampleType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicemultisampletype) method.

After completing the preceding steps, the application should have a list of display modes in which it can operate. The final step is to verify that enough device-accessible memory is available to accommodate the required number of buffers and antialiasing. This test is necessary because the memory consumption for the mode and multisample combination is impossible to predict without verifying it. Moreover, some display adapter architectures might not have a constant amount of device-accessible memory. This means that an application should be able to report out-of-video-memory failures when going into full-screen mode. Typically, an application should remove full-screen mode from the list of modes that it offers to a user, or it should attempt to consume less memory by reducing the number of back buffers or by using a less complex multisampling technique.

A windowed application performs a similar set of tasks.

1.  It determines the desktop rectangle covered by the client area of the window.
2.  It enumerates adapters, looking for the adapter whose monitor covers the client area. If the client area is owned by more than one adapter, then the application can choose to drive each adapter independently, or to drive a single adapter and have Direct3D transfer pixels from one device to another at presentation. The application can also disregard two preceding steps and use the D3DADAPTER\_DEFAULT adapter. Note that this might result in slower operation when the window is placed on a secondary monitor.
3.  The application should call [**IDirect3D9::CheckDeviceType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicetype) to determine if the device can support rendering to a back buffer of the specified format while in desktop mode. [**IDirect3D9::GetAdapterDisplayMode**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-getadapterdisplaymode) can be used to determine the desktop display format, as shown in the following code example.
    ```
    D3DPRESENT_PARAMETERS Params;
    // Initialize values for D3DPRESENT_PARAMETERS members. 

    // Use the current display mode.
    D3DDISPLAYMODE mode;

    if(FAILED(m_pD3D->GetAdapterDisplayMode(Device.m_uAdapter , &mode)))
        return E_FAIL;

    Params.BackBufferFormat = mode.Format;

    if(FAILED(m_pD3D->CheckDeviceType(Device.m_uAdapter, Device.m_DevType, 
    Params.BackBufferFormat, Params.BackBufferFormat, FALSE)))
        return E_FAIL;
    ```

    

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 
