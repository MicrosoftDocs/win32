---
title: Using the Windows Deployment Services Client API
description: In environments where a standard Windows Deployment Services (WDS) solution cannot be used to install Windows, the API of the WDS client enables developers to write custom deployment applications.
ms.assetid: 'abe2a7c7-989a-456e-80df-90d5b816db38'
keywords: ["Windows Deployment Services Windows Deployment Services , using the client API"]
---

# Using the Windows Deployment Services Client API

In environments where a standard Windows Deployment Services (WDS) solution cannot be used to install Windows, the API of the WDS client enables developers to write custom deployment applications. Applications can use this API to communicate with the WDS server to get information about system images available from the server. Custom WDS client applications should adhere to the following guidelines.

## Install the WDS Role on the Server

-   Windows Deployment Services (WDS) is the revised version of Remote Installation Services (RIS), you will need the WDS server role on the server to implement custom WDS client solutions.
-   WDS replaces RIS as the standard component starting with Windows Server 2008 and Windows Server 2003 with Service Pack 2 (SP2).
-   You must update the RIS server to WDS on Windows Server 2003 with Service Pack 1 (SP1). You can install the WDS server role with the [Windows Automated Installation Kit (WAIK)](http://go.microsoft.com/fwlink/p/?linkid=53552).

## Start Windows PE 2.0

Windows PE 2.0 must be started, if not already started. The WDS client and supporting DLLs are only loaded by setup.exe when it is in the Microsoft Windows Preinstallation Environment (Windows PE 2.0) phase of setup processing.

-   When a new computer is connected to the network, the built-in preboot execution environment (PXE) technology can be used to download the Network Boot Program. For more information about PXE-booting a computer to install Windows, see [The Windows Deployment Services Update Step-by-Step Guide](http://go.microsoft.com/fwlink/p/?linkid=66145).
-   A RAMDISK bootable image of Windows PE 2.0 can be stored in the .WIM format and downloaded as part of the network boot process. Windows PE can then be loaded and run directly from that media.

## Open a session with the WDS server

The WDS client must open a session with a WDS server.

-   Use the [**WdsCliCreateSession**](wdsclicreatesession.md) function to open a session with a WDS server. This function takes the name or IP address of the server and receives the address of the handle for the WDS client session.
-   If opening the session with the server will require authenticating the WDS client, the application should provide the address of a [**WDS\_CLI\_CRED**](wds-cli-cred.md) structure containing the client credentials when calling the [**WdsCliCreateSession**](wdsclicreatesession.md) function. The application can use the [**WdsCliAuthorizeSession**](wdscliauthorizesession.md) function to convert an anonymous session into an authenticated session.
-   When the session opened with the [**WdsCliCreateSession**](wdsclicreatesession.md) function is no longer needed, the application should use the [**WdsCliClose**](wdscliclose.md) function to close the handle and release resources held by the session.

## Enumerate system images on the WDS server

The WDS client can use the API to enumerate the system images on the WDS server.

-   Use the [**WdsCliFindFirstImage**](wdsclifindfirstimage.md) function to obtain a handle to the first image and to initialize the enumeration of images on the WDS server.
-   Use the [**WdsCliFindNextImage**](wdsclifindnextimage.md) function to increment the enumeration started by the [**WdsCliFindFirstImage**](wdsclifindfirstimage.md) function. The **WdsCliFindNextImage** function gets the handle for the next image.
-   Use the [**WdsCliGetImageIndex**](wdscligetimageindex.md) function to obtain the image index for the current image. This value is valid only until the [**WdsCliFindNextImage**](wdsclifindnextimage.md) or [**WdsCliClose**](wdscliclose.md) functions are used again.
-   Use the [**WdsCliGetEnumerationFlags**](wdscligetenumerationflags.md) function to get informational flags about image filtering.

## Get information about images

The WDS client can use the API to get information about the images on a WDS server. The following functions get information about the current image. Because the [**WdsCliFindFirstImage**](wdsclifindfirstimage.md) and [**WdsCliFindNextImage**](wdsclifindnextimage.md) functions change the current image handle value, the application should store any information it gets and will need in the future before calling the **WdsCliFindFirstImage** or **WdsCliFindNextImage** functions again.

-   Use the [**WdsCliGetImageArchitecture**](wdscligetimagearchitecture.md) function to get the processor architecture of the current image.
-   Use the [**WdsCliGetImagePath**](wdscligetimagepath.md) function to get the relative path to the image file that contains the current image.
-   Use the [**WdsCliGetImageSize**](wdscligetimagesize.md) function to get the image size.
-   Use the [**WdsCliGetImageVersion**](wdscligetimageversion.md) function to get the image version.
-   Use the [**WdsCliGetImageLanguage**](wdscligetimagelanguage.md) function to get the default language of the current image.
-   Use the [**WdsCliGetImageLanguages**](wdscligetimagelanguages.md) function to get an array of languages supported by the current image.
-   Use the [**WdsCliGetImageLastModifiedTime**](wdscligetimagelastmodifiedtime.md) returns the last-modified time for the current image.
-   Use the [**WdsCliGetImageName**](wdscligetimagename.md) function to get the name of the current image.
-   Use the [**WdsCliGetImageDescription**](wdscligetimagedescription.md) function to get the description of the current image.
-   Use the [**WdsCliGetImageGroup**](wdscligetimagegroup.md) function to get the image group name for the current image.
-   Use the [**WdsCliGetImageHalName**](wdscligetimagehalname.md) function to get the Hardware Abstraction Layer (HAL) name for the current image.

## Log WDS Client Events

The logging functionality of the WDS client library enables installation progress events to be sent from the client to the WDS server.

-   Use the [**WdsCliInitializeLog**](wdscliinitializelog.md) function to initialize the log for the WDS client session.
-   Use the [**WdsCliLog**](wdsclilog.md) function to write event messages to the WDS server log.
-   On Windows Server 2008, the WDS server writes client events to an application specific event log that is viewable through eventvwr.exe as well as the debug trace log. On Windows Server 2003 with debug logging enabled, the WDS server will write client events to the log file located at %windir%\\tracing\\wdsserver.log. WDS Client logging must be enabled on the server to capture these events.

## Related topics

<dl> <dt>

[About the Windows Deployment Services API](about-the-windows-deployment-services-api.md)
</dt> <dt>

[Using the Windows Deployment Services Server API](using-the-windows-deployment-services-server-api.md)
</dt> </dl>

 

 




