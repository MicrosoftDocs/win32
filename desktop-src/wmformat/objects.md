---
title: Objects
description: Objects
ms.assetid: f884e115-d41a-4f36-bcef-dfaef78510af
keywords:
- Windows Media Format SDK,objects
- Advanced Systems Format (ASF),objects
- ASF (Advanced Systems Format),objects
- objects,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Objects

The Windows Media Format SDK uses several objects to read, write, edit, and index ASF files, and to create and edit profiles. Each object supports a number of interfaces. Some interfaces are supported in multiple objects. In these cases, any differences in implementation are discussed in the reference section for the interface.

The objects in the Windows Media Format SDK are COM compliant. To make development easier, every object has an associated creation function or method. You should create objects by using the creation function or method rather than manually using the COM function **CoCreateInstance**.

Some interfaces have a number appended to their names, such as **IWMProfile2** and **IWMWriter3**. In each case, the numbered versions inherit all the methods of the earlier versions and add new functionality.

On each object page of this reference, the interfaces included in the main COM object are listed first, followed by callback interfaces that must be implemented by the application.

The following table lists the objects supported by this SDK with a description of the functionality of each and the function used to create it.



| Object                                                          | Description                                                                                                                                              | Creation function                                                        |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Backup Restorer](backup-restorer-object.md)                   | Backs up licenses, typically onto removable media, and then restores those licenses onto a different computer.                                           | [**WMCreateBackupRestorer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer?branch=master)                 |
| [Device Registration](device-registration-object.md)           | Manages the device registration database, which contains entries for media playback devices that are available through a network connection.             | [**WMCreateDeviceRegistration**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration?branch=master)         |
| [DRM Transcryptor](drm-transcryptor-object.md)                 | Converts media data that is DRM-protected into a data stream that can be sent to devices that use the Windows Media DRM 10 for Network Devices protocol. | [**WMCreateDRMTranscryptor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor?branch=master)               |
| [Indexer](indexer-object.md)                                   | Creates an index for ASF files to enable seeking in files with video streams.                                                                            | [**WMCreateIndexer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateindexer?branch=master)                               |
| [License Revocation Agent](license-revocation-agent-object.md) | Manages license revocation.                                                                                                                              | [**WMCreateLicenseRevocationAgent**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent?branch=master) |
| [Metadata Editor](metadata-editor-object.md)                   | Edits metadata in an ASF file header.                                                                                                                    | [**WMCreateEditor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateeditor?branch=master)                                 |
| [Profile Manager](profile-manager-object.md)                   | Provides interfaces to create, load, and save profiles. A profile is required to write an ASF file.                                                      | [**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master)                 |
| [Reader](reader-object.md)                                     | Reads ASF files. This object uses an asynchronous calling model for its operations.                                                                      | [**WMCreateReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatereader?branch=master)                                 |
| [Synchronous Reader](synchronous-reader-object.md)             | Reads ASF files using synchronous calls.                                                                                                                 | [**WMCreateSyncReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader?branch=master)                         |
| [Writer](writer-object.md)                                     | Writes ASF files.                                                                                                                                        | [**WMCreateWriter**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriter?branch=master)                                 |
| [Writer File Sink](writer-file-sink-object.md)                 | Controls ASF files written by the writer object.                                                                                                         | [**WMCreateWriterFileSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink?branch=master)                 |
| [Writer Network Sink](writer-network-sink-object.md)           | Controls live network streaming of ASF files written by the writer object.                                                                               | [**WMCreateWriterNetworkSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriternetworksink?branch=master)           |
| [Writer Push Sink](writer-push-sink-object.md)                 | Controls delivery of streaming content to publishing servers.                                                                                            | [**WMCreateWriterPushSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink?branch=master)                 |



 

The following table lists objects that are dependent upon other objects. These objects are created by methods of existing objects.



| Object                                                        | Description                                                                                                                                                                                                                                                                                                                           | Creation method                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bandwidth Sharing](bandwidth-sharing-object.md)             | Manages bandwidth sharing information in a profile. More than one bandwidth sharing object may exist for a profile. There are different methods for creating a bandwidth sharing object depending upon whether you want to create a new bandwidth sharing object or access an existing one.                                           | [**IWMProfile3::CreateNewBandwidthSharing**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewbandwidthsharing?branch=master)OR<br/> [**IWMProfile3::GetBandwidthSharing**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile3-getbandwidthsharing?branch=master)<br/>                                                                                                                                                                                                                                      |
| [Buffer](buffer-object.md)                                   | Contains a media sample and any associated data unit extensions. Used for both writing and reading samples.                                                                                                                                                                                                                           | [**IWMWriter::AllocateSample**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample?branch=master)OR<br/> [**IWMReaderAllocatorEx::AllocateForOutputEx**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforoutputex?branch=master)<br/> OR<br/> [**IWMReaderAllocatorEx::AllocateForStreamEx**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforstreamex?branch=master)<br/> OR<br/> Created automatically by the reader object or synchronous reader object for sample delivery.<br/> |
| [Input Media Properties](input-media-properties-object.md)   | Manages the properties of an input. One input properties object can exist for each input.                                                                                                                                                                                                                                             | [**IWMWriter::GetInputProps**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops?branch=master)                                                                                                                                                                                                                                                                                                                                                                      |
| [Mutual Exclusion](mutual-exclusion-object.md)               | Manages mutual exclusion information in a profile. Common uses for mutual exclusion are multiple bit rate content and soundtracks in several languages. There are different methods for creating a mutual exclusion object depending upon whether you want to create a new mutual exclusion object or access an existing one.         | [**IWMProfile::CreateNewMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion?branch=master)OR<br/> [**IWMProfile::GetMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusion?branch=master)<br/>                                                                                                                                                                                                                                              |
| [Output Media Properties](output-media-properties-object.md) | Manages the properties of an output. One output media properties object can exist for each output. These objects can be created by the reader or by the synchronous reader                                                                                                                                                            | [**IWMReader::GetOutputProps**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops?branch=master)OR<br/> [**IWMSyncReader::GetOutputProps**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputprops?branch=master)<br/>                                                                                                                                                                                                                                                                      |
| [Profile](profile-object.md)                                 | Contains the data in a profile while it is being manipulated. Profile objects are created any time the profile needs to be manipulated. There are different methods for creating a profile object depending upon whether you want to create a new profile or access an existing one.                                                  | [**IWMProfileManager::CreateEmptyProfile**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile?branch=master)OR<br/> [**IWMProfileManager::LoadProfileByData**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadprofilebydata?branch=master)<br/> OR<br/> [**IWMProfileManager::LoadProfileByID**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadprofilebyid?branch=master)<br/> OR<br/> [**IWMProfileManager::LoadSystemProfile**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadsystemprofile?branch=master)<br/>          |
| [Stream Configuration](stream-configuration-object.md)       | Manages the properties of a stream within a profile. Stream configuration objects are created by stream objects any time you need to access the information about a stream. There are different methods for creating a stream configuration object depending upon whether you want to create a new stream or access and existing one. | [**IWMProfile::CreateNewStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream?branch=master)OR<br/> [**IWMProfile::GetStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream?branch=master)<br/> OR<br/> [**IWMProfile::GetStreamByNumber**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber?branch=master)<br/>                                                                                                                                                                                   |
| [Stream Prioritization](stream-prioritization-object.md)     | Maintains the stream priority list for a profile. The streams will be dropped in order of increasing priority if available bandwidth is restricted. There can only be one stream prioritization object in a profile.                                                                                                                  | [**IWMProfile3::CreateNewStreamPrioritization**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewstreamprioritization?branch=master)                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 





