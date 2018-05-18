---
title: Objects
description: Objects
ms.assetid: 'f884e115-d41a-4f36-bcef-dfaef78510af'
keywords: ["Windows Media Format SDK,objects", "Advanced Systems Format (ASF),objects", "ASF (Advanced Systems Format),objects", "objects,about"]
---

# Objects

The Windows Media Format SDK uses several objects to read, write, edit, and index ASF files, and to create and edit profiles. Each object supports a number of interfaces. Some interfaces are supported in multiple objects. In these cases, any differences in implementation are discussed in the reference section for the interface.

The objects in the Windows Media Format SDK are COM compliant. To make development easier, every object has an associated creation function or method. You should create objects by using the creation function or method rather than manually using the COM function **CoCreateInstance**.

Some interfaces have a number appended to their names, such as **IWMProfile2** and **IWMWriter3**. In each case, the numbered versions inherit all the methods of the earlier versions and add new functionality.

On each object page of this reference, the interfaces included in the main COM object are listed first, followed by callback interfaces that must be implemented by the application.

The following table lists the objects supported by this SDK with a description of the functionality of each and the function used to create it.



| Object                                                          | Description                                                                                                                                              | Creation function                                                        |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Backup Restorer](backup-restorer-object.md)                   | Backs up licenses, typically onto removable media, and then restores those licenses onto a different computer.                                           | [**WMCreateBackupRestorer**](wmcreatebackuprestorer.md)                 |
| [Device Registration](device-registration-object.md)           | Manages the device registration database, which contains entries for media playback devices that are available through a network connection.             | [**WMCreateDeviceRegistration**](wmcreatedeviceregistration.md)         |
| [DRM Transcryptor](drm-transcryptor-object.md)                 | Converts media data that is DRM-protected into a data stream that can be sent to devices that use the Windows Media DRM 10 for Network Devices protocol. | [**WMCreateDRMTranscryptor**](wmcreatedrmtranscryptor.md)               |
| [Indexer](indexer-object.md)                                   | Creates an index for ASF files to enable seeking in files with video streams.                                                                            | [**WMCreateIndexer**](wmcreateindexer.md)                               |
| [License Revocation Agent](license-revocation-agent-object.md) | Manages license revocation.                                                                                                                              | [**WMCreateLicenseRevocationAgent**](wmcreatelicenserevocationagent.md) |
| [Metadata Editor](metadata-editor-object.md)                   | Edits metadata in an ASF file header.                                                                                                                    | [**WMCreateEditor**](wmcreateeditor.md)                                 |
| [Profile Manager](profile-manager-object.md)                   | Provides interfaces to create, load, and save profiles. A profile is required to write an ASF file.                                                      | [**WMCreateProfileManager**](wmcreateprofilemanager.md)                 |
| [Reader](reader-object.md)                                     | Reads ASF files. This object uses an asynchronous calling model for its operations.                                                                      | [**WMCreateReader**](wmcreatereader.md)                                 |
| [Synchronous Reader](synchronous-reader-object.md)             | Reads ASF files using synchronous calls.                                                                                                                 | [**WMCreateSyncReader**](wmcreatesyncreader.md)                         |
| [Writer](writer-object.md)                                     | Writes ASF files.                                                                                                                                        | [**WMCreateWriter**](wmcreatewriter.md)                                 |
| [Writer File Sink](writer-file-sink-object.md)                 | Controls ASF files written by the writer object.                                                                                                         | [**WMCreateWriterFileSink**](wmcreatewriterfilesink.md)                 |
| [Writer Network Sink](writer-network-sink-object.md)           | Controls live network streaming of ASF files written by the writer object.                                                                               | [**WMCreateWriterNetworkSink**](wmcreatewriternetworksink.md)           |
| [Writer Push Sink](writer-push-sink-object.md)                 | Controls delivery of streaming content to publishing servers.                                                                                            | [**WMCreateWriterPushSink**](wmcreatewriterpushsink.md)                 |



 

The following table lists objects that are dependent upon other objects. These objects are created by methods of existing objects.



