---
title: Performing Proximity Detection
description: Performing Proximity Detection
ms.assetid: 73207c4c-2d8d-4ec3-b3d0-78f55ee0a754
keywords:
- Windows Media Format SDK,performing proximity detection
- Windows Media Format SDK,proximity detection
- Advanced Systems Format (ASF),performing proximity detection
- ASF (Advanced Systems Format),performing proximity detection
- Advanced Systems Format (ASF),proximity detection
- ASF (Advanced Systems Format),proximity detection
- digital rights management (DRM),performing proximity detection
- DRM (digital rights management),performing proximity detection
- digital rights management (DRM),proximity detection
- DRM (digital rights management),proximity detection
- proximity detection
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Performing Proximity Detection

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before you can stream encrypted data to a registered device in the Windows Media DRM 10 for Network Devices protocol, you must perform a process called proximity detection (also called validation). This process involves sending messages to the device and receiving responses. The time it takes to receive a response is used to determine whether the device is "near" enough to the computer on the network to receive secure data. Confirming that the device is physically close to the client computer on the network helps to prevent spoofing and other unauthorized access.

When proximity detection is successfully completed, the device is said to be valid. You can check whether a device is valid by calling the [**IWMRegisteredDevice::IsValid**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-isvalid) method. Devices must be validated every 48 hours. A device that was validated more than 48 hours before your program runs must be revalidated by performing the proximity detection process again.

To perform proximity detection, you must establish communications with the device and then call the [**IWMProximityDetection::StartDetection**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmproximitydetection-startdetection) method. The detection process is completed asynchronously by the internal DRM components of the Windows Media Format SDK. Your application must include an implementation of the [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) interface to process proximity detection messages.

There are two messages that are sent by the proximity detection process: a result message and a completion message.

The result message, WMT\_PROXIMITY\_RESULT, is sent when the detection process is completed. The *hr* parameter of the [**OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method indicates whether the device was found to be near enough to the client computer. If the *hr* parameter of the result message indicates success, the *pValue* parameter contains a **DWORD** specifying the measured latency to the device in milliseconds.

The completion message, WMT\_PROXIMITY\_COMPLETED, is sent when the detection is finalized. You should release the [**IWMProximityDetection**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmproximitydetection) interface only after receiving this message.

When proximity detection for a device succeeds, the device registration database is automatically updated. Subsequent calls to [**IWMRegisteredDevice::IsValid**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-isvalid) will return **TRUE** until 48 hours have passed and the device needs to be revalidated.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Using the Windows Media DRM 10 for Network Devices Protocol**](using-the-windows-media-drm-10-for-network-devices-protocol.md)
</dt> </dl>

 

 




