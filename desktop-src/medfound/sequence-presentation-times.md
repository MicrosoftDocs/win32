---
description: This topic describes how the Sequencer Source handles presentation times during playback.
ms.assetid: 0d095e25-5ccf-4319-8767-07b417ed7ee8
title: Sequence Presentation Times
ms.topic: article
ms.date: 05/31/2018
---

# Sequence Presentation Times

This topic describes how the [Sequencer Source](sequencer-source.md) handles presentation times during playback.

## Overview

The sequencer source supports two different modes: playlist sequences and editing sequences.

In an editing sequence, the application specifies the duration of each segment in advance, before starting playback. In a playlist sequence, the application does not specify the duration in advance. (In fact, the duration might not be known.)

In both cases, you can specify a segment's media start and media stop time. These times specify the position in the source file where the segment begins and ends. For example, suppose that the source file is 90 seconds long. If you wanted to trim the first 10 seconds and the last 10 seconds, you would specify the following values:

-   Media start: 10 seconds
-   Media stop: 80 seconds

To specify the media start time, set the [MF\_TOPONODE\_MEDIASTART](mf-toponode-mediastart-attribute.md) attribute on the source node. To specify the media stop time, set the [MF\_TOPONODE\_MEDIASTOP](mf-toponode-mediastop-attribute.md) attribute on the source node.

To create an editing sequence, set the [MF\_SESSION\_GLOBAL\_TIME](mf-session-global-time-attribute.md) attribute when you create the Media Session. Otherwise, the Media Session expects playlist sequences. In an editing sequence, every segment topology must have the [MF\_TOPOLOGY\_PROJECTSTART](mf-topology-projectstart-attribute.md) attribute and the [MF\_TOPOLOGY\_PROJECTSTOP](mf-topology-projectstop-attribute.md) attribute.

## Playlist Sequences

In a playlist sequence, the presentation clock starts at zero and continues across segment boundaries. The native sources deliver samples with time stamps equal to the media time. The pipeline converts the time stamps to the correct presentation time as follows:

-   New time stamp = media time + offset − media start

The value of *offset* is the presentation time at which the previous segment ended. For the first segment, the offset is zero. Here are two examples of how these time-stamp conversions are calculated:

-   Example 1: Suppose the first segment (S1) is 10 seconds long, and the second segment (S2) has a media start time of zero. The native source uses the media time for its time stamps, so the first sample from S2 has a time stamp of zero. The offset is 10 seconds (the duration of S1), so the adjusted time stamp is:0 + 10 − 0 = 10 seconds.
-   Example 2: Suppose segment S1 is 10 seconds long, and S2 has a media start time of 5 seconds. The first sample from S2 has a time stamp of 5 seconds (media time). The offset is 10 seconds, so the adjusted time stamp is:5 + 10 − 5 = 10 seconds.

All pipeline components downstream from the source nodes receive samples with the adjusted time stamps. The source nodes in a topology can have different media start times, so the adjustments are calculated separately for each branch of the topology.

When the presentation switches to the next segment, the presentation clock does not stop or reset, and the presentation time increases monotonically. Before a new segment starts, the Media Session sends the application an [MESessionNotifyPresentationTime](mesessionnotifypresentationtime.md) event. The event specifies the starting time of the segment, relative to the presentation clock, and the value of the offset. When a new segment starts, the pipeline calls [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) on the sequencer source with the value VT\_EMPTY. The sequencer source sends an [MESourceStarted](mesourcestarted.md) event with no start time.

To seek, the application specifies a segment identifier plus a time offset within the segment. After the seek, the presentation clock starts at the *segment* offset. Here is an example of how that process works:

-   Example 3: The application seeks to segment S3, with a segment offset of 10 seconds. The presentation clock starts at 10 seconds (the segment offset). The offset does not include the duration of segments S1 and S2. The sequencer source sends an [MESourceStarted](mesourcestarted.md) event with a start time equal to the segment offset, 10 seconds.

After a seek, if playback continues to the next segment, the transition works just like the previous examples, except that the offset does not include the skipped segments.

Here are some further details that affect how samples are time stamped:

-   Decoders may need data beyond the media stop time. The pipeline pulls as much data from the source as the decoder requires, and then trims the decoder's output samples.
-   Transforms might buffer data. For example, an audio effect might need to do this. When a segment ends, the time stamp on the last sample from the transform is earlier than the end of the segment, because the transform is holding back some data. When the next segment starts, the time stamp on the first sample is slightly earlier than the start of the segment. There is no gap in the time stamps, so the data that reaches the media sink is continuous. When the final segment ends, the pipeline drains the transform, so no data is lost.
-   The source may need to start slightly earlier than the media start time, to pick up the previous key frame. Therefore, after the adjustment, the first sample might have a negative presentation time.

## Editing Sequences

In an editing sequence, the application specifies the segment boundaries in advance, by setting the [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md) and [**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md) attributes. The pipeline calculates adjustments for the time stamps in almost the same way as for a playlist sequence:

-   For the offset, it uses the value of [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md), instead of using the observed end of the segment.

-   For seeking, the offset uses a value equal to the segment's [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md) value plus the segment offset.

Therefore, the presentation time in an editing sequence is always relative to the start of the presentation, even if the application seeks to another segment.

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 



