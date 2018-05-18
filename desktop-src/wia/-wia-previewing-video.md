---
Description: 'The IWiaVideo interface enables an application to view video and capture still images from it.'
ms.assetid: '59eddbdc-4957-44be-a602-0763f3385e89'
title: Previewing Video
---

# Previewing Video

The [**IWiaVideo**](-wia-iwiavideo.md) interface enables an application to view video and capture still images from it. Perform the following steps to select the streaming video device and display a video stream in a window.

-   Call [CoCreateInstance](com.cocreateinstance) to retrieve a pointer to the [**IWiaDevMgr**](-wia-iwiadevmgr.md) interface.
-   Use the [**IWiaDevMgr::EnumDeviceInfo**](-wia-iwiadevmgr-enumdeviceinfo.md) method of the [**IWiaDevMgr**](-wia-iwiadevmgr.md) interface to obtain a pointer to the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) interface. For instructions on how to enumerate devices, see Enumerating System Devices.
-   Use the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) interface to obtain an [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interface pointer for each Windows Image Acquisition (WIA) device found.
-   Use the [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interface to get the DeviceID property of the desired device. A streaming video device has the StiDeviceTypeStreamingVideo flag of the WIA\_DIP\_DEV\_TYPE property set.
-   Use the [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interface to get the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [CoCreateInstance](com.cocreateinstance) to retrieve a pointer to the [**IWiaVideo**](-wia-iwiavideo.md) interface.
-   Set the [**IWiaVideo::ImagesDirectory**](-wia-iwiavideo-imagesdirectory.md) property of the [**IWiaVideo**](-wia-iwiavideo.md) interface to the value received from the WIA\_DPV\_IMAGES\_DIRECTORY property value.
-   Call [**IWiaVideo::CreateVideoByWiaDevID**](-wia-iwiavideo-createvideobywiadevid.md) on the [**IWiaVideo**](-wia-iwiavideo.md) interface, passing the device ID of the streaming image device and the handle of the window in which the video is to be displayed.

> [!Note]  
> WIA does not support video devices in Windows Server 2003, Windows Vista, or later. For those versions of the Windows, use [DirectShow](http://msdn.microsoft.com/en-us/library/ms783323(VS.85).aspx) to acquire images from video.

 

 

 



