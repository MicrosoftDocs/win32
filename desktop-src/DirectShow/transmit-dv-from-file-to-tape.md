---
description: Transmit DV from File to Tape
ms.assetid: f6dd8c4b-0535-42b9-a969-89e7b9e6ee0f
title: Transmit DV from File to Tape
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Transmit DV from File to Tape

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Transmit from DV AVI file to VTR tape is complicated somewhat by the fact that files can type-1 or type-2. To transmit a DV file to tape, do the following:

1.  Create an instance of the [MSDV Driver](msdv-driver.md) filter. For more information, see [Selecting a Capture Device](selecting-a-capture-device.md).
2.  Make sure the device is in VTR mode. Otherwise, you cannot transmit to tape.See [Device Mode](device-mode.md).
3.  Initialize the Capture Graph Builder, as described in [About the Capture Graph Builder](about-the-capture-graph-builder.md).
4.  Build the graph. The graph configuration depends on the DV file type:
    -   [Transmit from Type-1 File](transmit-from-type-1-file.md)
    -   [Transmit from Type-2 File](transmit-from-type-2-file.md)
5.  Put the device into record-pause mode, as described in [Controlling a DV Camcorder](controlling-a-dv-camcorder.md).
6.  Pause the filter graph. While the filter graph is paused, it sends a continuous stream that repeats the first frame of video.
7.  To start transmitting, put the device into record mode and then run the filter graph. It takes the device a certain amount of time until the recording head is able to record, so wait for about two seconds before running the graph. This might result in a few duplicated frames at the beginning of the tape, but it ensures that no data is lost.

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 



