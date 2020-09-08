---
title: Metering Content Usage
description: Metering Content Usage
ms.assetid: f87b5d95-a497-4356-817f-49ac3819df08
keywords:
- Windows Media Device Manager,metering content usage
- Device Manager,metering content usage
- programming guide,metering content usage
- desktop applications,metering content usage
- creating Windows Media Device Manager applications,metering content usage
- metering content usage
ms.topic: article
ms.date: 05/31/2018
---

# Metering Content Usage

With Windows Media 10 technology, you can now meter content usage on a portable device. If a Windows Media 10 license allows metering, the device can store the play count for songs and upload usage back to the license issuer over the Internet. This system enables content providers to adjust their royalty fees by accurately measuring content usage.

To meter content, the application must have a metering certificate provided by a licensing service built on the Windows Media Rights Manager 10 SDK. Only content licensed by this same service can be metered. For more information on how metering works, and how to build a license metering service, see the [Windows Media Rights Manager SDK documentation](/previous-versions/ms986509(v=msdn.10)) on MSDN. The SDK can be acquired by filling out the necessary information on the [Windows Media Licensing Page](https://www.microsoft.com/licensing/default).

An application can have metering built in to it, or you can build a COM plug-in for an existing application, such as the Windows Media Player, if the application accepts metering plug-ins.

An application should warn users if content usage will be metered. For more information, see the Microsoft Web pages listed in the [Privacy Statement](privacy-statement.md).

Acquiring metering data from a device can be slow. Therefore, if an application meters usage, it should do so frequently to prevent large amounts of data from accumulating on the device and slowing down the data transfer. To prevent data transfers that would be too slow, device manufacturers can send subsets of available metering data. The application should monitor the flags retrieved by [**IWMDRMDeviceApp::ProcessMeterResponse**](iwmdrmdeviceapp-processmeterresponse.md) to see if any more metering data remains on the device.

The following steps show how an application can meter content usage.

1.  Because metering is only available on devices that support Windows Media DRM 10 for Portable Devices, your application should at some point call **QueryDeviceStatus**, as described in [Handling Protected Content in the Application](handling-protected-content-in-the-application.md), to ensure that the device is valid and up to date.
2.  Request metering information from the device by calling [**IWMDRMDeviceApp::GenerateMeterChallenge**](iwmdrmdeviceapp-generatemeterchallenge.md).
3.  Send the retrieved metering data to the metering service at the URL retrieved by **GenerateMeterChallenge**. The format of data sent to the service depends on the scripting on that particular service. For example, some services might require the data sent as a POST command as a name/value pair. The service provider should let you know their particular formatting requirements.
4.  Get a response from the metering service, and send it to the device by calling [**IWMDRMDeviceApp::ProcessMeterResponse**](iwmdrmdeviceapp-processmeterresponse.md). This causes the device to reset play counts, and also returns a value indicating whether more metering data exists on the device that should be retrieved by calling **GenerateMeterChallenge** again.

For extensive information and sample code for metering, see the [Windows Media Web site](/previous-versions//bb614723(v=vs.85)).

 

 