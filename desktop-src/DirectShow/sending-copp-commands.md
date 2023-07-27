---
description: Sending COPP Commands
ms.assetid: aba0bd34-f5bb-4233-bde2-0dfd8f1ff0bf
title: Sending COPP Commands
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sending COPP Commands

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To send a Certified Output Protection Protocol (COPP) command, fill in an [**AMCOPPCommand**](/windows/win32/api/strmif/ns-strmif-amcoppcommand) structure as follows:

-   **guidCommandID**. The GUID that identifies the command. See the COPP Command Reference.
-   **dwSequence**. The command sequence number. Increment this value after each command. (This value is shown as **uCommandSeq** in [Initiating a COPP Session](initiating-a-copp-session.md).)
-   **cbSizeData**. The size, in bytes, of any data needed for the command.
-   **CommandData**. Data for the command.

After you have filled in this data, calculate the MAC for the command:

1.  Calculate the OMAC-1 tag for the block of data that appears after the **macKDI** member of the **AMCOPPCommand** structure.
2.  Copy this value into the **macKDI** member of the structure.

Now pass the structure to the [**IAMCertifiedOutputProtection::ProtectionCommand**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-protectioncommand) method.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



