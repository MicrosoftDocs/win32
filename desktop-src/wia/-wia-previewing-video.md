---
Description: The IWiaVideo interface enables an application to view video and capture still images from it.
ms.assetid: 59eddbdc-4957-44be-a602-0763f3385e89
title: Previewing Video
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Previewing Video

The [**IWiaVideo**](/windows/win32/Wiavideo/nn-wiavideo-iwiavideo?branch=master) interface enables an application to view video and capture still images from it. Perform the following steps to select the streaming video device and display a video stream in a window.

-   Call [CoCreateInstance](com.cocreateinstance) to retrieve a pointer to the [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) interface.
-   Use the [**IWiaDevMgr::EnumDeviceInfo**](/windows/win32/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo?branch=master) method of the [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) interface to obtain a pointer to the [**IEnumWIA\_DEV\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_info?branch=master) interface. For instructions on how to enumerate devices, see Enumerating System Devices.
-   Use the [**IEnumWIA\_DEV\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_info?branch=master) interface to obtain an [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface pointer for each Windows Image Acquisition (WIA) device found.
-   Use the [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface to get the DeviceID property of the desired device. A streaming video device has the StiDeviceTypeStreamingVideo flag of the WIA\_DIP\_DEV\_TYPE property set.
-   Use the [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface to get the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [CoCreateInstance](com.cocreateinstance) to retrieve a pointer to the [**IWiaVideo**](/windows/win32/Wiavideo/nn-wiavideo-iwiavideo?branch=master) interface.
-   Set the [**IWiaVideo::ImagesDirectory**](/windows/win32/Wiavideo/nf-wiavideo-iwiavideo-get_imagesdirectory?branch=master) property of the [**IWiaVideo**](/windows/win32/Wiavideo/nn-wiavideo-iwiavideo?branch=master) interface to the value received from the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [**IWiaVideo::CreateVideoByWiaDevID**](/windows/win32/Wiavideo/nf-wiavideo-iwiavideo-createvideobywiadevid?branch=master) on the [**IWiaVideo**](/windows/win32/Wiavideo/nn-wiavideo-iwiavideo?branch=master) interface, passing the device ID of the streaming image device and the handle of the window in which the video is to be displayed.

> [!Note]  
> WIA does not support video devices in Windows Server 2003, Windows Vista, or later. For those versions of the Windows, use [DirectShow](http://msdn.microsoft.com/en-us/library/ms783323(VS.85).aspx) to acquire images from video.

 

 

 



