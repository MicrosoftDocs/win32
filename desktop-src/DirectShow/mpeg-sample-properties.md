---
description: MPEG Sample Properties
ms.assetid: 339aab84-e5ad-4071-8b67-2b04cb17e450
title: MPEG Sample Properties
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MPEG Sample Properties

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

MPEG samples have the following characteristics.

**Time Stamps**

Not all samples have start and stop times. The sample stop time for packet and payload data is not useful; it is usually set to the start time plus one. MPEG packet or payload data samples will have a start and stop time set if the system layer packet they are generated from had a valid PTS.

For more information about time stamps, see section 2.4.1 of ISO1-11172: "The packet header may contain decoding and/or presentation time stamps (DTS and PTS) that refer to the first access unit in the packet."

For MPEG\_Stream major types, the start time is the byte position of the first byte, rated at 1 byte per second. The stop time is the byte position of the last byte. Thus, consecutive samples should have the stop time of the first packet equal to the start time of the next packet. For Video CD data, the origin of the medium must match the format of a video-CD file exposed by CDFS with the standard RIFF chunk at the start.

For MPEG video packet and payload types, the time stamp is the presentation time for the first video frame whose picture start code begins in the sample.

For MPEG audio packet and payload types, the time stamp is the presentation time for the first audio frame whose sync code starts in the sample.

It is assumed that packet and payload data without time stamps can be successfully prerolled by the handling filters.

**Discontinuities**

If there is a break in the stream (for example, a gap in the real-time data, or an error in the data or after a seek), the discontinuity property is set on the next media sample. This also allows for a time-stamp discontinuity.

**End-of-Stream Notifications**

When the decoder receives this notification, it must process any buffered data. Any new data must then start with the discontinuity property.

## Related topics

<dl> <dt>

[MPEG-2 Support in DirectShow](mpeg-2-support-in-directshow.md)
</dt> </dl>

 

 



