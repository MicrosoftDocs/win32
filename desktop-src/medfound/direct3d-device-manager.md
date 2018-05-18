---
Description: Direct3D Device Manager
ms.assetid: 'd82fd82d-510e-4004-b18b-8f2372e29701'
title: Direct3D Device Manager
---

# Direct3D Device Manager

The Microsoft Direct3D device manager enables two or more objects to share the same Microsoft Direct3D 9 device. One object acts as the owner of the Direct3D 9 device. To share the device, the owner of the device creates the Direct3D device manager. Other objects can obtain a pointer to the device manager from the device owner, then use the device manager to get a pointer to the Direct3D device. Any object that uses the device holds an exclusive lock, which prevents other objects from using the device at the same time.

> [!Note]  
> The Direct3D Device Manager supports Direct3D 9 devices only. It does not support DXGI devices.

 

To create the Direct3D device manager, call [**DXVA2CreateDirect3DDeviceManager9**](dxva2createdirect3ddevicemanager9.md). This function returns a pointer to the device manager's [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md) interface, along with a reset token. The reset token enables the owner of the Direct3D device to set (and reset) the device on the device manager. To initialize the device manager, call [**IDirect3DDeviceManager9::ResetDevice**](idirect3ddevicemanager9-resetdevice.md). Pass in a pointer to the Direct3D device, along with the reset token.

The following code shows how to create and initialize the device manager.


```C++
HRESULT CreateD3DDeviceManager(
    IDirect3DDevice9 *pDevice, 
    UINT *pReset, 
    IDirect3DDeviceManager9 **ppManager
    )
{
    UINT resetToken = 0;

    IDirect3DDeviceManager9 *pD3DManager = NULL;

    HRESULT hr = DXVA2CreateDirect3DDeviceManager9(&amp;resetToken, &amp;pD3DManager);

    if (FAILED(hr))
    {
        goto done;
    }

    hr = pD3DManager->ResetDevice(pDevice, resetToken);

    if (FAILED(hr))
    {
        goto done;
    }

    *ppManager = pD3DManager;
    (*ppManager)->AddRef();

    *pReset = resetToken;


done:
    SafeRelease(&amp;pD3DManager);
    return hr;
}
```



The device owner must provide a way for other objects to get a pointer to the [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md) interface. The standard mechanism is to implement the [**IMFGetService**](imfgetservice.md) interface. The service GUID is MR\_VIDEO\_ACCELERATION\_SERVICE.

To share the device among several objects, each object (including the owner of the device) must access the device through the device manager, as follows:

1.  Call [**IDirect3DDeviceManager9::OpenDeviceHandle**](idirect3ddevicemanager9-opendevicehandle.md) to get a handle to the device.
2.  To use the device, call [**IDirect3DDeviceManager9::LockDevice**](idirect3ddevicemanager9-lockdevice.md) and pass in the device handle. The method returns a pointer to the **IDirect3DDevice9** interface. The method can be called in a blocking mode or a non-blocking mode, depending on the value of the *fBlock* parameter.
3.  When you are done using the device, call [**IDirect3DDeviceManager9::UnlockDevice**](idirect3ddevicemanager9-unlockdevice.md). This method makes the device available to other objects.
4.  Before exiting, call [**IDirect3DDeviceManager9::CloseDeviceHandle**](idirect3ddevicemanager9-closedevicehandle.md) to close the device handle.

You should hold the device lock only while using the device, because holding the device lock prevents other objects from using the device.

The owner of the device can switch to another device at any time by calling [**ResetDevice**](idirect3ddevicemanager9-resetdevice.md), typically because the original device was lost. Device loss can occur for various reasons, including changes in the monitor resolution, power management actions, locking and unlocking the computer, and so forth. For more information, see the Direct3D documentation.

The [**ResetDevice**](idirect3ddevicemanager9-resetdevice.md) method invalidates any device handles that were opened previously. When a device handle is invalid, the [**LockDevice**](idirect3ddevicemanager9-lockdevice.md) method returns **DXVA2\_E\_NEW\_VIDEO\_DEVICE**. If this occurs, close the handle and call [**OpenDeviceHandle**](idirect3ddevicemanager9-opendevicehandle.md) again to obtain a new device handle, as shown in the following code.

The following example shows how to open a device handle and lock the device.


```C++
HRESULT LockDevice(
    IDirect3DDeviceManager9 *pDeviceManager,
    BOOL fBlock,
    IDirect3DDevice9 **ppDevice, // Receives a pointer to the device.
    HANDLE *pHandle              // Receives a device handle.   
    )
{
    *pHandle = NULL;
    *ppDevice = NULL;

    HANDLE hDevice = 0;

    HRESULT hr = pDeviceManager->OpenDeviceHandle(&amp;hDevice);

    if (SUCCEEDED(hr))
    {
        hr = pDeviceManager->LockDevice(hDevice, ppDevice, fBlock);
    }

    if (hr == DXVA2_E_NEW_VIDEO_DEVICE)
    {
        // Invalid device handle. Try to open a new device handle.
        hr = pDeviceManager->CloseDeviceHandle(hDevice);

        if (SUCCEEDED(hr))
        {
            hr = pDeviceManager->OpenDeviceHandle(&amp;hDevice);
        }

        // Try to lock the device again.
        if (SUCCEEDED(hr))
        {
            hr = pDeviceManager->LockDevice(hDevice, ppDevice, TRUE); 
        }
    }

    if (SUCCEEDED(hr))
    {
        *pHandle = hDevice;
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> </dl>

 

 



