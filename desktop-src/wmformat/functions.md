---
title: Functions
description: Functions
ms.assetid: '5d726c56-d0f3-4eb8-829f-3a0c1a0e0802'
keywords: ["Windows Media Format SDK,functions", "Advanced Systems Format (ASF),functions", "ASF (Advanced Systems Format),functions"]
---

# Functions

The Windows Media Format SDK includes functions for creating objects, and helper functions to simplify some procedures.

This SDK supports the following functions for initial creation of objects. If an object is not listed below, you must create it using an interface from another object. For more information, see [Objects](objects.md).



| Function                                                                             | Description                                                                                                                                             |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](wmcheckurlextension.md)                                   | Examines the file name extension in the URL or file name that is passed in as an argument                                                               |
| [**WMCheckURLScheme**](wmcheckurlscheme.md)                                         | Examines a network protocol and compares it to an internal list of supported schemes                                                                    |
| [**WMCreateBackupRestorer**](wmcreatebackuprestorer.md)                             | Creates a backup restorer object.                                                                                                                       |
| [**WMCreateCertificate**](wmcreatecertificate.md)                                   | Wraps the user's certificates into an object.                                                                                                           |
| [**WMCreateDeviceRegistration**](wmcreatedeviceregistration.md)                     | Creates a device registration object.                                                                                                                   |
| [**WMCreateDRMTranscryptor**](wmcreatedrmtranscryptor.md)                           | Creates a DRM transcryptor object.                                                                                                                      |
| [**WMCreateEditor**](wmcreateeditor.md)                                             | Creates a metadata editor object.                                                                                                                       |
| [**WMCreateIndexer**](wmcreateindexer.md)                                           | Creates an indexer object.                                                                                                                              |
| [**WMCreateLicenseRevocationAgent**](wmcreatelicenserevocationagent.md)             | Creates a license revocation agent object.                                                                                                              |
| [**WMCreateProfileManager**](wmcreateprofilemanager.md)                             | Creates a profile manager object.                                                                                                                       |
| [**WMCreateReader**](wmcreatereader.md)                                             | Creates a reader object.                                                                                                                                |
| [**WMCreateSecureChannel**](wmcreatesecurechannel.md)                               | Creates an object that implements [**IWMSecureChannel**](iwmsecurechannel.md).                                                                         |
| [**WMCreateSecureChannel\_Certified**](wmcreatesecurechannel-certified.md)          | Creates an object that implements [**IWMSecureChannel**](iwmsecurechannel.md).                                                                         |
| [**WMCreateSecureChannel\_Certified\_DES**](wmcreatesecurechannel-certified-des.md) | Creates an object that implements [**IWMSecureChannel**](iwmsecurechannel.md)..                                                                        |
| [**WMCreateSecureChannel\_DES**](wmcreatesecurechannel-des.md)                      | Creates an object that implements [**IWMSecureChannel**](iwmsecurechannel.md).                                                                         |
| [**WMCreateSyncReader**](wmcreatesyncreader.md)                                     | Creates a synchronous reader object.                                                                                                                    |
| [**WMCreateWriter**](wmcreatewriter.md)                                             | Creates a writer object.                                                                                                                                |
| [**WMCreateWriterFileSink**](wmcreatewriterfilesink.md)                             | Creates a writer file sink object.                                                                                                                      |
| [**WMCreateWriterNetworkSink**](wmcreatewriternetworksink.md)                       | Creates a writer network sink object.                                                                                                                   |
| [**WMCreateWriterPushSink**](wmcreatewriterpushsink.md)                             | Creates a writer push sink object.                                                                                                                      |
| [**WMIsAvailableOffline**](wmisavailableoffline.md)                                 | Verifies that an ASF file can be played from a cached copy.                                                                                             |
| [**WMIsContentProtected**](wmiscontentprotected.md)                                 | Checks a file for DRM-protected content.                                                                                                                |
| [**WMValidateData**](wmvalidatedata.md)                                             | Verifies that data from the beginning of a file is consistent with the header section of a file type that is supported by the Windows Media Format SDK. |



 

The following functions provide convenient shortcuts for analyzing files.



| Function                                             | Description                                                                                                                                  |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](wmcheckurlextension.md)   | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK, based on the file name extension.              |
| [**WMCheckURLScheme**](wmcheckurlscheme.md)         | Determines whether a network protocol is supported by the objects of the Windows Media Format SDK.                                           |
| [**WMIsAvailableOffline**](wmisavailableoffline.md) | Determines whether a file is available for playback offline.                                                                                 |
| [**WMIsContentProtected**](wmiscontentprotected.md) | Checks a file for DRM-protected content.                                                                                                     |
| [**WMValidateData**](wmvalidatedata.md)             | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK by analyzing data at the beginning of the file. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




