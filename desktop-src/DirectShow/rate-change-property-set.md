---
description: The Rate Change property set enables MPEG-2 source/parser filters to change the playback rate. MPEG-2 decoders should support this property set. The DVD Navigator and the Stream Buffer Engine both use this property set to control playback rates.
ms.assetid: f88c64ce-af76-49fe-8ebd-029928506243
title: Rate Change Property Set (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Rate Change Property Set

The Rate Change property set enables MPEG-2 source/parser filters to change the playback rate. MPEG-2 decoders should support this property set. The DVD Navigator and the Stream Buffer Engine both use this property set to control playback rates.



| Label | Value |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |



 



| Property ID                                                                   | Description                                                                            |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**AM\_RATE\_CorrectTS**](am-rate-correctts-property.md)                     | Informs the decoder that the Navigator is setting the correct time stamps.             |
| AM\_RATE\_ExactRateChange                                                     | Obsolete.                                                                              |
| [**AM\_RATE\_MaxFullDataRate**](am-rate-maxfulldatarate-property.md)         | Queries the decoder for the decoder's maximum data rate.                               |
| [**AM\_RATE\_QueryFullFrameRate**](am-rate-queryfullframerate-property.md)   | Queries the decoder for the decoder's maximum full-frame rate.                         |
| [**AM\_RATE\_QueryLastRateSegPTS**](am-rate-querylastratesegpts-property.md) | Queries the decoder for the start time of the rate segment that was set most recently. |
| [**AM\_RATE\_SimpleRateChange**](am-rate-simpleratechange-property.md)       | Sends a rate change to the decoder.                                                    |
| AM\_RATE\_Step                                                                | Obsolete. See [Frame Stepping Property Set](frame-stepping-property-set.md).          |
| [**AM\_RATE\_UseRateVersion**](am-rate-userateversion-property.md)           | Specifies which version of the rate change mechanism to use.                           |



 

## Remarks

In the context of this property set, rate measures the rate at which time stamps advance relative to the reference clock. Rate the inverse of playback speed. For example, if the playback speed is 2x, the time stamps must increase at 1/2 the normal rate. This translates to a faster playback speed, because samples are rendered earlier than normal.

Samples are sent to the decoder with a time stamp equal to the presentation time at 1x rate. The decoder must scale the time stamps on the output samples to the correct presentation time for the current rate. For example, if the rate is 1/2 (meaning the playback speed is 2x), the decoder must scale the time stamps by 1/2. Generally, only I frames have time stamps. The decoder must interpolate the time stamps for the B and P frames. Note that during reverse playback, time stamps continue to increase — time stamps never go backward.

Two versions of the Rate Change property set are defined, version 1.0 and version 1.1. The default behavior is given by version 1.0. Decoder vendors are encouraged to support version 1.1, because it provides a smoother playback experience. The DVD Navigator currently uses version 1.0. The Stream Buffer Engine uses version 1.1.

### Rate Change Version 1.0

Version 1.0 of the Rate Change property set defines the default behavior for MPEG-2 decoders.

The source filter signals a rate change by setting the [**AM\_RATE\_SimpleRateChange**](am-rate-simpleratechange-property.md) property. The data for this property is the new rate, plus the start time on the input sample when the rate takes effect. The decoder maintains a queue of pending rate changes, sorted by start time.

Before the DVD Navigator changes to a non-1x speed, it delivers all pending samples, temporarily sets the rate to 1.0, and flushes the graph. Then it sets the new rate. All rate changes are scheduled for the end of the current VOBU (video object unit). Note that flushing the graph resets the presentation time to zero.

The DVD Navigator operates either in *smooth mode* or in *scan mode*. In smooth mode, it sends every frame to the decoder, including B frames and P frames. The DVD Navigator uses smooth mode whenever playback speed is greater than zero but less than the decoder's maxmimum data rate. If playback speed is less than zero (reverse playback), or exceeds the decoder's maximum data rate, the DVD Navigator uses scan mode, where it sends just the I frames to the decoder. At very high speeds, it may skip some I frames; for example, it may send every other I frame.

By default, the DVD Navigator mutes the audio stream for rates other than 1.0. You can change this by calling [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) with the DVD\_AudioDuringFFwdRew flag.

### Rate Change Version 1.1

Version 1.1 of the Rate Change property set follows the same basic principles as version 1.0, with the following differences:

-   The source filter signals the decoder to use version 1.1 by setting the [**AM\_RATE\_UseRateVersion**](am-rate-userateversion-property.md) property. Otherwise, the decoder should use the version 1.0 behavior.
-   The source filter does not flush the graph between rate changes. Time stamps therefore increase monotonically across rate change boundaries, rather than resetting to zero.
-   Instead of queuing a rate change for a particular reference time, the source filter can specify that a rate change applies to the decoder's *most forward sample*, defined as the sample at the head of the decoder's outgoing queue. To do so, the source filter uses the [**AM\_RATE\_SimpleRateChange**](am-rate-simpleratechange-property.md) property but sets the start time equal to -1.
-   The source filter can query the decoder for the start time of the rate change that was queued most recently. It uses the [**AM\_RATE\_QueryLastRateSegPTS**](am-rate-querylastratesegpts-property.md) property for this purpose.
-   The source filter does not drop samples. If the rate exceeds the decoder's maximum data rate, the decoder should drop frames as necessary.
-   The source filter does not mute the audio stream, regardless of the audio decoder's maximum data rate. The audio decoder can drop samples if the playback speed exceeds the decoder's maximum rate. However, it should still maintain the queue of scheduled rate changes.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 




