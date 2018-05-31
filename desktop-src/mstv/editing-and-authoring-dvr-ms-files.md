---
title: Editing and Authoring dvr-ms Files
description: Editing and Authoring dvr-ms Files
ms.assetid: 26eb9664-f15d-49d8-92dd-1b4cedb38088
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Editing and Authoring dvr-ms Files

Extended access to dvr-ms files is not limited to playback; editing and authoring applications can also access the files, as long as they are not encrypted.

In some cases, video and audio streams may need to be handled separately during the editing or authoring process. The sample content consists of MPEG-2 video stream and MPEG-1 Layer 2 audio stream. Synchronization between audio and video requires that the relationship between media sample timestamps ([**IMediaSample::GetTime**](https://msdn.microsoft.com/library/windows/desktop/dd407012)) be maintained. These timestamps are rebased PES timestamps from 90 kHz to 10 MHz as found in the original PES header's PTS field.

The MPEG-2 video elementary stream read from a dvr-ms file is not guaranteed to start on a GOP boundary. "Start" in this instance can mean either the start of the recording or following any search into the recording. If a downstream component requires a GOP or sequence header before it can begin processing the stream, it must first discover the header in the received media samples, and discard any content that precedes it.

In simple editing scenarios, for example to remove specified time segments from a dvr-ms file and copy the resulting file to a new file, use the [RecComp Object](reccomp-object.md). This technique is very efficient because it does not involve any decoding or re-encoding of the elementary streams and you are not limited to the 1x rate limitation of the SBE sink.

## Related topics

<dl> <dt>

[About the dvr-ms File Format](about-the-dvr-ms-file-format.md)
</dt> </dl>

 

 




