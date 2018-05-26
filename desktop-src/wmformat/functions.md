---
title: Functions
description: Functions
ms.assetid: 5d726c56-d0f3-4eb8-829f-3a0c1a0e0802
keywords:
- Windows Media Format SDK,functions
- Advanced Systems Format (ASF),functions
- ASF (Advanced Systems Format),functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

The Windows Media Format SDK includes functions for creating objects, and helper functions to simplify some procedures.

This SDK supports the following functions for initial creation of objects. If an object is not listed below, you must create it using an interface from another object. For more information, see [Objects](objects.md).



| Function                                                                             | Description                                                                                                                                             |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlextension?branch=master)                                   | Examines the file name extension in the URL or file name that is passed in as an argument                                                               |
| [**WMCheckURLScheme**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlscheme?branch=master)                                         | Examines a network protocol and compares it to an internal list of supported schemes                                                                    |
| [**WMCreateBackupRestorer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer?branch=master)                             | Creates a backup restorer object.                                                                                                                       |
| [**WMCreateCertificate**](/windows/win32/Wmsdkidl/?branch=master)                                   | Wraps the user's certificates into an object.                                                                                                           |
| [**WMCreateDeviceRegistration**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration?branch=master)                     | Creates a device registration object.                                                                                                                   |
| [**WMCreateDRMTranscryptor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor?branch=master)                           | Creates a DRM transcryptor object.                                                                                                                      |
| [**WMCreateEditor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateeditor?branch=master)                                             | Creates a metadata editor object.                                                                                                                       |
| [**WMCreateIndexer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateindexer?branch=master)                                           | Creates an indexer object.                                                                                                                              |
| [**WMCreateLicenseRevocationAgent**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent?branch=master)             | Creates a license revocation agent object.                                                                                                              |
| [**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master)                             | Creates a profile manager object.                                                                                                                       |
| [**WMCreateReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatereader?branch=master)                                             | Creates a reader object.                                                                                                                                |
| [**WMCreateSecureChannel**](/windows/win32/Wmsecure/nf-wmsecure-wmcreatesecurechannel?branch=master)                               | Creates an object that implements [**IWMSecureChannel**](/windows/win32/Wmsecure/?branch=master).                                                                         |
| [**WMCreateSecureChannel\_Certified**](/windows/win32/Wmsecure/nf-wmsecure-wmcreatesecurechannel_certified?branch=master)          | Creates an object that implements [**IWMSecureChannel**](/windows/win32/Wmsecure/?branch=master).                                                                         |
| [**WMCreateSecureChannel\_Certified\_DES**](/windows/win32/Wmsecure/nf-wmsecure-wmcreatesecurechannel_certified_des?branch=master) | Creates an object that implements [**IWMSecureChannel**](/windows/win32/Wmsecure/?branch=master)..                                                                        |
| [**WMCreateSecureChannel\_DES**](/windows/win32/Wmsecure/nf-wmsecure-wmcreatesecurechannel_des?branch=master)                      | Creates an object that implements [**IWMSecureChannel**](/windows/win32/Wmsecure/?branch=master).                                                                         |
| [**WMCreateSyncReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader?branch=master)                                     | Creates a synchronous reader object.                                                                                                                    |
| [**WMCreateWriter**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriter?branch=master)                                             | Creates a writer object.                                                                                                                                |
| [**WMCreateWriterFileSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink?branch=master)                             | Creates a writer file sink object.                                                                                                                      |
| [**WMCreateWriterNetworkSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriternetworksink?branch=master)                       | Creates a writer network sink object.                                                                                                                   |
| [**WMCreateWriterPushSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink?branch=master)                             | Creates a writer push sink object.                                                                                                                      |
| [**WMIsAvailableOffline**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmisavailableoffline?branch=master)                                 | Verifies that an ASF file can be played from a cached copy.                                                                                             |
| [**WMIsContentProtected**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmiscontentprotected?branch=master)                                 | Checks a file for DRM-protected content.                                                                                                                |
| [**WMValidateData**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmvalidatedata?branch=master)                                             | Verifies that data from the beginning of a file is consistent with the header section of a file type that is supported by the Windows Media Format SDK. |



 

The following functions provide convenient shortcuts for analyzing files.



| Function                                             | Description                                                                                                                                  |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMCheckURLExtension**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlextension?branch=master)   | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK, based on the file name extension.              |
| [**WMCheckURLScheme**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmcheckurlscheme?branch=master)         | Determines whether a network protocol is supported by the objects of the Windows Media Format SDK.                                           |
| [**WMIsAvailableOffline**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmisavailableoffline?branch=master) | Determines whether a file is available for playback offline.                                                                                 |
| [**WMIsContentProtected**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmiscontentprotected?branch=master) | Checks a file for DRM-protected content.                                                                                                     |
| [**WMValidateData**](/windows/win32/wmsdkvalidate/nf-wmsdkvalidate-wmvalidatedata?branch=master)             | Tries to determine whether a file is readable by the objects of the Windows Media Format SDK by analyzing data at the beginning of the file. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




