---
description: This topic describes how a Media Foundation transform (MFT) should handle format changes during streaming.
ms.assetid: b0a94760-b4dd-4e50-a5ce-a1f674dde156
title: Handling Stream Changes
ms.topic: article
ms.date: 05/31/2018
---

# Handling Stream Changes

This topic describes how a Media Foundation transform (MFT) should handle format changes during streaming.

> [!IMPORTANT]
>
> This topic does not apply to encoders. Encoders should not propagate format changes as described in this topic. Encoders should only accept an input type that matches the currently configured output type.

 

## Overview of Format Changes

Generally, there are two reasons that a format can change during streaming.

-   The client might switch to a stream with a new format. For example, in digital television, this can occur due to a channel change.
-   In some video formats, such as H.264, the bitstream can signal a format change. Such changes might include changes in field dominance, video resolution, or pixel aspect ratio.

If the encoding type changes, the client might need to remove the MFT from the pipeline and replace it with another MFT. (For example, the client might need to swap in a new decoder.) This topic does not cover that situation. This topic covers only the case where the current MFT can handle the new format.

If the format changes, the MFT might require a new input type, a new output type, or both.

-   Changes to input type are initiated by the client. An MFT never changes its own input type.
-   Changes to output type are initiated by the MFT. The MFT signals that it requires a new output type, and the client negotiates the new output type with the MFT.

Thus, three distinct cases are possible:

-   The client sets a new input type. The MFT consumes the new format, with no change to its output type.
-   The client sets a new input type, and this triggers a change in the output type.
-   The input type does not change, but the MFT detects a format change in the bitstream, which requires a new output type.

## Implementing Format Changes

The remainder of this topic describes how the client should process a format change, and how to implement format changes in an MFT.

### Output Type

Any MFT can initiate a change to its output type, as follows:

1.  The client calls [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). The MFT responds as follows:
    1.  The MFT does not produce an output sample in [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).
    2.  The MFT sets the **MFT\_OUTPUT\_DATA\_BUFFER\_FORMAT\_CHANGE** flag in the **dwStatus** member of the [**MFT\_OUTPUT\_DATA\_BUFFER**](/windows/desktop/api/mftransform/ns-mftransform-mft_output_data_buffer) structure.
    3.  The [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method returns the error code **MF\_E\_TRANSFORM\_STREAM\_CHANGE**.
2.  The client calls [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype). This method returns an updated set of output types.
3.  The client calls [**SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) to set a new output type.
4.  The client resumes calling [**ProcessInput**](/windows/desktop/api/mfidl/nf-mfidl-imfqualitymanager-notifyprocessinput)/[**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).

### Input Type

Changes to the input type are initiated by the client, never by the MFT. If the input type changes, it might trigger a change to the output type.

The exact sequence of events depends on the value of the [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md) attribute.



| Value     | Description                                                     |
|-----------|-----------------------------------------------------------------|
| **FALSE** | Before the client sets a new input type, it must drain the MFT. |
| **TRUE**  | The client can set a new input type without draining the MFT.   |



 

An MFT exposes this attribute through its [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. The default value of this attribute is **FALSE**; if the MFT does not set the attribute, treat the value as **FALSE**.

**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE is FALSE**

1.  The client sends the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message.
2.  The client drains the MFT by calling [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) until **ProcessOutput** returns **MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT**.
3.  The client calls [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) to set the new input type.
4.  The MFT validates the input type. If the type is invalid, [**SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) returns **MF\_E\_INVALIDMEDIATYPE** or another error code. Otherwise, **SetInputType** returns S\_OK.
5.  Assuming the input type is valid, the MFT evaluates whether the output type also changes. If not, streaming continues, and no further action is required.
6.  If the output type changes:
    1.  The MFT invalidates its current output media type, and updates the list of available output media types.
    2.  The next call to [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) returns **MF\_E\_TRANSFORM\_STREAM\_CHANGE**, as described in the previous section.
    3.  The client calls [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) to get the updated list of output types.
    4.  The client calls [**SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype).

**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE is TRUE**

1.  The client calls [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) to set the new input type.
2.  The MFT validates the input type. If the type is invalid, [**SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) returns **MF\_E\_INVALIDMEDIATYPE** or another error code. Otherwise, **SetInputType** returns S\_OK.
3.  Assuming the input type is valid, the MFT evaluates whether the output type also changes. If not, streaming continues, and no further action is required.
4.  Before the output type changes, the MFT must process any cached input samples, as follows:
    1.  The MFT does not invalidate its current output type.
    2.  The MFT produces as much output as it can from the cached input samples.
    3.  It is optional whether the MFT accepts new input samples while it processes the cached samples. If so, the new input samples will use the new input format, so the MFT must keep track of the point when the format changed.
5.  After the MFT processes all of the samples that it received before the input type changed, the [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) returns **MF\_E\_TRANSFORM\_STREAM\_CHANGE**.
6.  The MFT invalidates its current output type, and updates the list of available output media types.
7.  The client negotiates the new output type, as described previously.

[Asynchronous MFTs](asynchronous-mfts.md) must return the value **TRUE** for the [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md) attribute. When using an asynchronous MFT, the client can assume that the **MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE** attribute is set to **TRUE**.

When [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md) is **TRUE**, the main difference is that the client is not required to drain the MFT before setting a new input type. As a result, the input type might change while the MFT is holding onto input samples. It is important that the MFT does not simply drop these samples. Also, the output type cannot change until the MFT processes all of its cached data.

The previous paragraph applies especially to video decoders, which can receive inter-coded frames out of temporal order, and thus need to cache them. If an MFT does not cache input samples, draining is essentially a no-op. In that case, the MFT can set [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md) to **FALSE** (or leave the attribute unset).

Also, note that every MFT is expected to handle format changes correctly after being drained. The [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md) attribute indicates whether the MFT supports format changes without draining.

## Change in Interlace Mode

Changes in the video interlacing mode are a special case, because they do not invalidate the current media type. Instead, the interlace mode is specified for each video frame by setting attributes on the media sample. A video MFT should check each input sample for the presence of these flags.

The interlace mode can change when the field dominance switches from top-field to bottom-field, or when the video switches between progressive and interlaced pictures.

For more information, see [Interlace Flags on Samples](video-interlacing.md).

## Related topics

<dl> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 



