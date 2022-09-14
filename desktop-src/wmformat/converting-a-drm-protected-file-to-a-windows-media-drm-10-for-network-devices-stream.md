---
title: Converting a DRM-Protected File to a Windows Media DRM 10 for Network Devices Stream
description: Converting a DRM-Protected File to a Windows Media DRM 10 for Network Devices Stream
ms.assetid: 11aa0cfd-6d87-4ec4-82d8-db2507402911
keywords:
- Windows Media Format SDK,converting DRM-protected files
- Windows Media Format SDK,DRM-protected files
- Advanced Systems Format (ASF),converting DRM-protected files
- ASF (Advanced Systems Format),converting DRM-protected files
- Advanced Systems Format (ASF),DRM-protected files
- ASF (Advanced Systems Format),DRM-protected files
- digital rights management (DRM),converting DRM-protected files
- DRM (digital rights management),converting DRM-protected files
- digital rights management (DRM),DRM-protected files
- DRM (digital rights management),DRM-protected files
- Windows Media Format SDK,Windows Media DRM 10 for Network Devices
- Windows Media Format SDK,DRM 10 for Network Devices
- Advanced Systems Format (ASF),Windows Media DRM 10 for Network Devices
- ASF (Advanced Systems Format),Windows Media DRM 10 for Network Devices
- Advanced Systems Format (ASF),DRM 10 for Network Devices
- ASF (Advanced Systems Format),DRM 10 for Network Devices
- digital rights management (DRM),Windows Media DRM 10 for Network Devices
- DRM (digital rights management),Windows Media DRM 10 for Network Devices
- digital rights management (DRM),DRM 10 for Network Devices
- DRM (digital rights management),DRM 10 for Network Devices
- Windows Media DRM 10 for Network Devices,converting DRM-protected files
- DRM 10 for Network Devices,converting DRM-protected files
ms.topic: article
ms.date: 05/31/2018
---

# Converting a DRM-Protected File to a Windows Media DRM 10 for Network Devices Stream

After a device is registered and validated, you can begin processing license request messages from it. License request messages are sent by devices when action from the application is needed. The only action currently supported is "Play", which is a request for secure data for playback.

When you receive a license request message, you should perform the following steps:

1.  Parse the license request message by calling the [**IWMDRMMessageParser::ParseLicenseRequestMsg**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmmessageparser-parselicenserequestmsg) method.
2.  Get the [**IWMRegisteredDevice**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistereddevice) interface for the device by calling the [**IWMDeviceRegistration::GetRegisteredDeviceByID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-getregistereddevicebyid) method, passing in the certificate and serial number obtained in step 1.
3.  Verify that the device is ready to receive secure data:
    -   Call [**IWMRegisteredDevice::IsApproved**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-isapproved) to verify that the device has been approved. Approval should always be based on user preference.
    -   Call [**IWMRegisteredDevice::IsValid**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-isvalid) to verify that the device has been validated within the last 48 hours. If the device is not valid, you need to perform proximity detection. For more information, see [Performing Proximity Detection](performing-proximity-detection.md).
    -   Call [**IWMRegisteredDevice::IsOpened**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-isopened) to verify that the device has been opened. If the device is not open, you can open it by calling [**IWMRegisteredDevice::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-open). You can only have 10 devices open on the computer at a time. It is possible that you may need to close another device before you can open the one for which you are processing the request. To close a device, call the [**IWMRegisteredDevice::Close**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-close) method.
4.  Create an instance of the DRM transcryptor object by calling the [**WMCreateDRMTranscryptor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor) function.
5.  Call the [**IWMDRMTranscryptor::Initialize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmtranscryptor-initialize) method to initialize the transcryptor. This method takes a pointer to your implementation of the [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) interface, which it uses to deliver status messages. This method also returns a license request message that must be sent to the device before continuing.
6.  When your application's [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method receives the WMT\_TRANSCRYPTOR\_INIT status message, call the [**IWMDRMTranscryptor::Seek**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmtranscryptor-seek) method to seek to the appropriate start position in the file. To start at the beginning of the file, you must call **Seek** with time 0.
7.  The transcryptor sends a WMT\_TRANSCRYPTOR\_SEEKED message when it is ready to deliver data from the file at the new presentation time. Make repeated calls to the [**IWMDRMTranscryptor::Read**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmtranscryptor-read) method to get converted chunks of media data. Each call is asynchronous and is not complete until a WMT\_TRANSCRYPTOR\_READ message is received. When you receive the message, you can send the data to the receiving device.
8.  When you receive a WMT\_TRANSCRYPTOR\_READ message with the *hr* parameter set to NS\_S\_TRANSCRYPTOR\_EOF, the entire file has been read. At this point, call the [**IWMDRMTranscryptor::Close**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmtranscryptor-close) method to close the file and free resources.
9.  When the WMT\_TRANSCRYPTOR\_CLOSED message is received, you can release the [**IWMDRMTranscryptor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmtranscryptor) interface.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Using the Windows Media DRM 10 for Network Devices Protocol**](using-the-windows-media-drm-10-for-network-devices-protocol.md)
</dt> </dl>

 

 