| Object                                                        | Description                                                                                                                                                                                                                                                                                                                           | Creation method                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bandwidth Sharing](bandwidth-sharing-object.md)             | Manages bandwidth sharing information in a profile. More than one bandwidth sharing object may exist for a profile. There are different methods for creating a bandwidth sharing object depending upon whether you want to create a new bandwidth sharing object or access an existing one.                                           | [**IWMProfile3::CreateNewBandwidthSharing**](iwmprofile3-createnewbandwidthsharing.md)OR<br/> [**IWMProfile3::GetBandwidthSharing**](iwmprofile3-getbandwidthsharing.md)<br/>                                                                                                                                                                                                                                      |
| [Buffer](buffer-object.md)                                   | Contains a media sample and any associated data unit extensions. Used for both writing and reading samples.                                                                                                                                                                                                                           | [**IWMWriter::AllocateSample**](iwmwriter-allocatesample.md)OR<br/> [**IWMReaderAllocatorEx::AllocateForOutputEx**](iwmreaderallocatorex-allocateforoutputex.md)<br/> OR<br/> [**IWMReaderAllocatorEx::AllocateForStreamEx**](iwmreaderallocatorex-allocateforstreamex.md)<br/> OR<br/> Created automatically by the reader object or synchronous reader object for sample delivery.<br/> |
| [Input Media Properties](input-media-properties-object.md)   | Manages the properties of an input. One input properties object can exist for each input.                                                                                                                                                                                                                                             | [**IWMWriter::GetInputProps**](iwmwriter-getinputprops.md)                                                                                                                                                                                                                                                                                                                                                                      |
| [Mutual Exclusion](mutual-exclusion-object.md)               | Manages mutual exclusion information in a profile. Common uses for mutual exclusion are multiple bit rate content and soundtracks in several languages. There are different methods for creating a mutual exclusion object depending upon whether you want to create a new mutual exclusion object or access an existing one.         | [**IWMProfile::CreateNewMutualExclusion**](iwmprofile-createnewmutualexclusion.md)OR<br/> [**IWMProfile::GetMutualExclusion**](iwmprofile-getmutualexclusion.md)<br/>                                                                                                                                                                                                                                              |
| [Output Media Properties](output-media-properties-object.md) | Manages the properties of an output. One output media properties object can exist for each output. These objects can be created by the reader or by the synchronous reader                                                                                                                                                            | [**IWMReader::GetOutputProps**](iwmreader-getoutputprops.md)OR<br/> [**IWMSyncReader::GetOutputProps**](iwmsyncreader-getoutputprops.md)<br/>                                                                                                                                                                                                                                                                      |
| [Profile](profile-object.md)                                 | Contains the data in a profile while it is being manipulated. Profile objects are created any time the profile needs to be manipulated. There are different methods for creating a profile object depending upon whether you want to create a new profile or access an existing one.                                                  | [**IWMProfileManager::CreateEmptyProfile**](iwmprofilemanager-createemptyprofile.md)OR<br/> [**IWMProfileManager::LoadProfileByData**](iwmprofilemanager-loadprofilebydata.md)<br/> OR<br/> [**IWMProfileManager::LoadProfileByID**](iwmprofilemanager-loadprofilebyid.md)<br/> OR<br/> [**IWMProfileManager::LoadSystemProfile**](iwmprofilemanager-loadsystemprofile.md)<br/>          |
| [Stream Configuration](stream-configuration-object.md)       | Manages the properties of a stream within a profile. Stream configuration objects are created by stream objects any time you need to access the information about a stream. There are different methods for creating a stream configuration object depending upon whether you want to create a new stream or access and existing one. | [**IWMProfile::CreateNewStream**](iwmprofile-createnewstream.md)OR<br/> [**IWMProfile::GetStream**](iwmprofile-getstream.md)<br/> OR<br/> [**IWMProfile::GetStreamByNumber**](iwmprofile-getstreambynumber.md)<br/>                                                                                                                                                                                   |
| [Stream Prioritization](stream-prioritization-object.md)     | Maintains the stream priority list for a profile. The streams will be dropped in order of increasing priority if available bandwidth is restricted. There can only be one stream prioritization object in a profile.                                                                                                                  | [**IWMProfile3::CreateNewStreamPrioritization**](iwmprofile3-createnewstreamprioritization.md)                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 





