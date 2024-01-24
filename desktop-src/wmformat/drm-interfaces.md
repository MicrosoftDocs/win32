---
title: Microsoft Windows Media DRM Client Interfaces
description: Microsoft Windows Media DRM Client Interfaces
ms.assetid: 27bbc33f-8102-4db2-bbc6-1a1da92bac80
keywords:
- Windows Media Format SDK,interfaces
- digital rights management (DRM),interfaces
- DRM (digital rights management),interfaces
- DRM Client Extended APIs,interfaces
- Client Extended APIs,interfaces
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft Windows Media DRM Client Interfaces

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table describes the interfaces supported by the Windows Media DRM Client APIs.



| Interface                                                                    | Description                                                                                                     |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**IDRMStatusCallback**](idrmstatuscallback.md)                             | Provides the definition for a status callback that you can implement to handle asynchronous DRM operations.     |
| [**IWMDRMDecrypt**](iwmdrmdecrypt.md)                                       | Provides a method for decrypting content.                                                                       |
| [**IWMDRMEncrypt**](iwmdrmencrypt.md)                                       | Provides a method for encrypting data in place.                                                                 |
| [**IWMDRMEncryptScatter**](iwmdrmencryptscatter.md)                         | Encrypts data from non-contiguous blocks.                                                                       |
| [**IWMDRMEventGenerator**](iwmdrmeventgenerator.md)                         | Extension of the **IMFMediaEventGenerator** interface that provides a method to cancel asynchronous operations. |
| [**IWMDRMIndividualizationStatus**](iwmdrmindividualizationstatus.md)       | Enables retrieval of advanced status information about the progress of individualization.                       |
| [**IWMDRMLicense**](iwmdrmlicense.md)                                       | Represents one or more licenses in the local license store.                                                     |
| [**IWMDRMLicenseBackupRestoreStatus**](iwmdrmlicensebackuprestorestatus.md) | Enables retrieval of detailed status information about a license backup or restore operation.                   |
| [**IWMDRMLicenseManagement**](iwmdrmlicensemanagement.md)                   | Enables management operations for the local license store.                                                      |
| [**IWMDRMLicenseManagement**](iwmdrmlicensemanagement.md)                   | Provides additional management options for the local license store.                                             |
| [**IWMDRMLicenseQuery**](iwmdrmlicensequery.md)                             | Enables applications to query the rights and license state for a protected file.                                |
| [**IWMDRMNetReceiver**](iwmdrmnetreceiver.md)                               | Provides methods needed create a Microsoft Windows Media DRM for Network Devices receiver application.          |
| [**IWMDRMNetTransmitter**](iwmdrmnettransmitter.md)                         | Provides methods needed create a Microsoft Windows Media DRM for Network Devices transmitter application.       |
| [**IWMDRMNonSilentLicenseAquisition**](iwmdrmnonsilentlicenseaquisition.md) | Provides methods that enable license acquisition with user intervention.                                        |
| [**IWMDRMProvider**](iwmdrmprovider.md)                                     | Creates the other objects of the Microsoft Windows Media DRM Client Extended APIs.                              |
| [**IWMDRMSecurity**](iwmdrmsecurity.md)                                     | Manages various security-related processes for the client computer and DRM subsystem.                           |
| [**IWMDRMSecurity**](iwmdrmsecurity.md)                                     | Manages component revocation and renewal.                                                                       |
| [**IWMSecureBuffer**](iwmsecurebuffer.md)                                   | Enables encryption and decryption of buffers.                                                                   |



 

## Related topics

<dl> <dt>

[**Programming Reference**](drm-programming-reference.md)
</dt> </dl>

 

 




