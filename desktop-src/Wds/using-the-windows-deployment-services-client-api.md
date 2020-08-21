---
title: Using the Windows Deployment Services Client API
description: In environments where a standard Windows Deployment Services (WDS) solution cannot be used to install Windows, the API of the WDS client enables developers to write custom deployment applications.
ms.assetid: abe2a7c7-989a-456e-80df-90d5b816db38
keywords:
- Windows Deployment Services Windows Deployment Services , using the client API
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Deployment Services Client API

In environments where a standard Windows Deployment Services (WDS) solution cannot be used to install Windows, the API of the WDS client enables developers to write custom deployment applications. Applications can use this API to communicate with the WDS server to get information about system images available from the server. Custom WDS client applications should adhere to the following guidelines.

## Install the WDS Role on the Server

-   Windows Deployment Services (WDS) is the revised version of Remote Installation Services (RIS), you will need the WDS server role on the server to implement custom WDS client solutions.
-   WDS replaces RIS as the standard component starting with Windows Server 2008 and Windows Server 2003 with Service Pack 2 (SP2).
-   You must update the RIS server to WDS on Windows Server 2003 with Service Pack 1 (SP1). You can install the WDS server role with the [Windows Automated Installation Kit (WAIK)](https://www.microsoft.com/download/details.aspx?id=10333).

## Start Windows PE 2.0

Windows PE 2.0 must be started, if not already started. The WDS client and supporting DLLs are only loaded by setup.exe when it is in the Microsoft Windows Preinstallation Environment (Windows PE 2.0) phase of setup processing.

-   When a new computer is connected to the network, the built-in preboot execution environment (PXE) technology can be used to download the Network Boot Program. For more information about PXE-booting a computer to install Windows, see [The Windows Deployment Services Update Step-by-Step Guide](/previous-versions/windows/it-pro/windows-vista/cc766320(v=ws.10)).
-   A RAMDISK bootable image of Windows PE 2.0 can be stored in the .WIM format and downloaded as part of the network boot process. Windows PE can then be loaded and run directly from that media.

## Open a session with the WDS server

The WDS client must open a session with a WDS server.

-   Use the [**WdsCliCreateSession**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclicreatesession) function to open a session with a WDS server. This function takes the name or IP address of the server and receives the address of the handle for the WDS client session.
-   If opening the session with the server will require authenticating the WDS client, the application should provide the address of a [**WDS\_CLI\_CRED**](/windows/win32/api/wdsclientapi/ns-wdsclientapi-wds_cli_cred) structure containing the client credentials when calling the [**WdsCliCreateSession**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclicreatesession) function. The application can use the [**WdsCliAuthorizeSession**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscliauthorizesession) function to convert an anonymous session into an authenticated session.
-   When the session opened with the [**WdsCliCreateSession**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclicreatesession) function is no longer needed, the application should use the [**WdsCliClose**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscliclose) function to close the handle and release resources held by the session.

## Enumerate system images on the WDS server

The WDS client can use the API to enumerate the system images on the WDS server.

-   Use the [**WdsCliFindFirstImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindfirstimage) function to obtain a handle to the first image and to initialize the enumeration of images on the WDS server.
-   Use the [**WdsCliFindNextImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindnextimage) function to increment the enumeration started by the [**WdsCliFindFirstImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindfirstimage) function. The **WdsCliFindNextImage** function gets the handle for the next image.
-   Use the [**WdsCliGetImageIndex**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimageindex) function to obtain the image index for the current image. This value is valid only until the [**WdsCliFindNextImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindnextimage) or [**WdsCliClose**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscliclose) functions are used again.
-   Use the [**WdsCliGetEnumerationFlags**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetenumerationflags) function to get informational flags about image filtering.

## Get information about images

The WDS client can use the API to get information about the images on a WDS server. The following functions get information about the current image. Because the [**WdsCliFindFirstImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindfirstimage) and [**WdsCliFindNextImage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclifindnextimage) functions change the current image handle value, the application should store any information it gets and will need in the future before calling the **WdsCliFindFirstImage** or **WdsCliFindNextImage** functions again.

-   Use the [**WdsCliGetImageArchitecture**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagearchitecture) function to get the processor architecture of the current image.
-   Use the [**WdsCliGetImagePath**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagepath) function to get the relative path to the image file that contains the current image.
-   Use the [**WdsCliGetImageSize**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagesize) function to get the image size.
-   Use the [**WdsCliGetImageVersion**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimageversion) function to get the image version.
-   Use the [**WdsCliGetImageLanguage**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagelanguage) function to get the default language of the current image.
-   Use the [**WdsCliGetImageLanguages**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagelanguages) function to get an array of languages supported by the current image.
-   Use the [**WdsCliGetImageLastModifiedTime**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagelastmodifiedtime) returns the last-modified time for the current image.
-   Use the [**WdsCliGetImageName**](/windows/win32/api/WdsClientApi/nf-wdsclientapi-wdscligetimagename) function to get the name of the current image.
-   Use the [**WdsCliGetImageDescription**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagedescription) function to get the description of the current image.
-   Use the [**WdsCliGetImageGroup**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagegroup) function to get the image group name for the current image.
-   Use the [**WdsCliGetImageHalName**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscligetimagehalname) function to get the Hardware Abstraction Layer (HAL) name for the current image.

## Log WDS Client Events

The logging functionality of the WDS client library enables installation progress events to be sent from the client to the WDS server.

-   Use the [**WdsCliInitializeLog**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdscliinitializelog) function to initialize the log for the WDS client session.
-   Use the [**WdsCliLog**](/windows/win32/api/WdsClientAPI/nf-wdsclientapi-wdsclilog) function to write event messages to the WDS server log.
-   On Windows Server 2008, the WDS server writes client events to an application specific event log that is viewable through eventvwr.exe as well as the debug trace log. On Windows Server 2003 with debug logging enabled, the WDS server will write client events to the log file located at %windir%\\tracing\\wdsserver.log. WDS Client logging must be enabled on the server to capture these events.

## Related topics

<dl> <dt>

[About the Windows Deployment Services API](about-the-windows-deployment-services-api.md)
</dt> <dt>

[Using the Windows Deployment Services Server API](using-the-windows-deployment-services-server-api.md)
</dt> </dl>

 

 