---
title: Working with Profiles
description: Working with Profiles
ms.assetid: e1e31632-0db7-47db-a992-f5db9d8824c1
keywords:
- Windows Media Format SDK,profiles
- Windows Media Format SDK,IWMCodecInfo3 interface
- profiles,about
- profiles,Windows Media Format SDK
- profiles,IWMCodecInfo3
- IWMCodecInfo3,about
ms.topic: article
ms.date: 05/31/2018
---

# Working with Profiles

This section describes how to design, create, and modify profiles. Each profile describes the streams that will make up a file and their relationships with each other. A profile object contains stream configuration information for each stream, mutual exclusion information for streams that cannot be delivered simultaneously, bandwidth sharing information, and stream prioritization information.

The main purpose of profiles is to provide stream configuration information to the writer object. The writer uses the information in a profile to coordinate with the codecs the process of compressing inputs. When you configure a compressed media stream, you specify the codec used to compress the data and the settings the codec uses. You can also create profiles for uncompressed streams. Several uncompressed stream types are supported. Even though they do not require a codec, these types have their own requirements for stream configuration. For more information, see [Configuring Streams](configuring-streams.md) and [Using Uncompressed Audio and Video Streams](using-uncompressed-audio-and-video-streams.md).

Stream configuration information for a stream using one of the Windows Media codecs must be obtained from the codec by using the methods of the [**IWMCodecInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3) interface. The procedure for using stream formats is different for video codecs than it is for audio codecs, but in both cases you must begin by obtaining the format from the codec. You should never try to manually configure a stream using one of the Windows Media codecs, because small errors in the profile can have a profound effect on the ASF file.

The basic steps in creating and/or modifying profiles are:

1.  Create an empty profile, or load an existing profile to edit.
2.  Configure each of the streams, if required, based on supported profile data retrieved from the codec that will be used to encode the stream.
3.  Configure mutual exclusion, if needed.
4.  Configure bandwidth sharing, if needed.
5.  Set the priority of the streams in the file, if required.

The following sections explain the process of creating and editing profiles.



| Section                                                        | Description                                                                                        |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Designing Profiles](designing-profiles.md)                   | Describes how to design a profile.                                                                 |
| [Creating Profiles](creating-profiles.md)                     | Describes how to create an empty profile.                                                          |
| [Configuring Streams](configuring-streams.md)                 | Describes how to configure streams and include them in a profile.                                  |
| [Using Mutual Exclusion](using-mutual-exclusion.md)           | Describes how to create mutual exclusion objects and include them in a profile.                    |
| [Using Bandwidth Sharing](using-bandwidth-sharing.md)         | Describes how to use bandwidth sharing in a profile.                                               |
| [Using Stream Prioritization](using-stream-prioritization.md) | Describes how to use stream prioritization in a profile.                                           |
| [Saving Profiles](saving-profiles.md)                         | Describes how to save your custom profiles to a file.                                              |
| [Using System Profiles](using-system-profiles.md)             | Describes how to work with system profiles to save time and effort in creating profiles.           |
| [Managing Packet Size](managing-packet-size.md)               | Discusses how to control the size of packets in the data streams of files made using your profile. |



 

**Note** Users of previous versions of the Windows Media Format SDK may be accustomed to using system profiles without modification to create their files. The Windows Media Format 9 Series SDK or later does not include any new system profiles that use the Windows Media 9 Series or later codecs. This is because of the increasing number of profiles that would be needed to cover the various features now offered by the codecs. You can still use the version 8 system profiles as a starting place for your profiles. For more information see [Using System Profiles](using-system-profiles.md). For information about the new mechanism for targeting profiles to specific delivery devices, see [Working with Device Conformance Templates](working-with-device-conformance-templates.md).

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




