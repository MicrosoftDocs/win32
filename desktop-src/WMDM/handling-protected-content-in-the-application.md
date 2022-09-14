---
title: Handling Protected Content in the Application
description: Handling Protected Content in the Application
ms.assetid: b59d4abc-e59d-47a7-8d91-825ac20ae2eb
keywords:
- Windows Media Device Manager,certificates
- Device Manager,certificates
- programming guide,certificates
- desktop applications,certificates
- creating Windows Media Device Manager applications,certificates
- certificates
- Windows Media Device Manager,DRM-protected content
- Device Manager,DRM-protected content
- programming guide,DRM-protected content
- desktop applications,DRM-protected content
- creating Windows Media Device Manager applications,DRM-protected content
- DRM-protected content
ms.topic: article
ms.date: 05/31/2018
---

# Handling Protected Content in the Application

\[The Windows Media DRM feature is deprecated and should not be used. Use [Microsoft PlayReady](/windows/uwp/audio-video-camera/playready-client-sdk) instead.\]

An application must have a transfer certificate to be able to handle DRM-protected content. To learn where to get this certificate, see [Tools for Development](tools-for-development.md). For handling unprotected content, you can use a dummy certificate as described in [Authenticating the Application](authenticating-the-application.md).

Before using a device, your application should determine whether the device supports Windows Media DRM 10 for Portable Devices, and if so, that the DRM components are current. (Current means that the secure clock is correct and that the device has been properly individualized.) If the device does not support this version of DRM, or if it cannot be updated, you can still send files to the device, but they might not be playable, depending on the license version.

> [!Note]  
> Individualization of devices is not currently supported.

 

If your application will link to Windows Media Format SDK methods, it will need to link to the Windows Media Format library WMStubDRM.lib. For more information on calling Windows Media Format methods on DRM-protected content, see "Enabling DRM Support" in the Windows Media Format SDK documentation. Note that there is a problem with linking to both Mssachlp.lib and WMStubDRM.lib. This is covered in [KB article 890079 on MSDN](https://support.microsoft.com/default.aspx?scid=kb;en-us;890079).

The following C++ code example determines whether a device is a Windows Media DRM 10 device and, if so, that its clock is up to date.

`HRESULT IsDRMClockUpToDate()`


```C++
{
    HRESULT hr = S_OK;

    // Create the DRM handler class.
    CComPtr<IWMDRMDeviceApp> pDRM;
    hr = pDRM.CoCreateInstance(CLSID_WMDRMDeviceApp, 0, CLSCTX_ALL);

    // Find out first if the device is a WMDRM 10 device, and if so,
    // whether it requires clock updates.
    DWORD status = 0;
    hr = pDRM->QueryDeviceStatus(pDevice, &status);

    if (FAILED(hr)
       || (!(WMDRM_DEVICE_ISWMDRM & status)) // Device is not WMDRM 10. 
       || (status & WMDRM_DEVICE_REVOKED))   // Device is revoked.
    {
        return E_FAIL;
    }
    else if (status & WMDRM_DEVICE_NEEDCLOCK || 
        status & WMDRM_DEVICE_REFRESHCLOCK)
    {
        // Attempt update. See following example.
        hr = UpdateDRM(status);
    }
    return hr;
}
```



If the device does support Windows Media DRM 10 for Portable Devices, and needs to be updated (that is, if the value of *status* in the previous example is not simply WMDM\_DEVICE\_ISWMDRM), the application should call [**IWMDRMDeviceApp::AcquireDeviceData**](iwmdrmdeviceapp-acquiredevicedata.md) and pass in the value of *status* to perform the required updates. The desktop computer must be connected to the Internet.

The following C++ example function attempts to update a DRM device.


```C++
HRESULT UpdateDRM(DWORD status)
{
    HRESULT hr = S_OK;
    hr = pDRM->AcquireDeviceData(pDevice, this, status, &result);
    if (hr != S_OK || result != 0)
    {
            return E_FAIL;
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> <dt>

[**Handling Protected Content**](handling-protected-content.md)
</dt> </dl>

 

 