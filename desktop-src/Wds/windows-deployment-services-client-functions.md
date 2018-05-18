---
title: Windows Deployment Services Client Functions
description: The following functions are used with the Windows Deployment Services Client API.
ms.assetid: '4cedd8a8-7f46-4229-9d96-58965b751e43'
---

# Windows Deployment Services Client Functions

The following functions are used with the Windows Deployment Services Client API.



| Function                                                                                 | Description                                                                                                                            |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [*PFN\_WdsCliCallback*](pfn-wdsclicallback.md)                                          | Progress notification and error messages during a file or image transfer.                                                              |
| [*PFN\_WdsCliTraceFunction*](pfn-wdsclitracefunction.md)                                | Receives debugging messages from the WDS client.                                                                                       |
| [**WdsCliAuthorizeSession**](wdscliauthorizesession.md)                                 | Converts an anonymous session into an authenticated session.                                                                           |
| [**WdsCliCancelTransfer**](wdsclicanceltransfer.md)                                     | Cancels a WDS transfer operation.                                                                                                      |
| [**WdsCliClose**](wdscliclose.md)                                                       | Closes a handle to a WDS session or image and releases resources.                                                                      |
| [**WdsCliCreateSession**](wdsclicreatesession.md)                                       | Starts a new session with a WDS server.                                                                                                |
| [**WdsCliFindFirstImage**](wdsclifindfirstimage.md)                                     | Starts the enumeration of images stored on a WDS server and returns a find handle that references the first image.                     |
| [**WdsCliFindNextImage**](wdsclifindnextimage.md)                                       | Advances the reference of a find handle to the next image stored on a WDS server.                                                      |
| [**WdsCliFreeStringArray**](wdsclifreestringarray.md)                                   | Frees the array of string values that gets allocated by the [**WdsCliObtainDriverPackages**](wdscliobtaindriverpackages.md) function. |
| [**WdsCliGetEnumerationFlags**](wdscligetenumerationflags.md)                           | Returns the image enumeration flag for the current image handle.                                                                       |
| [**WdsCliGetImageArchitecture**](wdscligetimagearchitecture.md)                         | Returns the processor architecture for the current image.                                                                              |
| [**WdsCliGetImageDescription**](wdscligetimagedescription.md)                           | Returns the description of the current image.                                                                                          |
| [**WdsCliGetImageGroup**](wdscligetimagegroup.md)                                       | Returns the image group name for the current image.                                                                                    |
| [**WdsCliGetImageHalName**](wdscligetimagehalname.md)                                   | Returns the Hardware Abstraction Layer (HAL) name for the current image.                                                               |
| [**WdsCliGetImageHandleFromFindHandle**](wdscligetimagehandlefromfindhandle.md)         | Returns an image handle for the current image.                                                                                         |
| [**WdsCliGetImageHandleFromTransferHandle**](wdscligetimagehandlefromtransferhandle.md) | Returns an image handle from a completed transfer handle.                                                                              |
| [**WdsCliGetImageIndex**](wdscligetimageindex.md)                                       | Returns the image index for the current image.                                                                                         |
| [**WdsCliGetImageLanguage**](wdscligetimagelanguage.md)                                 | Returns the default language of the current image.                                                                                     |
| [**WdsCliGetImageLanguages**](wdscligetimagelanguages.md)                               | Returns an array of languages supported by the current image.                                                                          |
| [**WdsCliGetImageLastModifiedTime**](wdscligetimagelastmodifiedtime.md)                 | Returns the last-modified time for the current image.                                                                                  |
| [**WdsCliGetImageName**](wdscligetimagename.md)                                         | Returns the name of the current image.                                                                                                 |
| [**WdsCliGetImageNamespace**](wdscligetimagenamespace.md)                               | Returns the name of the current image.                                                                                                 |
| [**WdsCliGetImagePath**](wdscligetimagepath.md)                                         | Returns the path to the image file that contains the current image.                                                                    |
| [**WdsCliGetImageSize**](wdscligetimagesize.md)                                         | Returns the size of the current image.                                                                                                 |
| [**WdsCliGetImageVersion**](wdscligetimageversion.md)                                   | Returns the version of the current image.                                                                                              |
| [**WdsCliGetTransferSize**](wdscligettransfersize.md)                                   | Returns the size of the current transfer.                                                                                              |
| [**WdsCliInitializeLog**](wdscliinitializelog.md)                                       | Initializes the log for the client.                                                                                                    |
| [**WdsCliLog**](wdsclilog.md)                                                           | Sends a log event to the WDS server.                                                                                                   |
| [**WdsCliObtainDriverPackages**](wdscliobtaindriverpackages.md)                         | Obtains from a WDS image, the driver packages (INF files) that can be used on this computer.                                           |
| [**WdsCliRegisterTrace**](wdscliregistertrace.md)                                       | Registers a callback function that will receive debugging messages.                                                                    |
| [**WdsCliTransferFile**](wdsclitransferfile.md)                                         | Transfers a file from a WDS server to the WDS client using a multicast transfer protocol.                                              |
| [**WdsCliTransferImage**](wdsclitransferimage.md)                                       | Transfers an image from a WDS server.                                                                                                  |
| [**WdsCliWaitForTransfer**](wdscliwaitfortransfer.md)                                   | Waits for a transfer to complete.                                                                                                      |



 



| Function                                                             | Description                                                                                                                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdsCliGetDriverQueryXml**](wdscligetdriverqueryxml.md)           | Generates an XML string which can be used to query a WDS server for driver packages. Available beginning with Windows 8 and Windows Server 2012.               |
| [**WdsCliObtainDriverPackagesEx**](wdscliobtaindriverpackagesex.md) | Obtains the driver packages (INF files) that are applicable to the specified WDS driver query XML. Available beginning with Windows 8 and Windows Server 2012. |



 

 

 




