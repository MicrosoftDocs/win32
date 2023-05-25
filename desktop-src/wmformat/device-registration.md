---
title: Device Registration
description: Device Registration
ms.assetid: 64a6f366-1317-47b6-94a2-ca2ef14d1f88
keywords:
- Windows Media Format SDK,device registration
- Windows Media Format SDK,registration of devices
- Advanced Systems Format (ASF),device registration
- ASF (Advanced Systems Format),device registration
- Advanced Systems Format (ASF),registration of devices
- ASF (Advanced Systems Format),registration of devices
- digital rights management (DRM),device registration
- DRM (digital rights management),device registration
- digital rights management (DRM),registration of devices
- DRM (digital rights management),registration of devices
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Registration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK provides access to the device registration database. This database is secured on the client computer and is used to register devices that support Windows Media DRM 10 for Network Devices.

When a device is added to a network to which the client computer is connected, the device attempts to contact a Windows Media DRM 10 for Network Devices transmitter application. After establishing communications, the device sends a registration request message.

Your application should perform the following steps when it receives a registration request message:

1.  Parse the message by calling the [**IWMDRMMessageParser::ParseRegistrationReqMsg**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmmessageparser-parseregistrationreqmsg) method. This method retrieves the device certificate and the device serial number, both of which are needed to identify the device.
2.  Call the [**IWMDeviceRegistration::GetRegisteredDeviceByID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-getregistereddevicebyid) method, passing in the certificate and device serial number retrieved in step 1. If the device is found, it is already registered and you can skip the next step.
3.  Call the [**IWMDeviceRegistration::RegisterDevice**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-registerdevice) method to add the device to the device registration database.

You can access information about any device in the registration database by retrieving the registered device object associated with it. There are two ways to get a registered device object. If you have the certificate and serial number of the device, you can call the [**IWMDeviceRegistration::GetRegisteredDeviceByID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-getregistereddevicebyid) method. If you do not have the certificate and serial number of the device, you can enumerate all the devices in the database by calling [**IWMDeviceRegistration::GetFirstRegisteredDevice**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-getfirstregistereddevice) followed by repeated calls to [**IWMDeviceRegistration::GetNextRegisteredDevice**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdeviceregistration-getnextregistereddevice) until a call returns S\_FALSE.

Before your application can send data to a device, you must ensure that the device is approved, validated, and open.

Device approval should involve interaction with the user. When a device sends a registration message, your application can prompt the user to decide whether the device is one that should receive that user's data. Then update the device registration database by calling the [**IWMRegisteredDevice::Approve**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-approve) method, passing **TRUE** or **FALSE** as appropriate.

Validation is also called proximity detection. This is a process by which the internal DRM objects of the Windows Media Format SDK determine whether the device is "near" enough to the computer running your application to securely transmit media. Nearness is determined by the time it takes to get a response to a message. This feature is intended to prevent unauthorized users from accessing your network and obtaining your secured media. For more information, see [Performing Proximity Detection](performing-proximity-detection.md).

To open a device, call [**IWMRegisteredDevice::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistereddevice-open).

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**IWMRegisteredDevice**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistereddevice)
</dt> <dt>

[**Using the Windows Media DRM 10 for Network Devices Protocol**](using-the-windows-media-drm-10-for-network-devices-protocol.md)
</dt> </dl>

 

 




