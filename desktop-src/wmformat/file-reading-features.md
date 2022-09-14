---
title: File Reading Features
description: File Reading Features
ms.assetid: ba6dd328-2250-4867-94e0-f66c70ac1bac
keywords:
- Windows Media Format SDK,file reading features
- Windows Media Format SDK,asynchronous file reading
- Windows Media Format SDK,synchronous file reading
- Advanced Systems Format (ASF),file reading features
- ASF (Advanced Systems Format),file reading features
- Advanced Systems Format (ASF),asynchronous file reading
- ASF (Advanced Systems Format),asynchronous file reading
- Advanced Systems Format (ASF),synchronous file reading
- ASF (Advanced Systems Format),synchronous file reading
- asynchronous file reading
- synchronous file reading
- synchronous readers,file reading features
- file reading
ms.topic: article
ms.date: 05/31/2018
---

# File Reading Features

Reading ASF files is one of the primary features of the Windows Media Format SDK. Two types of reading are supported: asynchronous and synchronous. Asynchronous file reading is handled by the reader object. The synchronous reader object is used to read files synchronously. For more information about the different reading objects, see [Reader Object](reader-object.md) and [Synchronous Reader Object](synchronous-reader-object.md).

In the most basic asynchronous file reading scenario, you must implement a callback method that the reader object will call when samples are ready. After you begin reading a file, your application waits for the samples to be delivered to your callback method. Asynchronous reading is useful for player applications, and supports features not available with synchronous reading. If your application needs to read files from a network location, or interact with a server running Windows Media Services, you must use the reader object. The disadvantage of the reader object is that a separate thread is used for each output delivered. Additionally, the reader object is not as flexible as the synchronous reader in how it can deliver samples.

With the synchronous reader you do not need to use any callback methods. Instead, you select a portion of the file to read and retrieve the samples one at a time with method calls. The synchronous reader is well suited to the needs of content-editing applications, where quick access to specific samples is essential. Because no callback methods are used by the synchronous reader, you can create applications to read ASF files with a minimum of coding overhead. However, the synchronous reader cannot open a file from a network location, or interact with a server running Windows Media Services, or read files protected with [*DRM*](wmformat-glossary.md).

The following topics discuss the features of the reader and the synchronous reader.



| Topic                                                              | Description                                                                                                        |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [User Allocated Sample Support](user-allocated-sample-support.md) | Discusses buffer allocation in the reader and synchronous reader, and how user allocation can improve performance. |
| [Output Format Enumeration](output-format-enumeration.md)         | Discusses output format enumeration.                                                                               |



 

In addition, the following topics from the writing features section also apply to file reading:

-   [Video Resizing](video-resizing.md)
-   [Color Space Conversion](color-space-conversion.md)
-   [Audio Resampling](audio-resampling.md)

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> </dl>

 

 




