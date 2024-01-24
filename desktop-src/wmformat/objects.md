---
title: Objects (Windows Media Format 11 SDK)
description: Objects
ms.assetid: f884e115-d41a-4f36-bcef-dfaef78510af
keywords:
- Windows Media Format SDK,objects
- Advanced Systems Format (ASF),objects
- ASF (Advanced Systems Format),objects
- objects,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Objects (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK uses several objects to read, write, edit, and index ASF files, and to create and edit profiles. Each object supports a number of interfaces. Some interfaces are supported in multiple objects. In these cases, any differences in implementation are discussed in the reference section for the interface.

The objects in the Windows Media Format SDK are COM compliant. To make development easier, every object has an associated creation function or method. You should create objects by using the creation function or method rather than manually using the COM function **CoCreateInstance**.

Some interfaces have a number appended to their names, such as **IWMProfile2** and **IWMWriter3**. In each case, the numbered versions inherit all the methods of the earlier versions and add new functionality.

On each object page of this reference, the interfaces included in the main COM object are listed first, followed by callback interfaces that must be implemented by the application.

The following table lists the objects supported by this SDK with a description of the functionality of each and the function used to create it.



| Object                                                          | Description                                                                                                                                              | Creation function                                                        |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Backup Restorer](backup-restorer-object.md)                   | Backs up licenses, typically onto removable media, and then restores those licenses onto a different computer.                                           | [**WMCreateBackupRestorer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer)                 |
| [Device Registration](device-registration-object.md)           | Manages the device registration database, which contains entries for media playback devices that are available through a network connection.             | [**WMCreateDeviceRegistration**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration)         |
| [DRM Transcryptor](drm-transcryptor-object.md)                 | Converts media data that is DRM-protected into a data stream that can be sent to devices that use the Windows Media DRM 10 for Network Devices protocol. | [**WMCreateDRMTranscryptor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor)               |
| [Indexer](indexer-object.md)                                   | Creates an index for ASF files to enable seeking in files with video streams.                                                                            | [**WMCreateIndexer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateindexer)                               |
| [License Revocation Agent](license-revocation-agent-object.md) | Manages license revocation.                                                                                                                              | [**WMCreateLicenseRevocationAgent**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent) |
| [Metadata Editor](metadata-editor-object.md)                   | Edits metadata in an ASF file header.                                                                                                                    | [**WMCreateEditor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateeditor)                                 |
| [Profile Manager](profile-manager-object.md)                   | Provides interfaces to create, load, and save profiles. A profile is required to write an ASF file.                                                      | [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager)                 |
| [Reader](reader-object.md)                                     | Reads ASF files. This object uses an asynchronous calling model for its operations.                                                                      | [**WMCreateReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatereader)                                 |
| [Synchronous Reader](synchronous-reader-object.md)             | Reads ASF files using synchronous calls.                                                                                                                 | [**WMCreateSyncReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader)                         |
| [Writer](writer-object.md)                                     | Writes ASF files.                                                                                                                                        | [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter)                                 |
| [Writer File Sink](writer-file-sink-object.md)                 | Controls ASF files written by the writer object.                                                                                                         | [**WMCreateWriterFileSink**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink)                 |
| [Writer Network Sink](writer-network-sink-object.md)           | Controls live network streaming of ASF files written by the writer object.                                                                               | [**WMCreateWriterNetworkSink**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-wmcreatewriternetworksink)           |
| [Writer Push Sink](writer-push-sink-object.md)                 | Controls delivery of streaming content to publishing servers.                                                                                            | [**WMCreateWriterPushSink**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink)                 |



 

The following table lists objects that are dependent upon other objects. These objects are created by methods of existing objects.



| Object                                                        | Description                                                                                                                                                                                                                                                                                                                           | Creation method                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bandwidth Sharing](bandwidth-sharing-object.md)             | Manages bandwidth sharing information in a profile. More than one bandwidth sharing object may exist for a profile. There are different methods for creating a bandwidth sharing object depending upon whether you want to create a new bandwidth sharing object or access an existing one.                                           | [**IWMProfile3::CreateNewBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewbandwidthsharing)OR<br/> [**IWMProfile3::GetBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-getbandwidthsharing)<br/>                                                                                                                                                                                                                                      |
| [Buffer](buffer-object.md)                                   | Contains a media sample and any associated data unit extensions. Used for both writing and reading samples.                                                                                                                                                                                                                           | [**IWMWriter::AllocateSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample)OR<br/> [**IWMReaderAllocatorEx::AllocateForOutputEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforoutputex)<br/> OR<br/> [**IWMReaderAllocatorEx::AllocateForStreamEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderallocatorex-allocateforstreamex)<br/> OR<br/> Created automatically by the reader object or synchronous reader object for sample delivery.<br/> |
| [Input Media Properties](input-media-properties-object.md)   | Manages the properties of an input. One input properties object can exist for each input.                                                                                                                                                                                                                                             | [**IWMWriter::GetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops)                                                                                                                                                                                                                                                                                                                                                                      |
| [Mutual Exclusion](mutual-exclusion-object.md)               | Manages mutual exclusion information in a profile. Common uses for mutual exclusion are multiple bit rate content and soundtracks in several languages. There are different methods for creating a mutual exclusion object depending upon whether you want to create a new mutual exclusion object or access an existing one.         | [**IWMProfile::CreateNewMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion)OR<br/> [**IWMProfile::GetMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusion)<br/>                                                                                                                                                                                                                                              |
| [Output Media Properties](output-media-properties-object.md) | Manages the properties of an output. One output media properties object can exist for each output. These objects can be created by the reader or by the synchronous reader                                                                                                                                                            | [**IWMReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops)OR<br/> [**IWMSyncReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputprops)<br/>                                                                                                                                                                                                                                                                      |
| [Profile](profile-object.md)                                 | Contains the data in a profile while it is being manipulated. Profile objects are created any time the profile needs to be manipulated. There are different methods for creating a profile object depending upon whether you want to create a new profile or access an existing one.                                                  | [**IWMProfileManager::CreateEmptyProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile)OR<br/> [**IWMProfileManager::LoadProfileByData**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadprofilebydata)<br/> OR<br/> [**IWMProfileManager::LoadProfileByID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadprofilebyid)<br/> OR<br/> [**IWMProfileManager::LoadSystemProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadsystemprofile)<br/>          |
| [Stream Configuration](stream-configuration-object.md)       | Manages the properties of a stream within a profile. Stream configuration objects are created by stream objects any time you need to access the information about a stream. There are different methods for creating a stream configuration object depending upon whether you want to create a new stream or access and existing one. | [**IWMProfile::CreateNewStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream)OR<br/> [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream)<br/> OR<br/> [**IWMProfile::GetStreamByNumber**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber)<br/>                                                                                                                                                                                   |
| [Stream Prioritization](stream-prioritization-object.md)     | Maintains the stream priority list for a profile. The streams will be dropped in order of increasing priority if available bandwidth is restricted. There can only be one stream prioritization object in a profile.                                                                                                                  | [**IWMProfile3::CreateNewStreamPrioritization**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewstreamprioritization)                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 





