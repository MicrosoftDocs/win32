---
title: Features Added in the Windows Media Format 9 Series SDK
description: Features Added in the Windows Media Format 9 Series SDK
ms.assetid: 73c4da27-a456-4845-a35b-edb75aa3f953
keywords:
- Windows Media Format SDK,features
- Windows Media Format SDK,new features
- Windows Media Format SDK,synchronous readers
- Windows Media Format SDK,frame-based indexing
- Windows Media Format SDK,SMPTE time codes
- Windows Media Format SDK,DirectShow filters
- Windows Media Format SDK,DRM writing capability
- Windows Media Format SDK,file sinks
- Windows Media Format SDK,DirectX Video Acceleration (DXVA)
- Windows Media Format SDK,multichannel audio
- Windows Media Format SDK,watermarking
- Windows Media Format SDK,multiple language support
- Windows Media Format SDK,device conformance templates
- Windows Media Format SDK,codec enumerations
- Windows Media Format SDK,mutual exclusion
- Windows Media Format SDK,multiple bit rate (MBR)
- Windows Media Format SDK,transcoding with smart recompression
- Windows Media Format SDK,smart recompression
- Windows Media Format SDK,recompression
- Windows Media Format SDK,metadata
- Windows Media Format SDK,dynamic pixel aspect ratio
- Windows Media Format SDK,interlaced video streams
- Windows Media Format SDK,two-pass encoding
- Windows Media Format SDK,WMStub.lib
- synchronous readers,about
- frame-based indexing
- SMPTE time codes,about
- DirectShow filters
- file sinks,enhancements
- multichannel audio,about
- watermarking,about
- codecs,enumerations
- mutual exclusion,about
- digital rights management (DRM),writing capability
- DRM (digital rights management),writing capability
- DirectX Video Acceleration (DXVA),about
- DXVA (DirectX Video Acceleration),about
- Advanced Systems Format (ASF),multiple language support
- ASF (Advanced Systems Format),multiple language support
- multiple bit rate (MBR),about
- MBR (multiple bit rate),about
- transcoding with smart recompression
- smart recompression
- recompression
- metadata,Windows Media Format SDK
- dynamic pixel aspect ratio
- interlaced video streams
- two-pass encoding,about
- 2-pass encoding,about
- WMStub.lib
ms.topic: article
ms.date: 05/31/2018
---

# Features Added in the Windows Media Format 9 Series SDK

The Windows Media Format 9 Series SDK introduced many improvements and features. This section provides an overview of those features for the benefit of users migrating from an earlier version of the SDK.

## Synchronous Reading

You can read ASF files with synchronous calls. When reading a file synchronously, you can change the settings of the reader while it is reading. The synchronous reading operations of the SDK do not provide support for reading files over the Internet, but you can use the standard COM interface, **IStream**, to read from custom sources.

## Frame-based Indexing

You can index ASF files based on video frames. Both the reader and the synchronous reader can seek to a frame of a video stream and synchronize the other streams to that frame.

## Indexing and Seeking with SMPTE Time Code

The Windows Media Format SDK enables you to store SMPTE time codes in ASF files. Files can be indexed by SMPTE time code, and both the asynchronous reader and synchronous reader can seek to SMPTE time code index entries.

## DirectShow Filters

The Windows Media Format SDK includes two Microsoft DirectShow® filters that enable DirectShow-based applications to read and write ASF files. DirectShow also enables applications to capture data from audio-video devices and decompress data from a variety of formats before re-encoding it as Windows Media-based content.

## Enhanced Profiles

Profiles can contain bandwidth sharing information and stream prioritization information. Bandwidth sharing enables you to specify that two or more streams, regardless of their individual bit rates, will never use more than a specified amount of bandwidth. The bandwidth sharing data in a profile is purely informational; it is not enforced by any logic in the SDK. Stream prioritization enables you to specify an order of priority for the streams in a profile. If there is not enough bandwidth at playback to stream the file properly, the lowest priority streams can be ignored in order to improve performance.

## DRM Writing Capability

In addition to the existing DRM-reading support, the Windows Media Format 9 Series SDK added support for writing ASF files with either DRM version 1 or DRM version 7 protection. This new capability enables "Live DRM" scenarios such as pay-per-view webcasting of live sporting events or concerts.

## Enhanced File Sink

Several new file sink capabilities were added to the 9 Series version of the SDK. You can configure the file sink to disable automatic indexing of newly created ASF files. You also have the option to configure it for unbuffered input and output.

## DirectX Video Acceleration

