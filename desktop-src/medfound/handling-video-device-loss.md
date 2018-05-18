---
Description: 'This topic describes how to detect device loss when using a video capture device.'
ms.assetid: '2bffe156-c507-437e-8f32-62aaebedd6f0'
title: Handling Video Device Loss
---

# Handling Video Device Loss

This topic describes how to detect device loss when using a video capture device. It contains the following sections:

-   [Register For Device Notification](#register-for-device-notification)
-   [Get the Symbolic Link of the Device](#get-the-symbolic-link-of-the-device)
-   [Handle WM\_DEVICECHANGE](#handle-wm-devicechange)
-   [Unregister For Notification](#unregister-for-notification)
-   [Related topics](#related-topics)

## Register For Device Notification

Before you start capturing from the device, call the [**RegisterDeviceNotification**](base.registerdevicenotification) function to register for device notifications. Register for the **KSCATEGORY\_CAPTURE** device class, as shown in the following code.


```C++
#include <Dbt.h>
#include <ks.h>
#include <ksmedia.h>

HDEVNOTIFY  g_hdevnotify = NULL;

BOOL RegisterForDeviceNotification(HWND hwnd)
{
    DEV_BROADCAST_DEVICEINTERFACE di = { 0 };
    di.dbcc_size = sizeof(di);
    di.dbcc_devicetype  = DBT_DEVTYP_DEVICEINTERFACE;
    di.dbcc_classguid  = KSCATEGORY_CAPTURE; 

    g_hdevnotify = RegisterDeviceNotification(
        hwnd,
        &amp;di,
        DEVICE_NOTIFY_WINDOW_HANDLE
        );

    if (g_hdevnotify == NULL)
    {
        return FALSE;
    }

    return TRUE;
}
```



## Get the Symbolic Link of the Device

Enumerate the video devices on the system, as described in [Enumerating Video Capture Devices](enumerating-video-capture-devices.md). Choose a device from the list, and then query the activation object for the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK](mf-devsource-attribute-source-type-vidcap-symbolic-link.md) attribute, as shown in the following code.


```C++
WCHAR      *g_pwszSymbolicLink = NULL;
UINT32     g_cchSymbolicLink = 0;

HRESULT GetSymbolicLink(IMFActivate *pActivate)
{
    return pActivate->GetAllocatedString(
        MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK,
        &amp;g_pwszSymbolicLink,
        &amp;g_cchSymbolicLink
        );
}
```



## Handle WM\_DEVICECHANGE

In your message loop, listen for [**WM\_DEVICECHANGE**](base.wm_devicechange) messages. The *lParam* message parameter is a pointer to a [**DEV\_BROADCAST\_HDR**](base.dev_broadcast_hdr_str) structure.


```C++
    case WM_DEVICECHANGE:
        if (lParam != 0)
        {
            HRESULT hr = S_OK;
            BOOL bDeviceLost = FALSE;

            hr = CheckDeviceLost((PDEV_BROADCAST_HDR)lParam, &amp;bDeviceLost);

            if (FAILED(hr) || bDeviceLost)
            {
                CloseDevice();

                MessageBox(hwnd, L"Lost the capture device.", NULL, MB_OK);
            }
        }
        return TRUE;
```



Next, compare the device notification message against the symbolic link of your device, as follows:

1.  Check the **dbch\_devicetype** member of the [**DEV\_BROADCAST\_HDR**](base.dev_broadcast_hdr_str) structure. If the value is **DBT\_DEVTYP\_DEVICEINTERFACE**, cast the structure pointer to a [**DEV\_BROADCAST\_DEVICEINTERFACE**](base.dev_broadcast_deviceinterface_str) structure.
2.  Compare the **dbcc\_name** member of this structure to the symbolic link of the device.


```C++
HRESULT CheckDeviceLost(DEV_BROADCAST_HDR *pHdr, BOOL *pbDeviceLost)
{
    DEV_BROADCAST_DEVICEINTERFACE *pDi = NULL;

    if (pbDeviceLost == NULL)
    {
        return E_POINTER;
    }

    *pbDeviceLost = FALSE;
    
    if (g_pSource == NULL)
    {
        return S_OK;
    }
    if (pHdr == NULL)
    {
        return S_OK;
    }
    if (pHdr->dbch_devicetype != DBT_DEVTYP_DEVICEINTERFACE)
    {
        return S_OK;
    }

    // Compare the device name with the symbolic link.

    pDi = (DEV_BROADCAST_DEVICEINTERFACE*)pHdr;

    if (g_pwszSymbolicLink)
    {
        if (_wcsicmp(g_pwszSymbolicLink, pDi->dbcc_name) == 0)
        {
            *pbDeviceLost = TRUE;
        }
    }

    return S_OK;
}
```



## Unregister For Notification

Before the application exits, call [**UnregisterDeviceNotification**](base.unregisterdevicenotification) to unregister for device notifications/


```C++
void OnClose(HWND /*hwnd*/)
{
    if (g_hdevnotify)
    {
        UnregisterDeviceNotification(g_hdevnotify);
    }

    PostQuitMessage(0);
}
```



## Related topics

<dl> <dt>

[Enumerating Video Capture Devices](enumerating-video-capture-devices.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



