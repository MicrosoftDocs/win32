---
description: Sources of DVD Region Information
ms.assetid: f4874aa7-c58a-49a3-9474-c621cc19156b
title: Sources of DVD Region Information
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sources of DVD Region Information

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are three sources of DVD region information that work together to determine the region for DVD playback on a Windows PC.

-   DVD Title. Most DVD titles are marked for a specific region. Some titles can be played in only one region, some can be played in multiple regions, and others can be played all regions. Regions 1 through 6 were defined in the original DVD-Video specification. Region 7 is currently undefined. Region 8 was added in 1999 for special venues, such as airplanes. DVD-ROM discs (those with no video zone) should not contain any region coding.
-   DVD-ROM Drive. There are two types of DVD-ROM drives: RPC Phase 1 (RPC1) drives and RPC Phase 2 (RPC2) drives. RPC1 drives do not have built-in hardware support for region management. For these drives, Windows maintains the region change count information and the region can be changed only once. RPC2 drives maintain the region change count information in hardware and in general the region of such drives can be changed up to 5 times.
-   DVD Decoder. Some DVD decoders, hardware or software, are set for a specific region. In general, the user cannot change the decoder's region.

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 



