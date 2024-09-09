---
title: Overview of the Windows Media Format SDK
description: Overview of the Windows Media Format SDK
ms.assetid: 9e5d6254-6261-4ca8-84d6-38050c93db22
keywords:
- Windows Media Format SDK,ASF file creation and editing
- Advanced Systems Format (ASF),file creation and editing
- ASF (Advanced Systems Format),file creation and editing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overview of the Windows Media Format SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK contains objects to perform tasks at three points in the life of an ASF file: creation, editing, and playback. Some applications, notably those for video editing, will use the broad functionality of the Windows Media Format SDK to read the contents of ASF files, alter that content, and write the results to a new file. However, it is easiest to think of this SDK in the three stages of file creation, editing, and playback.

## ASF File Creation with the Windows Media Format SDK

The process of writing ASF files with the Windows Media Format SDK is, at a high level, fairly simple. File creation is managed by a writer object. You tell the writer object what sort of file you want to create by specifying a profile object for it to use. Each profile object contains the settings for an ASF file. Some profiles are included with this SDK, and profile editing support is provided by a number of objects. When you have set a profile for the writer object to use, you can begin passing samples to the writer for processing. In most cases, a sample is a piece of audio or video that is uncompressed, but a sample can be any type of data.

Internally, the writer performs three major tasks. First, if the stream that a sample belongs to is to be compressed, the writer communicates with the encoding portion of the codec (compressor/decompressor) to compress the sample. Once the samples are in the form specified by the profile, the writer breaks the samples apart into packets of appropriate size to be streamed over a network. Finally, the data from the various streams is multiplexed, or interleaved so that samples with similar presentation times across all streams are close to one another in the data section of the ASF file.

The writer object does not actually write a file itself. It communicates with one or more objects called sinks, which deliver the data from the writer to its destination. In the case of local files, a file sink manages writing the data to the file. You can also configure network sinks to deliver the ASF data across a network. Commonly, more than one sink is used. For example, an application can stream a file across a network and save a copy as a file on a local disk simultaneously. By using a push sink, you can broadcast content from your writing application to one or more servers running Windows Media Services, which will then distribute the content to users.

## ASF File Editing with the Windows Media Format SDK (Metadata Editing)

Editing the contents of the data section of an ASF file involves rewriting the file. The Windows Media Format SDK does not provide any objects that manipulate the data section in place. For simple edits, such as concatenating two files, or cutting content from a file, you can read samples without decompressing them, and then write them to a new file using the same header information. More complicated edits involve making changes to the profile used for the new file.

The Windows Media Format SDK does support editing parts of the header section without rewriting the file. The header of an ASF file contains many different types of data. The most commonly edited are metadata attributes, which are name/value pairs that describe aspects of the content and the people involved in making it. You can edit metadata using the metadata editor object of the Windows Media Format SDK. This object will open an ASF file, enable you to change some of the contents of the header, write the changes to the file, and close the file. Metadata editing is very straightforward, with simple method calls to retrieve and set values.

## ASF File Reading with the Windows Media Format SDK

The Windows Media Format SDK provides two distinct objects for reading ASF files: the reader object and the synchronous reader object. The reader object is available in all versions of the SDK, while the synchronous reader object requires the Windows Media Format 9 Series SDK or a later version. The primary difference between the two is that the reader object delivers samples to your application by firing events to a callback method, while the synchronous reader provides individual samples in response to method calls.

To use the reader object, you must implement several callback methods to react to status and sample messages from the reader object. You configure the reader to deliver the content as you like, start the reader, and wait for the sample messages. The process of retrieving samples from an ASF file is basically the reverse of the writing process. The reader object communicates with the codecs required to decode any compressed streams and delivers uncompressed data to your application. You can also configure the reader object to deliver samples in their compressed state, so that you can include a previously encoded stream in a new file.

The synchronous reader object works in much the same way as the reader object. But instead of configuring callbacks, you must request each sample from the synchronous reader individually. Using the synchronous reader requires only a single thread, while using the reader requires multiple threads. The synchronous reader object has several advantages over the reader object in certain circumstances, mostly for content editing applications that need to quickly access different parts of a file and copy data between files. The synchronous reader object is much simpler to use, and makes seeking to specific places in the data section easy. However, the synchronous reader does not support reading files over a network and does not support digital rights management.

## Other Operations with the Windows Media Format SDK

In addition to the three main functional areas just described, the Windows Media Format SDK has objects to perform other operations relating to ASF files. The profile manager object is used to create and access profiles and to save them. The indexer object creates index objects in ASF files that allow seeking in video files. Finally, the reader object and writer object support digital rights management to protect the intellectual rights of content creators.

**Note** The intention of the ASF file structure and this SDK in general is to produce digital media files containing audio and video, and this documentation is written with that end in mind. However, the ASF file structure will work for other types of content, too. You may find many applications for ASF files that are not related to audio and video.

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> </dl>

 

 




