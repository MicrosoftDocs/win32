---
title: To Pause or Stop Playback
description: To Pause or Stop Playback
ms.assetid: '8e43ea80-36c7-4530-8ed3-dfdb64a3a2e3'
keywords: ["Advanced Systems Format (ASF),pausing playback", "ASF (Advanced Systems Format),pausing playback", "Advanced Systems Format (ASF),asynchronous readers", "ASF (Advanced Systems Format),asynchronous readers", "Advanced Systems Format (ASF),stopping playback", "ASF (Advanced Systems Format),stopping playback", "Advanced Systems Format (ASF),playback pausing or stopping", "ASF (Advanced Systems Format),playback pausing or stopping", "asynchronous readers,pausing playback", "asynchronous readers,stopping playback", "asynchronous readers,playback pausing or stopping"]
---

# To Pause or Stop Playback

When you call [**IWMReader::Start**](iwmreader-start.md) to begin playing a file, the asynchronous reader will continue processing in its own separate threads until the end of the file is reached. You can pause or stop the delivery of samples using the [**IWMReader::Pause**](iwmreader-pause.md) or [**IWMReader::Stop**](iwmreader-stop.md) methods respectively.

## Pausing

When you call **IWMReader::Pause** to pause playback of a file, the reader keeps track of the current position in the file. To resume playing after pausing, call [**IWMReader::Resume**](iwmreader-resume.md). Playback will resume from the point at which it paused.

## Stopping

When you call **IWMReader::Stop** to halt playback of a file, the reader does not keep track of any information about the progress of playback. To use **Stop** and later return to the stopping point you must save the presentation time of the last sample delivered and use it in your call to **IWMReader::Start**.

## Related topics

<dl> <dt>

[**IWMReader Interface**](iwmreader.md)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> </dl>

 

 




