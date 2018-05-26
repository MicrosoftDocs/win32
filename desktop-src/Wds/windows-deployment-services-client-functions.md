---
title: Windows Deployment Services Client Functions
description: The following functions are used with the Windows Deployment Services Client API.
ms.assetid: 4cedd8a8-7f46-4229-9d96-58965b751e43
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Deployment Services Client Functions

The following functions are used with the Windows Deployment Services Client API.



| Function                                                                                 | Description                                                                                                                            |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [*PFN\_WdsCliCallback*](/windows/win32/WdsClientAPI/nc-wdsclientapi-pfn_wdsclicallback?branch=master)                                          | Progress notification and error messages during a file or image transfer.                                                              |
| [*PFN\_WdsCliTraceFunction*](/windows/win32/WdsClientAPI/nc-wdsclientapi-pfn_wdsclitracefunction?branch=master)                                | Receives debugging messages from the WDS client.                                                                                       |
| [**WdsCliAuthorizeSession**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliauthorizesession?branch=master)                                 | Converts an anonymous session into an authenticated session.                                                                           |
| [**WdsCliCancelTransfer**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclicanceltransfer?branch=master)                                     | Cancels a WDS transfer operation.                                                                                                      |
| [**WdsCliClose**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliclose?branch=master)                                                       | Closes a handle to a WDS session or image and releases resources.                                                                      |
| [**WdsCliCreateSession**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclicreatesession?branch=master)                                       | Starts a new session with a WDS server.                                                                                                |
| [**WdsCliFindFirstImage**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclifindfirstimage?branch=master)                                     | Starts the enumeration of images stored on a WDS server and returns a find handle that references the first image.                     |
| [**WdsCliFindNextImage**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclifindnextimage?branch=master)                                       | Advances the reference of a find handle to the next image stored on a WDS server.                                                      |
| [**WdsCliFreeStringArray**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclifreestringarray?branch=master)                                   | Frees the array of string values that gets allocated by the [**WdsCliObtainDriverPackages**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliobtaindriverpackages?branch=master) function. |
| [**WdsCliGetEnumerationFlags**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetenumerationflags?branch=master)                           | Returns the image enumeration flag for the current image handle.                                                                       |
| [**WdsCliGetImageArchitecture**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagearchitecture?branch=master)                         | Returns the processor architecture for the current image.                                                                              |
| [**WdsCliGetImageDescription**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagedescription?branch=master)                           | Returns the description of the current image.                                                                                          |
| [**WdsCliGetImageGroup**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagegroup?branch=master)                                       | Returns the image group name for the current image.                                                                                    |
| [**WdsCliGetImageHalName**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagehalname?branch=master)                                   | Returns the Hardware Abstraction Layer (HAL) name for the current image.                                                               |
| [**WdsCliGetImageHandleFromFindHandle**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagehandlefromfindhandle?branch=master)         | Returns an image handle for the current image.                                                                                         |
| [**WdsCliGetImageHandleFromTransferHandle**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagehandlefromtransferhandle?branch=master) | Returns an image handle from a completed transfer handle.                                                                              |
| [**WdsCliGetImageIndex**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimageindex?branch=master)                                       | Returns the image index for the current image.                                                                                         |
| [**WdsCliGetImageLanguage**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagelanguage?branch=master)                                 | Returns the default language of the current image.                                                                                     |
| [**WdsCliGetImageLanguages**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagelanguages?branch=master)                               | Returns an array of languages supported by the current image.                                                                          |
| [**WdsCliGetImageLastModifiedTime**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagelastmodifiedtime?branch=master)                 | Returns the last-modified time for the current image.                                                                                  |
| [**WdsCliGetImageName**](/windows/win32/WdsClientApi/nf-wdsclientapi-wdscligetimagename?branch=master)                                         | Returns the name of the current image.                                                                                                 |
| [**WdsCliGetImageNamespace**](/windows/win32/WdsClientApi/nf-wdsclientapi-wdscligetimagenamespace?branch=master)                               | Returns the name of the current image.                                                                                                 |
| [**WdsCliGetImagePath**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagepath?branch=master)                                         | Returns the path to the image file that contains the current image.                                                                    |
| [**WdsCliGetImageSize**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimagesize?branch=master)                                         | Returns the size of the current image.                                                                                                 |
| [**WdsCliGetImageVersion**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetimageversion?branch=master)                                   | Returns the version of the current image.                                                                                              |
| [**WdsCliGetTransferSize**](/windows/win32/WdsClientApi/nf-wdsclientapi-wdscligettransfersize?branch=master)                                   | Returns the size of the current transfer.                                                                                              |
| [**WdsCliInitializeLog**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliinitializelog?branch=master)                                       | Initializes the log for the client.                                                                                                    |
| [**WdsCliLog**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclilog?branch=master)                                                           | Sends a log event to the WDS server.                                                                                                   |
| [**WdsCliObtainDriverPackages**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliobtaindriverpackages?branch=master)                         | Obtains from a WDS image, the driver packages (INF files) that can be used on this computer.                                           |
| [**WdsCliRegisterTrace**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliregistertrace?branch=master)                                       | Registers a callback function that will receive debugging messages.                                                                    |
| [**WdsCliTransferFile**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclitransferfile?branch=master)                                         | Transfers a file from a WDS server to the WDS client using a multicast transfer protocol.                                              |
| [**WdsCliTransferImage**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdsclitransferimage?branch=master)                                       | Transfers an image from a WDS server.                                                                                                  |
| [**WdsCliWaitForTransfer**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliwaitfortransfer?branch=master)                                   | Waits for a transfer to complete.                                                                                                      |



 



| Function                                                             | Description                                                                                                                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdsCliGetDriverQueryXml**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscligetdriverqueryxml?branch=master)           | Generates an XML string which can be used to query a WDS server for driver packages. Available beginning with Windows 8 and Windows Server 2012.               |
| [**WdsCliObtainDriverPackagesEx**](/windows/win32/WdsClientAPI/nf-wdsclientapi-wdscliobtaindriverpackagesex?branch=master) | Obtains the driver packages (INF files) that are applicable to the specified WDS driver query XML. Available beginning with Windows 8 and Windows Server 2012. |



 

 

 




