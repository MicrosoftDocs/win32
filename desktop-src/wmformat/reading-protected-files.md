---
title: Reading Protected Files
description: Reading Protected Files
ms.assetid: 24f839f1-ce57-4d06-b1a5-a6bea7b5b7bb
keywords:
- Windows Media Format SDK,reading protected files
- Windows Media Format SDK,protected files
- Advanced Systems Format (ASF),reading protected files
- ASF (Advanced Systems Format),reading protected files
- Advanced Systems Format (ASF),protected files
- ASF (Advanced Systems Format),protected files
- Advanced Systems Format (ASF),WMStubDRM.lib
- ASF (Advanced Systems Format),WMStubDRM.lib
- WMStubDRM.lib,reading protected files
- WMStubDRM.lib,protected files
- digital rights management (DRM),WMStubDRM.lib
- DRM (digital rights management),WMStubDRM.lib
ms.topic: article
ms.date: 05/31/2018
---

# Reading Protected Files

Reading a DRM-protected file or network stream basically involves attempting to open the file (or connect to the stream) and then handling any events that might be sent from the DRM components.

If a player is not DRM-enabled (does not link to a valid wmstubdrm.lib library) the [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) call fails when it tries to open a protected file and returns NS\_E\_PROTECTED\_CONTENT or some related error.

When a DRM-enabled application attempts to open a DRM-protected file, the DRM component automatically searches the local system for a valid license. If one is found, the DRM component automatically decrypts the file in a way that is completely transparent to the application. The action that an application may perform on the decrypted file depends on the rights specified in the license. For a full description of possible rights, see the Windows Media Rights Manager SDK documentation.

If the application does not have a valid license for a file, the player receives a status notification from the DRM component. The player application can then initiate the [*license acquisition*](wmformat-glossary.md) process. After a valid license has been received, the file can be accessed. The following sections describe the basic tasks that an application must perform in implementing the license acquisition process:

-   [Specifying the Actions To Be Performed](specifying-the-actions-to-be-performed.md)
-   [Handling License Acquisition Events](handling-license-acquisition-events.md)
-   [Individualizing DRM Applications](individualizing-drm-applications.md)
-   [Handling Individualization Events](handling-individualization-events.md)

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> <dt>

[**DRM Properties**](drm-properties.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