DirectX Video Acceleration (DXVA) is a technology that enables playback of high-bit-rate video (DVD quality or better) on less powerful machines with DXVA-enabled graphics cards. You can use the reader object of this SDK to enable DirectX Video Acceleration, if the hardware supports it, when playing ASF files.

## Multichannel Audio

You can encode and play multichannel audio. The Windows Media Audio 9 Professional codec supports formats with 6 channels and 8 channels as well as high definition stereo.

## Watermarking

You can encode ASF files with digital watermarks for security. All watermarking systems are different in their approach, but all embed identification into encoded content. Watermarking is performed using special third-party DirectX® media objects (DMOs).

## Support for Multiple Languages in ASF files

You can support multiple languages in ASF files, both in streams and in metadata. For example, you can create a video file with audio streams in several languages. At playback, the user can select which language to use, or your application can query the system information on the playing computer and select a language automatically. Metadata attributes can also be entered multiple times, with the values in different languages.

## Device Conformance Templates

To assist in targeting content to specific client devices, the Windows Media codecs now support device conformance templates. Each template contains a defined range of settings and codec features that should be used for media intended for a particular category of platforms. System profiles are no longer supported with the latest versions of the Windows Media codecs. All profiles must be customized to suit your needs. You can use device conformance templates to assist you in designing your profiles.

## Expanded Codec Enumeration

The profile manager object can query the Windows Media Audio and Video codecs for supported formats. You can set parameters for the formats retrieved. For example, you can retrieve all the quality-based variable bit rate formats supported by the Windows Media Audio 9 codec.

## Improved Mutual Exclusion

You can create named records containing multiple streams within a mutual exclusion object. You can also name mutual exclusion objects to make them easier to identify. This enables you to create layers of mutual exclusion. For example, a file can contain streams that are mutually exclusive by bit rate and by language. The language-based mutual exclusion would involve groups of streams, each group consisting of streams in the same language but mutually exclusive by bit rate.

## Expanded Multiple Bit Rate Support

Mutual exclusion support is included for multiple bit rate (MBR) audio and for video with streams of varying image sizes.

## Attributes for Streams

You can assign attributes to individual streams in ASF files. You must still use file-level attributes for MP3 files. This feature does not add any methods to the SDK, but the existing methods will now accept stream numbers other than zero.

## Transcoding with Smart Recompression

Smart recompression allows you to transcode Windows Media audio files from a high bit rate to a lower bit rate with better quality than previously achievable.

## Expanded Metadata Support

The Windows Media Format SDK provides the following new metadata features:

-   Index-based metadata tags, enabling multiple tags with the same name.
-   Ability to read DRM header attributes without a WMStubDRM.lib file.
-   Attributes with more than 64 kilobytes of associated data.
-   Attributes in multiple languages.
-   Dozens of new predefined attributes.

## Dynamic Pixel Aspect Ratio

Video streams that are composed of various types of content can be accommodated by identifying the pixel aspect ratio of the disparate samples in the stream. This enables the playing application to provide better playback of such content.

## Interlaced Video Streams

Previous versions of the Windows Media Format SDK have provided the ability to encode [*interlaced*](wmformat-glossary.md) content into a progressive-scan video stream. Starting with the Windows Media Format 9 Series SDK, you can encode interlaced video while preserving its interlaced format. This can result in improved playback, particularly on interlaced devices, such as television sets.

## Two-Pass Encoding

The new Windows Media codecs enable two-pass encoding. Content encoded in two passes can achieve higher quality output.

## New Speech Codec

This SDK includes the new Windows Media Audio 9 Voice codec which is optimized for encoding the human voice while using a low bit rate. This codec also provides superior performance for mixed music-voice content.

## Accessible Video Frame Duration

You can have the writer object of this SDK provide the duration of video frames to the reader.

## Streaming HTML

With previous version of this SDK, you were able to use a script command to signal your application to open a Web page. Starting with the Windows Media Format 9 Series SDK, you can store the components of Web pages in your ASF files, to ensure that there is no lag in presentations.

## WMStub.lib no longer required for build environment

The build-environment settings for the Windows Media Format SDK changed starting with the Windows Media Format 9 Series SDK. You no longer need to include WMStub.lib for applications using this SDK. However, DRM-enabled applications still must obtain and sign a separate license agreement, and obtain a unique static library from Microsoft. Contact wmla@microsoft.com for more information about the DRM library and license agreement. For more information about building projects with this SDK, see [Library Files and Compiler Settings](library-files-and-compiler-settings.md).

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> </dl>

 

 




