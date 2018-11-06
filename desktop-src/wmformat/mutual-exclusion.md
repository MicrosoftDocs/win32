---
title: Mutual Exclusion
description: Mutual Exclusion
ms.assetid: 3a3f6763-a241-4bbd-a6e8-62041b05622d
keywords:
- Windows Media Format SDK,mutual exclusion
- Advanced Systems Format (ASF),mutual exclusion
- ASF (Advanced Systems Format),mutual exclusion
- Windows Media Format SDK,MBR mutual exclusion
- Advanced Systems Format (ASF),MBR mutual exclusion
- ASF (Advanced Systems Format),MBR mutual exclusion
- Windows Media Format SDK,multiple bit rate (MBR)
- Advanced Systems Format (ASF),multiple bit rate (MBR)
- ASF (Advanced Systems Format),multiple bit rate (MBR)
- mutual exclusion,about
- multiple bit rate (MBR),mutual exclusion
- MBR (multiple bit rate),mutual exclusion
- mutual exclusion,bit rate
- mutual exclusion,language
- mutual exclusion,presentation
- mutual exclusion,unknown
- mutual exclusion,features
- mutual exclusion,advanced features
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Exclusion

Every ASF file contains one or more streams, each containing digital media data. Under normal circumstances, each stream is associated with a single output. On playback, the reader object delivers samples for each output. So, as a default, every stream in an ASF file is delivered by the reader on playback.

There are situations where you do not want every stream delivered to the client. For example, if you create a video file with five audio streams, one for each of five languages, you want only one of them to be delivered at a time. Mutual exclusion is a feature of the Windows Media Format SDK that enables you to specify a number of mutually exclusive streams that all equate to the same output.

Mutual exclusion is defined in the profile used to create a file. You configure mutual exclusion in a profile by using mutual exclusion objects. You add streams one at a time to the mutual exclusion object, set the type, and include the object in the profile.

The Windows Media Format SDK recognizes four types of mutual exclusion:

-   Bit rate
-   Language
-   Presentation
-   Unknown

## Mutual Exclusion by Bit Rate

Bit rate mutual exclusion is a special type of mutual exclusion and is more commonly referred to as multiple bit rate (MBR) mutual exclusion. An MBR mutual exclusion contains a number of streams that all originate from the same input, but are encoded at different bit rates. When playing a file with MBR, the reader determines the best stream to use based on the available bandwidth.

The Windows Media Format SDK supports MBR for audio and video streams. The SDK also supports a special type of MBR video called multiple video size MBR. This is like normal MBR video except that the individual streams can have different frame sizes. For example, you might have some streams at the default 320 x 240 video size and some others with higher bit rates and 640 x 480 video size.

## Mutual Exclusion by Language

Language-based mutual exclusion is designed for use with content (usually audio) recorded in several languages. A language-based mutual exclusion includes several streams that originate from unique inputs. Each input is the same content, but in a different language.

For mutual exclusion by language to work, the reading application must include logic to select the appropriate language. If you write an application to play ASF files, and you want to support files with language-based mutual exclusion, you should select the appropriate stream before beginning playback.

## Mutual Exclusion by Presentation

Presentation-based mutual exclusion is provided to support video streams that contain the same content encoded with different aspect ratios. Typically, this is used when providing video in a letterbox version (aspect ratio 16:9) as well as formatted for television screens (aspect ratio 4:3).

The selection of a presentation for playback is most often determined by the user. If you write an application to play ASF files and want to support files with presentation based mutual exclusion, you should present the user with the option of selecting a presentation type for viewing.

## Unknown Mutual Exclusion

You can create mutual exclusion based on any criteria you like. All custom mutual exclusion types should be created using the unknown type.

## Advanced Mutual Exclusion Features

You can also use mutual exclusion to assign streams to groups that are mutually exclusive of one another. For example, you might want to have audio streams in multiple languages and assign a different video stream to each. You use mutual exclusion to group each audio stream with its corresponding video stream and make all groups mutually exclusive.

The reader automatically selects streams for all mutual exclusions. For all types of mutual exclusion except MBR and language-based mutual exclusion, the reader always selects the default stream, which is the first stream added to the mutual exclusion object in the profile. For MBR, the reader selects the stream that best suits the available bandwidth at the time of playback. If you do not want to use the default stream, you can set stream selection to manual before starting to read a file.

Manual stream selection applies to the entire file. Difficulties can arise when you have mutual exclusions of different types in the same file. For example, a file can contain both bit-rate-based mutual exclusion and custom mutual exclusion. To select a stream other than the default in the custom mutual exclusion, you must use manual stream selection. If you use manual stream selection, however, the reader will not automatically select the multiple bit rate stream. You must plan for this eventuality in your application if you plan to support multiple types of mutual exclusion in a single file. Typically this means creating your own stream selection routines for normally automatic types of mutual exclusion.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Using Mutual Exclusion**](using-mutual-exclusion.md)
</dt> </dl>

 

 




