---
title: Creating a Windows Media Device Manager Application
description: Creating a Windows Media Device Manager Application
ms.assetid: 6a200bd9-19dd-4130-acb4-e038b469c334
keywords:
- Windows Media Device Manager,creating applications
- Device Manager,creating applications
- Windows Media Device Manager,programming guide
- Device Manager,programming guide
- programming guide,desktop applications
- programming guide,Windows Media Device Manager
- programming guide,plug-ins
- programming guide,creating applications
- Windows Media Device Manager,desktop applications
- Device Manager,desktop applications
- Windows Media Device Manager,plug-ins
- Device Manager,plug-insp
- plug-ins,creating
- plug-ins,programming guide
- desktop applications,creating
- creating Windows Media Device Manager applications,about
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Windows Media Device Manager Application

This section describes how to use Windows Media Device Manager in your application. The term "application" here means either an executable, such as a media player, or a COM plug-in, such as a metering plug-in.

Microsoft includes several service providers with Windows XP and Windows Media Player 10, including an MTP service provider, a Windows CE service provider (for devices running Windows CE and using the RAPI protocol, such as the Pocket PC), and a service provider for mass-storage category (MSC) devices. You can also create your own service provider to ensure communication with your own device; for more information, see [Creating a Service Provider](creating-a-service-provider.md).

There are a number of third-party legacy service providers that address a particular manufacturer's non-MTP, non-RAPI, or non-MSC device. These service providers are included on the driver disk shipped with these devices.

An application that uses Windows Media Device Manager must perform the following steps.

1.  **Become aware of privacy issues involved with developing an application.** See [Privacy Statement](privacy-statement.md) to learn about some privacy issues involving developing a Windows Media Device Manager application.
2.  **Include the required library and header files for your application.** See [Required Library and Header Files for an Application](required-library-and-header-files-for-an-application.md) to learn what files you will need to include in your project.
3.  **Authenticate the application and acquire the root IWMDMDevice interface.** The first task an application must do to use Windows Media Device Manager is to authenticate itself. This process verifies the identity of the application to Windows Media Device Manager using a dummy certificate for limited Windows Media Device Manager functionality, or using an official certificate for full functionality. For more information, see [Authenticating the Application](authenticating-the-application.md).
4.  **Enumerate the connected devices.** The first step in communicating with devices is to find out what devices are connected and accessible to Windows Media Device Manager. For more information, see [Enumerating Devices](enumerating-devices.md).
5.  **Check the status of the device's DRM components.** To use DRM-protected files, a device must be built on some version of Windows Media DRM for Portable Devices, and the DRM components must be up to date. Before you begin handling files on the device, it is best to see if the device supports DRM-protected files, and whether the device needs to be updated. For more information, see [Handling Protected Content in the Application](handling-protected-content-in-the-application.md).
6.  **Explore a device.** After you have found the device you want, you can explore the contents of that device. For more information, see [Exploring a Device](exploring-a-device.md).
7.  **Read files from the device, and write files to the device.** After you know about the layout of the device, you can begin transferring files to and from the device. For more information, see [Reading Files from the Device](reading-files-from-the-device.md) and [Writing Files to the Device](writing-files-to-the-device.md).
8.  **Create playlists on the device.** One kind of file you can write to the device is an abstract file, which is a collection of references to other files. Although the ability to write abstract files to a device depends on the service provider and the device, generally only MTP devices have this capability. For more information, see [Creating a Playlist on the Device](creating-a-playlist-on-the-device.md).

In addition to these steps, there are several more features that you can enable in your application:

-   **Notifications.** You can enable your application to receive notifications when devices connect or disconnect from the computer. For more information, see [Enabling Notifications](enabling-notifications.md).
-   **Logging.** Windows Media Device Manager uses a logging object that saves a record of its actions to a local text file. You can add messages to this log to help you analyze errors or performance in your application. For more information, see [Enabling Logging](enabling-logging.md).
-   **Metering content usage.** You can retrieve content usage statistics for licenses that grant this right. These statistics can then be sent up to a Web server to calculate royalty payments to content owners. For more information, see [Metering Content Usage](metering-content-usage.md).

**A note of caution**

Your application may need to work with a variety of devices, including some that you have not developed and have never tested your code against. These devices might or might not accurately respond to queries and commands, or implement MTP or other specifications. Be sure to include robust error checking and fallback functionality to deal with the unexpected. Program defensively.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




