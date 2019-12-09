---
title: Windows Media Format SDK Functions
description: Functions
ms.assetid: '10fa8f96-8030-4727-af5d-7c06229d05d8'
keywords:
- Windows Media Format SDK,functions
- Advanced Systems Format (ASF),functions
- ASF (Advanced Systems Format),functions
ms.topic: article
ms.date: 05/31/2018
---

# Functions

The Windows Media Format SDK includes functions for creating objects, and helper functions to simplify some procedures.

This SDK supports the following functions for initial creation of objects. If an object is not listed below, you must create it using an interface from another object. For more information, see [Objects](objects.md).



| Function                                                                             | Description                                                                                                                                             |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlextension)                                   | Examines the file name extension in the URL or file name that is passed in as an argument                                                               |
| [**WMCheckURLScheme**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlscheme)                                         | Examines a network protocol and compares it to an internal list of supported schemes                                                                    |
| [**WMCreateBackupRestorer**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer)                             | Creates a backup restorer object.                                                                                                                       |
| [**WMCreateCertificate**](https://msdn.microsoft.com/en-us/library/Dd757745(v=VS.85).aspx)                                   | Wraps the user's certificates into an object.                                                                                                           |
| [**WMCreateDeviceRegistration**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration)                     | Creates a device registration object.                                                                                                                   |
| [**WMCreateDRMTranscryptor**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor)                           | Creates a DRM transcryptor object.                                                                                                                      |
| [**WMCreateEditor**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateeditor)                                             | Creates a metadata editor object.                                                                                                                       |
| [**WMCreateIndexer**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateindexer)                                           | Creates an indexer object.                                                                                                                              |
| [**WMCreateLicenseRevocationAgent**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent)             | Creates a license revocation agent object.                                                                                                              |
| [**WMCreateProfileManager**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager)                             | Creates a profile manager object.                                                                                                                       |
| [**WMCreateReader**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatereader)                                             | Creates a reader object.                                                                                                                                |
| [**WMCreateSecureChannel**](/windows/desktop/api/Wmsecure/nf-wmsecure-wmcreatesecurechannel)                               | Creates an object that implements [**IWMSecureChannel**](https://msdn.microsoft.com/en-us/library/Dd743705(v=VS.85).aspx).                                                                         |
| [**WMCreateSecureChannel\_Certified**](/windows/desktop/api/Wmsecure/nf-wmsecure-wmcreatesecurechannel_certified)          | Creates an object that implements [**IWMSecureChannel**](https://msdn.microsoft.com/en-us/library/Dd743705(v=VS.85).aspx).                                                                         |
| [**WMCreateSecureChannel\_Certified\_DES**](/windows/desktop/api/Wmsecure/nf-wmsecure-wmcreatesecurechannel_certified_des) | Creates an object that implements [**IWMSecureChannel**](https://msdn.microsoft.com/en-us/library/Dd743705(v=VS.85).aspx)..                                                                        |
| [**WMCreateSecureChannel\_DES**](/windows/desktop/api/Wmsecure/nf-wmsecure-wmcreatesecurechannel_des)                      | Creates an object that implements [**IWMSecureChannel**](https://msdn.microsoft.com/en-us/library/Dd743705(v=VS.85).aspx).                                                                         |
| [**WMCreateSyncReader**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader)                                     | Creates a synchronous reader object.                                                                                                                    |
| [**WMCreateWriter**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter)                                             | Creates a writer object.                                                                                                                                |
| [**WMCreateWriterFileSink**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink)                             | Creates a writer file sink object.                                                                                                                      |
| [**WMCreateWriterNetworkSink**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriternetworksink)                       | Creates a writer network sink object.                                                                                                                   |
| [**WMCreateWriterPushSink**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink)                             | Creates a writer push sink object.                                                                                                                      |
| [**WMIsAvailableOffline**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmisavailableoffline)                                 | Verifies that an ASF file can be played from a cached copy.                                                                                             |
| [**WMIsContentProtected**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmiscontentprotected)                                 | Checks a file for DRM-protected content.                                                                                                                |
| [**WMValidateData**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmvalidatedata)                                             | Verifies that data from the beginning of a file is consistent with the header section of a file type that is supported by the Windows Media Format SDK. |



 

The following functions provide convenient shortcuts for analyzing files.



| Function                                             | Description                                                                                                                                  |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlextension)   | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK, based on the file name extension.              |
| [**WMCheckURLScheme**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlscheme)         | Determines whether a network protocol is supported by the objects of the Windows Media Format SDK.                                           |
| [**WMIsAvailableOffline**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmisavailableoffline) | Determines whether a file is available for playback offline.                                                                                 |
| [**WMIsContentProtected**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmiscontentprotected) | Checks a file for DRM-protected content.                                                                                                     |
| [**WMValidateData**](/windows/desktop/api/wmsdkvalidate/nf-wmsdkvalidate-wmvalidatedata)             | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK by analyzing data at the beginning of the file. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




