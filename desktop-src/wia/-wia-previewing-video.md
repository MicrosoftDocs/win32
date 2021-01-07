---
description: The IWiaVideo interface enables an application to view video and capture still images from it.
ms.assetid: 59eddbdc-4957-44be-a602-0763f3385e89
title: Previewing Video (WIA)
ms.topic: article
ms.date: 05/31/2018
---

# Previewing Video (WIA)

The [**IWiaVideo**](/windows/desktop/api/Wiavideo/nn-wiavideo-iwiavideo) interface enables an application to view video and capture still images from it. Perform the following steps to select the streaming video device and display a video stream in a window.

-   Call [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to retrieve a pointer to the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) interface.
-   Use the [**IWiaDevMgr::EnumDeviceInfo**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo) method of the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) interface to obtain a pointer to the [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface. For instructions on how to enumerate devices, see Enumerating System Devices.
-   Use the [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface to obtain an [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface pointer for each Windows Image Acquisition (WIA) device found.
-   Use the [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface to get the DeviceID property of the desired device. A streaming video device has the StiDeviceTypeStreamingVideo flag of the WIA\_DIP\_DEV\_TYPE property set.
-   Use the [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface to get the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to retrieve a pointer to the [**IWiaVideo**](/windows/desktop/api/Wiavideo/nn-wiavideo-iwiavideo) interface.
-   Set the [**IWiaVideo::ImagesDirectory**](/windows/desktop/api/Wiavideo/nf-wiavideo-iwiavideo-get_imagesdirectory) property of the [**IWiaVideo**](/windows/desktop/api/Wiavideo/nn-wiavideo-iwiavideo) interface to the value received from the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [**IWiaVideo::CreateVideoByWiaDevID**](/windows/desktop/api/Wiavideo/nf-wiavideo-iwiavideo-createvideobywiadevid) on the [**IWiaVideo**](/windows/desktop/api/Wiavideo/nn-wiavideo-iwiavideo) interface, passing the device ID of the streaming image device and the handle of the window in which the video is to be displayed.

> [!Note]  
> WIA does not support video devices in Windows Server 2003, Windows Vista, or later. For those versions of the Windows, use [DirectShow](/previous-versions//ms783323(v=vs.85)) to acquire images from video.

 

 

 
